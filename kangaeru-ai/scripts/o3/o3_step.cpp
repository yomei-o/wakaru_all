// 2D O(3) sigma model, Wolff single-cluster. Finite-volume coupling g2(L) = m(L)*L  (Luscher-Weisz-Wolff 1991).
// usage: o3_step beta L T nclusters seed   -> prints g2 with blocking error
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <random>
int main(int argc, char** argv) {
    double beta = atof(argv[1]); int L = atoi(argv[2]), T = atoi(argv[3]); long nc = atol(argv[4]); int seed = atoi(argv[5]);
    int V = L*T; std::vector<double> sx(V), sy(V), sz(V); std::mt19937_64 rng(seed); std::uniform_real_distribution<double> U(0, 1);
    auto rnd = [&]() { return U(rng); };
    auto randunit = [&](double& x, double& y, double& z) { double a, b, s; do { a = 2*rnd()-1; b = 2*rnd()-1; s = a*a+b*b; } while (s >= 1 || s == 0); double q = 2*sqrt(1-s); x = a*q; y = b*q; z = 1-2*s; };
    for (int i = 0; i < V; i++) randunit(sx[i], sy[i], sz[i]);
    auto idx = [&](int x, int t) { return ((t+T)%T)*L + (x+L)%L; };
    std::vector<int> stack; stack.reserve(V); std::vector<char> in(V);
    auto wolff = [&]() {
        double rx, ry, rz; randunit(rx, ry, rz); int s0 = (int)(rnd()*V); std::fill(in.begin(), in.end(), 0);
        stack.clear(); stack.push_back(s0); in[s0] = 1;
        while (!stack.empty()) {
            int i = stack.back(); stack.pop_back(); double pi = sx[i]*rx+sy[i]*ry+sz[i]*rz;
            int x = i % L, t = i / L; int nb[4] = {idx(x+1,t), idx(x-1,t), idx(x,t+1), idx(x,t-1)};
            for (int k = 0; k < 4; k++) { int j = nb[k]; if (in[j]) continue; double pj = sx[j]*rx+sy[j]*ry+sz[j]*rz;
                double a = 2*beta*pi*pj; if (a > 0 && rnd() < 1-exp(-a)) { in[j] = 1; stack.push_back(j); } }
            sx[i] -= 2*pi*rx; sy[i] -= 2*pi*ry; sz[i] -= 2*pi*rz;
        }
    };
    for (long c = 0; c < nc/10; c++) wolff();
    // zero-momentum time-slice correlator; measure every 'every' clusters; blocks for errors
    int every = 4; int nblk = 20; long per = nc/(every*nblk); std::vector<std::vector<double>> C(nblk, std::vector<double>(T, 0.0));
    std::vector<double> Sx(T), Sy(T), Sz(T);
    for (int b = 0; b < nblk; b++) for (long m = 0; m < per; m++) {
        for (int e = 0; e < every; e++) wolff();
        for (int t = 0; t < T; t++) { Sx[t] = Sy[t] = Sz[t] = 0; for (int x = 0; x < L; x++) { int i = t*L+x; Sx[t] += sx[i]; Sy[t] += sy[i]; Sz[t] += sz[i]; } }
        for (int d = 0; d < T; d++) { double acc = 0; for (int t = 0; t < T; t++) { int u = (t+d)%T; acc += Sx[t]*Sx[u]+Sy[t]*Sy[u]+Sz[t]*Sz[u]; } C[b][d] += acc/(T*L*(double)per); }
    }
    // mass from effective mass plateau averaged over t in [L, 2L] using cosh form; per block, then mean/err
    std::vector<double> g2b(nblk);
    for (int b = 0; b < nblk; b++) {
        double msum = 0; int n = 0;
        for (int t = L; t <= 2*L && t+1 < T/2; t++) { double r = (C[b][t+1]+C[b][t-1])/(2*C[b][t]); if (r > 1) { msum += acosh(r); n++; } }
        g2b[b] = (n ? msum/n : NAN)*L;
    }
    double mean = 0, var = 0; for (double g : g2b) mean += g/nblk; for (double g : g2b) var += (g-mean)*(g-mean)/(nblk-1.0);
    printf("beta=%.3f L=%d T=%d  g2(L)=m*L = %.4f +- %.4f\n", beta, L, T, mean, sqrt(var/nblk));
}

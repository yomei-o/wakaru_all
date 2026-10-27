# Borel–Padé resummation of the divergent series of Z(g) = ∫ e^{-x²/2 - g x⁴/4} dx/√(2π), and the Stokes phenomenon:
# for g < 0 the Borel sum is ambiguous; its imaginary part should equal the decay rate from the instanton,
# Im Z(-|g|) = ± (1/√2) e^{-1/(4|g|)} (1 + O(g))  [one-instanton, from the saddle x² = 1/|g|].
from mpmath import mp, mpf, gamma, quad, exp, sqrt, pi, inf, factorial, pade, polyval, mpc, im, re, cos, sin
mp.dps = 50
N = 60
c = [(-mpf(1)/4)**n*gamma(2*n+mpf(1)/2)*2**(2*n)/(sqrt(pi)*factorial(n)) for n in range(N+1)]   # (4n-1)!!/n! (-1/4)^n
b = [c[n]/factorial(n) for n in range(N+1)]                       # Borel transform coefficients
P, Q = pade(b, N//2, N//2)
def B(t): return polyval(P[::-1], t)/polyval(Q[::-1], t)
def Zexact(g): return quad(lambda x: exp(-x*x/2 - g*x**4/4), [-inf, inf])/sqrt(2*pi)
def borel(g, theta=0):                                            # Laplace integral along ray arg t = theta
    w = exp(mpc(0, theta))
    return quad(lambda s: exp(-s*w)*B(g*s*w)*w, [0, inf])   # t = s w:  ∫ e^{-t} B(g t) dt along the rotated ray
print("positive g: Borel–Padé vs exact (optimal truncation of the plain series was 3e-7 at g=0.02, 1e-2 at g=0.1)")
for g in [mpf('0.02'), mpf('0.1'), mpf('0.3'), mpf('1')]:
    print(f"  g={float(g):<5} |Borel-Padé - exact| = {float(abs(borel(g)-Zexact(g))):.1e}")
print("\nnegative g: lateral Borel sums (ray slightly above / below the real axis) and the instanton")
for g in [mpf('-0.05'), mpf('-0.1'), mpf('-0.2')]:
    up = borel(g, mpf('0.3')); dn = borel(g, mpf('-0.3'))       # rotate contour to avoid the pole on the positive axis
    inst = exp(-1/(4*abs(g)))/sqrt(2)
    print(f"  g={float(g):<6} Re(Borel) = {float(re(up)):.6f}   Im(Borel) = ±{float(abs(im(up))):.3e}   instanton e^(-1/4|g|)/√2 = {float(inst):.3e}   ratio {float(abs(im(up))/inst):.3f}   (up-dn imag {float(im(up)-im(dn)):.2e})")

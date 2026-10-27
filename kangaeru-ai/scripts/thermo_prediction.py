# Thermodynamics of prediction (Still, Sivak, Bell, Crooks 2012): for a system s driven by a signal x,
#   W_diss  >=  kT [ I(s_t; x_t) - I(s_t; x_{t+1}) ]  =  kT * (memory - predictive information)   (per step)
# Setup (all Gaussian, so the mutual informations are exact from covariances):
#   signal: OU process x_{t+1} = a x_t + sqrt(1-a²) ξ        (unit variance, correlation a)
#   system: overdamped particle in a trap centred at x_t, relaxing for a time τ per step at temperature T=1:
#           s' = x_t + (s - x_t) e^{-kτ} + noise with var (1 - e^{-2kτ})/k      (exact OU relaxation)
#   work per step = ΔU when the trap jumps from x_t to x_{t+1} at fixed s:  k/2[(s-x_{t+1})² - (s-x_t)²]
#   dissipated work = <W> - ΔF = <W> (ΔF = 0, the trap only translates)
import numpy as np
rng = np.random.default_rng(3); T = 1.0
def mi_gauss(u, v):                      # I(u;v) for jointly Gaussian scalars
    r = np.corrcoef(u, v)[0, 1]; return -0.5*np.log(1 - r*r)
def run(a, k, tau, n=400000):
    x = np.zeros(n+1); s = np.zeros(n+1); W = np.zeros(n)
    e = np.exp(-k*tau); sd = np.sqrt((1 - e*e)/k*T)
    x[0] = rng.standard_normal(); s[0] = x[0] + rng.standard_normal()/np.sqrt(k)
    for t in range(n):
        x[t+1] = a*x[t] + np.sqrt(1-a*a)*rng.standard_normal()
        W[t] = 0.5*k*((s[t]-x[t+1])**2 - (s[t]-x[t])**2)             # trap jumps: work done on the particle
        s[t+1] = x[t+1] + (s[t]-x[t+1])*e + sd*rng.standard_normal()  # relaxation in the new trap
    s_, x_, xn = s[1:-1], x[1:-1], x[2:]                              # state after relaxing in trap x_t; next signal x_{t+1}
    Imem = mi_gauss(s_, x_); Ipred = mi_gauss(s_, xn); Wd = W[1:].mean()   # W[t] uses s_t, x_t, x_{t+1}
    return Imem, Ipred, Wd
print(f"T=1. per-step quantities (nats).  bound: W_diss >= I_mem - I_pred")
print(f"{'a':>5}{'k':>6}{'kτ':>6}{'I_mem':>8}{'I_pred':>8}{'nonpred':>9}{'W_diss':>9}{'W/nonpred':>11}")
for a in [0.5, 0.9]:
    for k, tau in [(1.0, 0.2), (1.0, 1.0), (1.0, 5.0), (10.0, 0.5), (10.0, 5.0), (0.2, 5.0)]:
        Im, Ip, Wd = run(a, k, tau); np_ = Im - Ip
        print(f"{a:>5}{k:>6}{k*tau:>6.1f}{Im:>8.4f}{Ip:>8.4f}{np_:>9.4f}{Wd:>9.4f}{(Wd/np_ if np_ > 1e-6 else float('nan')):>11.2f}")
print("  nonpred = I_mem - I_pred = information the particle keeps about the signal that does not help predict its next value.")

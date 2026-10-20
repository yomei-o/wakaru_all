# Prediction D: antithetic ES cannot diffuse over the symmetric saddle (noise = 0 there), so it escapes by
# single big kicks. Large kicks from the left well always point right (g ~ 4 x sigma^2 eps^4, x<0).
# Rate (no fit): k = (1/r) * P( -r*g(x_min, eps) > |x_min| ),  r = eta/N  (sum of heavy tails ~ its max)
# => ln tau ~ (N/eta)^{1/2}, not Arrhenius ln tau ~ N/eta.
import sys, numpy as np
from scipy.stats import norm
sys.path.insert(0, r'C:\prog\claude\lines\scripts')
from es_trap_sim3 import run
s = 0.3; xm = np.sqrt(1-3*s*s); x = -xm
def g_of(e): return (4*x**3-4*x)*e**2 + 4*x*s*s*e**4         # antithetic single-sample estimator at x
# P(-r*g > xm): -g = a e^2 + b e^4 with a = -(4x^3-4x) (<0 here), b = -4 x s^2 (>0); solve b u^2 + a u - xm/r = 0, u = e^2
def p_jump(r):
    a, b = -(4*x**3-4*x), -4*x*s*s
    u = (-a + np.sqrt(a*a + 4*b*xm/r))/(2*b)
    return 2*norm.sf(np.sqrt(u))
print(f"antithetic ES, sigma={s}: single-jump prediction vs measurement (N=1, eta=r)")
print(f"{'r=eta/N':>9}{'pred tau':>11}{'measured':>11}{'esc%':>7}")
for r in [0.05, 0.03, 0.02, 0.0125, 0.01]:
    pred = 1/(p_jump(r)/r)
    m, f = run(s, 'anti', 0.0, r, 1, M=400, tcap=50*pred)
    print(f"{r:>9}{pred:>11.1f}{m:>11.1f}{f*100:>7.1f}", flush=True)

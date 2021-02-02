from classy import Class
import matplotlib.pyplot as plt
from math import pi
import numpy as np

kim_clTT = np.loadtxt("kim_n0_vrel0.txt")

params = {
    'dmb_target': 'hydrogen',   # set target
    'h': 0.67556,
    'omega_b': 0.022032,
    'omega_cdm': 1.0e-20,
    'omega_dmb': 0.12038,
    'sigma_dmb': 1.0e-25,
    'm_dmb': 1.0,
    'n_dmb': 0,
    'Vrel_dmb': 0,
    'Omega_k': 0.,
    'A_s': 2.215e-9,
    'n_s': 0.96,
    'tau_reio': 0.0925,
    'output': 'tCl',
}
cosmo = Class()
cosmo.set(params)
cosmo.compute()

cls = cosmo.raw_cl(2500)
ll = cls ['ell'][2:]
clTT = cls ['tt'][2:]

vera_clTT = clTT*ll*(ll+1)/2./pi
ell = ll

fig_TT, ax_TT = plt.subplots()

ax_TT.semilogx(ell,100*(vera_clTT-kim_clTT)/vera_clTT,linestyle='-')

cosmo.struct_cleanup()

ax_TT.set_title('Vrel values: Vera = 0, Kim = 0')
ax_TT.set_xlim([2,2500])
ax_TT.set_xlabel(r'$\ell$')
ax_TT.set_ylabel(r'$100 x (C_\ell^\mathrm{vera}-C_\ell^\mathrm{kim})/C_\ell^\mathrm{vera}$')
fig_TT.tight_layout()
fig_TT.savefig('vera_0_kim_0_n0.pdf')   # name output plot

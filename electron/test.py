from classy import Class

params = {
    'h': 0.67556,
    'omega_b': 0.022032,
    'omega_cdm': 1.0e-20,
    'omega_dmeff': 0.12038,
    'm_dmeff': 1.0,
    'sigma_dmeff': 0.0,
    'npow_dmeff': 0,
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

import matplotlib.pyplot as plt
from math import pi

plt.figure(1)
plt.xscale('log'); plt.yscale('linear');plt.xlim(2,2500)
plt.xlabel(r'$\ell$')
plt.ylabel(r'$[\ell(\ell+1)/2\pi] C_\ell^\mathrm{TT}$')
plt.plot(ll,clTT*ll*(ll+1)/2./pi,'r-')
plt.savefig('spectra_dmeff.pdf')

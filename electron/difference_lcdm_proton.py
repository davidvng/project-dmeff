from classy import Class
import matplotlib.pyplot as plt
from math import pi

params = {
    'h': 0.67556,
    'omega_b': 0.022032,
    'omega_cdm': 0.12038,
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

lcdmy = clTT*ll*(ll+1)/2./pi
lcdmx = ll

cosmo.struct_cleanup()

elecparams = {
    'h': 0.67556,
    'omega_b': 0.022032,
    'omega_cdm': 1.0e-20,
    'omega_dmeff': 0.12038,
    'm_dmeff': 1.0,
    'sigma_dmeff': 1.7e-25,
    'npow_dmeff': 0,
    'Omega_k': 0.,
    'A_s': 2.215e-9,
    'n_s': 0.96,
    'tau_reio': 0.0925,
    'output': 'tCl',
}

cosmo = Class()
cosmo.set(elecparams)
cosmo.compute()

cls = cosmo.raw_cl(2500)
ll = cls ['ell'][2:]
clTT = cls ['tt'][2:]

elecy = clTT*ll*(ll+1)/2./pi
elecx = ll

plt.figure(1)
plt.xscale('log'); plt.yscale('linear');plt.ylim(-3,3);plt.xlim(2,2500)
plt.xlabel(r'$\ell$')
plt.ylabel(r'$100 x (C_\ell^\mathrm{LCDM}-C_\ell^\mathrm{elec})/C_\ell^\mathrm{LCDM}$')
plt.plot(lcdmx,100*(lcdmy-elecy)/lcdmy,'r-')
plt.savefig('difference_lcdm_proton.pdf')

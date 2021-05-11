from classy import Class
import matplotlib.pyplot as plt
from math import pi
import numpy as np

params = {
    'dmb_target': 'electron',   # set target
    'h': 0.67556,
    'omega_b': 0.022032,
    'omega_cdm': 1.0e-20,
    'omega_dmb': 0.12038,
    'm_dmb': 1.0e-6,
    'n_dmb': 4,
    'Omega_k': 0.,
    'A_s': 2.215e-9,
    'n_s': 0.96,
    'tau_reio': 0.0925,
    'output': 'tCl,pCl,lCl,mPk','lensing':'yes','P_k_max_1/Mpc':3.0,
}

cosmo = Class()
cosmo.set(params)
cosmo.compute()

kk = np.logspace(-4,np.log10(50),1000)
Pk = []
for k in kk:
    Pk.append(cosmo.pk(k,0.)) # function .pk(k,z)
    
plt.figure(1)
plt.xscale('log');plt.yscale('log');plt.xlim(kk[0],kk[-1])
plt.xlabel(r'$k \,\,\,\, [h/\mathrm{Mpc}]$')
plt.ylabel(r'$P(k) \,\,\,\, [\mathrm{Mpc}/h]^3$')
plt.plot(kk,Pk,'b-')
plt.savefig('pk_dme_test.pdf')

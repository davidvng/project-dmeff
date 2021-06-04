from classy import Class
import matplotlib.pyplot as plt
from math import pi
import numpy as np

params = {
    'h': 0.67556,
    'omega_b': 0.022032,
    'omega_cdm': 0.12038,
    'Omega_k': 0.,
    'A_s': 2.215e-9,
    'n_s': 0.96,
    'tau_reio': 0.0925,
    'output': 'tCl,pCl,lCl,mPk','lensing':'yes','P_k_max_1/Mpc':200.0,
}

cosmo = Class()
cosmo.set(params)
cosmo.compute()

kk = np.logspace(-4,np.log10(200),1000)
Pk_lcdm = []
for k in kk:
    Pk_lcdm.append(cosmo.pk(k,0.)) # function .pk(k,z)

cosmo.struct_cleanup()

dmeparams = {
    'dmb_target': 'electron',   # set target
    'h': 0.67556,
    'omega_b': 0.022032,
    'omega_cdm': 1.0e-20,
    'omega_dmb': 0.12038,
    'm_dmb': 1.0,
    'n_dmb': -4,
    'Vrel_dmb': 30,
    'sigma_dmb': 1.0e-32,
    'Omega_k': 0.,
    'A_s': 2.215e-9,
    'n_s': 0.96,
    'tau_reio': 0.0925,
    'output': 'tCl,pCl,lCl,mPk','lensing':'yes','P_k_max_1/Mpc':200.0,
}

fig_TT, ax_TT = plt.subplots()

kk = np.logspace(-4,np.log10(200),1000)
legarray = ['CMB, mx=1 GeV, s0=1.0e-32 cm2']

M = Class()
M.set(dmeparams)
M.compute()

Pk_dme = []
for k in kk:
    Pk_dme.append(M.pk(k,0.)) # function .pk(k,z)

Pk = np.array(Pk_dme) / np.array(Pk_lcdm)

ax_TT.semilogx(kk,Pk,color='b',linestyle='-')

M.struct_cleanup()

#plt.xscale('log');plt.yscale('linear')
ax_TT.set_xlim(0.05,200)
ax_TT.set_ylim(0.005,1.05)
ax_TT.set_xticks([0.1,1,10,100])
ax_TT.set_xticklabels([0.1,1,10,100])
ax_TT.set_yticks([0.05,0.25,0.5,0.75,1.0])
ax_TT.set_yticklabels([0.05,0.25,0.5,0.75,1.0])
ax_TT.set_xlabel(r'$k \,\,\,\, [h/\mathrm{Mpc}]$')
ax_TT.set_ylabel(r'$P_{dme} / P_{LCDM}$')
ax_TT.legend(legarray)
fig_TT.tight_layout()
fig_TT.savefig('pk_n-4_MW.pdf')

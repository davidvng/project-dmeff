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

dmbparams = {
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
    'output': 'tCl',
}

var_name = 'log10sigma_dmb'   # set varying parameter
var_min = -29   # set min
offset = 6
var_max = var_min + offset   # set max
var_num = offset + 1   # set total amount of cases

kvec = np.logspace(-4,np.log10(3),1000)
legarray = []
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'purple', 'gray', 'maroon', 'navy', 'aqua']

fig_TT, ax_TT = plt.subplots()

for i in range(var_num):

    var = var_min + (var_max-var_min)*i/(var_num-1.)
    print('*Compute with %s=%e'%(var_name,var))
    
    legarray.append(np.power(10, var))
    var_color = colors[i%11]

    M = Class()
    M.set(dmbparams)
    M.set({var_name:var})
    M.compute()

    clM = M.raw_cl(2500)
    ll = clM['ell'][2:]
    clTT = clM['tt'][2:]
    
    dmby = clTT*ll*(ll+1)/2./pi
    dmbx = ll

    ax_TT.semilogx(lcdmx,100*(lcdmy-dmby)/lcdmy,color=var_color,linestyle='-')

    M.struct_cleanup()
    
ax_TT.set_xlim([2,2500])
ax_TT.set_xlabel(r'$\ell$')
ax_TT.set_ylabel(r'$100 x (C_\ell^\mathrm{LCDM}-C_\ell^\mathrm{dmb})/C_\ell^\mathrm{LCDM}$')
ax_TT.legend(legarray)
fig_TT.tight_layout()
fig_TT.savefig('dme_n4_1keV_cl_diffs_test.pdf')   # name output plot

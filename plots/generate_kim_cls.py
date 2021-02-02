from classy import Class
import matplotlib.pyplot as plt
from math import pi
import numpy as np

params = {
    'dmeff_target': 'hydrogen',   # set target
    'h': 0.67556,
    'omega_b': 0.022032,
    'omega_cdm': 1.0e-20,
    'omega_dmeff': 0.12038,
    'sigma_dmeff': 1.0e-25,
    'm_dmeff': 1.0,
    'npow_dmeff': 0,
    'Vrel_dmeff': 0,
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

print(lcdmy)
print(lcdmx)

a_file = open("kim_n0_vrel0.txt", "w")
np.savetxt(a_file, lcdmy)

a_file.close()

cosmo.struct_cleanup()

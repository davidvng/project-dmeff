from classy import Class
import numpy as np

params = {
    'dmb_target': 'electron',   # set target
    'h': 0.67556,
    'omega_b': 0.022032,
    'omega_cdm': 1.0e-20,
    'omega_dmb': 0.12038,
    'sigma_dmb': 2.25e-23,
    'm_dmb': 1.0e-3,
    'n_dmb': 2,
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

combined = np.vstack((ll,clTT)).T

a_file = open("dme_n2_1MeV.txt", "w")
np.savetxt(a_file, combined)

a_file.close()

cosmo.struct_cleanup()

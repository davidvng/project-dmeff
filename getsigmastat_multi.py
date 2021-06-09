from getdist import loadMCSamples

chains = ['dme_n-4_10MeV_vr30', 'dme_n-4_100keV_vr30', 'dme_n-4_10keV_vr30']
for i in range(len(chains)):
    sample = loadMCSamples(f'chains/{chains[i]}', settings={'ignore_rows': 0.3})
    stats = sample.getMargeStats()
    par1 = stats.parWithName('sigma_dmb')
    print(chains[i])
    print('sigma_dmb mean: %.5E std: %.5E lower: %.5E upper: %.5E (%s)'%(par1.mean, par1.err, par1.limits[1].lower, par1.limits[1].upper, '95%'))

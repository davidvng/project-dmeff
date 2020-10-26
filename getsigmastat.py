from getdist import loadMCSamples
sample = loadMCSamples('chains/dmb_test3', settings={'ignore_rows': 0.3})
stats = sample.getMargeStats()
par1 = stats.parWithName('sigma_dmb')
print('sigma_dmb mean: %.5E std: %.5E lower: %.5E upper: %.5E (%s)'%(par1.mean, par1.err, par1.limits[1].lower, par1.limits[1].upper, '95%'))

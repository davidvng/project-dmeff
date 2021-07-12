from getdist import loadMCSamples

#add chain names into array
chains = ['dmb_n6_1GeV_vr0','dmb_n6_1MeV_vr0_run2','dmb_n6_1keV_vr0_run2','dmb_n-2_1TeV_vr30_run2','dmb_n-4_1TeV_vr30_run2','dmb_n0_100MeV_vr0_run2','dmb_n0_10MeV_vr0_run2','dmb_n4_100MeV_vr0_run2','dmb_n6_10GeV_vr0_run2','dmb_n6_100MeV_vr0_run2','dmb_n2_1MeV_vr0_run2','dmb_n2_1keV_vr0_run2']
for i in range(len(chains)):
    sample = loadMCSamples(f'chains/{chains[i]}', settings={'ignore_rows': 0.3})
    print(chains[i], ": ", sample.confidence(10, 0.05, upper=True))

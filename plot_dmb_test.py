from getdist import plots

analysis_settings = {'ignore_rows': '0.3'}
g=plots.get_subplot_plotter(chain_dir=r'/home1/davidvng/repos/project-dmeff/chains',analysis_settings=analysis_settings)
roots = ['dmb_test']
params = ['omega_b', 'omega_dmb', 'H0', 'logA', 'n_s', 'tau_reio', 'sigma_dmb']
g.triangle_plot(roots, params, filled=True)
g.export('dmb_test.pdf')

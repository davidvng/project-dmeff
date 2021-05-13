For installation of python packages, run

    pip install -r requirements.txt

Launch the application with

    python tornadoserver.py

Then in any browser open the URL

    http://localhost:7777

------------------------------------------------------------

Cache files are located in cache/, so to clear the cache, run

    rm cache/*

------------------------------------------------------------

Running RSI with dark-matter baryon interactions

Run the following step and follow the rest from above:

    (In ../python/) python setup.py build

------------------------------------------------------------
Developing the code:

This commit adds the following changes to the files mentioned,

    In /Calc2D/
    1. TransferFunction.py (lines 14,49)
    2. CalculationClass.py (line 122)

    Updated the parameter value of omega_cdm = 10^-20 in settings.update() in order to switch
    from the standard cosmological model to the dmeff interacting model with
    omega_dmeff = omega_m - omega_b (Omega_matter - Omega_baryons)

    Also, in the Transfer Function, changed the transfer quantity for "d_cdm" to "d_dmeff"

    In /static/js/parameterConfig.js (lines 60, 78-101)
    Added sliders with appropriate minimum, maximum, and default values for dark-matter
    particle mass (m_dmeff), velocity dependence variance (npow_dmeff), and the interaction
    cross section for dark-matter baryon interactions (sigma_dmeff). These values can be input
    in the RealSpaceInterface after the application is launched.

    Note: For Sigma_dmeff, setting values must be done in the format 1.0e-22 which is 10^-22

    In static/js/simulation.js (lines 2,9)
    Changed the quantity "d_cdm" to "d_dmeff" in the start of the file to get the delta function
    for dark-matter baryon interactions instead of the Lambda CDM model

    In templates/Header.html (line 88)
    Changed every instance of cdm to dmeff to allow the frontend display to sync to dmeff variables
    on the back end

------------------------------------------------------------
Future possibilities:

    The RSI code can be changed to vary the ranges of interaction cross section, the possibilities of
    velocity dependence (can be expanded to n<0), and explored for a larger mass range.

    These changes can be made in /static/js/parameterConfig.js

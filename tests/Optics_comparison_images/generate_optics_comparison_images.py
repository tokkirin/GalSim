# Copyright (c) 2012-2023 by the GalSim developers team on GitHub
# https://github.com/GalSim-developers
#
# This file is part of GalSim: The modular galaxy image simulation toolkit.
# https://github.com/GalSim-developers/GalSim
#
# GalSim is free software: redistribution and use in source and binary forms,
# with or without modification, are permitted provided that the following
# conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions, and the disclaimer given in the accompanying LICENSE
#    file.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions, and the disclaimer given in the documentation
#    and/or other materials provided with the distribution.
#
"""This script generates images in tests/Optics_comparison_images/ used by a unit test
test_OpticalPSF_aberration() in tests/test_optics.py.
Images in the directory is generated by using commit 1833aa076ab7878439fcd40c4610cf761d4afd6b
"""
import os
import sys

import galsim

if __name__ == "__main__":
    lod = 0.04
    obscuration = 0.3
    imsize = 128

    # predefine image of fixed size for drawing into
    im = galsim.ImageD(imsize, imsize)

    # defocus
    optics = galsim.optics.OpticalPSF(lod, defocus = .5, obscuration = obscuration, oversampling=1)
    im = optics.draw(im, dx=0.2*lod)
    im.write(os.path.join(os.path.abspath(os.path.dirname(__file__)), "optics_defocus.fits"))

    # astig1
    optics = galsim.optics.OpticalPSF(lod, defocus = .5, astig1 = .5, obscuration = obscuration,
                                      oversampling=1)
    im = optics.draw(im, dx=0.2*lod)
    im.write(os.path.join(os.path.abspath(os.path.dirname(__file__)), "optics_astig1.fits"))

    # astig2
    optics = galsim.optics.OpticalPSF(lod, defocus = .5, astig2 = .5, obscuration = obscuration,
                                      oversampling=1)
    im = optics.draw(im, dx=0.2*lod)
    im.write(os.path.join(os.path.abspath(os.path.dirname(__file__)), "optics_astig2.fits"))

    # coma1
    optics = galsim.optics.OpticalPSF(lod, coma1 = .5, obscuration = obscuration, oversampling=1)
    im = optics.draw(im, dx=0.2*lod)
    im.write(os.path.join(os.path.abspath(os.path.dirname(__file__)), "optics_coma1.fits"))

    # coma2
    optics = galsim.optics.OpticalPSF(lod, coma2 = .5, obscuration = obscuration, oversampling=1)
    im = optics.draw(im, dx=0.2*lod)
    im.write(os.path.join(os.path.abspath(os.path.dirname(__file__)), "optics_coma2.fits"))

    # trefoil1
    optics = galsim.optics.OpticalPSF(lod, trefoil1 = .5, obscuration = obscuration, oversampling=1)
    im = optics.draw(im, dx=0.2*lod)
    im.write(os.path.join(os.path.abspath(os.path.dirname(__file__)), "optics_trefoil1.fits"))

    # trefoil2
    optics = galsim.optics.OpticalPSF(lod, trefoil2 = .5, obscuration = obscuration, oversampling=1)
    im = optics.draw(im, dx=0.2*lod)
    im.write(os.path.join(os.path.abspath(os.path.dirname(__file__)), "optics_trefoil2.fits"))

    # spherical
    optics = galsim.optics.OpticalPSF(lod, spher = .5, obscuration = obscuration, oversampling=1)
    im = optics.draw(im, dx=0.2*lod)
    im.write(os.path.join(os.path.abspath(os.path.dirname(__file__)), "optics_spher.fits"))

    # all aberrations
    optics = galsim.optics.OpticalPSF(
        lod, defocus=.5, astig1=0.5, astig2=0.3, coma1=0.4, coma2=-0.3, trefoil1=-0.2,
        trefoil2=0.1, spher=-0.8, obscuration=obscuration, oversampling=1)
    im = optics.draw(im, dx=0.2*lod)
    im.write(os.path.join(os.path.abspath(os.path.dirname(__file__)), "optics_all.fits"))

    # 5 support struts in the pupil plane, of thickness 4% of the pupil diameter, with the
    # uppermost strut angled at 8 degrees to the vertical, with a touch of astigmatism, coma and
    # defocus
    optics = galsim.optics.OpticalPSF(
        lod, obscuration=obscuration, nstruts=5, strut_thick=0.04, strut_angle=8.*galsim.degrees,
        astig2=0.04, coma1=-0.07, defocus=0.09, oversampling=1)
    im = optics.draw(im, dx=0.2*lod)
    im.write(os.path.join(os.path.abspath(os.path.dirname(__file__)), "optics_struts.fits"))

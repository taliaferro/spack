# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-norbert
#
# You can edit this file again by typing:
#
#     spack edit py-norbert
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyNorbert(PythonPackage):
    """
    Norbert is an implementation of the multichannel Wiener filter, that is a 
    very popular way of filtering multichannel audio in the time-frequency 
    domain for several applications, notably speech enhancement and source 
    separation.
    """

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://sigsep.github.io/norbert/"
    pypi = "norbert/norbert-0.2.1.tar.gz"

    license("MIT", checked_by="taliaferro")

    version("0.2.1", sha256="bd4cbc2527f0550b81bf4265c1a64b352cab7f71e4e3c823d30b71a7368de74e")

    depends_on("py-setuptools", type="build")
    depends_on("py-scipy", type="run")


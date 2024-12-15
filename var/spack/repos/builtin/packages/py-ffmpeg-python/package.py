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
#     spack install py-ffmpeg-python
#
# You can edit this file again by typing:
#
#     spack edit py-ffmpeg-python
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyFfmpegPython(PythonPackage):
    """
    Python bindings for ffmpeg with complex filter support.
    """

    homepage = "https://github.com/kkroening/ffmpeg-python"
    pypi = "ffmpeg-python/ffmpeg-python-0.2.0.tar.gz"

    license("Apache-2.0", checked_by="taliaferro")

    version("0.2.0", sha256="65225db34627c578ef0e11c8b1eb528bb35e024752f6f10b78c011f6f64c4127")

    depends_on("py-setuptools", type="build")

    depends_on("py-future", type="run")
    depends_on("ffmpeg", type="run")


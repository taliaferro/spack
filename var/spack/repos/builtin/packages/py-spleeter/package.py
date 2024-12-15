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
#     spack install py-spleeter
#
# You can edit this file again by typing:
#
#     spack edit py-spleeter
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PySpleeter(PythonPackage):
    """
    Spleeter is Deezer's audio source-separation library with pretrained models.
    """

    homepage = "https://research.deezer.com/projects/spleeter.html"
    pypi = "spleeter/spleeter-2.4.0.tar.gz"

    license("MIT", checked_by="taliaferro")

    version("2.4.0", sha256="6da636b7a39b363fc8410988d093ed067d0de6dcc689bed27ac419ee22e95ae5")
    
    # variant("musdb", default=False, description="Include dependencies for parsing MUSDB18 source-separation dataset.")

    depends_on("py-poetry-core", type="build")

    with when("@2.4.0"):
        depends_on("python@3.7.1:3.10", type=("build", "run"))
        depends_on("py-ffmpeg-python@0.2.0:", type="run") # TODO
        depends_on("py-httpx+http2@0.2.0:", type="run")
        depends_on("py-typer@0.3.2:", type="run")
        depends_on("py-tensorflow@2.5.0:2.10.0", type="run")
        depends_on("py-pandas@1.3.0:", type="run")
        depends_on("py-norbert@0.2.1:", type="run") # TODO
        depends_on("py-numpy@:1.999.0", type="run") # numpy < 2.0.0
        # depends_on("py-musdb@0.4.0:", when="+musdb")
        # depends_on("py-museval@0.4.0:", when="+musdb")
        


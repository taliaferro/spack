# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Act(GoPackage):
    """Run your GitHub Actions locally!"""

    homepage = "https://nektosact.com/"
    url = "https://github.com/nektos/act/archive/refs/tags/v0.2.66.tar.gz"

    license("MIT", checked_by="taliaferro")

    version("0.2.66", sha256="128a88d966df451730448235ca0d5c804a642fc5f183fb613a5f4f92d9dc12e7")




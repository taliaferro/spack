# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Dqlite(AutotoolsPackage):
    """
    Embeddable, replicated and fault-tolerant SQL engine.
    """

    homepage = "https://dqlite.io"
    url = "https://github.com/canonical/dqlite/archive/refs/tags/v1.16.7.tar.gz"

    maintainers("taliaferro")

    license("LGPL-3.0", checked_by="taliaferro")

    version("1.16.7", sha256="5a4d202940147e2552009cd8d4a5166a749ff6275ae8bef652c97529bb4b530f")

    depends_on("c", type="build")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")

    depends_on("sqlite")
    depends_on("libuv")
    depends_on("lz4")

    def autoreconf(self, spec, prefix):
        autoreconf("--install", "--verbose", "--force")


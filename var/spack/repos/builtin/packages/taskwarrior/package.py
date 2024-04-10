# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Taskwarrior(CMakePackage):
    """
    Taskwarrior is Free and Open Source Software that manages your TODO list
    from the command line.  It is flexible, fast, and unobtrusive. It does
    its job then gets out of your way.
    """

    homepage = "https://taskwarrior.org/"
    url = "https://github.com/GothenburgBitFactory/taskwarrior/releases/download/v3.0.0/task-3.0.0.tar.gz"

    maintainers("taliaferro")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("MIT", checked_by="taliaferro")

    version("3.0.0", sha256="30f397081044f5dc2e5a0ba51609223011a23281cd9947ea718df98d149fcc83")
    version("2.6.2", sha256="b1d3a7f000cd0fd60640670064e0e001613c9e1cb2242b9b3a9066c78862cfec")

    depends_on("gnutls")
    depends_on("libuuid")
    depends_on("rust@1.64.0:", when="@3.0.0:")

    def patch(self):
      if self.spec.satisfies("@3.0.0:"):
        # new major release adds rust to the codebase. A bug in cmake/Corrosion
        # causes release builds of the integration tests to fail.
        # See https://github.com/GothenburgBitFactory/taskwarrior/issues/3294
        filter_file('"taskchampion/integration-tests",', "", "Cargo.toml")


# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Elixir(MakefilePackage):
    """
    Elixir is a dynamic, functional language for building scalable and maintainable applications.
    """

    homepage = "https://elixir-lang.org/"
    url = "https://github.com/elixir-lang/elixir/archive/refs/tags/v1.17.2.tar.gz"

    maintainers("taliaferro")

    license("Apache-2.0", checked_by="taliaferro")

    version("1.17.2", sha256="7bb8e6414b77c1707f39f620a2ad54f68d64846d663ec78069536854247fb1ab")

    depends_on("erlang")
    def setup_build_environment(self, env):
        env.set("PREFIX", prefix)


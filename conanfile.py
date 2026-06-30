from conan import ConanFile
from conan.errors import ConanInvalidConfiguration
from conan.tools.files import copy, collect_libs
from conan.tools.microsoft import MSBuild, MSBuildToolchain
import os

class LokiConan(ConanFile):
    name = "loki"
    description = "C++ library of designs, containing flexible implementations of common design patterns and idioms"
    author = "CSW <csw@werfen.com>"
    topics = ("conan", "loki")
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"

    exports_sources = (
        "src/*",
        "include/*",
        "test/*",
        "Loki.sln",
        "!src/Debug/*",
        "!src/Release/*"
    )

    def generate(self):
        msbuild_tc = MSBuildToolchain(self)
        msbuild_tc.generate()

    def build(self):
        msbuild = MSBuild(self)

        arch = str(self.settings.arch)
        if arch == "x86":
            msbuild.platform = "Win32"
        else:
            raise ConanInvalidConfiguration(f"Loki does not support '{arch}' architecture")

        msbuild.build(
            sln=os.path.join(self.source_folder, "Loki.sln"),
            targets=["Library", "UnitTest"]
        )

    def package(self):
        if self.settings.build_type == "Debug":
            binaries_folder = os.path.join(self.source_folder, "lib", "Debug") 
        else:
            binaries_folder = os.path.join(self.source_folder, "lib", "Release") 
            
        copy(self, "*.h",   dst=os.path.join(self.package_folder, "include", "loki"), src=os.path.join(self.source_folder, "include", "loki"))
        copy(self, "*.lib", dst=os.path.join(self.package_folder, "lib"), src=binaries_folder)
        copy(self, "*.pdb", dst=os.path.join(self.package_folder, "lib"), src=binaries_folder)

    def package_info(self):
        self.cpp_info.libs = collect_libs(self)
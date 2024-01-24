from conans import ConanFile, tools


class LokiConan(ConanFile):
    name = "Loki"
    description = "C++ library of designs, containing flexible implementations of common design patterns and idioms"
    author = "CSW <csw@werfen.com>"
    topics = ("conan", "loki")
    license = "MIT"
    generators = "visual_studio"
    settings = "os", "compiler", "build_type", "arch"

    def package(self):
        self.copy("*.h", dst="include/loki", src="include/loki")
        self.copy("*.lib", dst="lib", src=("src/%s" % self.settings.build_type))
        self.copy("*.pdb", dst="lib", src=("src/%s" % self.settings.build_type))

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
from conan import ConanFile
from conan.errors import ConanInvalidConfiguration
from conan.tools.files import collect_libs
from conan.tools.microsoft import MSBuild


class LokiConan(ConanFile):
	name = "Loki"
	description = "C++ library of designs, containing flexible implementations of common design patterns and idioms"
	author = "CSW <csw@werfen.com>"
	topics = ("conan", "loki")
	license = "MIT"
	package_type = "library"
	settings = "os", "compiler", "build_type", "arch"

	def build(self):
		msbuild = MSBuild(self)
		msbuild.build_type = self.settings.build_type
		arch = self.settings.get_safe('arch')
		if arch == 'x86':
			msbuild.platform = 'Win32'
		else:
			raise ConanInvalidConfiguration(f"Loki does not support '{arch}' architecture")
		msbuild.build(sln='Loki.sln', targets=['Library'])

	def package(self):
		binaries_folder = f"lib/{self.settings.build_type}"
		
		self.copy("*.h", dst="include/loki", src="include/loki")
		self.copy("*.lib", dst="lib", src=binaries_folder)
		self.copy("*.pdb", dst="lib", src=binaries_folder)

	def package_info(self):
		self.cpp_info.libs = collect_libs(self)
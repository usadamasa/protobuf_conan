from conans import ConanFile, CMake, tools


class ProtobufConan(ConanFile):
    name = "protobuf"
    version = "3.5.1.1"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Protobuf here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"

    def source(self):
        self.run('git clone --depth=1 -b v%s https://github.com/google/protobuf.git' % self.version)

    def build(self):
        with tools.chdir('protobuf'):
            self.run("./autogen.sh")
            self.run("./configure --prefix=${PWD}/installed")
            self.run("make -j2")
            self.run("make install")

    def package(self):
        self.copy("*.h", dst="include", src="protobuf/installed/include")
        self.copy("*proto*.lib", dst="lib", keep_path=False)
        self.copy("*proto*.dll", dst="bin", keep_path=False)
        self.copy("*proto*.so", dst="lib", keep_path=False)
        self.copy("*proto*.dylib", dst="lib", keep_path=False)
        self.copy("*proto*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["protobuf"]

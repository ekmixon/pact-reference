from conans import ConanFile, VisualStudioBuildEnvironment, CMake, tools

class CbindgenTestConan(ConanFile):
    name = "pact_ffi"
    version = "0.0.4"
    description = "Pact/Rust FFI bindings"
    url = "https://pactfoundation.jfrog.io/artifactory/pactfoundation-conan/"
    homepage = "https://github.com/pact-foundation/pact-reference"
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    no_copy_source = True
    requires = "openssl/1.1.1k"
    topics = ("pact", "consumer-driven-contracts", "contract-testing", "mock-server")

    def build(self):
        if self.settings.os == "Windows":
            url = f"https://github.com/pact-foundation/pact-reference/releases/download/libpact_ffi-v{str(self.version)}/pact_ffi-windows-x86_64.lib.gz"

            tools.download(url, "pact_ffi.lib.gz")
            tools.unzip("pact_ffi.lib.gz")
        elif self.settings.os == "Linux":
            url = f"https://github.com/pact-foundation/pact-reference/releases/download/libpact_ffi-v{str(self.version)}/libpact_ffi-linux-x86_64.a.gz"

            tools.download(url, "libpact_ffi.a.gz")
            tools.unzip("libpact_ffi.a.gz")
        elif self.settings.os == "Macos":
            url = f"https://github.com/pact-foundation/pact-reference/releases/download/libpact_ffi-v{str(self.version)}/libpact_ffi-osx-x86_64.a.gz"

            tools.download(url, "libpact_ffi.a.gz")
            tools.unzip("libpact_ffi.a.gz")
        else:
            raise Exception("Binary does not exist for these settings")
        tools.download(
            f"https://github.com/pact-foundation/pact-reference/releases/download/libpact_ffi-v{str(self.version)}/pact.h",
            "include/pact.h",
        )

        tools.download(
            f"https://github.com/pact-foundation/pact-reference/releases/download/libpact_ffi-v{str(self.version)}/pact-cpp.h",
            "include/pact-cpp.h",
        )

    def package(self):
        self.copy("libpact_ffi*.a", "lib", "")
        self.copy("pact_ffi*.lib", "lib", "")
        self.copy("*.h", "", "")

    def package_info(self):  # still very useful for package consumers
        self.cpp_info.libs = ["pact_ffi"]

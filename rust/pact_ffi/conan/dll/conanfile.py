from conans import ConanFile, VisualStudioBuildEnvironment, CMake, tools

class CbindgenTestConan(ConanFile):
    name = "pact_ffi_dll"
    version = "0.0.4"
    description = "Pact/Rust FFI bindings (DLL/Shared Lib)"
    url = "https://pactfoundation.jfrog.io/artifactory/pactfoundation-conan/"
    homepage = "https://github.com/pact-foundation/pact-reference"
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    no_copy_source = True
    requires = "openssl/1.1.1k"
    topics = ("pact", "consumer-driven-contracts", "contract-testing", "mock-server")

    def build(self):
        if self.settings.os == "Windows":
            url = f"https://github.com/pact-foundation/pact-reference/releases/download/libpact_ffi-v{str(self.version)}/pact_ffi-windows-x86_64.dll.gz"

            tools.download(url, "pact_ffi.dll.gz")
            tools.unzip("pact_ffi.dll.gz")
            url = f"https://github.com/pact-foundation/pact-reference/releases/download/libpact_ffi-v{str(self.version)}/pact_ffi-windows-x86_64.dll.lib.gz"

            tools.download(url, "pact_ffi.dll.lib.gz")
            tools.unzip("pact_ffi.dll.lib.gz")
        elif self.settings.os == "Linux":
            url = f"https://github.com/pact-foundation/pact-reference/releases/download/libpact_ffi-v{str(self.version)}/libpact_ffi-linux-x86_64.so.gz"

            tools.download(url, "libpact_ffi.so.gz")
            tools.unzip("libpact_ffi.so.gz")
        elif self.settings.os == "Macos":
            url = f"https://github.com/pact-foundation/pact-reference/releases/download/libpact_ffi-v{str(self.version)}/libpact_ffi-osx-x86_64.dylib.gz"

            tools.download(url, "libpact_ffi.dylib.gz")
            tools.unzip("libpact_ffi.dylib.gz")
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
        self.copy("libpact_ffi*.so", "lib", "")
        self.copy("libpact_ffi*.dylib", "lib", "")
        self.copy("pact_ffi*.lib", "lib", "")
        self.copy("pact_ffi*.dll", "bin", "")
        self.copy("*.h", "", "")

    def package_info(self):  # still very useful for package consumers
        self.cpp_info.libs = ["pact_ffi"]

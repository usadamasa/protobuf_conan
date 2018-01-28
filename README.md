# conanfile for protobuf

Generate [conan](https://www.conan.io/) package for protobuf.

# Supporting Platform

## Supported

| OS          | Compiler   | Build Config     |
|-------------|------------|------------------|
| [OSX](#OSX) | Apple-LLVM | {Dynamic,Static} |

## In Progress

| OS                  | Compiler    | Build Config                     |
|---------------------|-------------|----------------------------------|
| [Ubuntu](#Ubuntu)   | {gcc,clang} | {Dynamic,Static}                 |
| [Windows](#Windows) | msvc2012    | {MD,MT,MTd,MDd}/{Dynamic,Static} |

# Usage

## OSX

``` {.bash}
# if you first time.
sudo xcode-select --install
brew install \
    autoconf \
    automake \
    conan \
    libtool \

# building
conan create . protobuf/3.5.1+build1@${CONAN_USER}/${CONAN_CHANNEL} \
    -s compiler=apple-clang \
    -s compiler.libcxx=libc++ \
    -s compiler.version=9.0 \

# uploading
conan upload --all protobuf/3.5.1+build1@${CONAN_USER}/${CONAN_CHANNEL}

```

## Ubuntu
T.B.D.

## Windows
T.B.D. ( reference official https://github.com/google/protobuf/blob/master/cmake/README.md )\
TO specific {MT,MD}/{Debug,Release} Build Configs.

{
  description = "C++ Development Environment with Clang and Modern Libraries";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            # 编译工具
            gcc
            clang-tools
            lldb
            cmake
            ninja
            direnv
            clang
            gnumake
            gdb
            libglvnd
            mesa
            libGL
            linuxHeaders
            pkg-config

            vulkan-tools
            vulkan-loader
            vulkan-validation-layers
            vulkan-headers
            
            # C++ 库
            spdlog
            fmt
            nlohmann_json
            pugixml
            wayland
            libffi
            sdl3
          ];

          shellHook = ''
            echo "🚀 C++ Development Environment Ready!"
            echo ""
            echo "📦 Available Libraries:"
            echo "  • spdlog (logging): ${pkgs.spdlog}"
            echo "  • fmt (formatting): ${pkgs.fmt}"
            echo "  • boost: ${pkgs.boost}"
            echo "  • catch2 (testing): ${pkgs.catch2_3}"
            echo "  • nlohmann_json: ${pkgs.nlohmann_json}"
            echo "  • protobuf: ${pkgs.protobuf}"
            echo "  • grpc: ${pkgs.grpc}"
            echo ""
            echo "🔧 Build Tools:"
            echo "  • Compiler: $(clang++ --version | head -n1)"
            echo "  • CMake: $(cmake --version | head -n1)"
            echo ""
            
            # 环境变量
            export CXX=clang++
            export CC=clang
            export CXXFLAGS="-std=c++23"
            
            # CMake 配置
            export CMAKE_PREFIX_PATH="${pkgs.spdlog}:${pkgs.fmt}:${pkgs.boost}:${pkgs.catch2_3}:${pkgs.nlohmann_json}:${pkgs.protobuf}:${pkgs.grpc}:$CMAKE_PREFIX_PATH"
            export PKG_CONFIG_PATH="${pkgs.spdlog}/lib/pkgconfig:${pkgs.fmt}/lib/pkgconfig:${pkgs.protobuf}/lib/pkgconfig:${pkgs.grpc}/lib/pkgconfig:$PKG_CONFIG_PATH"
            
            # 别名
            alias cppbuild="clang++ -std=c++23 -Wall -Wextra -O2"
            alias cppdebug="clang++ -std=c++23 -Wall -Wextra -g -O0"
            alias cbuild="cmake --build build"
            alias cconfig="cmake -B build -DCMAKE_BUILD_TYPE=Release"
            alias cdebug="cmake -B build -DCMAKE_BUILD_TYPE=Debug"
          '';
          
          # 为 C++ 项目设置的环境变量
          CMAKE_BUILD_TYPE = "Debug";
          CMAKE_EXPORT_COMPILE_COMMANDS = "ON";
        };
      }
    );
}

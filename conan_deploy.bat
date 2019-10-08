conan export-pkg . Loki/0.1.7@systelab/stable -s arch=x86 -s build_type=Debug -s compiler.toolset=v141 -s compiler.version=15 -s compiler.runtime=MDd --force
conan export-pkg . Loki/0.1.7@systelab/stable -s arch=x86 -s build_type=Release -s compiler.toolset=v141 -s compiler.version=15 -s compiler.runtime=MD --force
conan upload Loki/0.1.7@systelab/stable --all -r systelab-test --force

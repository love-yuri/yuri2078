# Apollo指南

> 写于 2024-4-6 Apollo-version: 9.0

## 安装

> 这部分可以看[官方说明](https://apollo.baidu.com/community/Apollo-Homepage-Document?doc=BYFxAcGcC4HpYIbgPYBtXIHQCMEEsATAV0wGNkBbWA5UyRFdZWVBEAU0hFgoIH0adPgCY%2BADwCiAVnEBBCeIAcATnETFcgMxKZkgGxKAwkoDsa3YoAi45WdGSLxsYt0SzY%2BXICMa98oAMSgYALF7%2B2NhemsLBJsrCYZqKwors7AikBIp6miYmpFJSXpigFKhAA)
>
> 这部分可以看[官方说明](https://apollo.baidu.com/community/Apollo-Homepage-Document?doc=BYFxAcGcC4HpYIbgPYBtXIHQCMEEsATAV0wGNkBbWA5UyRFdZWVBEAU0hFgoIH0adPgCY%2BADwCiAVnEBBCeIAcATnETFcgMxKZkgGxKAwkoDsa3YoAi45WdGSLxsYt0SzY%2BXICMa98oAMSgYALF7%2B2NhemsLBJsrCYZqKwors7AikBIp6miYmpFJSXpigFKhAA)
>
> 这部分可以看[官方说明](https://apollo.baidu.com/community/Apollo-Homepage-Document?doc=BYFxAcGcC4HpYIbgPYBtXIHQCMEEsATAV0wGNkBbWA5UyRFdZWVBEAU0hFgoIH0adPgCY%2BADwCiAVnEBBCeIAcATnETFcgMxKZkgGxKAwkoDsa3YoAi45WdGSLxsYt0SzY%2BXICMa98oAMSgYALF7%2B2NhemsLBJsrCYZqKwors7AikBIp6miYmpFJSXpigFKhAA)

1. 安装docker

2. 添加软件源

   ```bash
   sudo mkdir -p /etc/apt/sources.list.d/
   sudo touch /etc/apt/sources.list.d/apolloauto.list
   sudo echo 'deb [arch=amd64 signed-by=/etc/apt/keyrings/apolloauto.gpg] https://apollo-pkg-beta.cdn.bcebos.com/apollo/core \
   bionic main' >> /etc/apt/sources.list.d/apolloauto.list
   ```

3. 开始安装

   ```bash
   sudo apt install apollo-neo-env-manager-dev --reinstall
   git clone https://github.com/ApolloAuto/application-core.git apollo
   cd apollo
   aem start
   aem enter # 进入容器
   ```

4. 编译模块
   - `buildtool build -p core` 编译core模块
   - `buildtool install routing planning-*` 安装routing 和 planning 的所有模块

## 配置场景集

> 需要先进行安装。 本次使用新版界面。老的界面可以去看官方的 [Profile安装教程](https://apollo.baidu.com/community/article/1031)

1. 复制个人链接

   1. 打开[链接](https://apollo.baidu.com/workspace)
   2. 点击右上角个人信息
   3. 点击左侧服务权益
   4. 点击仿真
   5. 点击插件安装 -> 重置
   6. 复制链接到apollo 容器，直接终端运行。

2. 启动 `Dreamview` -> `aem bootstrap start --plus`

3. 点击资源管理

   ![image-20240409213711578](/home/yuri/love-yuri/learn/notes/markdown/Apollo指南.assets/image-20240409213711578.png)

4. 选择场景， 没有场景集的自己去控制台下载场景集

5. 然后点击右侧下载

6. 选择指定部分

   1. 模式选择: Pnc
   2. 模块开启 Planning
   3. 操作选择 Scenario_Sim
   4. 点击当前资源里的任意一个
   5. 

   ![image-20240409213922908](/home/yuri/love-yuri/learn/notes/markdown/Apollo指南.assets/image-20240409213922908.png)

7. 点击左下角开始

   ![image-20240409214058865](/home/yuri/love-yuri/learn/notes/markdown/Apollo指南.assets/image-20240409214058865.png)



## clangd

> 如果优雅的使用clangd 进行开发? 如果有需要使用 vscode的clangd插件进行开发的可以用这个
>
> 这部分按需使用！！！！
>
> 这部分按需使用！！！！
>
> 这部分按需使用！！！！

### 重新安装python3.9

> 因为bazel 转compile_commands.json 的脚本最低需要python 3.9 而apollo只有 3.6所以需要重新安装。亲测 3.9.7可行

```bash
# 安装python3.9， 只在python3.9测试。 下面一行直接复制就行了
sudo apt-get remove python && cd ~ && mkdir yuri && cd yuri && sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget -y && wget -c 'https://registry.npmmirror.com/-/binary/python/3.9.7/Python-3.9.7.tgz' && tar -xf Python-3.9.7.tgz && cd Python-3.9.7 && ./configure --enable-optimizations && make && sudo make altinstall

python3.9 --version # 验证结果， 如果正确输出再进行下一步

# 设置默认python 版本
sudo update-alternatives --install /usr/bin/python3 python /usr/local/bin/python3.9 2 && sudo update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.9 2
```

### 安装pip

> 重新安装python pip会出问题，需要重新安装pip

```bash
# 重新安装pip
cd ~/yuri && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3 get-pip.py --index-url https://pypi.tuna.tsinghua.edu.cn/simple && pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 重新安装两个库，不然buildtool 会报错
pip install requests jinja2 && sudo cp /usr/lib/python3/dist-packages/lsb_release.py /usr/bin/
```

### 测试

使用buildtool 测试是否能够正常使用。

### 生成 compile_commands.json

> 以下所有操作都在 `/apollo_workspace` 目录下进行

1. 将planning常用包添加到本地

   `buildtool install routing cyber planning-*`

2. 先进行编译: `buildtool build -p planning`

3. 打开`/apollo_workspace/WORKSPACE`， 在顶部添加

   ```bash
   load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
   
   
   # Hedron's Compile Commands Extractor for Bazel
   # https://github.com/hedronvision/bazel-compile-commands-extractor
   http_archive(
       name = "hedron_compile_commands",
   
       # Replace the commit hash (0e990032f3c5a866e72615cf67e5ce22186dcb97) in both places (below) with the latest (https://github.com/hedronvision/bazel-compile-commands-extractor/commits/main), rather than using the stale one here.
       # Even better, set up Renovate and let it do the work for you (see "Suggestion: Updates" in the README).
       url = "https://github.com/hedronvision/bazel-compile-commands-extractor/archive/0e990032f3c5a866e72615cf67e5ce22186dcb97.tar.gz",
       strip_prefix = "bazel-compile-commands-extractor-0e990032f3c5a866e72615cf67e5ce22186dcb97",
       # When you first run this tool, it'll recommend a sha256 hash to put here with a message like: "DEBUG: Rule 'hedron_compile_commands' indicated that a canonical reproducible form can be obtained by modifying arguments sha256 = ..."
   )
   load("@hedron_compile_commands//:workspace_setup.bzl", "hedron_compile_commands_setup")
   hedron_compile_commands_setup()
   load("@hedron_compile_commands//:workspace_setup_transitive.bzl", "hedron_compile_commands_setup_transitive")
   hedron_compile_commands_setup_transitive()
   load("@hedron_compile_commands//:workspace_setup_transitive_transitive.bzl", "hedron_compile_commands_setup_transitive_transitive")
   hedron_compile_commands_setup_transitive_transitive()
   load("@hedron_compile_commands//:workspace_setup_transitive_transitive_transitive.bzl", "hedron_compile_commands_setup_transitive_transitive_transitive")
   hedron_compile_commands_setup_transitive_transitive_transitive()
   
   
   ```

   

4. 在 `/apollo_workspace` 下新建`BUILD` 文件。加入

   ```bash
   load("@hedron_compile_commands//:refresh_compile_commands.bzl", "refresh_compile_commands")
   
   refresh_compile_commands(
       name = "refresh_compile_commands",
   
       # Specify the targets of interest.
       # For example, specify a dict of targets and any flags required to build.
       # 需要编译的目标文件
       targets = {
         "//modules/planning/planning_component:libplanning_component.so": "",
         "//modules/planning/planning_interface_base:apollo_planning_planning_interface_base": "",
         "//modules/planning/planning_base:apollo_planning_planning_base":"",
         "//cyber":"",
       },
       # No need to add flags already in .bazelrc. They're automatically picked up.
       # If you don't need flags, a list of targets is also okay, as is a single target string.
       # Wildcard patterns, like //... for everything, *are* allowed here, just like a build.
         # As are additional targets (+) and subtractions (-), like in bazel query https://docs.bazel.build/versions/main/query.html#expressions
       # And if you're working on a header-only library, specify a test or binary target that compiles it.
   )
   
   ```

5. 在终端中运行 `bazel run :refresh_compile_commands`

6. 执行如下命令，拷贝pb文件

7. ```bash
   #!/bin/bash
   ###
    # @Author: love-yuri yuri2078170658@gmail.com
    # @Date: 2024-04-08 20:25:38
    # @LastEditTime: 2024-04-09 21:59:54
    # @Description: apollo 脚本
   ### 
   
   basePath="/opt/apollo/neo/include/"
   targetPat="/usr/include/"
   
   # 查找pb文件
   result=$(sudo find "$basePath" -name "*.pb.h" | uniq)
   
   # 输出结果
   for item in $result; do
     oriPath=${item/$basePath}
     dirPath=$(dirname $oriPath)
     echo "sudo cp ${item} ${targetPat}${oriPath}"
     sudo mkdir -p  "${targetPat}${dirPath}"
     sudo cp "${item}" "${targetPat}${oriPath}"
   done
   ```

   

1. 
# git命令

## 全局设置

+ ``` git config --global user.name "love-yuri" ``` 设置用户名
+ ``` git config --global user.email "yuri2078170658@gmail.com" ``` 设置邮箱账号
+ ``` git config --global http.sslVerify "false" ``` 取消全局验证
+ `ssh-keygen -t ed25519 -C "yuri2078170658@gmail.com"` 生成密钥

## 取消全局代理

+ ``` git config --global --unset http.proxy ```
+ ``` git config --global --unset https.proxy ```

## 常用命令

+ ``` git add file-name ``` 添加指定文件
+ ``` git add . ``` 添加目录下所有文件
+ ``` git commit -a ``` 提交文件 然后进行编辑
+ ``` git commit -m "main" ``` 提交文件并以 “main” 作为提交
+ ``` git branch -M main ``` 新建分支
+ ``` git push -u origin main ``` 推送文件到main 分支
+ ``` git log ``` 查看历史提交日志
+ `git update-index --assume-unchanged <file>` git不再追踪该文件的更改   
+ `git branch --set-upstream-to=origin/master master` 设置本地分支同步更新远程分支
+ `git remote -v` 查看远程分支情况

## 回退操作

- ```` git fetch --all ```` 拉取所有远程更新
- ``` git reset --hard commit_id ``` 回退到指定commit
- `git reset --hard HEAD~1` 回退指定个数的commit
- ` git push --force origin main` 强制推送-覆盖远程分支

> 以下回退操作HEAD~1 回退一个commit，他会带着 merge 的 commit 一起回退

- `git reset --hard origin/main` 回退/同步到远程分支 （丢弃本地修改)
- `git reset origin/main` 回退/同步到远程分支 （保留本地修改)
- `git reset --hard HEAD~1` 撤销commit 并且不会保留更改
- `git reset --mixed HEAD~1` 撤销commit 并且保留更改 - 不会添加到暂存区
- `git reset --soft HEAD~1` 撤销commit 并且保留更改 - 会添加到暂存区

> 回退结束后使用该指令强制推送

- `git push --force origin main` 强制推送覆盖远程分支

## 子仓库操作

1. `git submodule add {git}` 在项目中添加子模块，会自动生成 `.gitmodules` 文件
2. ` git clone --recurse-submodules {url}` 克隆仓库顺带初始化子仓库

## linux 常用修复命令

1. 每次都要输入密码

     ` git config --global credential.helper store `

## curl 报错

1. `https://www.ipaddress.com/website/raw.githubusercontent.com/` 查看ip地址

2. hosts添加以下内容

3. ```
   185.199.108.133 raw.githubusercontent.com 
   185.199.109.133 raw.githubusercontent.com 
   185.199.110.133 raw.githubusercontent.com 
   185.199.111.133 raw.githubusercontent.com 
   ```

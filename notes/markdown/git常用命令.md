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
+ ``` git push main ``` 推送到远程 main 分支
+ `git update-index --assume-unchanged <file>` git不再追踪该文件的更改   
+ `git reset --hard HEAD~1` 回退当前merge（尚未提交）
+ `git clone --recurse-submodules <主仓库地址>` 克隆并更新子仓库

## 回退操作

- ```` git fetch --all ```` 拉取所有远程更新
- ``` git reset --hard commit_id ``` 回退到指定commit
- `git reset --hard HEAD~1` 回退指定个数的commit
- ` git push --force origin main` 强制推送-覆盖远程分支

- `git reset --hard origin/main` 回退/同步到远程分支 （丢弃本地修改)
- `git reset origin/master` 回退/同步到远程分支 （保留本地修改)

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

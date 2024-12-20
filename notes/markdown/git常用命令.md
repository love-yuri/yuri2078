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
+ ``` git reset --hard commit_id ``` 回退到某个版本
+ ``` git push main ``` 推送到远程 main 分支
+ `git update-index --assume-unchanged <file>` git不再追踪该文件的更改   
+ `git reset --hard HEAD~1` 回退当前merge（尚未提交）

## 远程覆盖本地

+ ``` git fetch --all ```
+ ``` git reset --hard origin/main ```
+ ``` git pull ```

```bash
git config --global http.sslVerify "false"
git config --global --unset http.proxy
git config --global --unset https.proxy 
git add ..
git commit -m "main"
git push -u origin main

```

## linux 常用修复命令

1. 每次都要输入密码

     ` git config --global credential.helper store `

## githun 仓库密钥 更新时间 1.9

`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`

## curl 报错

1. `https://www.ipaddress.com/website/raw.githubusercontent.com/` 查看ip地址

2. ```
   185.199.108.133 raw.githubusercontent.com 
   185.199.109.133 raw.githubusercontent.com 
   185.199.110.133 raw.githubusercontent.com 
   185.199.111.133 raw.githubusercontent.com 
   ```

   

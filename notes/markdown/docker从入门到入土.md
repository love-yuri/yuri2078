# docker从入门到入土

## 安装

1.  安装docker`sudo pacman -S docker` 别的系统参考 [链接](https://mirrors.tuna.tsinghua.edu.cn/help/docker-ce/)

2. 将docker加入当前用户组 `sudo usermod -aG docker $USER`

3. 退出登录/重启/刷新用户组 （三选一）

4. 启动docker服务 `sudo system start docker` 启动docker

5. 输入`docker info` 正确输出则启动成功

6. 换源

   ```bash
   # 创建目录
   sudo mkdir -p /etc/docker
   
   # 写入配置文件
   sudo tee /etc/docker/daemon.json <<-'EOF'
   {
       "registry-mirrors": [
       	"https://docker-0.unsee.tech",
           "https://docker-cf.registry.cyou",
           "https://docker.1panel.live"
       ]
   }
   EOF
   
   # 重启docker服务
   sudo systemctl daemon-reload && sudo systemctl restart docker
   
   ```

7. 测试链接: `ping -c 3 docker-0.unsee.tech`

## 常用指令

- `docker ps -a` 查看所有容器

## Dockerfile


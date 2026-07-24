# MobSF 中文版 - 本地 Docker 部署指南

## 前提条件

- 已安装 Docker Desktop（`brew install --cask docker`）
- 已启动 Docker Desktop（打开应用）

## 快速部署（3 条命令）

```bash
cd ~/MobSF-zh

# 1. 构建中文版镜像（首次约 5-10 分钟）
docker build -t mobsf-zh .

# 2. 运行容器
docker run -d --name mobsf -p 8000:8000 -p 1337:1337 \
  -v $HOME/.MobSF:/home/mobsf/.MobSF \
  mobsf-zh

# 3. 查看日志确认启动
docker logs -f mobsf
```

## 访问

打开浏览器访问：
```
http://127.0.0.1:8000
```

默认账号：
- 用户名：`mobsf`
- 密码：`mobsf`

## 常用操作

```bash
# 停止
docker stop mobsf

# 启动（已创建的容器）
docker start mobsf

# 重启
docker restart mobsf

# 查看日志
docker logs -f mobsf

# 进入容器
docker exec -it mobsf bash

# 删除容器（不影响数据）
docker rm -f mobsf

# 删除镜像
docker rmi mobsf-zh
```

## 数据持久化

扫描数据、上传文件等存储在 `~/.MobSF/` 目录，删除容器不会丢失。
要彻底清除数据：
```bash
rm -rf ~/.MobSF
```

## 更新代码后重新部署

```bash
cd ~/MobSF-zh
git pull origin master
docker rm -f mobsf
docker build -t mobsf-zh .
docker run -d --name mobsf -p 8000:8000 -p 1337:1337 \
  -v $HOME/.MobSF:/home/mobsf/.MobSF \
  mobsf-zh
```

## 生产环境部署（docker-compose）

```bash
cd ~/MobSF-zh/docker
docker-compose up -d
```
这会启动 MobSF + PostgreSQL + Nginx，适合正式环境使用。

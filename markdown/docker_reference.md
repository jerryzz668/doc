# docker_reference

官方文档：

# 一、Introduction

image:镜像就是个包，是个死的东西。相当于python包。

container:把image启动了你就获得了一个独立的容器, 进入这个启动的容器就相当于一个conda 环境了。

# 二、Install

## 1. 查看系统版本

```
$ cat /etc/os-release
NAME="Ubuntu"
VERSION="18.04.5 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.5 LTS"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic
```

## 2. ubuntu[安装教程](https://docs.docker.com/engine/install/ubuntu/#uninstall-docker-engine)

1. 根据官方教程前进

```
$ sudo apt-get update
$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
# 这里会弹出一个warning，不用管
$ uname -a
# 查看系统内核信息
Linux jerry 5.4.0-73-generic #82~18.04.1-Ubuntu SMP Fri Apr 16 15:10:02 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
# 对应安装x86_64
$ echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
# docker引擎安装，ce对应为社区版本
# 一定要先执行sudo apt-get update，要不然会报错
```

到现在为止，安装完毕

> 源的切换（optional）
> 

```
阿里云：https://y0qd3iq.mirror.aliyuncs.com
网易：http://hub-mirror.c.163.com
中国科技大学：https://docker.mirrors.ustc.edu.cn
………………
修改文件 /etc/docker/daemon.json
{
      "registry-mirrors": ["https://y0qd3iq.mirror.aliyuncs.com",""]
}
```

> 执行docker version时报错
> 

```
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.24/version: dial unix /var/run/docker.sock: connect: permission denied
```

这是因为docker进程使用 Unix Socket 而不是 TCP 端口。而默认情况下，Unix socket 属于 root 用户，因此需要 **root权限** 才能访问。解决方法：

```
$ sudo groupadd docker
$ sudo gpasswd -a $jerry docker # 查看是否存在于docker用户组, jerry为账户名
$ sudo gpasswd -a $USER docker  # 将当前用户添加到docker用户组
$ newgrp docker     # 更新用户组
$ docker version    # 成功执行
```

> hello-world测试
> 

```
$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
b8dfde127a29: Pull complete
Digest: sha256:9f6ad537c5132bcce57f7a0a20e317228d382c3cd61edae14650eec68b2b345c
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

> 查看当前镜像
> 

```
$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
hello-world   latest    d1165f221234   3 months ago   13.3kB
Ps:
REPOSITORY： 镜像的仓库源
TAG：镜像的标签
IMAGE ID：镜像的id
CREATED：镜像的创建时间
SIZE：镜像的大小
```

## 3. image build

以两种方式举例

```
yolov5_mmdetection_runtime/   # 根据dockerfile进行Build
yolov5_mmdetection_20210421.tar.gz    # 可以直接docker load
```

1. 根据dockerfile构建

```
$ docker build -f ./Dockerfile -t yolov5_mmdetection_1:1.0 .
# docker build -f dockerfile文件路径 -t 镜像名:[tag] .
经过一段时间的等待
Successfully built cec3587f725c
Successfully tagged yolov5_mmdetection_1:1.0

# 查看当前镜像
$ docker images
REPOSITORY             TAG                             IMAGE ID       CREATED         SIZE
yolov5_mmdetection_1   1.0                             cec3587f725c   2 minutes ago   13.7GB
hello-world            latest                          d1165f221234   3 months ago    13.3kB
nvidia/cuda            11.0-cudnn8-devel-ubuntu16.04   a42cfaadafba   5 months ago    7.72GB
```

1. docker load

```
$ docker load -i yolov5_mmdetection_20210421.tar.gz
$ docker images
REPOSITORY             TAG       IMAGE ID       CREATED             SIZE
micro_i_baseruntime    1.1b      f9be0ed18d82   6 weeks ago         13.9GB
# 已成功Load
```

> 启动容器
> 

```
docker run [可选参数] imageid
# 参数说明
--name="Name"           # 容器名字，用来区分容器
-d                      # 表明以后台方式运行
-it                     # -i以交互模式运行，通常与 -t 同时使用
-p  127.0.0.1:80:8080   # 将容器8080端口映射到本地主机127.0.0.1的80端口
-P                      # 大写是随机指定端口
```

启动刚刚创建的镜像(简化版)

```powershell
$ docker run -it cec3587f725c /bin/bash  # 即可进入容器
ctrl+p+q 不关闭容器退出
$ docker ps  # 查看当前运行中的容器
CONTAINER ID   IMAGE          COMMAND       CREATED              STATUS              PORTS     NAMES
0c6c70c56875   cec3587f725c   "/bin/bash"   About a minute ago   Up About a minute   22/tcp    gallant_nobel
$ docker exec -it 0c6c70c56875 /bin/bash    # 再次进入刚刚的容器
$ docker exec -it xzh_torch bash
$ docker attach container_id
```

# 三、docker

## 1. docker run/commit

```
$ docker run --gpus all --name="yolo_test_demo" -td -v /home/adt/wyProject/mmdetection-master:/workspace/mmdetection --restart=always --ipc=host -p 7832:22 micro_i_baseruntime:1.1b
执行之后容器中的/workspace/mmdetection已经和本地的/home/adt/wyProject/mmdetection-master建立了映射，所以可以直接在本地的/home/adt/wyProject/mmdetection-master目录下进行coding，在容器中运行代码
$ pip list  # 查看当前容器的环境，已经包含了yolov5和mmdet的对应环境，直接python运行即可

# 当安装新的包或者需要迭代新的版本时，提交容器成为一个新的副本
docker commit   # 提交容器成为一个新的副本
docker commit -m "" -a "作者" 容器id 目标镜像名:[TAG]    # -m当前版本提交的描述信息
比如：
$ docker commit -m="add test.py" -a="rainbows" 0c6c70c56875 yolov5_mmdetection_1:1.1
$ docker images
REPOSITORY             TAG                             IMAGE ID       CREATED          SIZE
yolov5_mmdetection_1   1.1                             d46d1f8b2838   7 seconds ago    13.7GB
yolov5_mmdetection_1   1.0                             cec3587f725c   27 minutes ago   13.7GB
hello-world            latest                          d1165f221234   3 months ago     13.3kB
nvidia/cuda            11.0-cudnn8-devel-ubuntu16.04   a42cfaadafba   5 months ago     7.72GB
```

## 2. docker stop/rm

```bash
docker stop 容器id    # 停止当前正在运行的容器
docker rm 容器id      # 删除容器
docker rmi 镜像id     # 删除镜像
```

## 3. docker push

```bash
$ docker login
$ docker tag yolox:v1 jerryzz668/tensorrt7.2.2:latest
$ docker push jerryzz668/tensorrt7.2.2:latest
```

## 4. docker import/export

```bash
$ docker export 3fdd28cd1201 > yolox_demo.tar  # 将容器导出为image
$ docker import yolox_demo.tar  yolox_demo:v2  # 将image导入
```

## 5. remove docker

```
$ sudo apt-get remove docker docker-engine docker.io containerd runc
如果提示没有删除，则进入/var/lib/docker手动删除
$ sudo apt-get purge docker-ce docker-ce-cli containerd.io
$ sudo rm -rf /var/lib/docker
$ sudo rm -rf /var/lib/containerd
```

现场机台一键安装docker

```bash
cd
# install docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# delete sudo limit
sudo groupadd docker
sudo gpasswd -a ${USER} docker
sudo systemctl restart docker
sudo chmod a+rw /var/run/docker.sock

# install packages about GPU
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
```
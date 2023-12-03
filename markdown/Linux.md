# 一、Linux

## Tmux

```
pip install tmux                           # 安装tmux

tmux new -s <name-of-my-session>           # 创建新的session

tmux a -t <name-of-my-session>             # 进入session

tmux ls                                    # 查看列表

tmux rename-session -t old-name new-name   # 重命名session

ctrl+b s                                   # 会话间切换

ctrl+b %                                   # 左右切割窗口

ctrl+b "                                   # 上下切割窗口

ctrl+b ⬅️/➡️                                 # 切换分割窗口

ctrl+b+⬅️/➡️                                 # 调整子窗口大小

ctrl+b d                                   # 临时退出但不删除

ctrl+b :kill-session                       # 会话内退出并删除session

ctrl+b :kill-server                        # 会话内删除所有session

tmux kill-session -t <name-of-my-session>  # 会话外删除指定session
```

## Linux

```
mv file1 file2                              # 重命名文件

mv file path                                # 移动文件

cp file path                                # 复制文件

df -h                                       # 查看磁盘使用

scp user@IP:path-to-file path-to-local      # 从服务器向本地拷贝文件

scp path-to-file user@IP:path-to-server     # 从本地向服务器拷贝文件

-r                                          # 拷贝文件夹需要在scp后加

find ./ -type f | wc -l                     # 查看当前路径下文件数量

find ./ -size +1M                           # 查看当前路径下大于1M的文件

find . -name "*.py" | xargs grep "demo"     # 查找当前路径下所有带有demo字段的py文件

ls -l|grep "^-"| wc -l                      # 查看当前目录下的文件数量（不包括目录中的文件）

ls -l|grep "^d"| wc -l                      # 查看当前目录下的文件夹数量

ls *-*-1[3-6].jpg | wc -l                   # 查看13到16尾缀的jpg数量，'-'换成','表示13和16

cp -r *-12.jpg ../12                        # 拷贝当前路径下所有*12.jpg到上一级12文件夹下

ls -lh <file-name>                          # 查看文件大小和时间

du -sh                                      # 查看当前目录总大小

du -sh xxx                                  # 查看当前路径下xxx文件夹的大小

du -h –max-depth=0 *                        # 查看直接子目录文件及文件夹大小

du -h -d 1                                  # 查看1级目录每个文件大小

python -u  demo.py > ./log.out              # 将print的内容输出到log里，-u：按顺序打印，>：重定向

touch xxx.py                                # 新建文件

tree -L 2                                   # 查看二级目录

Linux下**kill**掉所有python进程（包括运行脚本.sh）

```sudo pkill python```

```sudo ps -ef | grep python3 | awk '{print $2}' | xargs kill -9```
```

## Linux new user

```
useradd -d /home/${USER} -m ${USER}         # linux添加新用户

passwd ${USER}                              # linux设置密码

usermod -aG sudo ${USER}                    # 添加sudo权限

usermod -a -G root ${USER}                  # 添加组别

vim /etc/sudoers                            # sudo权限

chsh -s /bin/bash                           # linux修改默认终端为bash

gpasswd -a  ${USER} docker                  # linux将普通用户加入docker组

su - user                                   # 服务器端账户切换
```

## VIM

```
:set number/nu            # 设置行号

:234                      # 快速跳转234行

gg                        # 快速跳到文档top

shift + g                 # 快速跳到文档bottom

yyp                       # vim复制当前行到下一行(yy复制，p是粘贴)

dd                        # 删除当前行

ndd                       # 删除多行

nyy                       # 复制多行（比如3yy，复制3行）

u                         # 撤销

ctrl+r                    # 反撤销

d+i,symbol                # 删除symbol中内容

:s/from/to/               # 将当前行中的第一个from，替换成to。如果当前行含有多个
                            from，则只会替换其中的第一个。

:s/from/to/g              # 将当前行中的所有from都替换成to

:.s/from/to/g             # 当前行进行替换，33s表示在第33行进行替换，$表示在最后一行进行替换

:10,20s/from/to/g         # 对第10行到第20行的内容进行替换。1,.表示一到当前行。.,$表示当前行到最后一行

:%s/from/to/g             # 对所有行的内容进行替换

- vim下快速切换到头 ｜；切换到尾 $      (非insert状态下)

- vim批量注释和解注释：

  - 注释：ctrl+v进入可视块模式，方向键选中需要注释的内容（需要注释的行有选中即可），按大写的“I”，输入注释符“#”or“//“，然后按两下ESC。

    取消注释：ctrl+v进入可视块模式，选中要删除的注释符（tip：注释符要全部选中），按d即可取消注释。

- vim里搜索关键字：/关键字   enter，即可从当前位置向下查找关键字，按n查找关键字下一个位置，shift+n查找上一个位置

- vim里搜索关键字：?关键字   enter，即可从当前位置向下查找关键字，按n查找关键字上一个位置，shift+n查找上一个位置
```

## SSH

`ssh username@IP -p xxx`

## ZIP

```
tar -zcvf index.tar.gz(目标文件) index(源文件或文件夹)   # 单文件或文件夹打包,目标文件为要打包的文件的文件名，打包后的文件格式取决于目标文件的后缀名，如果后缀名不加.gz则不压缩

tar -zcvf index.tar.gz index css/ js/ imgs/          # 多文件或文件夹 混合打包

tar -czf - index | split -b 200m -d - index.tar.gz   # 分卷压缩index目录，并保持每个压缩包的大小不超过200M字节。命令执行后，会生成index.tar.gz00、index.tar.gz01等文件

split -b 3072m index.zip index.zip.                  # 讲index.zip压缩包切分成每个3G大小的子压缩包，名字为index.zip.aa/index.zip.ab etc.

cat index.tar.gz* > index.tar.gz                     # 将各个分卷压缩包合成为一个index.tar.gz文件
```

## Unzip

```
tar -zxvf index.tar.gz                 # 解压index.tar.gz到当前目录下,c换成了x

tar -zxvf index.tar.gz /home/zhangyan  # 解压index.tar.gz到 /home/zhangyan 目录下

                                       # 同样可以使用其他压缩，如bz/tgz等，用法一样，只是需要更改文件后缀名
```

## 配置Conda源

```
conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/linux-64
conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/linux-64
conda config --set show_channel_urls yes
打开用户目录下的 “.condarc” 文件，如果channels 下面有 “- default” 的话需要删除它
```

## 创建git公钥

```
1. cd ~/.ssh
2. ssh-keygen -t rsa -C "jerryzz668@163.com"
3. 把生成的公钥(id_rsa.pub的内容)放入个人设置里
创建ssh免密登录 ssh -T git@gitee.com
```

# 二、Git

## git merge

```
1. git fetch
2. 重要文件拷出去
3. git reset --hard origin/master
```

## git push

```
1. git branch xxx(xxx为分支名)          # 新建分支
2. git branch -a                       # 查看所有分支
3. git checkout xxx(xxx为分支名)        # 切换到某一分支
4.
    git add .
    git commit -m ''
    git push origin xxx(xxx为提交代码的分支名称)
```

## git reset

```
git log --pretty=oneline
git log --oneline -5                     # 回看最近5此提交log
git reset --hard id(commit前的一大串ID号)  # 回滚（版本回退）
按q退出，无需暴力

git push origin HEAD --force             # git回滚又不需要了，想让他和本地一样

git reflog                               # 查看历史操作命令，找到你要的id，依旧使用上文的git reset --hard id,又回退到当初一模一样的版本啰！
```

```
# 开发分支（dev）上的代码达到上线的标准后，要合并到 master 分支
git checkout dev
git pull
git checkout master
git merge dev
git push -u origin master
```

```
# 当master代码改动了，需要更新开发分支（dev）上的代码
git checkout master
git pull
git checkout dev
git merge master
git push -u origin dev
```


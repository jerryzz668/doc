# Shell

# 一、shell常用命令

## 基本指令

Shell里0为True，0以外为False

---

```bash
str='text'                                 # 定义常量

var=`find . -name '*.s3cfg'`               # 讲shell指令执行结果赋值给变量

find . -name '*[09,10].jpg'                # 查看当前目录下09.jpg和10.jpg结尾的文件

ls |egrep '*09.jpg|*10.jpg'                # 查看当前目录下09.jpg和10.jpg结尾的文件

val=`expr 2+2`
echo "两数之和为： $val"                     # shell基本运算

==                                         # 连按，自动缩进，5==:当前行向后5行同时缩进

[ ! $a ] && echo "a is null"               # 判断变量为空
```

## shell中$常用

```bash
$0                    Shell 的命令本身
$1到$9                表示 Shell 的第几个参数
$?                    显示最后命令的执行情况(bool值)
$#                    传递到脚本的参数个数

-eq      equals等于
-ne      no equals不等于
-gt      greater than 大于
-lt      less than小于
-ge      greater equals大于等于
-le      less equals小于等于
# -eq，-ne等比较符只能用于数字比较，有字符也会先转换成数字然后进行比较

&&       # &&前的命令执行成功了就继续执行后面的命令
```

## 提取文件名和目录名

```
var=/dir1/dir2/file.txt
echo ${var##*/}   # file.txt

${var##*/}  ${var#*.}  ${var%%*.}  ${var%/*}
# ${}用来提取和替换等操作，可以提取很多内容, #：表示从左边算起第一个, %：表示从右边算起第一个, ##：表示从左边算起的最后一个, %%：表示从右边算起的最后一个, 换句话来说，＃总是表示左边算起，％总是表示右边算起。
# ＊：表示要删除的内容，对于#和##的情况，它位于指定的字符（例子中的'/'和'.'）的左边，表于删除指定字符及其左边的内容；对于%和%%的情况，它位于指定的字符（例子中的'/'和'.'）的右边，表示删除指定字符及其右边的内容。这里的'*'的位置不能互换，即不能把*号放在#或##的右边，反之亦然
```

## 程序报错终止运行

```
cd ../Documents ||! echo '错误信息' || exit   # 程序正常运行，后边不执行，程序报错，打印错误信息并退出
```

## 查看程序运行时间

```bash
start_time=`date +%s`
<command-to-execute>
end_time=`date +%s`
echo execution time was `expr $end_time - $start_time` s
```

## 查看文件

---

```bash
# head and tail 加-n后 表示输出到指定行，head是开头到指定行，tail是指定行到结尾，+代表正数第几行，-代表倒数第几行
head -n 2 filename                         # 输出开头2行内容
tail -n 2 filename                         # 输出倒数2行内容
tail -f filename                           # 实时查看filename

sed -n '50,55p' filename                   # 输出第50-55行内容
sed -n '10p;50,55p' filename               # 输出第10行和50-55行内容
sed -n 50p filename                        # 输出第50行内容
```

## 外部传参

---

```bash
# test.sh文件内容
echo "执行的文件名：$0";
echo "第一个参数为：$1";
echo "第二个参数为：$2";
echo "第三个参数为：$3";
# 从外部向.sh脚本传参数。脚本内获取参数的格式为：**$n**。**n** 代表一个数字，1 为执行脚本的第一个参数，2 为执行脚本的第二个参数，以此类推……其中 **$0** 为执行的文件名（包含文件路径）
```

执行脚本bash test.sh 1 2 3

```
执行的文件名：./test.sh
第一个参数为：1
第二个参数为：2
第三个参数为：3
```

## 查看当前路径

---

```bash
basepath=$(cd `dirname $0`; pwd)
echo "$basepath"
```

## 字符串拼接

---

```bash
str="Test"
str1=$name$str                  # 中间不能有空格
str2="$name $str"               # 如果被双引号包围，那么中间可以有空格
str3=$name": "$str              # 中间可以出现别的字符串
str4="$name: $str"              # 这样写也可以
str5="${name}Script: ${str}"    # 这个时候需要给变量名加上大括号
echo $str1
echo $str2
echo $str3
echo $str4
echo $str5
```

# 二、判断与循环

## if else

---

```bash
# 提示变量过多，将变量用==双引号==引起来
if [ condition ]
then
    command
elif condition
then
    command
else
    command
fi

if [ condition ]; then
    command
elif [ condition ]; then
    command
else
    command
fi
```

## for 循环

---

```bash
for var in item1 item2...itemN
do
    command1
    command2
    ...
    commandN
done
# 写成一行
for var in item1 item2 ... itemN; do command1; command2… done;
# var可用$var进行调用
```

```
# 通常情况下 shell 变量调用需要加 $,但是 for 的 (()) 中不需要,下面来看一个例子
for((i=1;i<=5;i++));do
    echo "这是第 $i 次调用";
done;
```

## while循环

---

```bash
while condition
do
    command
done
```

## while死循环

---

```bash
bool=true
while $bool
do
    python train.py
done
```

## until循环

---

```bash
# until 循环执行一系列命令直至条件为 true 时停止
until condition
do
    command
done
```

## case…esac

---

```bash
echo '输入 1 到 4 之间的数字:'
echo '你输入的数字为:'
read var
case $var in
    1)  echo '你选择了 1'
    ;;
    2)  echo '你选择了 2'
    ;;
    3)  echo '你选择了 3'
    ;;
    4)  echo '你选择了 4'
    ;;
    *)  echo '你没有输入 1 到 4 之间的数字'
    ;;
esac
```

# 三、Shell func

## function

---

```bash
funWithReturn(){
    echo "这个函数会对输入的两个数字进行相加运算..."
    echo "输入第一个数字: "
    read aNum
    echo "输入第二个数字: "
    read anotherNum
    echo "两个数字分别为 $aNum 和 $anotherNum !"
    return $(($aNum+$anotherNum))
}
funWithReturn
echo "输入的两个数字之和为 $? !"
```

```bash
#测试 $?  显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。
function demoFun1(){
    echo "这是我的第一个 shell 函数!"
    return `expr 1 + 1`
}

demoFun1
echo $?  # 2
echo $?  # 0
```

## let

---

```bash
# let 命令是 BASH 中用于计算的工具，用于执行一个或多个表达式，变量计算中不需要加上 $ 来表示变量。如果表达式中包含了空格或其他特殊字符，则必须引起来
let a=5+4
let b=9-3
echo $a $b
```

# 四、/dev/null 文件

---

```bash
# 如果希望执行某个命令，但又不希望在屏幕上显示输出结果，那么可以将输出重定向到 /dev/null
$ command > /dev/null
```
# terminal

```
ps aux | grep -i python | grep -v grep | cut -c 9-15 | xargs kill -s 9

find . -name "*.py" | xargs grep "demo"

pip config set global.index-url https://pypi.doubanio.com/simple/

ls *-*-1[3-6].jpg | wc -l
```
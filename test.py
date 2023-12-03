import os
a = 'markdown/test.md'
# b = a.rindex('.')
c = os.path.basename(a).split('.')[0]
print(c)
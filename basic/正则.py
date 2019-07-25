import re

# re.match(pattern, string, flags=0)
res=re.match(r'www(.*)','www.baidu.com')
print(re)
print(res.span())
print(res.group())
print(res.group(1))

# re.search(pattern, string, flags=0)
line = "Cats are smarter than dogs"

searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if searchObj:
   print ("searchObj.group() : ", searchObj.group())
   print ("searchObj.group(1) : ", searchObj.group(1))
   print ("searchObj.group(2) : ", searchObj.group(2))
else:
   print ("Nothing found!!")

#re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。

#re.sub用于替换字符串中的匹配项。
#re.sub(pattern, repl, string, count=0, flags=0)
phone = "2004-959-559 # 这是一个国外电话号码"
 
# 删除字符串中的 Python注释 
num = re.sub(r'#.*$', "", phone)
print ("电话号码是: ", num)
 
# 删除非数字(-)的字符串 
num = re.sub(r'\D', "", phone)
print ("电话号码是 : ", num)

#repl 参数是一个函数
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
 
s = 'A23G4HFD567'
print(re.sub(r'(?P<value>\d+)', double, s))

#compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
#re.compile(pattern[, flags])
# flags : 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：

# re.I 忽略大小写
# re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
# re.M 多行模式
# re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
# re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
# re.X 为了增加可读性，忽略空格和 # 后面的注释

#其他现查


DATA = (
'Mountain View, CA 94040',
'Sunnyvale, CA',
'Los Altos, 94023',
'Cupertino 95014',
'Palo Alto CA',
)
for datum in DATA:
    print(re.split(r', |(?= (?:\d{5}|[A-Z]{2})) ', datum))

#?=组成匹配模式但不包含在组中
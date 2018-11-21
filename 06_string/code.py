'''
处理字符串时，经常需要访问其中的各个字符。
Python使用方括号来标识字符串索引：方括号内的数字指出了要获取哪个字符
如果索引超出了字符串末尾，将导致“超出范围”错误
'''
# s = 'apple'
# print(s[0])  # 'a'
# print(s[1])  # 'p'


'''
负数索引
假设你要访问s的最后一个字符，而不是第一个字符。
为此，可使用难看的表达式s[len(s)-1]，这当然可行，但相当复杂。
所幸的是，在访问字符串末尾附近的字符方面，Python提供了一种更便利的方式：负数索引。
其理念是，沿从右向左的方向，用负数表示字符串中字符的索引
'''
# s = 'apple'
# print(s[-1])  # 'e'

'''
使用for循环访问字符
'''

# for c in 'Hi there!':
#     print(c)  # Hi there!

'''
使用常规字符串索引
'''
# s = 'Hi there!'
# for i in range(len(s)):
#     print(s[i])

'''
字符编码/解码
'''
# print(ord('a'))  # 97
# print(chr(97))  # a

'''
转义字符
字符	含义
\\	反斜杠
\'	单引号
\"	双引号
\n	换行符
\r	回车
\t	水平制表符

行尾
 在表示文本行末尾方面，不同操作系统遵循的标准也不同。
 例如，Windows使用\r\n表示行尾，OS X和Linux使用\n，而OS X之前的Mac操作系统使用\r。
 大多数优秀编辑器都至少能够识别\r\n和\n。你会偶尔遇到不能识别行尾标记的程序（如Windows“记事本”），因此可能出现这样的情形：所有内容都出现在一行、增加了换行或每行末尾都有^M字符。
 避免这种问题的最简单方式是，使用能正确处理行尾标记的文本编辑器。
'''

'''
字符串切片
 在Python中，可使用切片从字符串中提取子串。要对字符串执行切片操作，可指定两个索引：要提取的第一个字符的索引；要提取的最后一个字符的索引加1。
 执行切片操作时，也可使用负数索引，虽然这更难懂。
'''
# food = 'apple pie'
# print(food[0:5])  # apple
# print(food[:5])  # apple
# print(food[6:])  # pie
# print(food[:])  # apple pie


'''
标准字符串函数
 Python字符串自带了大量很有用的函数，要查看所有这些函数，可调用dir并将参数指定为任何字符串（如dir('')）
'''

'''
字符串测试函数
 函数名	什么情况下返回True
 s.endswith(t)	s以字符串t结尾
 s.startswith(t)	s以字符串t打头
 s.isalnum()	s只包含字母或数字
 s.isalpha()	s只包含字母
 s.isdecimal()	s只包含表示十进制数字的字符
 s.isdigit()	s只包含数字字符
 s.isidentifier()	s是合法的标识符
 s.islower()	s只包含小写字母
 s.isnumeric()	s只包含数字
 s.isprintable()	s只包含可打印字符
 s.isspace()	s只包含空白字符
 s.istitle()	s是个大小写符合头衔要求（title-case）的字符串
 s.isupper()	s只包含大写字母
 t in s	s包含字符串t
'''
# print('str'.islower())

'''
字符串搜索函数
 函数名	返回值
 s.find(t)	如果没有找到子串t，则返回-1；否则返回t在s中的起始位置
 s.rfind(t)	与find相同，但从右往左搜索
 s.index(t)	与find相同，但如果在s中找不到t，则引发ValueError异常
 s.rindex(t)	与index相同，但从右往左搜索
 一般而言，函数find和index返回传入字符串第一次出现时的起始位置索引，而rfind和rindex返回传入字符串最后一次出现时的起始位置索引。
'''
# print('abd'.find('b'))

'''
改变大小写的函数
函数名	返回的字符串
 s.capitalize()	将s[0]改为大写
 s.lower()	让s的所有字母都小写
 s.upper()	让s的所有字母都大写
 s.swapcase()	将小写字母改为大写，并将大写字母改为小写
 s.title()	让s的大小写符合头衔的要求
'''

'''
设置格式的函数
 函数名	返回的字符串
 s.center(n, ch)	包含n个字符的字符串，其中s位于中央，两边用字符ch填充
 s.ljust(n, ch)	包含n个字符的字符串，其中s位于左边，右边用字符ch填充
 s.rjust(n, ch)	包含n个字符的字符串，其中s位于右边，左边用字符ch填充
 s.format(vars)	见正文
'''
# s = 'abcdefgh'
# print(s.center(20, '-'))  # ------abcdefgh------
# print(s.ljust(20, '-'))  # abcdefgh------------

'''
剥除函数
 剥除函数用于删除字符串开头或末尾多余的字符
 默认情况下，将剥除空白字符；如果指定了一个字符串参数，将剥除该字符串中的字符
 
 函数名	返回的字符串
 s.strip(ch)	从s开头和末尾删除所有包含在字符串ch中的字符
 s.lstrip(ch)	从s开头（左端）删除所有包含在字符串ch中的字符
 s.rstrip(ch)	从s末尾（右端）删除所有包含在字符串ch中的字符
'''
# name = ' Gill Bates '
# print(name.lstrip()) #'Gill Bates '
# print(name.rstrip())  # ' Gill Bates'
# print(name.strip())  # 'Gill Bates'

# title = '_-_- Happy Days!! _-_-'
# print(title.strip())  # _-_- Happy Days!! _-_-
# print(title.strip('_-'))  # Happy Days!!
# print(title.strip('_ -'))  # Happy Days!!

'''
分拆函数
 分拆函数将字符串拆分成多个子串
 
 s.partition(t)	将s拆分为三个字符串（head、t和tail），其中head为t前面的子串，而tail为t后面的子串
 s.rpartition(t)	与partition相同，但从s的右端开始搜索t
 s.split(t)	以t为分隔符，将s划分成一系列子串，并返回一个由这些子串组成的列表
 s.rsplit(t)	与split相同，但从s的右端开始搜索t
 s.splitlines()	返回一个由s中的各行组成的列表
'''
# url = 'www.google.com'
# print(url.partition('.'))  # '('www', '.', 'google.com')'
# print(url.rpartition('.'))  # '('www.google', '.', 'com')'

# story = 'A long time ago, a princess ate an apple.'
# print(story.split())  # '['A', 'long', 'time', 'ago,', 'a', 'princess', 'ate', 'an', 'apple.']'

'''
替换函数
 函数名	返回的字符串
 s.replace(old, new)	将s中的每个old替换为new
 s.expandtabs(n)	将s中的每个制表符替换为n个空格
'''

# s = 'up, up and away'
# print(s.replace('up', 'down'))  # 'down, down and away'
# print(s.replace('up', ''))  # ',  and away'


'''
其他字符串函数
 函数名	返回的值
 s.count(t)	t在s中出现的次数
 s.encode()	设置s的编码，更详细的信息请参阅在线文档（http://docs.python.org/3/library/ stdtypes.html#str.encode）
 s.join(seq)	使用s将seq中的字符串连接成一个字符串
 s.maketrans(old,new)	创建一个转换表，用于将old中的字符改为new中相应的字符；请注意，s可以是任何字符串，它不影响返回的转换表
 s.translate(table)	使用指定转换表（使用maketrans创建的）对s中的字符进行替换
 s.zfill(width)	在s左边添加足够多的0，让字符串的长度为width
'''
# print(' '.join(['once', 'upon', 'a', 'time']))  # 'once upon a time'
# print('-'.join(['once', 'upon', 'a', 'time']))  # 'once-upon-a-time'
# print(''.join(['once', 'upon', 'a', 'time']))  # 'onceuponatime'

'''
正则表达式
 运算符	描述的字符串
 xy?      	x、xy
 x|y	    x、y
 x*	        ' '、x、xx、xxx、xxxx等
 x+      	x、xx、xxx、xxxx等
 
'''
# import re

# str = 'done'
# print(re.match('done|quit', str) != None)

'''
 Python库re规模庞大，其中有大量正则表达式函数可用于执行字符串处理任务，
 如匹配、分拆和替换；还有提高常用正则表达式处理速度的技巧，以及众多匹配常用字符的捷径。
 模块re的文档（http://docs.python.org/3/library/re.html）提供了其他一些示例。
'''

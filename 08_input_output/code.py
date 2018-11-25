'''
字符串插入
 字符串插入表达式总是采用这样的格式：format % values，其中format是包含一个或多个%字符的字符串。
'''
# x = 1 / 81
# print(x)
# print('value: %.2f' % x)
# print('value: %.5f' % x)

'''
转换说明符
 说明符	含义
 d	整数
 o	八进制（基数为8的）值
 x	小写十六进制（基数为16的）数
 X	大写十六进制（基数为16的）数
 e	小写科学记数法表示的浮点数
 E	大写科学记数法表示的浮点数
 F	浮点数
 s	字符串
 %	%字符
'''
# x = 0.012345679012345678
# print('x = %f' % x)
# x = 0.012346
# print('x = %e' % x)
# x = 1.234568e-02
# print('x = %E' % x)

'''
在格式字符串中包含任意数量的说明符，但必须为每个说明符提供一个值
 格式字符串相当于简单模板，将用指定的值填充。值是以元组方式指定的，它们的排列顺序必须与替换顺序一致。
'''
# a, b, c = 'cat', 3.14, 6
# s = "There's %d %ss older than %.2f years" % (c, a, b)
# print(s)

'''
格式字符串
 另一种创建美观字符串的方式是结合使用格式字符串和字符串函数format(value, format_ spec)。
'''
# print('My {pet} has {prob}'.format(pet='dog', prob='fleas'))  # My dog has fleas
# print('My {0} has {1}'.format('dog', 'fleas'))  # My dog has fleas

'''
可以像字符串插入那样使用转换说明符
'''
# print('1/81 = {x}'.format(x=1 / 81))  # 1/81 = 0.012345679012345678
# print('1/81 = {x:f}'.format(x=1 / 81))  # 1/81 = 0.012346
# print('1/81 = {x:.3f}'.format(x=1 / 81))  # 1/81 = 0.012

'''
可以使用大括号来指定格式设置参数
'''
# print('num = {x:.{d}f}'.format(x=1 / 81, d=3))  # num = 0.012
# print('num = {x:.{d}f}'.format(x=1 / 81, d=4))  # num = 0.0123

'''
读写文件
 函数名	作用
 os.getcwd()	返回当前工作目录的名称
 os.listdir(p)	返回一个字符串列表，其中包含路径p指定的文件夹中所有文件和文件夹的名称
 os.chdir(p)	将当前工作目录设置为路径p
 os.path.isfile(p)	当路径p指定的是一个文件的名称时，返回True，否则返回False
 os.path.isdir(p)	当路径p指定的是一个文件夹的名称时，返回True，否则返回False
 os.stat(fname)	返回有关fname的信息，如大小（单位为字节）和最后一次修改时间
'''

import os


def list_cwd():
    """
    列出目录下文件列表

    :return:
    """
    return os.listdir(os.getcwd())  # ['code.py', 'test.py', 'dict']


def files_cwd():
    """
    获取目录下文件列表

    :return:
    """
    return [p for p in list_cwd() if os.path.isfile(p)]  # ['code.py', 'test.py']


def folders_cwd():
    """
    获取目录下文件夹列表

    :return:
    """
    return [p for p in list_cwd() if os.path.isdir(p)]  # ['dict']


def list_py(path=None):
    """
    获取目录下py文件

    :param path:
    :return:
    """
    if path is None:
        path = os.getcwd()
    return [fname for fname in os.listdir(path) if os.path.isfile(fname) if fname.endswith('.py')]


def size_in_bytes(fname):
    """
    计算单个文件大小
    :param fname:
    :return:
    """
    return os.stat(fname).st_size


def cwd_size_in_bytes():
    """
    计算文件夹下所有文件大小
    :return:
    """
    total = 0
    for name in files_cwd():
        total = total + size_in_bytes(name)
    return total


def cwd_size_in_bytes2():
    """
    计算文件夹下所有文件大小
    :return:
    """
    return sum(size_in_bytes(f)
               for f in files_cwd())


'''
Python文件打开模式
 'r'	为读取而打开文件（默认模式）
 'w'	为写入而打开文件
 'a'	为在文件末尾附件而打开文件
 'b'	二进制模式
 't'	文本模式（默认模式）
 '+'	为读写打开文件
'''


def print_file1(fname):
    """
    逐行读取文本文件
    :param fname:
    :return:
    """

    f = open(fname, 'r')
    for line in f:
        print(line, end='')
    f.close()  # 这行代码是可选的


# print_file1('test.py')


def print_file2(fname):
    """
    将整个文本文件作为一个字符串进行读取
    :param fname:
    :return:
    """
    f = open(fname, 'r')
    print(f.read())
    f.close()


# print_file2('test.py')


def add_to_story(line, fname='story.txt'):
    """
    附加到文本文件末尾
    :param line:
    :param fname:
    :return:
    """
    f = open(fname, 'a')
    f.write(line)


# add_to_story("\nis a story", 'test.py');

def insert_title(title, fname='story.txt'):
    """
    将字符串插入到文件开头
    :param title:
    :param fname:
    :return:
    """
    f = open(fname, 'r+')
    temp = f.read()
    temp = title + '\n\n' + temp
    f.seek(0)  # 让文件指针指向文件开头
    f.write(temp)


# insert_title('title', 'test.py')


def is_gif(fname):
    """
    处理二进制文件

    这个函数检查fname是不是GIF图像文件,方法是检查其前4个字节是不是 (0x47, 0x49, 0x46, 0x38)
    :param fname:
    :return:
    """
    f = open(fname, 'br')
    first4 = tuple(f.read(4))
    return first4 == (0x47, 0x49, 0x46, 0x38)


# print(is_gif('test.py'))


import urllib.request

page = urllib.request.urlopen('http://www.python.org')
print(page)
html = page.read()
# print(html)

'''
它让你能够以编程方式在浏览器中显示网页
'''
import webbrowser

# webbrowser.open('http://www.yahoo.com')

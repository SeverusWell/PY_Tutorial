# coding=UTF-8
import math

'''
函数是一大块可重用的代码。它是有名称的代码块，接受输入、提供输出并可存储在文件中供以后使用。
几乎任何Python代码都可放在函数中。
Python为函数提供了强大支持。例如，它提供了很多给函数传递数据的方式；它还允许在函数中包含文档字符串，让你或其他程序员能够获悉函数的工作原理
即便函数不接受任何输入（即没有参数），也必须在函数名后添加圆括号(),()让Python执行指定的函数
'''
# print(dir())

'''
不返回值的函数
有些函数（如print）不返回值
'''
# var = print('str')
# print(var) # None

'''
给函数名赋值
你必须小心，以避免无意间让内置函数名指向其他函数或值。不幸的是，Python并不会阻止你编写类似下面的代码
'''
# dir = 3
# dir()  # 报错
# 这里让dir指向了数字3，导致你再也无法访问dir原来指向的函数！要恢复原样，需要重启Python。

'''
定义函数
与变量名一样，函数名也只能包含字母、数字和下划线_，且不能以数字打头

Python文档字符串通常遵循一种标准格式约定：
  用三引号标识文档字符串的开始和结束位置；
  第1行是函数的简要描述，对程序员很有帮助；
  接下来是详情和示例。
  文档字符串的其他好处与内置函数一样，你也可轻松地查看自己编写的函数的文档字符串
  如果函数没有包含return语句，Python将认为它以下述代码行结束： return None

'''

# def area(radius):
#     """ Returns the area of a circle
#     with the given radius.
#     For example:
#     >>> area(5.5)
#     95.033177771091246
#     """
#     return math.pi * radius ** 2
#
#
# print(area(5.5))  # 95.033177771091246


'''
变量的作用域
 首次赋值发生在函数内的变量被称为局部变量
 函数的参数也被视为局部变量
 局部变量只能在其所属函数中使用，这一点很重要；在函数外面，不能访问函数的局部变量。
 函数结束时，其局部变量被自动删除
'''

'''
全局变量
 在函数外面声明的变量称为全局变量，程序中的任何函数或代码都可读取它。然而，在函数中给全局变量重复赋值时需要特别小心。请看下面的代码：
'''
# name = 'Jack'
#
#
# def say_hello():
#     print('Hello ' + name + '!')
#
#
# def change_name(new_name):
#     name = new_name
#
#
# say_hello()  # say_hello
# change_name('Piper')
# say_hello()  # say_hello (全局变量name的值并没有变)

'''
要访问全局变量，必须使用关键字global
'''

# def change_name(new_name):
#     global name
#     name = new_name

'''
使用main函数
 在你编写的任何Python程序中，通常都至少应该使用一个函数：main()。
 根据约定，main()函数被认为是程序的起点
 main只是一种约定，完全是可选的。
'''

# def main():
#     pwd = input('What is the password? ')
#     if pwd == 'apple':
#         print('Logging on ...')
#     else:
#         print('Incorrect password.')
#     print('All done!')

'''
按引用传递参数
 按值传递参数时，将创建其拷贝，并将该拷贝传递给函数。如果传递的值很大，复制可能消耗大量时间和内存
 Python不支持按值传递
'''

# def add(a, b):
#     return a + b
#
#
# x, y = 3, 4
# print(add(x, y))


'''
默认值
 函数可根据需要使用任意数量的默认参数，但带默认值的参数不能位于没有默认值的参数前面。
'''

# def greet(name, greeting='Hello'):
#     print(greeting, name + '!')
#
#
# greet('Bob')  # Hello Bob!
#
# greet('Bob', 'Good morning')  # Good morning Bob!


'''
关键字参数
 调用使用关键字参数的函数时，以param = value的方式传递数据
 它们清晰地指出了参数值，有助于提高程序的可读性；其次，关键字参数的顺序无关紧要。
 对于包含大量参数的函数来说，这两点都很有帮助，因为很难记住这些函数的参数的顺序和含义。
'''

# def shop(where='store', what='pasta', howmuch='10 pounds'):
#     print('I want you to go to the', where)
#     print('and buy', howmuch, 'of', what + '.')
#
#
# shop()  # I want you to go to the store and buy 10 pounds of pasta.
# shop(what='towels')  # I want you to go to the store and buy 10 pounds of towels.
# shop(howmuch='a ton', what='towels')  # I want you to go to the store and buy a ton of towels.
# shop(howmuch='a ton', what='towels', where='bakery')  # I want you to go to the bakery and buy a ton of towels.

'''
模块
 模块是一系列相关的函数和变量
 要创建模块，可创建一个.py文件，在其中包含用于完成任务的函数
 模块与常规Python程序之间唯一的差别是用途不同：模块是一个由函数组成的工具箱，用于编写其他程序。
 因此，模块通常没有main()函数。要使用模块，只需导入它即可
'''
# import shapes

# print(dir(shapes))
# shapes.square(5)
# shapes.triangle(3)

'''
你还可导入模块的所有内容
'''
# from shapes import *

# rectangle(3, 8)

'''
名称空间
 名称空间基本上就是一组独特的变量名和函数名。
 要让模块中的名称在模块外面可见，你必须使用import语句。


 假设Jack和Sophie合作开发一个大型编程项目。Jack住在西海岸，而Sophie住在东海岸。
 他们达成了一致，Jack将其所有代码都放在模块jack.py中，Sophie将其所有代码都放在模块sophie.py中。
 他们各自独立地工作，最终都编写了函数save_file(fname)，但这两个函数只是函数头相同，功能截然不同。
 这两个函数位于不同的模块，即便同名也没有关系，因为它们位于不同的名称空间。
 Jack编写的函数的全名为jack.save_file(fname)，而Sophie编写的函数的全名为sophie. save_file(fname)

 模块可避免名称冲突，让程序员能够独立地进行开发。即便你不与其他程序员合作，名称冲突也是个恼人的问题，在程序很大很复杂时尤其如此。
 当然，即便使用了模块，像下面这样做依然会导致名称冲突：
 这种import语句将每个模块的所有内容都加入到当前名称空间，将覆盖其他同名的内容。因此，在较大的程序中，明智的做法是不使用from ... import *语句。
'''
# from jack import *
# from sophie import *

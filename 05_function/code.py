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
'''


def area(radius):
    """ Returns the area of a circle
    with the given radius.
    For example:
    >>> area(5.5)
    95.033177771091246
    """
    return math.pi * radius ** 2


print(area(5.5))  # 95.033177771091246

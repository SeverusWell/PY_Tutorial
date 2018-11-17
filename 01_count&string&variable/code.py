# import sys

'''
整数算术
Python支持4种基本算术运算：+（加）、-（减）、* （乘）和/（除）。
Python还使用**和%来分别表示乘方和求余
'''
# print(5 + 9)
# print(22 - 6)
# print(2 ** 4)
# print(25 % 7)
# print(1 + 2 * 3)
# print((1 + 2) * 3)

'''
整除
Python还有一个整除运算符//，其工作原理类似于/，但结果总是整数。
例如，7 // 3的结果为2——将小数点后面的值丢弃（而不是四舍五入）。
'''
# print(7 // 3)

'''
求值顺序(运算优先级)

**	指数 (最高优先级)
~ + -	按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //	乘，除，取模和取整除
+ -	加法减法
>> <<	右移，左移运算符
&	位 'AND'
^ |	位运算符
<= < > >=	比较运算符
<> == !=	等于运算符
= %= /= //= -= += *= **=	赋值运算符
is is not	身份运算符
in not in	成员运算符
not and or	逻辑运算符
'''

'''
长度不受限制
Python对整数的长度没有限制
'''
# print(27 ** 100)

'''
浮点数算术
在Python中，浮点数是带小数点的数字，例如，–3.1、2.999和–4.0都是浮点数。
(所有适用于整数的算术运算都可用于浮点数)
'''
# print(3.8 + -43.2)
# print(5.6 // 2)  # 2.0

'''
对于非常大或非常小的浮点数，通常用科学记数法表示。
'''
# print(8.8 ** -5.4) # 7.939507629591553e-06 (e-06表示将它前面的数字乘以10–6)

'''
在使用小数点方面，Python非常灵活
'''
# print(3.)  # 3.0
# print(.5)  # 0.5

'''
溢出
与整数不同，浮点数存在上限和下限，超出上限或下限将导致溢出错误。
溢出错误意味着计算结果太大或太小，Python无法将其表示为浮点数。
面对溢出错误，Python可能沉默不语，即继续执行错误的计算，而不告诉你出了问题。
一般而言，避免溢出错误的职责由程序员承担
'''
# print(500.0 ** 10000) # OverflowError: (34, 'Result too large')

'''
精度有限
'''
# print(1 - 2 / 3)  # 0.33333333333333337

'''
复数
复数是涉及-1的平方根的数字，在Python中，用1j表示–1的平方根。
'''
# print(1j * 1j)  # (-1+0j)

'''
模块math中的一些函数
函数	描述
ceil(x)	大于或等于x的整数
cos(x)	x的余弦
degrees(x)	将x弧度转换为度数
exp(x)	e的x次方
factorial(n)	计算n的阶乘（n!）。n! = 1*2*3…*n，其中n必须是整数
log(x)	以e为底的x的对数
log(x, b)	以b为底的x的对数
pow(x, y)	x的y次方
radians(x)	将x度转换为弧度数
sin(x)	x的正弦
sqrt(x)	x的平方根
tan(x)	x的正切
'''

'''
导入模块
要使用模块math或其他任何Python模块，都必须先导入:
import math
这样就可以访问任何数学函数了，方法是在函数前面加上math.

另一种导入模块的方式:
from math import *
这样调用math模块中的任何函数时，都无需在前面加上math.(import math通常更安全，因为它不会覆盖任何既有函数)
'''
import math

# print(math.sqrt(5))  # 2.23606797749979
# print(math.sqrt(2) * math.tan(22))  # 0.012518132023611912

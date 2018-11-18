'''
布尔逻辑
使用4个主要的逻辑运算符（也叫逻辑连接符）来组合布尔值：not、and、or和==
表达式
 p == q
 p != q
 p and q
 p or q
 not p
'''
# print(True or False)
# print(not False)
# print(not (not True))

'''
短路求值
其中X为任何布尔表达式。
因为开头的False导致整个and表达式为False，所以表达式False and X的值不依赖于X——总是为False。
在这样的情况下，Python根本不计算X的值，而在遇到False and时就此罢手，并返回结果False。这可提高布尔表达式的计算速度
'''
# print(False and True)

'''
if语句
if语句总是以关键字if打头，而这个关键字后面总是一个布尔表达式。这种表达式被称为if条件（简称为条件）。
if条件后面是一个冒号（:）。正如你将看到的，Python将:用作if语句头、循环头和函数头的结束标记。
从if到:的部分被称为if语句头。如果if语句头中的条为True，将立即执行语句print('Logging on ...')，并跳过语句print('Incorrect password.')，永远不执行它。
如果if语句头中的条件为False，将跳过语句print('Logging on ...')，只执行语句print('Incorrect password.')。
无论在哪种情况下，都会执行最后的语句print('All done!')。

我们通常将包含多行的整个if结构是为一条if语句。
你必须在关键字if后面至少添加一个空格。
关键字if、条件和结尾的:必须位于同一行。
在if语句中，else代码块是可选的，可根据要解决的问题决定是否包含它。
'''
# if input('What is the password? ') == 'apple':
#     print('Logging on ...')
# else:
#     print('Incorrect password.')
# print('All done!')
'''
代码块和缩进
Python的一个与众不同之处是，使用缩进来标识代码块。
 代码行print('Logging on ...')和print('Incorrect password.')是两个不同的代码块。
 这些代码块只有一行，但Python允许你编写包含任意数量语句的代码块。
 要在Python中标识代码块，必须以同样程度缩进代码块的每一行。
在其他大多数编程语言中，缩进只用于让代码更美观；但在Python中，必须使用缩进来指出语句所属的代码块。
 例如，最后一条语句final print('All done!')没有缩进，因此不属于else代码块。
'''

'''
if/elif语句
'''
# age = int(input('How old are you? '))
# if age <= 2:
#     print(' free')
# elif 2 < age < 13:
#     print(' child fare')
# else:
#     print('adult fare')

'''
条件表达式
在第2行，=右边的表达式被称为条件表达式，其结果要么为'yuck'要么为'yum'
一般而言，仅当条件表达式可让代码更简单时才使用它们。
'''
# food = input("What's your favorite food? ")
# reply = 'yuck' if food == 'lamb' else 'yum'
# print(reply)

'''
循环
基本for循环重复执行给定代码块指定的次数。
for循环的第1行被称为for循环头。for循环总是以关键字for打头，接下来是循环变量（这里为i），然后是关键字in。
关键字in后面通常（但并非总是）是range(n)和结束符号:。
for循环重复执行循环体（循环头后面的语句块）n次。
'''
# for i in range(10):
#     print(i)
'''
默认情况下，初始值为0，并逐递增到n - 1（而不是n）。
从0而不是1开始可能看起来有点怪，但在编程中很常见。 如果要修改循环的初始值，可在range中添加初始值：
'''
# for i in range(1,11):
#     print(i)

'''
注意到第一个参数为10，第二个参数为0，而第三个参数（被称为步长）为-1。另一种做法是使用更简单的范围，并在循环体中修改i。
'''
# for i in range(10, 0, -1):
#     print(i)

'''
while循环
while循环本身以关键字while打头，这一行被称为while循环头，而它后面缩进的代码被称为while循环体。
while循环头总是以while打头，后面跟着循环条件——返回True或False的布尔表达式。
 首先，Python检查循环条件为True还是False，如果为True，就执行循环体；
 如果为False，就跳过循环体（即跳出循环）并执行后面的语句。
 在条件为True并执行循环体后，Python再次检查条件。
 只要循环条件为True，Python就不断执行循环。
'''
# i = 0
# while i < 10:
#     print(i)
#     i = i + 1

'''
break语句提供了一种便利方式，让你能够从循环体内的任何地方跳出循环
'''
# n = int(input('How many numbers to sum? '))
# total = 0
# for i in range(n):
#     s = input('Enter number ' + str(i + 1) + ': ')
#     if 'done' == s:  # break
#         break
#     if 'continue' == s:  # continue
#         continue
#     total = total + int(s)
# print('The sum is ' + str(total))

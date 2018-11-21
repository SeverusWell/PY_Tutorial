'''
type命令
 检查值或变量的数据类型
'''
# print(type(5))  # <class 'int'>


'''
序列
 在Python中，序列是一组按顺序排列的值。Python有3种内置的序列类型：字符串、元组和列表。
 序列的优点之一是，像前一章介绍的字符串一样支持索引和切片。因此，所有序列都具备如下特征.
 
 第一个正索引为零，指向左端。
 第一个负索引为-1，指向右端。
 可使用切片表示法来复制子序列，例如，seq[begin:end]复制seq的如下元素：从索引begin指向的元素到索引end - 1指向的元素。
 可使用+和*进行拼接（即合并）。要进行拼接，序列的类型必须相同，即不能把元组和列表一起进行拼接。
 可使用函数len计算其长度，例如，len(s)返回序列s包含的元素数。
 表达式x in s检查序列s是否包含元素x。换句话说，如果x位于s中，则x in s返回True，否则返回False。
 实际上，字符串和列表是最常用的序列；元组有其独特用途，但不那么常见。
'''

'''
元组
 元组是一种不可变序列，包含零个或更多个值。它可以包含任何Python值，甚至可以包含其他元组。
 
 元组用圆括号括起，其中的元素用逗号分隔。空元组用()表示，但只包含一个元素的元组（单元素元组）
 采用不同寻常的表示法(x,) 如果省略单元素元组末尾的逗号，就不是创建元组，而是用圆括号将表达式括起
'''
# items = (-6, 'cat', (1, 2))
# print(type(items)) #<class 'tuple'>
# print(len(items))  # 3
# print(items[-1])  # (1, 2)
# print(items[-1][0])  # 1

'''
元组是不可变的
 这意味着创建元组后就不能修改它。这种特征并不独特，字符串、整数和浮点数都是不可变的。
 如果要修改元组，就必须创建一个体现更改的新元组。例如，下面的代码演示了如何删除元组的第一个元素
'''
# lucky = (6, 7, 21, 77)
# lucky2 = lucky[1:]
# print(lucky)  # (6, 7, 21, 77)
# print(lucky2)  # (7, 21, 77)

'''
元组函数
 函数名	返回值
 x in tup	如果x是元组tup的一个元组，则返回True，否则返回False
 len(tup)	元组tup包含的元素数
 tup.count(x)	元素x在元组tup中出现的次数
 tup.index(x)	元组tup中第一个元素x的索引；如果x未包含在元组tup中，将引发ValueError异常

'''
# pets = ('dog', 'cat', 'bird', 'dog')
# print('cow' in pets)# False
# print(len(pets))#4
# print(pets.count('dog')) #2
# print(pets.count('fish')) #0
# print(pets.index('dog'))  # 0
# print(pets.index('bird')) #2
# pets.index('mouse') #ValueError: tuple.index(x): x not in tuple

'''
与字符串一样，也可使用+和*来拼接元组
'''
# tup1 = (1, 2, 3)
# tup2 = (4, 5, 6)
# print(tup1 + tup2)  # (1, 2, 3, 4, 5, 6)
# print(tup1 * 2)  # (1, 2, 3, 1, 2, 3)

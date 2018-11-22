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


'''
与字符串和元组一样，你可使用索引和切片来访问元素和子列表
列表可包含任何类型的值：数字、字符串甚至其他序列。
空列表用[]表示，而只包含一个元素（x）的单元素列表写做[x]（与元组不同，对单元素列表来说，并非必须以逗号结尾）。
'''
# lst = [3, (1,), 'dog', 'cat']
# print(lst) # [3, (1,), 'dog', 'cat']
# print(lst[1])  # (1,)
# print(lst[2])  # dog
# print(lst[1:3])  # [(1,), 'dog']
# print(lst[2:])  # ['dog', 'cat']
# print(lst[-3:])  # [(1,), 'dog', 'cat']
# print(lst[:-3])  # [3]

'''
列表是可变的，这是区分列表和元组的重要特征
列表元素指向（而不是包含）相应的值，明白这一点很重要
'''
# pets = ['frog', 'dog', 'cow', 'hamster']
# print(pets) #['frog', 'dog', 'cow', 'hamster']
# pets[2] = 'cat'
# print(pets)  # ['frog', 'dog', 'cat', 'hamster']

'''
列表元素指向相应的值，这可能导致一些不可思议的行为
'''
# snake = [1, 2, 3]
# print(snake)  # [1, 2, 3]
# snake[1] = snake
# print(snake)  # [1, [...], 3]

'''
列表函数
 列表有很多实用函数。
 除count只是返回一个数字外，其他所有函数都修改传递给它们的列表。因此它们是修改函数，使用时必须小心
 
 函数名	返回值
 s.append(x)	在列表s末尾添加元素x
 s.count(x)	返回元素x在列表s中出现的次数
 s.extend(lst)	将lst的所有元素都添加到列表s末尾
 s.index(x)	返回第一个x元素的索引
 s.insert(i, x)	将元素x插入到索引i指定的元素前面，结果是s[i] == x
 s.pop(i)	删除并返回s中索引为i的元素
 s.remove(x)	删除s中的第一个x元素
 s.reverse()	反转s中元素的排列顺序
 s.sort()	将s的元素按升序排列
'''

# def numnote(lst):
#     msg = []
#     for num in lst:
#         s = ''
#         if num < 0:
#             s = str(num) + ' is negative'
#         elif 0 <= num <= 9:
#             s = str(num) + ' is a digit'
#         if s:
#             msg.append(s)
#     return msg
#
#
# # 下面是一个调用该函数的示例：
# print(numnote([1, 5, -6, 22]))  # ['1 is a digit', '5 is a digit', '-6 is negative']

'''
列表排序
'''
# lst = ['up', 'down', 'cat', 'dog']
# lst.sort()
# print(lst)  # ['cat', 'dog', 'down', 'up']
# lst.reverse()
# print(lst)  # ['up', 'down', 'dog', 'cat']

'''
列表解析
'''
# print([n * n for n in range(1, 11)])  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print([n * 2 for n in range(1, 11)])  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# print([c for c in 'pizza'])  # ['p', 'i', 'z', 'z', 'a']
# print([c.upper() for c in 'pizza'])  # ['P', 'I', 'Z', 'Z', 'A']

# names = ['al', 'mei', 'jo', 'del']
# print([n.capitalize() for n in names])  # ['Al', 'Mei', 'Jo', 'Del']

'''
使用列表解析进行筛选
'''
# nums = [-1, 0, 6, -4, -2, 3]
# print([n for n in nums if n > 0])  # [6, 3]

'''
字典
 首先，字典中的键必须是独一无二的，即在同一个字典中，任何两个键-值对的键都不能相同。
 对键的第二个限制是，键必须是不可变的。因此，字典键不能是列表，也不能是字典。
 为何要这样要求呢？因为键-值对在字典中的存储位置是根据键计算得到的。即便键发生细微变化，键-值对在字典中的位置也将变化。这可能导致键-值对丢失或无法访问。
'''
# color = {'red': 1, 'blue': 2, 'green': 3}
# print(color)  # {'red': 1, 'blue': 2, 'green': 3}
# print(color['blue'])  # 2

'''
字典函数
 
 函数名	返回的值
 d.items()	返回一个由字典d的键-值对组成的视图（view）
 d.keys()	返回一个由字典d的键组成的视图
 d.values()	返回一个由字典d的值组成的视图
 d.get(key)	返回与key相关联的值
 d.pop(key)	删除键key并返回与之相关联的值
 d.popitem()	删除字典d中的某个键-值对并返回相应的键-值
 d.clear()	删除字典d的所有元素
 d.copy()	复制字典d
 d.fromkeys(s, t)	创建一个新字典，其中的键来自s，值来自t
 d.setdefault(key, v)	如果键key包含在字典d中，则返回其值；否则，返回v并将(key, v)添加到字典d中
 d.update(e)	将e中的键-值对添加到字典d中；e可能是字典，也可能是键-值对序列
 
 正如你看到的，要获取字典中的值，标准方式是使用方括号表示法：d[key]返回与key相关联的值。调用d.get(key)可完成同样的任务。
 无论采取哪种方式，如果key没有包含在字典d中，都将引发KeyError异常。
 如果你预先不确定某个键是否包含在字典中，可使用key in d进行检查。如果key包含在字典d中，这个表达式将返回True，否则返回False。
 这种检查的效率极高，与用于序列的in相比尤其如此
 
 函数items()、keys()和values()都返回一个特殊对象——视图。视图被链接到原始字典，因此如果字典发生变化，视图也将相应地变化
'''
# color = {'blue': 2, 'orange': 4, 'green': 3, 'red': 0}
# k = color.keys()
# print(k)  # dict_keys(['blue', 'orange', 'green', 'red'])
# for i in k:
#     print(i)
# blue
# orange
# green
# red

# color.pop('red')
# print(color)  # {'blue': 2, 'orange': 4, 'green': 3}

# for i in k:
#     print(i) # 十分神奇,k中元素竟然发生了变化
# blue
# orange
# green

'''
集合
 集合是一系列不重复的元素。集合类似于字典，但只包含键，而没有相关联的值。
 可变集合和不可变集合。对于可变集合，你可添加和删除元素，而不可变集合一旦创建就不能修改。
 集合最常见的用途可能是用于删除序列中的重复元素
 与字典一样，集合的元素排列顺序也是不确定的
'''
# lst = [1, 1, 6, 8, 1, 5, 5, 6, 8, 1, 5]
# s = set(lst)
# print(s)  # {8, 1, 5, 6}

'''
需要使用集合时，可参阅在线文档，网址为http://docs.python.org/3/library/stdtypes.html# set- types-set-frozenset。
'''

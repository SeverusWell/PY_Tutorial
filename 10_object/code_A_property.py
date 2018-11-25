class Person:
    """ Class to represent a person
    """

    # def __init__(self):
    #     print('__init__(self):')
    #     # 在OOP中，self是一个指向对象本身的变量
    #     self.name = ''
    #     self.age = 0

    def __init__(self, name='', age=0):
        print("__init__(self, name='', age=0):")
        self.name = name
        self._age = age

    @property
    def age(self):
        print('age(self):')
        return self._age

    @age.setter
    def age(self, age):
        print('set_age(self, age):')
        if 0 < age <= 150:
            self._age = age

    def display(self):
        print("Person(name : '%s',  age : %s)" % (self.name, self.age))

    def __str__(self):
        return "Person(name : '%s',  age : %s)" % (self.name, self.age)

    # 还可定义特殊方法__repr__，它返回对象的“官方”（official）表示。
    def __repr__(self):
        return str(self)


p = (Person('Moe', 55))
print(p)  # Person(name : 'Moe',  age : 55)
p.age = 10
print(p)  # Person(name : 'Moe',  age : 10)
p.age = -10
print(p)  # Person(name : 'Moe',  age : 10)
# 直接访问私有变量
p._age = 44
print(p)  # Person(name : 'Moe',  age : 44)


'''
不以下划线打头的变量是公有变量，任何代码都可访问它们。
编写大型程序时，一条实用的经验规则是，首先将所有对象变量都设置为私有的（即以两个下划线打头），再在有充分理由的情况下将其改为公有的。
这可避免无意间修改对象内部变量导致的错误。
'''
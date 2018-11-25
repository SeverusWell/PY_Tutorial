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
        self.age = age

    def display(self):
        print("Person(name : '%s',  age : %s)" % (self.name, self.age))

    def __str__(self):
        return "Person(name : '%s',  age : %s)" % (self.name, self.age)

    # 还可定义特殊方法__repr__，它返回对象的“官方”（official）表示。
    def __repr__(self):
        return str(self)

    def set_age(self, age):
        if 0 < age <= 150:
            self.age = age


# p = Person()
# print(p.age)
# print(p.name)
# p.age = 55
# print(p.age)
# p.name = 'Moe'
# print(p.name)

# p.display()  # Person(name : 'Moe',  age : 55)
# print(str(p))  # Person(name : 'Moe',  age : 55)


p = (Person('Moe', 55))
print(p)  # Person(name : 'Moe',  age : 55)
p.set_age(10)
p.set_age(-10)
print(p)  # Person(name : 'Moe',  age : 10)

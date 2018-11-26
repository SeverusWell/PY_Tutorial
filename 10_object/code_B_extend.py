class Player:
    def __init__(self, name):
        self._name = name
        self._score = 0

    def reset_score(self):
        self._score = 0

    def incr_score(self):
        self._score = self._score + 1

    def get_name(self):
        return self._name

    def __str__(self):
        return "name = '%s', score = %s" % (self._name, self._score)

    def __repr__(self):
        return 'Player(%s)' % str(self)


# p = Player('Moe')
# print(p)  # name = 'Moe', score = 0
# p.incr_score()
# print(p)  # name = 'Moe', score = 1
# p.reset_score()
# print(p)  # name = 'Moe', score = 0


# class Human(Player):
#     """
#     单纯继承
#     """
#     pass
#
#
# h = Human('Jerry')
# print(h)  # name = 'Jerry', score = 0
# h.incr_score()
# print(h)  # name = 'Jerry', score = 1
# h.reset_score()
# print(h)  # name = 'Jerry', score = 0


class Human(Player):
    """
    重写方法
    """

    def __repr__(self):
        return 'Human(%s)' % str(self)


class Computer(Player):
    def __repr__(self):
        return 'Computer(%s)' % str(self)


h = Human('Jerry')
# print(h)

'''
调用 __repr__
'''
print(repr(h))

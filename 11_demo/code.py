# s = 'A long time ago, in a galaxy far,far away ...'
# print(len(s))  # 45
# print(s.split())  # ['A', 'long', 'time', 'ago,', 'in', 'a', 'galaxy', 'far,far', 'away', '...']

t = 'a long time ago in a galaxy far far away'
# print(t.split())  # ['a', 'long', 'time', 'ago', 'in', 'a', 'galaxy', 'far', 'far', 'away']
# print(len(t.split()))  # 10
#
# print(set(t.split()))  # {'long', 'ago', 'galaxy', 'in', 'a', 'far', 'away', 'time'}
# print(len(set(t.split())))  # 8

s = "I'd like a copy!"
# print(s.lower())  # i'd like a copy!
# print(s.replace('!', ''))  # I'd like a copy

keep = {'a', 'b', 'c', 'd', 'e',
        'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y',
        'z',
        ' ', '-', "'"}


def normalize(s):
    """Convert s to a normalized string.
    """
    result = ''
    for c in s.lower():
        if c in keep:
            result += c
    return result


def normalize2(s):
    """Convert s to normalized string.
    """
    return ''.join(c for c in s.lower() if c in keep)



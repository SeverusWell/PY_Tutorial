# print(open('unicorn.dat'))
# print(1/0)
'''
手动抛异常
'''
# raise IOError('This is a test!')


'''
捕获异常
'''


def get_age():
    while True:
        try:
            n = int(input('How old are you? '))
            return n
        except ValueError:
            print('Please enter an integer value.')


# get_age()

'''
捕获多种异常
'''


def convert_to_int1(s, base):
    try:
        return int(s, base)
    except (ValueError, TypeError):
        return 'error'


'''
如果要分别处理不同的异常，可使用多个except子句
'''


def convert_to_int2(s, base):
    try:
        return int(s, base)
    except ValueError:
        return 'value error'
    except TypeError:
        return 'type error'


'''
捕获所有异常
'''


def convert_to_int3(s, base):
    try:
        return int(s, base)
    except:
        return 'error'


'''
清理操作
 在try/except块中，可包含执行清理操作的finally代码块
'''


def invert(x):
    try:
        return 1 / x
    except ZeroDivisionError:
        return 'error'
    finally:
        print('invert(%s) done' % x)


'''
使用with语句时，将在for循环结束后立即执行文件对象清理操作（即关闭文件），避免了不再需要的f处于打开状态。
'''
fname = 'test.txt'
num = 1
with open(fname, 'r') as f:
    for line in f:
        print('{0:04} {1}'.format(num, line), end='')  # 格式字符串
        # print('%04d %s' % (num, line), end='')
        num = num + 1

import platform

'''
打印python版本
'''
# print(platform.python_version())

'''
从键盘读取字符串
'''
# name = input('What is your first name? ').strip()  # 使用函数strip()将开头和末尾的空白字符删除
# print('Hello ' + name.capitalize() + '!')  # 函数name.capitalize()确保字符串的第一个字符为大写，而其他字符为小写

'''
在print语句中，必须将整数变量转换为字符串，这样才能打印它
'''
# print("I'm " + str(10) + ' years old')

'''
print在标准输出窗口中打印每个字符串，并用空格分隔它们
'''
# print('jack', 'ate', 'no', 'fat')

'''
修改字符串分隔符
'''
# print('jack', 'ate', 'no', 'fat', sep='.')

'''
print打印完指定内容后添加一个换行符：\n。
换行符导致光标移到下一行，因此默认情况下，调用print后不能在同一行打印任何内容
要在同一行打印所有文本，可将第一行的结束字符指定为空字符串
'''
# print('jack ate ', end='')
# print('no fat')  # jack ate no fat

'''
对用户输入的字符串求值(eval() 函数用来执行一个字符串表达式，并返回表达式的值。)
'''
# print(eval(input('? ')))

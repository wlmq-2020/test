# # # s1 = "我本将心照明月"
# # # s2 = "无奈明月照沟渠"
# # #
# # # print ((s1 + s2)*3)
# #
# #
#
# # !/usr/bin/python3
#
# # a = "Hello"
# # b = "Python"
# #
# # print("a + b 输出结果：", a + b)
# # print("a * 2 输出结果：", a * 2)
# # print("a[1] 输出结果：", a[1])
# # print("a[1:4] 输出结果：", a[1:4])
# #
# # if ("H" in a):
# #     print("H 在变量 a 中")
# # else:
# #     print("H 不在变量 a 中")
# #
# # if "M" not in a:
# #     print("M 不在变量 a 中")
# # else:
# #     print("M 在变量 a 中")
# #
# # print(r'\n')

# # print(R'\n')
#
#
# # n = ['liqi', 'wuxuejing', 'jiqiren', 'chouyou']
# # print(n)
# #
# #
# #
# # info = {
# #         "name":"Liqi",
# #         "age":"30",
# #         "fuck":"Af2213"
# #        }
# #
# # print(info["age"])
# # print('\v')
# #
#
#
# # para_str = """这是一个多行字符串的实例\
# # 多行字符串可以使用制表符
# # TAB ( \t )。
# # 也可以使用换行符 [ \n ]。
# # """
# # print (para_str)
#
#
# n = 'salsas'
#
# print(n.upper())
# print('-------------------')
# print(n.capitalize())
# print(n.center(50,'-'))
# print('--------1')
#
# print(n.endswith('as',0,6))
#
# print(n.title
#       ())
#
#

# keys = [1,2,3,4,5]
#
# print({}.fromkeys(keys,100))


# abc = {'name':'liqi','age':20}
# print(abc)
# print(abc.keys())
# # abc = dict(name='wuxuejing',age=18)
# # print(abc)
# # abc =dict({'name':'chouyou','age':1})
# # print(abc)
# abc['job']='teacher'
# print(abc)
# print(abc.keys())
# abc['name']= 'chouyou'
# print(abc)
# print(abc.keys())
# abc.setdefault('make',[1,2,3])
# print(abc)
# print(abc.keys())


# hash('m')
#
# def printnum(x):
#     for i in range(x):
#         print(i)
#         return
# printnum(10)


# def a(x, y):
#     if x == y:
#         return x, y
#
#
# print (a(3, 3))
# # 创建文件abc.txt
# f = open(file='C:\\Users\\Administrator\\Desktop\\abc.txt', mode='w')
# f.write('吴雪静  女   28  \n')
# f.write('李麒    男   28  \n')
#
# print('----')
#
# f.close()
# # 追加文件
# f = open(file='C:\\Users\\Administrator\\Desktop\\abc.txt', mode='a')
# f.write('臭鼬    母   0.9  \n')
# f.close()
# # 查看文件
# f = open(file='C:\\Users\\Administrator\\Desktop\\abc.txt', mode='r')
# date = f.read()
# print(date)
# f.close()
#
# f = open(file='C:\\Users\\Administrator\\Desktop\\bz_bd_2p.cer')
# print(f.read())
# f.close()
#
# for i in range(100):
#     prin t(i)

# f = open(file='C:\\Users\\Administrator\\Desktop\\NRS00198D_20190624.txt')
# f.seek(2)
# # date=f.read()
# # print(date)
# f.close()
#
# f = open(file='C:\\Users\\Administrator\\Desktop\\aaa.txt',mode='a')
#
#
# f.close()
#
# f = open(file='C:\\Users\\Administrator\\Desktop\\aaa.txt',mode='r')
# f.seek(2)
# print(f.readline())
# print(f.readline(8))
# date=f.read()
# print(date)
# print('----------')
#
# f.close()
#
# f = open(file='C:\\Users\\Administrator\\Desktop\\aaa.txt',mode='a')
# f.write('机器人    无    10    2')
# f.close()
# a+追加  r+  最前面加
# f = open(file='C:\\Users\\Administrator\\Desktop\\aaa.txt', mode='a+')
# f.write('\n金蟾      无    10   10')
# f.close()
#
# f = open(file='C:\\Users\\Administrator\\Desktop\\aaa.txt', mode='r+')
# f.seek(2)
# f.write('姬姬')
# f.close()
#
# from itertools import count

#
# f = open(file='C:\\Users\\Administrator\\Desktop\\aaa.txt', mode='r')
# f_new = open(file='C:\\Users\\Administrator\\Desktop\\bbb.txt', mode='w')
# old_str = '无'
# new_str = '多'
# for line in f:
#     if '无' in line:
#         line = line.replace(old_str, new_str)
#     f_new.write(line)
#
# f.close()
# f_new.close()
#
# f = open(file='C:\\Users\\Administrator\\Desktop\\bbb.txt', mode='r')
# date = f.read()
# print(date)
#
#
# f_new.close()
#

#
# import sys
# print(sys.argv)
#
# print('请输入一下指令替换文件内容 python your_script.py’ old_str new_str filename')
# old_str = input('old_str :')
# new_str = input('new_str :')
# filename = input('filename :')
# print('需要替换的文件是：'+filename+'将文件中的:'+old_str+'替换成:'+new_str)
#
#

# import os
#
#
# date = []
# for Oldfile in os.listdir(r'C:\Users\Administrator\PycharmProjects\Big_py_learn'):
#     f_1=open(file='abc.txt',mode='a')
#     f_1.write(Oldfile+'\n')
#     f_1.close()
#
# f_1=open(file='abc.txt',mode='r')
# date = f_1.read()
# # print(date)
# i = input(':')
# if i in date:
#     print('文件存在')
#     print(i)
#     print('----')
#     print(date)
#     print('----')
#     print(date[8])
# else:
#     print('不存在')
#
# f_1 = open(file='abc.txt', mode='w')
# f_1.write('')
# f_1.close()
#
# import sys
# import os
#
# for Oldfile in os.listdir(r'C:\Users\Administrator\PycharmProjects\Big_py_learn'):
#     f_list = open(file='abc.txt', mode='a')
#     f_list.write(Oldfile + '\n')
#     f_list.close()
#
# f_list = open(file='abc.txt', mode='r')
# date = f_list.read()
# f_list.close()
#
# print(date)

# 乘法表
# for i in range(1, 10):
#     a = ''
#     for j in range(1, i+1):
#             a += str(j) + '*' + str(i) + '=' + str(i * j) + ' '
#     print(a)

# a= int(input('输一个奇数：'))
# b= a//2
# str_a = ' '
# str_b = '*'
#
# for i in range(-b,b+1):
#     c = abs(i)
#     print(str_a*c+str_b*(a-2*c)+str_a*c)
# print(' '*20)
# for i in range(-b,b+1):
#     c = abs(i)
#     print(i,c,b)
#     print(str_a*(b-c)+str_b*(c*2+1)+str_a*(b-c))


# a = {'name':'ll','age':18}
# print(type(a))
# b = [1,2]
# print(type(b))
# c = (1,2)
# print(type(c))
#
# a.copy()
# b.copy()
#
# a = {1}
# print(type(a))
#
#
#
# f = open('aaa.txt','rb')  #读取一个utf-8文件
# f = f.read()
# print(f)
#
# s_unicode = f.decode('gbk')  #解析utf-8 解码成unicode
# print('s_unicode'+s_unicode)
# s_gbk = s_unicode.encode('utf-8')
# print('s_gbk',s_gbk)
#
# a = open('aaa.txt','wb')
# a.write(s_gbk)
# a.close()


# def multiply (x,y):
#     res = x**y
#     return res
# n = multiply(2,3)
# print(n)

#
# def register(name, age, major, country="cn", *args, **kwargs):  ##*args  和**kwargs 站位
#     """
#
#     :param name:
#     :param age:
#     :param major:
#     :param country:
#     :return:
#     """
#
#     info = """
#     -----------你的注册信息----------
#     name : %s
#     age : %s
#     major : %s
#     country : %s
#     args : %s
#     kwargs : %s
#     """ % (name, age, major, country, args, kwargs)
#     print(info)
#
#
# register('LiQi', 18, 'cs', 'CN', 's', 'M', sex='F', addr='阿克苏')
#


# def register(name, *args, **kwargs):
#     print(name, args, kwargs)
#
#
# register('LiQi', 18, 'CS', 'FF', ACD='FF', sex='F')


# namse = {'name','LiQi', 'XiFu','WuXueJing'}   #列表集合，函数内赋值
#
#
# def chane():
#     namse.add('LiQia')
#
#
# chane()
# print(namse)


###函数嵌套，执行顺序
# from Tools.scripts.mailerdaemon import x

# name = '李麒'

# def change():
#     name = '李麒爱学习'
#     print('第二层调用',name)
#
#     def change2():
#         name = '你好未来'
#         print('第三层调用',name)
#
#     change2()
#     print('第一层调用', name)
#
#
# print('最外层调用',name)
# change()


##密名函数

# def calc(x,y):
#     return x**y
#
# print(calc(2,5))
#
#
# c = lambda x,y: x**y
# print(c(2,5))

# def c(x):
#     return x ** 2
#

# b = map(lambda x: x ** 2 if x > 3 else x ** 3, [1, 2, 3, 4, 5])
# print(b)
#
# for i in b:
#     print(i)


# def get_abs(n):
#     return int(str(n).strip('-'))
#
#
# print(get_abs(-9))
# print(abs(-9))

# 高级函数，调用函数，调用函数开平方在相加
# def add(x, y, f):
#     return f(x) + f(y)
#
#
# def f(c):
#     return c ** 2
#
#
# d = add(2, 3, f)
# print(d)

# 高级函数，调用函数，调用函数求余数在相加
# def add(x,y,f):
#     return f(x,y) + f(y,x)
#
# def f(x,y):
#     return x%y
#
# v = add(20,6,f)
#
# print(v)


# ##递归
#
# n = 100
#
# while n >1 :
#     n = n/2
#     print(n)
#
# print('*'*40)


# 用函数循环,  自己调用自己

# def calc(n):
#     print(n)
#     n = int(n / 2)
#     if n > 0:
#         calc(n)

# calc(100)


# if find < c :


# def des(x):
#     len(a)
#     b = int(b/2)
#     print(b)
#     if x < a[0:int(len(a)/2)]:
#         a = a[0:int(len(a)/2)]
#     # elif x > a[c]:
#     #
#     # elif x == a[c]:
#     #     print(a[c]+'在列表当中')
#     #     exit()
#     des(x)
#
# des(3)

# eval  一个list改变成int  可以用eval还原成原来的属性
# names = ['liqi','wuxuejing','chouyou']
#
# f = open('names','w')
# f.write(str(names))
#
# f.close()
#
# f = open('names')
# d = f.read()
# print(d)
# print(type(d))
# d = eval(d)
# print(type(d))
# print(d[2])

# 执行字符串里的python语句
# exec("print('hello word')")

# filter()  过滤  条件为true  打印出来， 为flase 丢弃
# a = list(filter(lambda x:x%2==0 , [1,3,5,7,9,11,13,16,17,19]))
# print(a)
#
# id 打印内存地址
# print(id(a))

#
# print(hex(10))
# print(oct(10))


# a = (1,2,3)
# b = [1, 2, 3]
# c = {1,2,3}
#
# a = frozenset(a)
# b = frozenset(b)
#
#
# print(isinstance(a, frozenset))
# print(isinstance(b, frozenset))
# print(isinstance(c, frozenset))
#
# print(type(a))
# print(type(b))
# print(type(c))

#
# a = {1,2,3,4,5,6,7}
# b = list(map(lambda x:x%2*3,a))
# print(b)
#
# max(a)
# max(b)
# print(max(a))
# print(max(b))

# 内置方法
# print(dir(__builtins__))

# 局部变量locals()--->最近的上层空间enclosing---->全局变量globals()---> 内置方法builtins-in

# 名称空间函数嵌套时读取赋值的顺序
# locals()--->enclosing---->globals()---> builtins-in

#
# #闭包， 创建一个外层函数，然后建立一个内层函数，内层函数打印一个数据，程序结束。返回一个函数名（不带括号）
# # 至外层函数。  外层函数赋值给一个变量。  变量加括号后会引用内层函数。
#
# def outer():
#     name = '吴雪婧'
#
#     def inner():
#         print('Inner',name)
#
#     return inner
#
#
# func = outer()
# print(func)  #返回inner的内存地址
# func()  #相当于执行inner()
#


###装饰器
# account = {
#     'is_auth': False,
#     'username': 'lq',
#     'password': '123'
# }
#
#
# def login(func):
#     def inner(*args,**kwargs):
#         if account['is_auth'] is False:
#             username = input('user:')
#             password = input('password:')
#             if username == account['username'] and password == account['password']:
#                 print('welcome login')
#                 account["is_auth"] = True
#                 func(*args,**kwargs)
#             else:
#                 print('wrong user or pass')
#
#         else:
#             print('用户已经登录，验证通过')
#             func(*args,**kwargs)
#     return inner
#
# def pay_money(func):
#     def incc(*args,**kwargs):
#         print('已支付VIP费用')
#         func(*args,**kwargs)
#     return incc
#
#
# def home():
#     print('欢迎来到-------首页-------专区')
#
# @pay_money
# @login
# def CN():
#
#     print('欢迎来到-------中国-------专区')
#
#
# def US():
#     print(''
#           '欢迎来到-------美国-------专区')
#
# @pay_money
# @login
# def JP(level):
#     if level > 3 :
#         print('欢迎来到-------日本-------专区')
#
# home()
# CN()
# JP(4)
#


#
# def log(func):
#     def inner(*args,**kwargs):
#         print('call %s():' % func.__name__)
#         return func(*args,**kwargs)
#     return inner
#
# @log
# def now():
#     print('2019-10-6')
#
#
# now()
#


##将a里的数据都加1 有哪些方法
# from copy import d
#
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

##1.用map和lambda函数实现
# a = list(map(lambda x:x+1 , a))
# # print(a)


##2.建立一个新列表循环加1

# b = []
# for i in a :b.append(i+1)
# a = b
# print(a)

##用index查找循环加1

# enumerate() 函数用于将一个可遍历的数据对象
# (如列表、元组或字符串) 组合为一个索引序列，
# 同时列出数据和数据下标，一般用在 for 循环当中。

# for index,i in enumerate(a):
#     a[index] += 1
#
# print(a)

# 列表生成式
# a = [i+1 for i in a]
# print(a)


####生成器  边执行边运算
# for i in range(10000):
#     print(i)
#
#     if i > 100:
#         break

# count = 0
# while count <100000:
#     print(count)
#     count += 1
#     print(count)

# b = [i for i in range(20)]  ##列表
# print(b)
# print('*'*20)
# c = (i for i in range(20))  ##生成器
# for i in c:
#     print(i)


###斐波拉契数列
# 除 第一个数和第二个数，任何一个数都是前2个数的和。
# 1,1,2,3,5，8，,13,21,34,…………


###  把函数中生成的变量改 成yield b   就变成函数生成式
# def fao(n):
#     a = 0
#     b = 1
#     count = 0
#     while count < n:
#         tmp = a
#         a = b
#         b = tmp+ b
#         yield b ### 原来print(b)
#         count += 1
#
# print(fao(20))
# f = fao(20)
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
#  print(next(f))


####单线程下的多并发

# def g_test():
#     while True:
#         n = yield
#         print('从外面接收n：', n)
#
# g = g_test()
# g.__next__()  #调用生成器，同事发送none发送到yield
#
# for i in range(10):
#     g.send(i)
#


##吃包子  c1,c2,c3  3个人吃 包子
##生产者    同时生成同事吃

# def consumer(name):
#     print('消费者%s准备吃包子啦。。。'%name)
#     while True:
#         baozi = yield
#         print('消费者%s收到包子编号：%s'%(name,baozi))
#
#
# c1 = consumer('c1')
# c2 = consumer('c2')
# c3 = consumer('c3')
# c1.__next__()
# c2.__next__()
# c3.__next__()
#
# for i in range(10):
#     print('----------生成第%s包子-------- '%i)
#     c1.send(i)
#     c2.send(i)
#     c3.send(i)


# def nmn():
#     while True:
#         n = yield
#         print('外部获取到一个值付给n：',n)
#
# g = nmn()
# g.__next__()
#
# for i in range(5):
#     g.send(i)
#

# 还是吃 包子##
# def eat(name):
#     print('%s准备开始吃包子' % (name))
#     while True:
#         baozi = yield
#         print('%s吃的第%s笼包子' %(name,baozi))
#
# aa = eat('aa')
#  bb = eat('bb')
# cc = eat('cc')
#
# aa.__next__()
# bb.__next__()
# cc.__next__()
#
# for i in range(5):
#     print('-------蒸出的第%s笼包子'%i,'-----------')
#     aa.send(i)
#     bb.send(i)
#     cc.send(i)


# import sys
#
# print('命令行参数如下:')
# for i in sys.argv:
#     print('i:',i, ' ')
#
# for a in range(6):
#     print('\n\nPython 路径为：', sys.path[a], ' ')


# # 写函数，计算传入数字的参数和,动态传参数
# def sum(*num):
#     sum = 0
#     for i in num:
#         sum += i
#     return sum
#
#
# print(sum(20, 10, 22))

# 2，写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改
# import sys
# import os

#
# name = list(sys.argv)
# a = name[1]
# b = name[2]
# c = name[3]
# n = 0
# print(a, b, c)
# f_dir = os.listdir('C:/Users/Administrator/PycharmProjects/Big_py_learn/')
# for i in f_dir:
#     if i == a:
#         print('读取%s内容，准备开始将"%s"修改成"%s" ' % (a, b, c))
#         f = open('C:/Users/Administrator/PycharmProjects/Big_py_learn/%s' % a, 'br')
#         f = list(f.read().decode('gbk'))
#         print(f)
#         long = len(f)
#         for i in f:
#             while n < long:
#                 n += 1
#                 if i == b:
#                     print('准备开始替换'+i)
#                     f = open('C:/Users/Administrator/PycharmProjects/Big_py_learn/New_%s' % a, 'a')
#                     f.write(c)
#                     f.close()
#                     break
#                 else:
#                     f = open('C:/Users/Administrator/PycharmProjects/Big_py_learn/New_%s' % a, 'a')
#                     f.write(i)
#                     f.close()
#                     break


# 3，写函数，检查用户传入的对象（字符串，列表，元组）的每一个元素是否含有空内容
# 字符串    如果字符串中只包含空白，则返回 True，否则返回 False.   isspace()
# 列表      和字典提取出数据转化成字符串，然后判断是否有空内容


# if isinstance(a, int):
#     print("a is int")
# elif isinstance(d, dict):
#     print("d is dict")

# a = [1, 2, 3, 'b', 'c', '', '', 4, 5, 6]
# # a = 'I am a student'
# # a = (1, 2, 3, 4, 5, ' ', '', 4, 5, 6)
# n = 0
#
# if isinstance(a, str):
#     print("a is str")
#     while n < len(a):
#         if a[n].isspace():
#             print('有空格或者空内容')
#             exit()
#         else:
#             pass
#         n += 1
# elif isinstance(a, list):
#     print("a is list")
#     while n < len(a):
#         if a[n] == " ":
#             print('有空格或者空内容')
#             exit()
#         else:
#             pass
#         n += 1
#     print('没有空内容')
# elif isinstance(a, tuple):
#     print("a is tuple")
#     while n < len(a):
#         if a[n] != " ":
#             pass
#         else:
#             print('有空内容')
#             exit()
#         n += 1
#     print('没有空内容')
# else:
#     print('没有符合的类型')

# 4.写函数，检查传入字典的每一个value的长度，如果大于2，那么仅保留前两个长度的内容
# ，并将断内容返回调用者，注意传入的数据可以是str，list，dict
#
# m = {'name': 'li qi', 'sex': 'man', 'score': '100', 'run': (1.2, 2.3, 3.3, 4.4, 5.5),
#      'course': {'语文': 97, '数学': 100, '英语': 88}}
# u = {'语文': 9723, '数学': 100123, '英语': 88123}
#
#
#
# def cc(m):
#     for i in m.keys():
#         if type(m.get(i)) is dict:
#             for n in m.get(i).keys():
#                 m[i][n] = str(m[i][n])
#                 m[i][n] = (m[i][n][:2])
#         else:
#             if len(m.get(i)) > 2:
#                 m[i] = m[i][:2]
#     print(m)
#
# cc(m)


# 解释闭包，写一个,装饰器

# def sum(func):
#     def say_hello(*args, **kwargs):
#         print('Hello world')
#         return func()
#     return say_hello
#
#
# @sum
# def chen():
#     print('*'*20)
#
#
# chen()
#

# 6，写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组  例如 [（红心’，2）（‘草花’，2）。。（‘黑桃A’）]
# puke = []
# a = ['红桃', '梅花', '方块', '黑桃']
# e = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
# for i in a:
#     for l in e:
#         m = (i, l)
#         puke.append(m)
# print(puke)

# 7.写函数，传入n个数，返回字典['max':最大值,'mix':最小值]
# a = (5, 6, 7, 8, 9, 11, 13, 15)
# print(max(a))
# print(min(a))
#
#
# def com(x):
#     a = max(x)
#     b = min(x)
#     c = {}
#     c['max'] = a
#     c['min'] = b
#     print(c)
#
#
# com(a)


# 8 写函数，专门计算图形的面积
# 其中嵌套函数，计算圆的面积，正方形的面积，长方形的面积
# 调用函数area（‘圆形’，圆半径）返回圆的面积
# 调用函数area（‘正方形’，圆半径）返回正方形的面积
# 调用函数area（‘长方形’，圆半径）返回长方形的面积

# def area(*args):
#     # 判断参数
#     if args[0] == '长方形':
#         def 计算长方形面积():
#             s = args[1] * args[2]
#             return s
#
#         return 计算长方形面积()
#     elif args[0] == '正方形':
#         def 计算正方形面积():
#             s = args[1] ** 2
#             return s
#
#         return 计算正方形面积()
#     elif args[0] == '圆形':
#         def 计算圆形面积():
#             s = 3.14 * (args[1] ** 2)
#             return s
#
#         return 计算圆形面积()
#
#
# print(area('长方形', 2, 3))
# print(area('正方形', 5))
# print(area('圆形', 6))


# 9写函数， 传入一个参数n 返回n的阶乘

# def factorial(n):
#     m = n + 1
#     res = 1
#     for i in range(m):
#         # print(i)
#         if i == 0:
#             pass
#         else:
#             res = res *i
#     print(res)
#
#
# factorial(4)


# 10 编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件）
# ，要求登录成功一次，后续的函数都无需再输入用户名和密码

# a = {'user': 'li', 'passwd': 123, 'auth': 1}
#
# def login(func):
#     def inner():
#         if a['user'] == 'li' and a['passwd'] == 123 and a['auth'] == 1:
#             print('登录成功')
#             a['auth'] = 2
#             return func()
#         elif a['auth'] == 2:
#             print('已经认证，可以访问下面的信息')
#             return func()
#     return inner
#
#
#
#
# @login
# def EARTH():
#     print('*'*10,'欢迎来到地球','*'*10)
#
#
#
# @login
# def CN():
#     print('*'*10,'欢迎来到中国','*'*10)
#
# @login
# def UN():
#     print('*'*10,'欢迎来到英国','*'*10)
#
# @login
# def USA():
#
#     print('*'*10,'欢迎来到美国','*'*10)
#
# EARTH()
# CN()
# USA

# 迭代器
# a = [i for i in range(10)]
# for i in a:
#     print(i, end=' ')

# print('***************')

# b = (c for c in range(10))
# for e in b:
#     print(e, end=', ')

# 生成器属于迭代器，
# 生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
# 用yield的 就是生成器，每次执行一句代码，返回一个值，节省空间

# import sys
#
#
# def fib(n):
#     a, b, count = 0, 1, 0
#     while True:
#         if count > n:
#             return
#         # tmp = b
#         # b = a + b
#         # a = tmp
#         a,b = b,a+b
#         yield a
#         count += 1
#
#
# a = fib(10)
# print(next(a))
# print(next(a))
# print('yield,会从函数中调出来执行此行程序，执行完成后继续执行下面的程序')
# print(next(a))
# print(next(a))
#
# while True:
#     try:
#         print('呕吼:', next(a))
#     except StopIteration:
#         sys.exit()


# def myYield_1():
#     a, i = 'yield', 0
#     while True:
#         print('before #%d' % i, end=", ")
#         yield a, i
#         print('after #%d' % i, end=", ")
#         i += 1
#
#
# def myYield_2():
#     a, i = 'yield_a', 0
#     b, i = 'yield_b', 0
#     while True:
#         print('before #%d' % i, end=", ")
#         yield a, i
#         yield b, i
#         print('after #%d' % i, end=", ")
#         i += 1
#
#
# it1 = iter(myYield_1())
# it2 = iter(myYield_2())
#
# for i in range(10):
#     print("next #%d" % i, end=": ")
#     print(next(it1))
# print('\n')
# for i in range(10):
#     print("next #%d" % i, end=": ")
#     print(next(it2))
#


#
# import os
# os.getcwd()      # 返回当前的工作目录
#
# os.chdir('/')   # 修改当前的工作目录
# os.system('mkdir today')   # 执行系统命令 mkdir
#

# 题目 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# 解法1
# a = 0
# for i in range(1, 5):
#     for j in range(1, 5):
#         for q in range(1, 5):
#             if i != j and i != q and j != q:
#                 print(i, j, q)
#                 a += 1
# print(a)

# # 解法2
# # import itertools
# # sum2=0
# # a=[1,2,3,4]
# # for i in itertools.permutations(a,3):
# #     print(i)
# #     sum2+=1
# # print(sum2)
# #
# # # 解法3
# #
# # a = set() #集合
# #
# # for i in range(1, 5):
# #     for j in range(1, 5):
# #         for q in range(1, 5):
# #             if i != j and i != q and j != q:
# #                 b = i*100+j*10+q
# #                 a.add(b)
# #
# # print(a)
# # print(len(a))


# 实例002：“个税计算”
# 题目 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？

# profit = int(input('Show me the money: '))
# bonus = 0
# thresholds = [100000, 100000, 200000, 200000, 400000]
# rates = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
# for i in range(len(thresholds)):
#     if profit <= thresholds[i]:
#         bonus += profit * rates[i]
#         profit = 0
#         break
#     else:
#         bonus += thresholds[i] * rates[i]
#         print(bonus,i)
#         profit -= thresholds[i]
# bonus += profit * rates[-1]
# print(bonus)

# 实例003：完全平方数
# 题目 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
#
# 程序分析 因为168对于指数爆炸来说实在太小了，所以可以直接省略数学分析，用最朴素的方法来获取上限:


#
# cc = set()
# bb = set()
# for x in range(1000):
#     for y in range(1000):
#         if y ** 2 == x + 100:
#             # print(x,y)
#             cc.add(x)
#
# for x in range(1000):
#     for z in range(1000):
#         if z ** 2 == x + 168:
#             # print(x,z)
#             bb.add(x)
#
# print(cc&bb)

#
# 实例004：这天第几天
# 题目 输入某年某月某日，判断这一天是这一年的第几天？
# def isLeapYear(y):
#     return (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0))
#
#
#
# year = int(input('输入年'))
# month = int(input('输入月'))
# day = int(input('输入日'))
# res = 0
# time = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#
# if isLeapYear(year):
#     time[2] += 1
# for i in range(month):
#     res += time[i]
# print(res+day)

# 实例005：三数排序
# 题目 输入三个整数x,y,z，请把这三个数由小到大输出
# 解法1
# a = []
# x = int(input('输入x:'))
# a.append(x)
# y = int(input('输入y:'))
# a.append(y)
# z = int(input('输入z:'))
# a.append(z)
#
# print(min(a),end=' ')
# for i in range(0,3):
#     if min(a) < a[i] < max(a):
#         print(a[i],end=' ')
# print(max(a),end=' ')

# 解法2

# raw = []
# for i in range(3):
#     x = int(input('int%d: ' % (i)))
#     raw.append(x)
#
# for i in range(len(raw)):
#     for j in range(i, len(raw)):
#         if raw[i] > raw[j]:
#             raw[i], raw[j] = raw[j], raw[i] #先运算右侧的在赋值给左侧
# print(raw)
#
# raw2 = []
# for i in range(3):
#     x = int(input('int%d: ' % (i)))
#     raw2.append(x)
# print(sorted(raw2))

#
# 实例006：斐波那契数列
# 题目 斐波那契数列。

# def fib(arg):
#     a, b, n = 0, 1, 0
#     while n < arg:
#         a, b = b, a + b
#         n += 1
#         print(a)
#
#
# fib(10)

#
# 实例007：copy
# 题目 将一个列表的数据复制到另一个列表中。
#
# 程序分析 使用列表[:]，拿不准可以调用copy模块。

# a = [1,2,3,4,5,6,(1,2,3)]
# b = [4,5,6,7,8,9]
#
# for i in a:
#     b.append(i)
#
#
# print(b)


# 实例008：九九乘法表
# 题目 输出 9*9 乘法口诀表。
#
# 程序分析 分行与列考虑，共9行9列，i控制行，j控制列。
# 方法1
# for i in range(1, 10):
#     for j in range(1, 10):
#         if i == j:
#             print(j, '*', i, '=', i * j)
#         elif j < i:
#             print(j, '*', i, '=', i * j, end='  ')
#
# # 方法2
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%2ld ' % (i, j, i * j), end='')
#     print()


# 实例009：暂停一秒输出
# 题目 暂停一秒输出。
#
# import time
# for i in range(4):
#     print(str(int(time.time()))[-2:])
#     time.sleep(1)

# 实例010：给人看的时间
# # 题目 暂停一秒输出，并格式化当前时间。
# #
# # 程序分析 同009.

# import time
# while True:
#     print(time.strftime('%Y-%m-%d %H:%M:%S'))
#     time.sleep(1)

# 实例011：养兔子
# 题目 有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

# 程序分析 考虑到三个月成熟，可以构建四个数据，
# 其中：一月兔每个月长大成为二月兔，二月兔变三月兔，三月兔变成年兔，
# 成年兔（包括新成熟的三月兔）生等量的一月兔。

# month = int(input('繁殖几个月？： '))
# month_1 = 1
# month_2 = 0
# month_3 = 0
# month_elder = 0
# for i in range(month):
#     month_1, month_2, month_3, month_elder = month_elder + month_3, month_1, month_2, month_elder + month_3
#     print('第%d个月共' % (i + 1), month_1 + month_2 + month_3 + month_elder, '对兔子')
#     print('其中1月兔：', month_1)
#     print('其中2月兔：', month_2)
#     print('其中3月兔：', month_3)
#     print('其中成年兔：', month_elder)

#
# 实例012：100到200的素数
# 题目 判断101-200之间有多少个素数，并输出所有素数。
#
# 程序分析 判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
# 用else可以进一步简化代码.

# 方法1
# a = set()
# b = set()
# for i in range(100, 200):
#     for j in range(2, i - 1):
#         if i % j == 0:
#             a.add(i)
# b = {i for i in range(100, 200)}
# c = b - a
#
# for i in c :
#     print(i,end=" ")
#
#
# print(' ')
# # 方法2
# import math
#
# for i in range(100, 200):
#     flag = 0
#     for j in range(2, round(math.sqrt(i)) + 1):
#         if i % j == 0:
#             flag = 1
#             break
#     if flag:
#         continue
#     print(i, end=' ')
#
# print('\nSimplify the code with "else"\n')
# # 方法3
# for i in range(100, 200):
#     for j in range(2, round(math.sqrt(i)) + 1):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=' ')


# 实例013：所有水仙花数
# 题目 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

# 方法1
# for a in range(1,10):
#     for b in range(0,10):
#         for c in range(0, 10):
#             if a*100+b*10+c == a**3+b**3+c**3:
#                 print(a*100+b*10+c)
# print('*******************************************')
# #方法2
# for i in range(100,1000):
#     s=str(i)
#     one=int(s[-1])
#     ten=int(s[-2])
#     hun=int(s[-3])
#     if i == one**3+ten**3+hun**3:
#         print(i)

#
# 实例014：分解质因数
# 题目 将一个整数分解质因数。例如：输入90,打印出90=233*5。
#
# 程序分析 根本不需要判断是否是质数，从2开始向数本身遍历，能整除的肯定是最小的质数。

# num = int(input('输入一个整数：'))
# x = num
# a = []
# for i in range(2, num + 1):
#     while num != 1:
#         if num % i == 0:
#             a.append(i)
#             num = num / i
#         else:
#             break
# b = len(a)
# c = b - 1
# for i in a:
#     if b > 0:
#         print(i, end='')
#         b -= 1
#     if c > 0:
#         print('*', end='')
#         c -= 1
# print('=%s'%x)


# 方法2
# target = int(input('输入一个整数：'))
# print(target, '= ', end='')
#
# if target < 0:
#     target = abs(target)
#     print('-1*', end='')
#
# flag = 0
# if target <= 1:
#     print(target)
#     flag = 1
#
# while True:
#     if flag:
#         break
#     for i in range(2, int(target + 1)):
#         if target % i == 0:
#             print("%d" % i, end='')
#             if target == i:
#                 flag = 1
#                 break
#             print('*', end='')
#             target /= i
#             break


# 实例015：分数归档
# 题目 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

# sco = int(input('分数:'))
# if sco >= 90:
#     print('评分为A')
# elif 89 >= sco >= 60:
#     print('评分为B')
# elif sco < 60:
#     print('评分为C')

# 实例016：输出日期
# 题目 输出指定格式的日期。
#
# 程序分析 使用 datetime 模块。
# 方法1
# import time
#
# print(time.strftime('%Y-%m-%d , %H:%M:%S'))

# import datetime
# print(datetime.date.today())
# print(datetime.date(2333,2,3))
# print(datetime.date.today().strftime('%d/%m/%Y'))
# day=datetime.date(1111,2,3)
# day=day.replace(year=day.year+22)
# print(day)

#
# 实例017：字符串构成
# 题目 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
#
# 程序分析 利用 while 或 for 语句,条件为输入的字符不为 ‘\n’。
# 方法1

# string=input("输入字符串：")
# alp=0
# num=0
# spa=0
# oth=0
# for i in range(len(string)):
#     if string[i].isspace():
#         spa+=1
#     elif string[i].isdigit():
#         num+=1
#     elif string[i].isalpha():
#         alp+=1
#     else:
#         oth+=1
# print('space: ',spa)
# print('digit: ',num)
# print('alpha: ',alp)
# print('other: ',oth)


#
# 实例018：复读机相加
# 题目 求s=a+aa+aaa+aaaa+aa…a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
#
# a= input('被加数字：')
# n= int(input('加几次？：'))
# res= 0
# for i in range(n):
#     res+= int(a)
#     a+=a[0]
# print('结果是：', res)
#

# 实例019：完数
# 题目 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
# 方法1
# for i in range(1,1000):
#     a = set()
#     res = 0
#     for j in range(1,i):
#         if i % j == 0:
#             a.add(j)
#             res += j
#     if res == i:
#         print(i)

# 方法2
# def factor(num):
#     target=int(num)
#     res=set()
#     for i in range(1,num):
#         if num%i==0:
#             res.add(i)
#             res.add(num/i)
#     return res
#
# for i in range(2,1001):
#     if i==sum(factor(i))-i:
#         print(i)

# 实例020：高空抛物
# 题目 一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
# 方法1
# high = 100
# times = 10
# res = 0
# while times > 0:
#     high /= 2
#     times -= 1
#     res += 2*high
# print(high)
# print(res + 100)

# 方法1
# high=200
# total=100
# for i in range(10):
#     high/=2
#     total+=high
#     print(high/2)
# print('总长：',total)

#
# 实例021：猴子偷桃
# 题目 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，
# 又多吃了一个第二天早上又将剩下的桃子吃掉一半，
# 又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。
# 求第一天共摘了多少。

# 程序分析 按规则反向推断：猴子有一个桃子，他偷来一个桃子，觉得不够又偷来了与手上等量的桃子，一共偷了9天。
# day = 0
# tao = 1
# while day < 9:
#     day +=1
#     tao = 2*(tao+1)
#     print('第%s天,有%s个桃'%(day,tao))
#
#
# peach=1
# for i in range(9):
#     peach=(peach+1)*2
# print(peach)

# 实例022：比赛对手
# 题目 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
# 有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
# 方法1
# a = {'y', 'z'}
# b = {'x', 'y', 'z'}
# c = {'y'}
#
# for i in a:
#     for p in b:
#         for r in c:
#             if len({i, p, r}) == 3:
#                 print(i, 'vs', 'a ', p, 'vs', 'b ', r, 'vs', 'c ', )

# 实例023：画菱形
# 题目 打印出如下图案（菱形）:
# 方法1
# x = '*'
# k = ' '
# def ling(n):
#     c = int((n - 1) / 2)
#     if (n - 1) % 2 == 0:
#         for i in range(-c, c+1):
#             print(abs(i)*k+(n-2*abs(i))*x+abs(i)*k)
#     else:
#         print('请输入一个奇数')
#
# ling(11)


# 方法2
# def draw(num):
#     a="*"*(2*(4-num)+1)
#     print(a.center(9,' '))
#     if num!=1:
#         draw(num-1)
#         print(a.center(9,' '))
# draw(5)

#
# 实例024：斐波那契数列II
# 题目 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13…求出这个数列的前20项之和。
#
# 程序分析 就是斐波那契数列的后一项除以前一项。
# 方法1
# a = 1
# b = 2
# n = 20
# sum = 0
# while n > 0:
#     sum += b/a
#     a,b = b , a+b
#     n -= 1
#
# print(sum)
#
# 方法2
# a = 2.0
# b = 1.0
# s = 0
# for n in range(1,21):
#     s += a / b
#     a,b = a + b,a
# print (s)


# 实例025： 阶乘求和
# 题目 求1+2!+3!+…+20!的和。
#
# 程序分析 1+2!+3!+…+20!=1+2(1+3(1+4(…20(1))))

# 方法2
# res = 1
# for i in range(20, 1, -1):
#     res = i * res + 1
# print(res)
#

# 方法1
# def chen(m):
#     m = m + 1
#     res = 1
#     while m > 1:
#         res = res * (m - 1)
#         m -= 1
#     return res
#
#
# a = 0
# for i in range(21):
#     a += chen(i)
#
# print(a)
#


# 实例026：递归求阶乘
# 题目 利用递归方法求5!。
#
# 程序分析 递归调用即可。


# def chen(n):
#     return n*chen(n-1) if n >1 else 1
#
#
# print(chen(5))

#
# 实例027：递归输出
# 题目 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。


# def rec(string):
#     if len(string) != 1:
#         rec(string[1:])
#     print(string[0], end='')
#
#
# rec(input('string here:'))


# 实例028：递归求等差数列
# 题目 有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
# 问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。
# 问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
#
# def year(n):
#     a = 8
#     n =a +2*n
#     return n
#
# print(year(2))
#
# def age(n):
#     if n==1:
#         return 10
#     return 2+age(n-1)
# print(age(1))


# 实例029：反向输出
# 题目 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
#
# 程序分析 学会分解出每一位数,用字符串的方法总是比较省事。

# n = input('输入一个整数：')
# n = str(n)
# print('%s是一个%s数'%(n,len(n)))
# print(n[::-1])


# 实例030：回文数
# 题目 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
#
# 程序分析 用字符串比较方便,就算输入的不是数字都ok。

# n = str(input('输入一个数字判断是否是回文数字：'))
# a = 0
# b = len(n) - 1
# flag = True
# while a < b:
#     if n[a] != n[b]:
#         print('不是回文数')
#         flag = False
#         break
#     a, b = a + 1, b - 1
#
# if flag:
#     print('是回文数字')


# 实例031：字母识词
# 题目 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

# 周一Monday 周二Tuesday 周三Wednesday 周四Thursday 周五Friday 周六Saturday 周日Sunday
#
# weekS = {'a': 'Saturday', 'u': 'Sunday'}
# weekT = {'u': 'Tuesday', 'h': 'Thursday'}
# week = {'m': 'Monday', 'w': 'Wednesday', 'f': 'Friday', 't': weekT, 's': weekS}
#
# letter = week[str(input('输入一个字母，来判断是星期几:')).lower()]
#
# if letter == weekS or letter == weekT:
#     letter = letter[str(input('输入第二个字母，来判断是星期几:')).lower()]
# print(letter)


#
# 实例032：反向输出II
# 题目 按相反的顺序输出列表的值。
#
# 程序分析 无。

# a = ['one', 'two', 'three']
# print(a[::-1])


# 实例033：列表转字符串
# 题目 按逗号分隔列表。

# a = ['one', 'two', 'three']
# print(type(a),a)
# a = str(a)
#
# print(type(a),a)
#
# b = ['one', 'two', 'three']
# c =''
# for i in b:
#     c += i
#
# print(c)


# 实例035：设置输出颜色
# 题目 文本颜色设置。
#
# 程序分析 无。

# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
#
#
# print(bcolors.WARNING + "警告的颜色字体?" + bcolors.OKBLUE)
# print(bcolors.HEADER + "警告的颜色字体?" )


# 实例036：算素数
# 题目 求100之内的素数。
#
# 程序分析 用else执行for循环的奖励代码（如果for是正常完结，非break）。

# for i in range(2, 100):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)


# lo=int(input('下限：'))
# hi=int(input('上限：'))
# for i in range(1, 100):
#     if i > 1:
#         for j in range(2, i):
#             if (i % j) == 0:
#                 break
#         else:
#             print(i)


# 实例037：排序
# 题目 对10个数进行排序。

# a = [5, 29, 54, 83, 43, 14, 67, 87, 59, 13, 1, 11, 100]
# c = int(len(a)) - 1
#
#
# def nn(n):
#     while n > 1:
#         for i in range(c):
#             if a[i] < a[i + 1]:
#                 pass
#             else:
#                 a[i], a[i + 1] = a[i + 1], a[i]
#         n -= 1
#
#     return a
#
#
# print(nn(len(a)))
# a.sort()
# print(a)


# 方法2
# raw = []
# for i in range(10):
#     x = int(input('int%d: ' % (i)))
#     raw.append(x)
#
# for i in range(len(raw)):
#     for j in range(i, len(raw)):
#         if raw[i] > raw[j]:
#             raw[i], raw[j] = raw[j], raw[i]
# print(raw)

# 方法3  方法4
# a = [5, 29, 54, 83, 43, 14, 67, 87, 59, 13, 1, 11, 100]
# a.sort()
# print(a)
#
# b = [5, 29, 54, 83, 43, 14, 67, 87, 59, 13, 1, 11, 100]
# print(sorted(b))

# 实例038：矩阵对角线之和
# 题目 求一个3*3矩阵主对角线元素之和。

# mat = [[1,2,3],
#        [4,5,6],
#        [7,8,9]]
#
# res=0
# for i in range(len(mat)):
#     res+=mat[i][i]
# print(res)

# 实例039：有序列表插入元素
# 题目 有一个已经排好序的数组。
# 现输入一个数，要求按原来的规律将它插入数组中。
#
# 程序分析 首先判断此数是否大于最后一个数，
# 然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。
#
# lis=[1,10,100,1000,10000,100000]
# n=int(input('insert a number: '))
# lis.append(n)
# for i in range(len(lis)-1):
#     if lis[i]>=n:
#         for j in range(i,len(lis)):
#             lis[j],lis[-1]=lis[-1],lis[j]
#         break
# print(lis)


# 实例040：逆序列表
# 题目 将一个数组逆序输出。

# a = [123,342,654,765,876,987,239,198]
#
# a.sort(reverse=True )
# print(a)

# 实例041：类的方法与变量
# 题目 模仿静态变量的用法。

# def dummy():
#     i = 0
#     print(i)
#     i += 1
#
#
# class cls:
#     i = 999
#
#     def dummy(self):
#         print(self.i)
#         self.i += 1
#
#
# a = cls()
# for i in range(10):
#     print('函数')
#     dummy()
#     print('类')
#     a.dummy()
#
#
# 实例042：变量作用域
# 题目 学习使用auto定义变量的用法。

# i = 0
# n = 0
#
# def dummy():
#     i=0
#     print('函数i：',i)
#     i+=1
# def dummy2():
#     global n
#     print('函数n：',n)
#     n+=1
# print('局部内部的同名变量')
# for j in range(20):
#     print('i:',i)
#     dummy()
#     i+=1
# print('global声明同名变量')
# for k in range(20):
#     print('n:',n)
#     dummy2()
#     n+=10


#
# 实例043：作用域、类的方法与变量
# 题目 模仿静态变量(static)另一案例。
#
# 程序分析 综合实例041和实例042。
#
# class dummy:
#     num=1
#     def Num(self):
#         print('class dummy num:',self.num)
#         print('global num: ',num)
#         self.num+=1
#
# n=dummy()
# num=1
# for i in range(5):
#     num*=10
#     n.Num()
#
# 实例044：矩阵相加
# 题目 计算两个矩阵相加。


# X = [[12, 7, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# Y = [[5, 8, 1],
#      [6, 7, 3],
#      [4, 5, 9]]
#
# res= [[0,0,0],
#      [0,0,0],
#      [0,0,0]]
#
# for i in range(len(res)):
#     for j in range(len(res)):
#         res[i][j] = X[i][j] + Y[i][j]
#
# print(res)

#
# 实例045：求和
# 题目 统计 1 到 100 之和。

# a = range(101)
# print(a)
# print(sum(a))
#
# res = 0
# for i in range(101):
#     res += i
#
# print(res)

#
# 实例046：打破循环
# 题目 求输入数字的平方，如果平方运算后小于 50 则退出。
# 方法1
# while True:
#     x = int(input('输入一个数字：'))
#
#     if x**2 < 50:
#         break
#     else:
#         print(x**2)

# 方法2

# while True:
#     try:
#         n=float(input('输入一个数字：'))
#     except:
#         print('输入错误')
#         continue
#     dn=n**2
#     print('其平方为：',dn)
#     if dn<50:
#         print('平方小于50，退出')
#         break

#
# 实例047：函数交换变量
# 题目 两个变量值用函数互换。
#
# 程序分析 无
# 方法2
# def exc(a,b):
#     return (b,a)
# a=0
# b=10
# a,b=exc(a,b)
# print(a,b)
#
# # 方法1
# def cds(x,y):
#     x,y = y,x
#     print(x,y)
#
#
# cds(1,5)

#
# 实例048：数字比大小
# 题目 数字比较。
#
# 程序分析 无
#
# a=int(input('a='))
# b=int(input('b='))
# if a<b:
#     print('a<b')
# elif a>b:
#     print('a>b')
# else:
#     print('a=b')

#
# 实例049：lambda
# 题目 使用lambda来创建匿名函数。

# a = lambda x: x**2
# print(a(2))

# 实例050：随机数
# 题目 输出一个随机数。
#
# 程序分析 使用 random 模块。

# print(random.uniform(10,20))
#
# print(random.randint(1,6))
# print(random.choice('1231asdasdasd'))

# a = random.choice('1231asdasdasd')
# print(a)


# 实例051：按位与
# 题目 学习使用按位与 & 。
#
# 程序分析 0&0=0; 0&1=0; 1&0=0; 1&1=1。

# a=8
# print(a)
# b=a&2
# print(b)
# b=b&7
# print(b)


# 实例052：按位或
# 题目 学习使用按位或 | 。
#
# 程序分析 0|0=0; 0|1=1; 1|0=1; 1|1=1

# a=0o77
# print(a|3)
# print(a|3|7)

# 实例053：按位异或
# 题目 学习使用按位异或 ^ 。
#
# 程序分析 0^0=0; 0^1=1; 1^0=1; 1^1=0

# a=0o77
# print(a^3)
# print(a^3^7)


# 实例054：位取反、位移动
# 题目 取一个整数a从右端开始的4〜7位。
#
# 程序分析 可以这样考虑：
# (1)先使a右移4位。
# (2)设置一个低4位全为1,其余全为0的数。可用(0<<4)
# (3)将上面二者进行&运算。


# a = 8
# b = 0  # 0
# print(b)
# b = ~b  # 1
# print(b)
# b = b << 4  # 10000
# print(b)
# b = ~b  # 1111
# print(b)
# c = a >> 4
# d = c & b
# print('a:', bin(a))
# print('b:', bin(b))
# print('c:', bin(c))
# print('d:', bin(d))
#
# x =1
# y =2
# z = -3
# print(~x)
# print(~y)
# print(~z)
# ## ~ 按位取反  就是  先加1 之后乘以-1
#
#

#
#
# 实例060：字符串长度
# 题目
# 计算字符串长度。
#
# 程序分析
# 无。
#
# s = 'zhangguang101'
# print(len(s))
#
# 实例061：杨辉三角
# 题目
# 打印出杨辉三角形前十行。
#
# 程序分析
# 无。
#


# def generate(numRows):
#     r = [[1]]
#     for i in range(1,numRows):
#         r.append(list(map(lambda x,y:x+y, [0]+r[-1],r[-1]+[0])))
#     return r[:numRows]
# a=generate(2)
# for i in a:
#     print(i)
#


#
# 实例062：查找字符串
# 题目 查找字符串。
#
# 程序分析 无。

# a ='sdfsdfasdfasdf2312312312'
# b = '23'
# c = 'fs'
#
# print(a.find(b))
# print(a.find(c))
# print(a[2:4])

#
# 实例066：三数排序
# 题目 输入3个数a,b,c，按大小顺序输出。

# a = int(input('输第一个数：'))
# b = int(input('输第二个数：'))
# c = int(input('输第三个数：'))
#
# d = [a,b,c]
# d.sort(reverse=1)
# print(d)
#


# 实例067：交换位置
# 题目 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
#
# a = [123,564,78,231,564,328,321,987,534,90]
#
# d = max(a)   #最大的数
# e = min(a)   #最小的数
#
# x = a.index(d)  #最大数的位置
# y = a.index(e)  #最小数的位置
#
# a[0],a[-1],a[x],a[y] = a[x],a[y],a[0],a[-1]
# print(a)


#
# 实例068：旋转数列
# 题目 有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
#
# from collections import *
# li=[1,2,3,4,5,6,7,8,9]
# deq=deque(li,maxlen=len(li))
# print(li)
# deq.rotate(int(input('rotate:')))
# print(list(deq))


# 实例069：报数
# 题目 有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），
# 凡报到3的人退出圈子，问最后留下的是原来第几号的那位。

# if True:
#     n = int(input('请输入总人数:'))
#     num = []      # 圈里的人数
#     for i in range(n):
#         num.append(i + 1)
#
#     i = 0         # 循环人数
#     k = 0         # 每个人数的数
#     m = 0         # 数到3的人会被置零，然后m加1
#
#     while m < n - 1:    # m< n -1 意思就是置零的数要比总人数少1  会剩下最后一个人
#         if num[i] != 0: k += 1 # 如果这个人的值不是0，那么k+1
#         if k == 3:      # 当k等于3时
#             num[i] = 0  # 将num[i]这个人的值置0
#             k = 0       # k置0，重新数
#             m += 1      # 置零的人数要加1
#         i += 1          # 继续数下一个人
#         if i == n: i = 0  # 当i每数一个人加1，最后和总人数相当时，置0,然后循环可以继续
#
#     i = 0               # i置0 ，下面的循环从头开始判断
#     while num[i] == 0: i += 1   # 如果num[i]是0，那么继续判断下一个数，如果不是 那么打印这个数
#     print(num[i])
#
#


# 实例070：字符串长度II
# 题目 写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。
#
# 程序分析 无。
#
# def lenofstr(s):
#     return len(s)
#
# print(lenofstr('tanxiaofengsheng'))


# 实例071：输入和输出
# 题目
# 编写input()
# 和output()
# 函数输入，输出5个学生的数据记录。
#
# 程序分析
# 无。

N = 3

# stu
# num : string
# name : string
# score[4]: list
# student = []
# for i in range(5):
#     student.append(['', '', []])
#
#
# def input_stu(stu):
#     for i in range(N):
#         stu[i][0] = input('input student num:\n')
#         stu[i][1] = input('input student name:\n')
#         for j in range(3):
#             stu[i][2].append(int(input('score:\n')))
#
#
# def output_stu(stu):
#     for i in range(N):
#         print('%-6s%-10s' % (stu[i][0], stu[i][1]))
#         for j in range(3):
#             print('%-8d' % stu[i][2][j])
#
#
#
# input_stu(student)
# print(student)
# output_stu(student)


#
# 实例074：列表排序、连接
# 题目 列表排序及连接。
#
# 程序分析 排序可使用 sort() 方法，连接可以使用 + 号或 extend() 方法。

#
# x = [11, 12, 13, 4, 5]
# y = ['g', 'b', 'c', 'd', 'e']
#
# x.sort()
# print(x)
# y.sort()
# print(y)
#
# print(x+y)
# x.extend(y)


# 实例075：不知所云

# if True:
#     for i in range(5):
#         n = 0
#         if i != 1: n += 1
#         if i == 3: n += 1
#         if i == 4: n += 1
#         if i != 4: n += 1
#         if n == 3: print(64 + i)


# 实例076：做函数
# 题目 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+…+1/n,当输入n为奇数时，调用函数1/1+1/3+…+1/n


# def su(n):
#     res = 0
#     if n % 2 == 0:
#         for i in range(2,n+1,2):
#             res += 1/i
#         print(res)
#     else:
#         for i in range(1,n+1,2):
#             res += 1/i
#         print(res)
# su(4)


# 实例077：遍历列表
# 题目 循环输出列表
#
# # 程序分析 无。
#
# l=['moyu','niupi','xuecaibichi','shengfaji','42']
# for i in range(len(l)):
#     print(l[i])
#
#
# for i in l:
#     print(i)


# 实例078：字典
# 题目 找到年龄最大的人，并输出。请找出程序中有什么问题。
# 方法1
# person = {"li":18,"wang":50,"zhang":20,"sun":22}
# a = []
# b = []
# for i,j in person.items():
#     a.append((i,j))
#     b.append(j)
# for i in range(len(b)):
#     if a[i][1] == sorted(b)[-1]:
#         print(a[i])
#
#
# # 方法2
# if __name__ == '__main__':
#     person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
#     m = 'li'
#     for key in person.keys():
#         if person[m] < person[key]:
#             m = key
#
#     print('%s,%d' % (m, person[m]))


# 实例079：字符串排序
# 题目 字符串排序。
#
# 程序分析 无。

# l=['baaa','aaab','aaba','AAaa','abaa']
# l.sort()
# print(l)


# 实例080：猴子分桃
# 题目 海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，
# 多了一个，这只猴子把多的一个扔入海中，拿走了一份。第二只猴子把剩下的桃子又平均分成五份，
# 又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，
# 问海滩上原来最少有多少个桃子？


# if __name__ == '__main__':
#     i = 0
#     j = 1
#     x = 0
#     while (i < 5) :
#         x = 4 * j
#         for i in range(0,5) :
#             if(x%4 != 0) :
#                 break
#             else :
#                 i += 1
#             x = (x/4) * 5 +1
#         j += 1
#     print(x)
#
#     for p in range(5):
#         x=(x-1)/5*4
#     print(x)
#


#
# 实例081：求未知数
# 题目 809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，
# 8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。

# 方法1
# for i in range(10,14):
#     if 809*i == 800*i+9*i and 8*i<100 and 9*i>100:
#         print('??为',i,'809*i值为',809*i)

# 方法2
# a = 809
# for i in range(10,100):
#     b = i * a
#     if b >= 1000 and b <= 10000 and 8 * i < 100 and 9 * i >= 100:
#         print(b,' = 800 * ', i, ' + 9 * ', i)


# for i in range(10,100):
#     if 8*i>99 or 9*i<100:
#         continue
#     if 809*i==800*i+9*i:
#         print(i)
#         break


# 实例082：八进制转十进制

# a = 0o10
# print(a)


# # 实例083：制作奇数
# # 题目 求0—7所能组成的奇数个数。
#
#
#
# def cc(n):
#     if n == 1:
#         print('能组成4个奇数')
#     elif n == 2:
#         print('能组成28个奇数')
#     elif n >= 3:
#         a = 7*4*(n - 2)*8
#         print('能组成%s个奇数'%a)
#


#
# 实例084：连接字符串
# 题目 连接字符串。

# 程序分析 无。
#
# delimiter = '123'
# mylist = ['Brazil', 'Russia', 'India', 'China']
#
# for i in mylist:
#     delimiter += i
# print(delimiter)
#
# ##
# delimiter = ','
# mylist = ['Brazil', 'Russia', 'India', 'China']
# print(delimiter.join(mylist))


# 实例085：整除
# 题目 输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
# a = 0
#
#
# def n(x):
#     global a
#     while x % 9 == 0:
#         # if x % 9 == 0:
#             x /= 9
#             a += 1
#     return a
# print(n(81*9))


# if __name__ == '__main__':
#     zi = int(input('输入一个数字:'))
#     n1 = 1
#     c9 = 1
#     m9 = 9
#     sum = 9
#     while n1 != 0:
#         if sum % zi == 0:
#             n1 = 0
#         else:
#             m9 *= 10
#             sum += m9
#             c9 += 1
#     print ('%d 个 9 可以被 %d 整除 : %d' % (c9,zi,sum))
#     r = sum / zi
#     print ('%d / %d = %d' % (sum,zi,r))


#
# 实例086：连接字符串II
# 题目 两个字符串连接程序。
#
# 程序分析 无。

# a='guangtou'
# b='feipang'
# print(b+a)


# 实例087：访问类成员
# 题目 回答结果（结构体变量传递）。
#
# 程序分析 无。

# class student:
#     heigh = 10
#     age = 0
#     name = ''
#     def  __init__(self):
#         self.heigh = 1
#         self.age = 2
#         self.name = 'lq'
#
# def f(stu):
#     stu.age = 18
#     stu.heigh = 100
#     stu.name = 'chou'
#
# a = student()
#
# print(a.heigh)
# print(a.age)
# f(a)
# print(a.heigh)
# print(a.age)


# class student:
#         x = 0
#         c = 0
# def f(stu):
#         stu.x = 20
#         stu.c = 'c'
# a= student()
# a.x = 3
# a.c = 'a'
# f(a)
# print(a.x,a.c)


#
# 实例088：打印星号
# 题目 读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。

# a = 0
# b = []
# while a != 50:
#     a = random.randint(1,50)
#     b.append(a)
#
# print(b)
# for i in b:
#     print(int(i/2) *' ',int(i/2)*'*')


#
# 实例089：解码
# 题目 某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
# 每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
# res = 0
# n = str(input('输入一个四位的数字进行加密:')[:4])
# a = []
# for i in n:
#     a.append((int(i)+5)%10)
#
# a[0],a[3]=a[3],a[0]
# a[1],a[2]=a[2],a[1]
# print(a)
#
# 实例090：列表详解
# 题目
# 列表使用实例。
#
# 程序分析
# 无。

# list
# 新建列表
# testList = [10086, '中国移动', [1, 2, 4, 5]]
#
# # 访问列表长度
# print(len(testList))
# # 到列表结尾
# print(testList[1:])
# # 向列表添加元素
# testList.append('i\'m new here!')
#
# print(len(testList))
# print(testList[-1])
# # 弹出列表的最后一个元素
# print(testList.pop(1))
# print(len(testList))
# print(testList)
# # list comprehension
# # 后面有介绍，暂时掠过
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# print(matrix)
# print(matrix[1])
# col2 = [row[1] for row in matrix]  # get a  column from a matrix
# print(col2)
# col2even = [row[1] for row in matrix if row[1] % 2 == 0]  # filter odd item
# print(col2even)


# import time
# import datetime
#
# print(time.time())
# print(time.ctime())
# print(time.strftime('%Y-%m-%d %H-%M-%S'))


# 实例092：time模块II
# 题目
# 时间函数举例2。
#
# 程序分析
# 如何浪费时间。

# if __name__ == '__main__':
#     import time
#
#     start = time.time()
#     for i in range(3000):
#         print(i)
#     end = time.time()
#
#     print(end - start)


# 实例093：time模块III
# 题目 时间函数举例3。
#
# 程序分析 如何浪费时间。

# if __name__ == '__main__':
#     import time
#     start = time.clock()
#     for i in range(100):
#         print(i)
#     end = time.clock()
#     print('different is %6.3f' % (end - start))


# 实例094：time模块IV
# 题目
# 时间函数举例4。
#
# 程序分析
# 如何浪费时间。

# if __name__ == '__main__':
#     import time
#     import random
#
#     play_it = input('do you want to play it.(\'y\' or \'n\')')
#     while play_it == 'y':
#         c = input('input a character:\n')
#         i = random.randint(0, 2 ** 32)%100
#         print('please input number you guess:\n')
#         start = time.clock()
#         a = time.time()
#         guess = int(input('input your guess:\n'))
#         while guess != i:
#             if guess > i:
#                 print('please input a little smaller')
#                 guess = int(input('input your guess:\n'))
#             else:
#                 print('please input a little bigger')
#                 guess = int(input('input your guess:\n'))
#         end = time.clock()
#         b = time.time()
#         var = (end - start) / 18.2
#         print(var)
#         # print 'It took you %6.3 seconds' % time.difftime(b,a))
#         if var < 15:
#             print('you are very clever!')
#         elif var < 25:
#             print('you are normal!')
#         else:
#             print('you are stupid!')
#         print('Congradulations')
#         print('The number you guess is %d' % i)
#         play_it = input('do you want to play it.')


#
# 实例096：计算复读次数
# 题目 计算字符串中子串出现的次数。
#
# 程序分析 无。

# s1='xuebixuebixuebixuebixuebixuebixuebixue'
# s2 = 'ue'
#
# print(s1.count(s2))


# 实例097：磁盘写入
# 题目 从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。
# upper 变大写  lower变小写
# filedoc = open('test.txt','w')
# while True:
#     a = input('为#则停止输入：')[:1].upper()
#     if a != '#':
#         filedoc.write(a)
#     else:
#         exit()
#


# ), 输出到一个新文件C中。
# # 实例099：磁盘读写
# # 题目 有两个磁盘文件A和B,各存放一行字母,
# # 要求把这两个文件中的信息合并(按字母顺序排列

#
# filedoca = open('a.txt','r')
# filedocb = open('b.txt','r')
# filedocc = open('c.txt','w')
#
# a = filedoca.readlines()
# b = filedocb.readlines()
# c = ''
# for i in a:
#     c += i + ' '
#
# for i in b:
#     c += i + ' '
# filedocc.write(c)


# 实例100：列表转字典
# 题目 列表转换为字典。


# a = [1, 2, 3,]
# l = ['e', 'b', 'c']
# x = dict(zip(a,l))
# print(x)
# h = list(x.keys())
# print(h)
# g = list(x.values())
# print(g)


# 生成器读取数据
# a = (i for i in range(10))
#
# print(next(a))
# print(a.__next__())


#
# c = random.randint(10000,99999)
#
# print(c)

# 九九乘法表
#
# for i in range(1, 10):
#         for j in range(1, i+1):
#             print("%d*%d=%d \t" % (j, i, i*j), end="")
#         print()


# 波那契数列  0，1，1，2，3，5，8,...
# num=int(input("需要几项？"))
# n1=0
# n2=1
# count=2
# if num<=0:
#     print("请输入一个整数。")
# elif num==1:
#     print("斐波那契数列:")
#     print(n1)
# elif num==2:
#     print("斐波那契数列:")
#     print(n1,",",n2)
# else:
#     print("斐波那契数列:")
#     print(n1,",",n2,end=" , ")
#     while count<num:
#         sum=n1+n2
#         print(sum,end=" , ")
#         n1=n2
#         n2=sum
#         count+=1
# print()


# 姆斯特朗数
# 果一个n位正整数等于其各位数字的n次方之和, 则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。
# num = int(input("请输入一个数字: "))
# sum = 0
# n = len(str(num))
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** n
#     temp //= 10
# if num == sum:
#     print(num, "是阿姆斯特朗数")
# else:
#     print(num, "不是阿姆斯特朗数")


# def logger(filename, channel):
#     """
#     日志方法
#     :param filename:filename
#     :param channel:输入的目的地，屏幕(termianl),文件(file),屏幕加文件(both)
#     :return
#     """
#
#     filename = open('test_log.txt', 'r')
#     filename = filename.read()
#     print(filename)
#
#
# logger(filename='test_log.txt', channel='file')


# 14 用map 处理字符串列表，把列表中所有人都变成***_sb 比分alex_sb

# name = ['alex', 'wupeiqi', 'yuanhao', 'mairui']
#
#
# def xy(n):
#     n = str(n) + '_sb'
#     return n
#
#
# A = []
# c = (map(xy, name))
# print(list(c))
#
# ee = map(lambda x:x+'_sb',name)
# print(list(ee))

# 15 用filter 函数处理数字列表，将列表中所有的偶数筛选出来
#
# nax = [1, 3, 5, 6, 7, 8]
#
# na = list(filter(lambda x:x%2==0,nax))
#
# print(na)


##
# 如下，每个小字典的name对应股票名字，shares对应多少股，price对应股票的价格
# 通过哪个内置的函数可以计算购买每只股票的总价
# 用filter 过滤出单价大于100的股票有哪些

# portfolio = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}]

# for i in range(len(portfolio)):
#     portfolio[i]['money'] = round(portfolio[i]['shares']*portfolio[i]['price'],2)
#     print(portfolio[i]['name'],portfolio[i]['money'])

# for i in range(len(portfolio)):
#     if portfolio[i]['price'] > 100:
#         print(portfolio[i])

# ret = map(lambda dic : {dic['name']:round(dic['shares']*dic['price'],2)},portfolio)
# print(list(ret))
#

# 17 列表 li = ['alex','eng','sd','pizza','akq']  吧字母a开头的大写

# li = ['alex', 'eng', 'sd', 'pizza', 'akq']
#
# for i in li:
#     if i[0] == 'a':
#         li[li.index(i)]= i.capitalize()
# print(li)


# 18 列表 li = ['alex','eng','sd','pizza','akq']  以每个元素的第2个字母倒序排序

# li = ['alex','eng','sd','pizza','akq']
# a = []
# n = 0
# for i in li:
#     a.append(i[1])
#     a.sort(reverse=1)
# for i in a:
#     for j in li:
#         if i ==j[1]:
#             a[n] = j
#             n += 1
# print('正常排序:                   ',li)
# print('以每个元素的第2个字母倒序排序:',a)

# f = open('bbb.txt','r')
# c = f.readlines()
#
# f = open('bbb.txt','w')
# for i in c:
#     if '发发发' == i.strip():
#         pass
#     else:f.write(i)

# 23写一个计算程序执行时间的装饰器

# import time
#
# def timing(func):
#     def inner(*args):
#         start = time.time()
#         func(*args)
#         end = time.time()
#         print('程序运行了%d秒'%(end-start))
#     return inner
#
#
# @timing
# def test(n):
#     print('程序正在运行')
#     time.sleep(n)
#     print('程序运行结束')
#
# test(20)


# 24 lambda 实例

# a = list(filter(lambda y:y%2==0,map(lambda x:x**2 if x > 10 else x**3, [i for i in range(30)])))
# print(a)


# 25 写一个骰子游戏，要求用户压大小，赔率一赔一。
# 要求三个骰子，每个骰子的值从1-6.摇大小，每次打印摇出的三个骰子的值
# import random
#
# d = 0
# while d != '#':
#     d = input('请猜大或者小：')
#     res = 0
#     a = random.randint(1, 6)
#     b = random.randint(1, 6)
#     c = random.randint(1, 6)
#     res = a + b + c
#     print(res)
#     if d =='大' and res >10:
#         print('*************恭喜你猜对了')
#         continue
#     elif d == '小' and res <=10:
#         print('*************恭喜你猜对了')
#         continue
#     elif d !='大' and d!='小':
#         print('输入错误')
#         continue
#     else:
#         print('对不起，猜错了')
#         continue

#
# print('Hello world')
#
# def say(n):
#     print('你好,%s'%n)
#
# say('yyy')


import os
import sys

# print(os.getcwd())  # 打印当前脚本工作路径
# print(os.listdir('.'))  # 打印当前文件夹下的文件名
# os.move  # 删除一个文件
# os.removedirs()  # 删除多个目录
# os.path.isdir()   # 检查给出的路径是否是个目录
# os.path.isfile()   # 检查给出的路径是否是个文件
# os.path.isabs()  # 检查给出的路径是否是一个绝对路径
# os.path.exists()   # 判断给出个路径是否存在

# print(os.path.split(r'C:\Users\Administrator\PycharmProjects\Big_py_learn\venv\Scripts\python.exe'))
# 分割一个路径和文件名

# print(os.path.splitext(r'C:\Users\Administrator\PycharmProjects\Big_py_learn\venv\Scripts\python.exe'))
# 分割一个路径和拓展名

# print(__file__)  # 打印当前程序路径
# print(os.path.abspath(__file__))  # 打印当前程序绝对路径
# print(os.path.dirname(r'C:\Users\Administrator\PycharmProjects\Big_py_learn\venv\Scripts\python.exe'))
# 获取文件路径名称

# print(os.path.basename(r'C:\Users\Administrator\PycharmProjects\Big_py_learn\venv\Scripts\python.exe'))
# 获取文件名称
# os.system()  # 打印shell命令
# print(os.getenv('path'))  # 打印环境变量
# print(os.environ)  #  打印系统所有环境变量
# os.environ.setdefault('HOME',a'/asd/asd')  # 设置环境变量
# print(os.name)  #打印你使用的平台
# print(os.linesep) # 获取当前平台使用的终止符
# os.renames(old= ,new=) 重命名
# os.mkdir()  # 创建单个目录
# os.makedirs()  # 创建多级目录
# os.chmod()  # 修改文件权限及时间戳

# print(os.stat(r'C:\Users\Administrator\PycharmProjects\Big_py_learn\venv\Scripts\python.exe'))
# 获取文件属性

# print(os.path.getsize(r'C:\Users\Administrator\PycharmProjects\Big_py_learn\venv\Scripts\python.exe'))
# 获取文件大小

# os.path.join(dir,filename)  # 结合目录名和文件名
#
# os.get_terminal_size()  # 获取当前终端大小
# os.kill()   # 杀死进程
#


# sys.argv  # 命令行参数list
# sys.exit()  # 退出
# sys.version  # 版本信息
# sys.path   # 返回模块的搜索路径
# print(sys.platform)  # 返回操作系统的平台名称

# sys.stdout.write('please:')
# val = sys.stdin.readline()
# print(val)


# 复制文件
import shutil
# shutil.copy('log.db','log.dbbk')
# shutil.copyfile('log.db','log1.db')
# shutil.copymode()  # copy权限
# shutil.copytree('123','NEW_123',ignore=shutil.ignore_patterns('*.bmp'))
# 辅助文件夹123，新的名字是NEW_123，复制的时候排除*.bmp


# 压缩文件
import zipfile
import os

# f = []
# z = zipfile.ZipFile('NEW_123.zip', 'w')
# c = os.walk(r'C:\Users\Administrator\PycharmProjects\Big_py_learn\123')
# for a,b,d in c:
#     for e in d:
#         f.append(os.path.join(a,e))
#
# for i in f:
#     print(i)
#     z.write(i)
#
# z.close()
#
# # 解压文件
#
# z = zipfile.ZipFile('NEW_123.zip', 'r')
# z.extractall(path=r'C:\Users\Administrator\PycharmProjects\Big_py_learn\321')
# z.close()
#


## 按列检索出相关的数据

# f = open('NRS00198D_20190624.txt', 'r')
# f = f.readlines()
# lie = []
# line = []
# for i in f:
#     i.split()
#     # print(i)
#     lie.append(i)
# for i in range(len(lie)):
#     # print(lie[i])
#     line.append(lie[i].split())
#
# print(line[1][0])
# for a in line:
#     print(a[0]+' '+a[1])
#
# import re
#
# f = open('NRS00198D_20190624.txt','r')
# date_time = re.findall('[a]{3}',f.read())
# print(date_time)
# # date = list(map(int,date_time))
# # print(date)
#


# import socket
#
# phone = socket.socket()
# phone.bind(('192.168.0.103', 8000))
# phone.listen(5)
# while True:
#     print('服务器开始运行------->')
#     conn, addr = phone.accept()  # 接受链接消息
#     while True:
#         try:
#             msg = conn.recv(1024)
#             print('', msg.decode('utf-8'))
#             conn.send(msg)  # 发消息
#         except Exception:
#             break


# import threading
#
# def task(name):
#     print('拿快递',name)
#
# t = []
# t.append(threading.Thread(target=task,args=('a1',)))
# t.append(threading.Thread(target=task,args=('b2',)))
# t.append(threading.Thread(target=task,args=('c3',)))
#
# for i in t:
#     i.start()


# 用socket和threading 结合创建多线程socket服务
# import socket
# import threading
# import time
#
# phone = socket.socket()
# phone.bind(('192.168.0.103',8888))
# phone.listen(5)
#
# def task():
#     print('准备接受数据')
#     time.sleep(5)
#     data = conn.recv(1024)
#     print(data)
#     conn.close()
#
# while True:
#     print('正在监听8888端口')
#     conn,addr = phone.accept()
#     t = threading.Thread(target=task)
#     t.start()


#
# # 了解socketserver 底层代码
# #
# import socketserver
#
#
# class MyServer(socketserver.BaseRequestHandler):
#     def handle(self):
#         # self.request    # conn
#         # self.client_address  # addr
#         # self.server
#         print('---->',self.request)   # <socket.socket fd=524, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('192.168.0.103', 8888), raddr=('192.168.0.109', 1566)>
#         print('---->',self.client_address)  # ('192.168.0.109', 1566)
#         print('---->',self.server) # <socketserver.ThreadingTCPServer object at 0x0000024CD526AB38>
#
#
# server = socketserver.ThreadingTCPServer(('192.168.0.103',8888),MyServer)
# # server = socketserver.ForkingTCPServer(('127.0.0.1',8888),MyServer) # 多进程,windows有些问题
# server.serve_forever()
#
# # a = 123
# # def func():
# #     a = 456
# #     def inner():
# #         print(a)
# #     return inner
# #
# # v = func()
# #
# # v()
# #
# #
# # res1 = 1 if 1>2 else 2
# # print(res1)
#
#
# import socket
#
# client = socket.socket()
# client.connect(('192.168.0.109',8800))
# client.send(b'Hello')
#
# import subprocess
#
#
# import os
#
# print(os.path.getsize(__file__))
# mes = os.popen('ipconfig').read()
# print(mes)
#
# sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 重用地址端口
# sock_server.bind(('127.0.0.1', 8088))


# a = ['1dfg.txt','123.txt','123sf.txt','wer.txt','asd.txt']
# # v = ''
# # for i in range(len(a)):
# #     v += a[i]+ ' '
# # print(v)

#
# import hashlib
#
# file_message_md5 = (hashlib.md5(b'abc'))
# file_message_md5.update(b'sadf')
# file_message_md5 =file_message_md5.hexdigest()


# a  = 4560000
# b = a.to_bytes(10,'big')
# print(a,b)
#
# a = b'\x00\x00\x00\x00\x00\x00\x00E\x94\x80'
# b = b'abc'
#
# e = int.from_bytes(a,'big')
# f = int.from_bytes(b,'big')
#
#
# print(e,f)


## 想用多线程传输文件 失败告终
# import os
# import threading
# import time
# import queue
#
# os.chdir(r'C:\Users\Administrator\Desktop\liqi')
#
#
# def superman(file, num, i):
#     total_size = os.path.getsize(file)
#     smail_size = total_size // num
#     f = os.open(file, os.O_RDONLY)
#
#     os.lseek(f, i * smail_size, 0)
#     mess = os.read(f, smail_size)
#     time.sleep(0.1)
#     print('读取完成', mess, time.time())
#     with open('abc.exe', 'ab') as f:
#         f.write(mess)
#
# q = queue.Queue()
# start = time.time()
# task=[]
# for i in range(1001):
#     t = threading.Thread(target=superman, args=('dabaicai_v5.2uefi.exe', 1000,i))
#     task.append(t)
# for fun in task:
#     time.sleep(0.1)
#     fun.start()
#
# print('总共用时:',time.time()-start)


# import json
# cc = {'name':'liqi','age':30}
# print(cc,type(cc))
#
# bb = json.dumps({'name':'liqi','age':30})
# print(bb,type(bb))
#
# cc = json.loads(bb)
# print(cc,type(cc))

# import os
#
# os.chdir(r'C:\Users\Administrator\Desktop\liqi')
# f = open('NRS00150D_20190624.txt','rb')
# f.seek(1035)调到1035字节出 继续读取后面的文件
# for i in f:
#     print(i)


import threading

## 普通函数方法多线程
# def func(args):
#     a = threading.currentThread() # 可以获取调用函数的线程名称,可以用setname设置
#     print(a.name)
#     print(args)
#
#
# t = threading.Thread(target=func,args=(11,))
# t.start()
#
# a = threading.currentThread() # 可以获取调用主程序的线程名称,可以用setname设置
# # a.setName('liqi')
# print(a.name)
#
# print(123)


##  用面向对象的方法开多线程
#
#
# class MyThread(threading.Thread):
#
#     def run(self):
#         print(111,self._args,self._kwargs)
#
#
# th1 = MyThread(args=(11,),kwargs={'ab':123})
# th1.start()
# print(th1.name)
# th2 = MyThread(args=(22,))
# th2.start()
# print(th2.name)
# print('end')

#
# v1 = [11,22,33]
# v2 = map(lambda x: x+1, v1)
# for i in v2:
#     print(i)

############################ 同步锁和递归锁 #####################################
# import time
# import threading
#
# n = 10
# lock = threading.RLock()   # 递归锁  可以锁n次   然后解n次   一般都用这个rlock 递归锁
# # lock = threading.Lock()    # 同步锁  只能锁一次,然后接开一次  在继续
#
# def task(i):
#     lock.acquire()
#     lock.acquire()
#     global n
#     print('当前线程i:', i, '读取到n的值', n)
#     n = i
#     time.sleep(0.1)
#     print()
#     print('当前线程i:', i, '修改后n的值', n)
#     lock.release()
#     lock.release()
#
# for i in range(10):
#     t = threading.Thread(target=task, args=(i,))
#     t.start()
#
#

#
# ##################### 信号量 #####################
#
# import time
# import threading
#
# lock = threading.BoundedSemaphore(3)   # 默认一次运行开启1个进程,  后面的数据改开启的进程数量
#
# def task(i):
#     lock.acquire()
#     print(i)
#     time.sleep(1)
#     lock.release()
#
# for i in range(10):
#     t = threading.Thread(target=task, args=(i,))
#     t.start()
#


##################### Condition - 方式1 （条件变量）#####################
#
# import time
# import threading
#
# lock = threading.Condition()   # 作用:根据输入的值,决定释放几个线程
#
# def task(i):
#     print('线程进来了')
#     lock.acquire()
#     lock.wait()  # 等待lock.notify(N)   接受N的值来决定释放几个线程
#     print(i)
#     time.sleep(1)
#     lock.release()
#
# for i in range(5):
#     t = threading.Thread(target=task, args=(i,))
#     t.start()
#
# while True:
#     inp = int(input('>>>'))
#     lock.acquire()
#     lock.notify(inp)          # 根据输入的值,决定释放几个线程
#     lock.release()
#


##################### Condition - 方式2 （条件变量）#####################

# import time
# import threading
#
# lock = threading.Condition()   # 进去一下开启,然后根据用户定义数字,觉得放出几个进程
#
# def func():
#     print('来执行func函数啦')
#     input('>>>')
#     return True
#
# def task(i):
#     print('线程进来了')
#     lock.wait_for(func)
#     print(i)
#     time.sleep(1)
#     print('--------->执行完task函数')
#
#
# for i in range(10):
#     t = threading.Thread(target=task, args=(i,))
#     t.start()


###################### Condition条件变量 根据参数,放参数中数量的线程##########################生产者和消费者模式
#
# import threading
# import time
#
# con = threading.Condition()
#
# num = 0
#
# # 生产者
# class Producer(threading.Thread):
#
#     def __init__(self):
#         threading.Thread.__init__(self)
#
#     def run(self):
#         # 锁定线程
#         global num
#         con.acquire()
#         while True:
#             print ("开始添加！！！")
#             num += 1
#             print ("火锅里面鱼丸个数：%s" % str(num))
#             time.sleep(1)
#             if num >= 5:
#                 print ("火锅里面里面鱼丸数量已经到达5个，无法添加了！")
#                 # 唤醒等待的线程
#                 con.notify()  # 唤醒小伙伴开吃啦
#                 print('----------->con.notify()')
#                 # 等待通知
#                 con.wait() # 跳转到另外一个线程的wait
#                 print('----------->con.wait()')
#         # 释放锁
#         # con.release()
#
# # 消费者
# class Consumers(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#
#     def run(self):
#         con.acquire()
#         global num
#         while True:
#             print ("开始吃啦！！！")
#             num -= 1
#             print ("火锅里面剩余鱼丸数量：%s" %str(num))
#             time.sleep(2)
#             if num <= 0:
#                 print('锅底没货了，赶紧加鱼丸吧')
#                 con.notify()  # 唤醒其它线程
#                 print('=======>con.notify()')
#                 # 等待通知
#                 con.wait()  # 跳转到另外一个线程的wait
#                 print('========>con.wait()')
#         # con.release()
#
# p = Producer()
# c = Consumers()
# p.start()
# c.start()


###################多线程之事件（Event) 一次放所有线程通过######################
# # a和b小伙伴等待命令然后准备开始吃过火锅
# import time
# import threading
#
# Event = threading.Event()


# def chihuoguo(name):
#     print('%s 已经准备好了' % threading.currentThread().name)
#     print('%s 已经准备好了' % name)
#     time.sleep(2)
#     Event.wait()
#     print('%s收到命令开始吃火锅' % threading.currentThread().name)
#     print('%s收到命令开始吃火锅' % name)
#
#
# order_list = []
# task = threading.Thread()
# one = threading.Thread(target=chihuoguo, args=('liqi',))
# two = threading.Thread(target=chihuoguo, args=('wuxuejing',))
# order_list.append(one)
# order_list.append(two)
# for i in order_list:
#     i.start()
#
# time.sleep(0.1)
# print('发出吃火锅的命令')
# Event.set()


# # 当小伙伴a,b,c集结完毕后，请客的人发话：开吃咯！
#
# import threading
# import time
#
# event = threading.Event()
#
#
# def chihuoguo(name):
#     # 等待事件，进入等待阻塞状态
#     print ('%s 已经启动' % threading.currentThread().getName())
#     print ('小伙伴 %s 已经进入就餐状态！'%name)
#     time.sleep(1)
#     event.wait()
#     # 收到事件后进入运行状态
#     time.sleep(0.1)
#     print ('%s 收到通知了.' % threading.currentThread().getName())
#     print ('%s 小伙伴 %s 开始吃咯！'%(time.time(), name))
#
#
# class myThread (threading.Thread):   # 继承父类threading.Thread
#     def __init__(self, name):
#         '''重写threading.Thread初始化内容'''
#         threading.Thread.__init__(self)
#
#         self.people = name
#
#     def run(self):   # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
#         '''重写run方法'''
#         time.sleep(0.1)
#         chihuoguo(self.people)     # 执行任务
#         print("qq交流群：226296743")
#         print("结束线程: %s" % threading.currentThread().getName())
#
# # 设置线程组
# threads = []
# # 创建新线程
# thread1 = myThread("a")
# thread2 = myThread("b")
# thread3 = myThread("c")
#
# # 添加到线程组
# threads.append(thread1)
# threads.append(thread2)
# threads.append(thread3)
#
# # 开启线程
# for thread in threads:
#     thread.start()
#
# time.sleep(3)
# # 发送事件通知
# print ('集合完毕，人员到齐了，开吃咯！')
# event.set()


######################## 线程池 #########################
#
# from concurrent.futures import ThreadPoolExecutor
# import time
# pool = ThreadPoolExecutor(5)
#
# def func(args):
#     time.sleep(1)
#     print(args,time.time())
#     time.sleep(1)
# for i in range(10):
#     pool.submit(func,i)


# import threading
#
# l = threading.local()
#
# DATA_DICT = {}
# def func(args):
#     ident = threading.get_ident()
#     DATA_DICT[ident] = args
#     print(DATA_DICT[ident],args)
#
# for i in range(10):
#     t=threading.Thread(target=func,args=(i,))
#     t.start()


################队列成产者和消费者###################
#
# import threading
# import time
# import queue
#
# q = queue.Queue()
#
#
# def produce(args):
#     while True:
#         time.sleep(4)
#         q.put('包子')
#         print('厨师%s生产了1个包子' % args)
#
#
# def consumers(args):
#     while True:
#         time.sleep(3)
#         q.get()
#         print('顾客%s吃了1个包子' % args)
#
#
# for i in range(1, 3):
#     p = threading.Thread(target=produce, args=(i,))
#     p.start()
#     time.sleep(3)
#
# for i in range(1, 3):
#     c = threading.Thread(target=consumers, args=(i,))
#     c.start()
#     time.sleep(3)


######################################################################
#
#
# import socket
# import select
#
#
# class Req(object):
#     def __init__(self, sk, func):
#         self.sk = sk
#         self.func = func
#         # print('执行Req构造函数')
#
#     #
#     def fileno(self):
#         # print('执行fileno函数',self.sk.fileno())
#         return self.sk.fileno()
#
#
# class Nb(object):
#     def __init__(self):
#         self.conn_list = []
#         self.socket_list = []
#
#     def add(self, url, func):
#         client = socket.socket()
#         client.setblocking(False)
#         try:
#             client.connect((url, 80))
#         except BlockingIOError as e:
#             pass
#
#         obj = Req(client, func)
#         self.conn_list.append(obj)
#         self.socket_list.append(obj)
#         print(self.conn_list, self.socket_list)
#
#     def run(self):
#         while True:
#             rlist, wlist, elist = select.select(self.socket_list, self.conn_list, [], 0.05)
#             for sk in wlist:
#                 try:
#                     sk.sk.sendall(b'GET /s?wd=china HTTP/1.0\r\nhost:www.baidu.com\r\n\r\n')
#                     self.conn_list.remove(sk)
#                 except OSError as e:
#                     print(e)
#             for mes in rlist:
#                 chunk_list = []
#                 while True:
#                     try:
#                         mes_data = mes.sk.recv(8096)
#                         if not mes_data:
#                             break
#                         chunk_list.append(mes_data)
#                         message = b''.join(chunk_list)
#                         mes.func(message)
#                         self.socket_list.remove(mes)
#                         mes.sk.close()
#                     except Exception as e:
#                         break
#
#             if not self.socket_list:
#                 break
#
#
# def baidu_response(data):
#     print('--------->', data)
#
#
# def sougou_response(data):
#     print('--------->', data)
#
#
# def oldboy_response(data):
#     print('--------->', data)
#
#
# t1 = Nb()
# t1.add('www.baidu.com', baidu_response)
# t1.add('www.sogou.com', sougou_response)
# t1.add('www.oldboyedu.com', oldboy_response)
# t1.run()
#


##################### 封装 ###########################
### 封装之前
# v = [
#     [11, 22],
#     [22, 33],
#     [33, 44],
# ]
#
# for item in v:
#     item.append(55)
# print(v)


### 封装之后
#
# class Foo(object):
#     def __init__(self, data,girl):
#         self.row = data
#         self.girl = girl
#
#     def append(self, num):
#         self.row.append(num)
#         print(self.row)
#         print(self.girl)
#
#
# v = [
#     Foo([11, 22],'雪梨'),
#     Foo([22, 33],'予曦'),
#     Foo([33, 44],'大G'),
# ]
#
# for item in v:          # 这段代码不改
#     item.append(55)     # 这段代码不改
# print(v)                # 这段代码不改

###################  单线程 #######################
# def f1():
#     print(11)
#     print(22)
#
#
# def f2():
#     print(33)
#     print(44)
#
#
# f1()
# f2()

#####################  协程是微线程  #####################
# 微线程,对一个现场进行分片,使得线程在代码之间进行来回切换,
# 而不是按原来逐行执行
#############  程序员自己决定执行那一条参数  ##############
#
# import greenlet
#
#
# def f1():
#     print(11)
#     gr2.switch() # 切到f2
#     print(22)
#     gr2.switch() # 切到f2
#
#
# def f2():
#     print(33)
#     gr1.switch() # 切到f1
#     print(44)
#
#
# # 协程 gr1
# gr1 = greenlet.greenlet(f1)
# # 协程 gr2
# gr2 = greenlet.greenlet(f2)
#
# gr1.switch() # 开始f1函数

########  协程存在的意义
# greenlet 是进行程序的切换
# gevent 可以检测到i/o          这两个组合起来后就会变成   碰到i/o 就进行程序切换

#
# from gevent import monkey
#
# monkey.patch_all()  # 这句代码, 遇到io会自动执行greenlet的switch  自动切换
# import gevent
# import requests
#
#
# def get_page1(url):
#     res = requests.get(url)
#     print(url, res.content)
#     print(url)
#
# gevent.joinall([
#     gevent.spawn(get_page1, 'https://www.baidu.com/'),
#     gevent.spawn(get_page1, 'https://www.163.com/'),
#     gevent.spawn(get_page1, 'https://www.sina.com/'),
#     gevent.spawn(get_page1, 'https://www.hao123.com/'),
# ])

import socket


"""
网络基础
OSI七层
BS和CS架构
SOCKET代码


进程,线程,协程区别
线程的基本写法,实例化 继承,锁Rlock 进程数据共享 Therading.local

4 协程
协程+io :gevent

IO多路复用

异步,同步,阻塞,非阻塞
"""

# import socket
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',80))
# sk.listen(5)
# conn,addr = sk.accept()
# print('服务端监听80端口,有数据发送')
# mess_list = []
# while True:
#     mess = conn.recv(1024)
#     if not mess:
#         break
#     mess_list.append(mess)
# print(mess_list)



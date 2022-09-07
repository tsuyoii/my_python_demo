# -*- coding: UTF-8 -*-
#详情参考菜鸟教程，python实例 

# 两数之和
# a = int(input('请输入数字a'))
# b = int(input('请输入数字b'))

# print('两数之和为： ',a+b)




# 平方根
# num = float(input('请输入数字'))
# print('数字{0}的平方根为{1:0.3f}'.format(num,num**0.5))




# 求二元一次方程式
# a = float(input('请输入系数a'))
# b = float(input('请输入系数b'))
# c = float(input('请输入系数c'))

# # ax^2+bx+c=0
# d = (b**2)-(4*a*c)
# x1 = (-b-(d**0.5))/(2*a)
# x2 = (-b+(d**0.5))/(2*a)

# if(a==0):
#     print('方程解为x={0}'.format(-c/b))
# else:
#     print('方程式的解为x1={0},x2={1}'.format(x1,x2))






# 生成0～9之间的随机数
# import random
# print(random.randrange(0,9))






# 交换两个变量
# a = int(input('输入变量a'))
# b = int(input('输入变量b'))
# print('交换前a={0},b={1}'.format(a,b))
# # 法一
# # t = a
# # a = b
# # b = t

# # 更优雅的法二
# a,b = b,a
# print('交换后a={0},b={1}'.format(a,b))






# 判断字符串是否是数字
# def is_number(s):
#     try:
#         float(s)
#     except:
#         print('非数字{0}'.format(s))
#         return False
#     else:
#         print('数字{0}'.format(s))
#         return True

# print(is_number(input('请输入字符串')))







# 判断奇数偶数
# num = int(input('请输入一个数字'))
# if(num % 2):
#     print('{0}是奇数'.format(num))
# else:
#     print('%d是偶数'%num)





# 判断是否是闰年
# year = int(input('请输入判断年份'))
# if(year % 100 == 0):
#     if(year % 4 == 0):
#         print('%d是闰年'%year) #整百年能被400整除的是闰年
#     else:
#         print('%d不是闰年'%year)
# elif(year % 4 == 0):
#     print('%d是闰年'%year)
# else:
#     print('%d不是闰年'%year)





# 求几个数中的最大数
# max(1,5,2,0,-3,-100,99)





# 判断一个数是否是质数/素数(只能被1和自己整除)
# def is_prime(num):
#     list=[]
#     if(num<=1):
#         print('%d不是质数，小于等于1'%num)
#         return False
#     for i in range(2,int((num/2)+1)):
#         if(num%i==0):
#             # list+=[i,int(num//i)]
#             list+=[i]
#     if(list):
#         print('%d不是质数,可以被整除:'%num,list)
#         return False
#     else:
#         print('%d是质数'%num)
#         return True

# print(is_prime(int(input('请输入一个数字'))))


# 指定范围内的质数
# def range_prime(a,b):
#     list=[]
#     for num in range(a,b+1):
#         if num>1:
#             for i in range(2,num):
#                 if(num%i==0):
#                     break
#             else:
#                 list+=[num]
#     print(list)

# a = int(input('请输入最小范围'))
# b = int(input('请输入最大范围'))

# print('[{0},{1}]内的质数有:'.format(a,b))
# range_prime(a,b)







# 打印九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{0} * {1} = {2}'.format(i,j,i*j),end=' ')
#     else:
#         print('\n')






# 斐波那契数列
# num = int(input('需要打印前几项'))
# count = 1
# list=[0,1]
# if(num<=2):
#     print(list[0:num])
# else:
#     for i in range(2,num):
#         count = list[i-1]+list[i-2]
#         list+=[count]
#     else:
#         print(list)

# 用递归实现斐波那契数列
# def recur_fibo(n):
#     if(n<=1):
#         return n
#     else:
#         return (recur_fibo(n-1)+recur_fibo(n-2))






# 输出阿姆斯特朗数
# (一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数)
# 如（1^3+5^3+3^3=153）

# 判断一个数是否是阿姆斯特朗数
# def is_amustlan(num):
#     # print('0.'+num)
#     length=len(str(num))
#     sum=0
#     for i in range(0,length):
#         sum+=int(str(num)[i])**length
#     if(sum==int(num)):
#         print('%d是阿姆斯特朗数'%int(num))
#         return True
#     else:
#         return False
# is_amustlan(input('请输入数字'))







# 十进制转二进制、八进制、十六进制
# dec = int(input('请输入数字'))
# print('十进制数为:',dec)
# print('二进制数为:',bin(dec))
# print('八进制数为:',oct(dec))
# print('十六进制数为:',hex(dec))




# ASCII码与字符相互转换
## 字符
# c = input('请输入字符')
## ASCII码
# a = int(input('输入一个ASCII码'))
# print('字符{0}对应的ASCII码为{1}'.format(c,ord(c)))
# print('ASCII码{0}对应的字符为{1}'.format(a,chr(a)))







# 最大公约数
# def com_divisor(a,b):
#     for i in range(a+1,2,-1):
#         # &与  ｜或
#         if((a%i==0) & (b%i==0)):
#             return i
#     else:
#         return 1
# a = int(input('请输入num1'))  
# b = int(input('请输入num2'))  
# print('{0}和{1}的最大公约数为{2}'.format(a,b,com_divisor(a,b)))






# 最小公倍数  54*4 24*9 216
# def com_multiple(a,b):
#     # if(a*i%b==0) a*i就是最小公倍数
#     i=0
#     c,d = max(a,b),min(a,b)
#     while True:
#         i+=1
#         if((c*i)%d==0):
#             return c*i
        
# a = int(input('请输入num1'))
# b = int(input('请输入num2'))
# print('{0}和{1}的最小公倍数是{2}'.format(a,b,com_multiple(a,b)))





# 生成日历
# import calendar
# yy = int(input('输入年份'))
# mm = int(input('输入月份'))
# print(calendar.month(yy,mm))





# 文件IO操作
# 写文件
# with open('test.txt','wt') as out_f:
#     out_f.write('该文本会写入到文件中\n看到我了吧！')

# # 读文件
# with open('test.txt','rt') as in_f:
#     text = in_f.read()
# print(text)






# 计算每个月的天数
# 输出的是一个元组(5,31)第一个元素表示第一天是星期六（0～6表示星期一～星期日），第二个元素表示有31天
# import calendar
# monthRange = calendar.monthrange(2022,1)
# print(monthRange)





# 获取昨天日期
# import datetime
# def getYesterday():
#     today = datetime.date.today()
#     oneday = datetime.timedelta(days=1)
#     return today-oneday

# print(getYesterday())





# 约瑟夫生死游戏
# list=[]
# count=[]
# for i in range(1,31):
#     list += [i]
# while (len(list)>15):
#     print('%d号下船了'%list[8])
#     count+=list[9:len(list)]
#     count+=list[0:8]
#     # print(count)
#     list = count
#     count=[]






# 五人分鱼
# 除了第一次以外，其余每次本来可以分4份，结果都被分成了5份
# i=1
# xe = 1
# total=0
# while i<=5:
#     total += xe+1
#     xe = xe*5+1     #e醒来时有6条，则d 醒来时有31条
#     print(xe)
#     i+=1
# print(xe)
# 答案有待考证

# i=1
# xe = 6
# total=0
# while i<=4:
#     total += xe+1
#     xe = xe*4+1     #d醒来时有31条，扔了1条，分5份，拿走一份6条，还剩30-6=xe*4=24条，所以e醒来时有6条
#     print(xe)
#     i+=1
# print(xe)











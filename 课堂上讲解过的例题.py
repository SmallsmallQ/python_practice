"""
# 案例一 置逆四位整数
m = int(input("请输入一个4位十进制正整数："))
a = m // 1000
b = (m % 1000) // 100
c = (m % 100) // 10
d = m % 10
m= d * 1000 + c * 100 + b * 10 + a
print("置逆后整数：" , m )

# 案例二 测试运算符号
a=int(input("请输入a"))
b=int(input("请输入b"))
if a==b:
    print("相等")
if a!=b:
    print("不相等")

# 逻辑运算符运算
# and or not
    
# 一些内置函数
import math
print(dir(math))

# 三角形面积计算
import math
a=float(input("请输入三角形边长"))
b=float(input("请输入三角形边长"))
c=float(input("请输入三角形边长"))
if a+b>c and a+c>b and b+c>a:
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"三角形的面积={area}")
else:
    print("无法构成三角形")

# 简单的计算题目
import random 
a=random.randint(0,100)
b=random.randint(0,100)
answer=float(input((a+b=)))
if answer==a+b:
    print("You are corret!")
else:
    print("你错了")

# 计算1**2**2+....+n**2的答案

N=int(input("请输入n的值："))
sum=0
for i in range(1,N+1):
    sum+=i**2
print(f"最终的结果是{sum}")

# 字符串运算符
a="hello"
b="world"
print(a+b)
print(a[0])
judge=bool("a" in a)
print(judge)
print("%d+%d=%d"%(45,23,45+23))
a=a.upper()
print(a)
"""
# 字符串函数
s="Xi'an Jiaotong University"
print(len(s))
print(s*2)
judge=bool("x" in s)
print(judge)
print(s.lower())
print(s.upper())
print(s.rstrip())
print(s.split())
print(s.isdigit())

s="Hello"
list1=["hello","world"]
s1.join(list1)
print(s1)

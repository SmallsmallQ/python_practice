"""编写函数isprime(a)用来判断变量a是否为素数。
若是素数，函数返回1，否则返回0。输入一个正整数n，测试函数，找出任意给定的n个整数中的素数。"""
def isprime(a):
    if a <=1:
        return 0
    elif a ==2:
        return 1
    else:
        for i in range(2,a,1):
            if (a%i)==0:
                return 0
            else:
                return 1
num=int(input("请输入你的整数："))
for j in range(0,num+1):
    k=isprime(j)  
    print(k)
    if k==0:
        print(f"你输入的{j}不是素数")
    else:
        print(f"你输入的{j}是素数")

    
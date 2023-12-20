##编写函数gbs(a,b)，求两个正整数的最小公倍数和最大公约数，输入两个正整数a和b，测试自编函数gbs(a,b)
def gbs(a, b):
    smaller = min(a, b)
    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            gbs=i 
    lcm=a*b/gbs
    return gbs, lcm
a=int(input("请输入a的值"))
b=int(input("请输入b的值"))
x,y=gbs(a,b)
print(f"两个数的最大公约数为{x}")
print(f"两个数的最小公倍数为{y}")
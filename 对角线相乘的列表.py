"""
编写程序完成如下功能：A）定义二维数组8×8；B）自动生成数组中每个数据元素值为(i+1)×(j+1)
i和j分别为行列坐标，输出该数组所有元素；
计算主对角线元素之和，计算次对角线元素之和，
并输出；D）将主对角线元素之和加到第一行中每个元素中，然后输出第一行所有元素值。运行示例如下：
输入二维数组维数：8
[1, 2, 3, 4, 5, 6, 7, 8]
[2, 4, 6, 8, 10, 12, 14, 16]
[3, 6, 9, 12, 15, 18, 21, 24]
[4, 8, 12, 16, 20, 24, 28, 32]
[5, 10, 15, 20, 25, 30, 35, 40]
[6, 12, 18, 24, 30, 36, 42, 48]
[7, 14, 21, 28, 35, 42, 49, 56]
[8, 16, 24, 32, 40, 48, 56, 64]
主对角线元素之和= 204 次对角线元素之和= 120
加上主对角线之和后，第1行 [205, 206, 207, 208, 209, 210, 211, 212]
"""
n = int(input("输入二维数组维数:"))
a = []
for i in range(0, n):
    a.append([])
    for j in range(0, n):
        a[i].append((i + 1) * (j + 1))
for i in range(n):
    print(a[i])

m1 = 0
m2 = 0

# 计算主对角线和次对角线的和
for i in range(n):
    m1 += a[i][i]
    m2 += a[i][n - 1 - i]

# 打印主对角线和次对角线的和
print("主对角线元素之和=", m1, "次对角线元素之和=", m2)

# 将主对角线的和加到第一行每个元素上
for i in range(n):
    a[0][i] += m1

# 打印修改后的第一行
print("加上主对角线之和后，第1行", a[0])

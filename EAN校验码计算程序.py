the_first_12=input("请输入前12位数字：")
odd_sum = 0
even_sum = 0
for i in range(0, 12, 2):
     odd_sum += int(the_first_12[i])
for i in range(1, 12, 2):
    even_sum = even_sum + int(the_first_12[i])
total = odd_sum + 3 * even_sum
checksum = (10 - (total % 10)) % 10
checksum = str(checksum)
total=the_first_12+checksum
print(f"最后得到的EAN码是：{total}")

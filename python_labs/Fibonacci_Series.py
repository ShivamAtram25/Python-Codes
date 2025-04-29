num1 = 0
num2 = 1

print(num1)
print(num2)
for fibo in range(18):
    newfibo = num1 + num2
    print(newfibo)
    num1 = num2
    num2 = newfibo
    
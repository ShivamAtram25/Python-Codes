a = int(input("Enter the number : "))
i = 1
while(i<=a):
    if(a[i] % 2 == 0):
        print(f"even = {count(a[i])}")
    if(a[i] % 2 == 1):
        print(f"odd = {count(a[i])}")
        print(f"zero = {count(a[i])}")
    else:
        print(f"zero = {count(a[i])}")
    i = i + 1
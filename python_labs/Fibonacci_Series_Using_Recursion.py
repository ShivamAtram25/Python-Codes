
num1=0
num2=1
print(0)
print(1)
count = 2

# print(num1)
# print(num2)

def fibonacci(num1, num2):
    global count
    if count <= 19:   
        newfibo = num1 + num2
        print(newfibo)
        num1 = num2
        num2 = newfibo
        count += 1
        fibonacci(num1,num2)
    else:
        return

    
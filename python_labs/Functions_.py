# def EvenOdd(i):
#     if (i % 2 == 0):
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")
        
# num = int(input("Enter the number : "))
# EvenOdd(num)

# def Greeting(name):
#     print(f"Good Morning {name}, Have a nice day")
    
# name = input("Enter your name : ")
# Greeting(name)

def fibonacci(num):
        num1 = 0
        num2 = 1

        print(num1)
        print(num2)
        for fibo in range(num):
            newfibo = num1 + num2
            print(newfibo)
            num1 = num2
            num2 = newfibo
            
num = int(input("Enter the number : "))
fibonacci(num)
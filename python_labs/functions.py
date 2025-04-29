#def EvenOdd(x):
 #      print("even")
#    else :
#        print("Odd")
        
#EvenOdd(1)
#EvenOdd(4)
#EvenOdd(113)

# def add(num1 , num2):
#     num3 = num1 +num2 
#     return num3 
    
# print(add(1,2))
# def mul(num1,num2):
#     num3=num1*num2
#     return num3
# print(mul(2,3))


# def Pattern(n):
#     i =0
#     j =0
#     for i in range(n+1):
#         for j in range(i):
#             print("*",end="")
#         print()
# Pattern(9)

# def Pattern2(n):
#     for i in range(n,0,-1):
#         print("*"*i)

# num = int(input("Enter the number : "))
# Pattern2(num)


def myfun(x , y=50):
    x[0]=20
    print("x = ",x)

x =[10,11,12,13,14,15]
myfun(x)
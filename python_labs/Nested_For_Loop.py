# num = int(input("Enter the Number : "))
# count = 0
# while(num> 0):
#         num //= 10
#         count += 1
# print(count)


# n= int(input("Enter the Number : "))
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end="")
#     print()

# n= int(input("Enter the Number : "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
    
    
# n= int(input("Enter the Number : "))
# num = 1
# for i in range(1,n+1):
#     for j in range(i):
#         print(num,end=" ")
#         num += 1
#     print()

num = int(input("Enter the Number : "))
rev = 0
while(num != 0):
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10

print(f"Reverse number is : {rev}")
    
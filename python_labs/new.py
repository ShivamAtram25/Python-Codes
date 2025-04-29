def countofDigit(num):
    odd_count = 0
    even_count = 0
    zero_count = 0
    
    while(num> 0):
       digit = num % 10
       
       if digit == 0:
           zero_count += 1
           
       elif digit % 2 == 0:
            even_count += 1
        
       else:
           odd_count += 1
           
       num //= 10
       
    return odd_count,even_count,zero_count

number = int(input("Enter the Number : ")) 

odd , even, zero = countofDigit(number)

print(f"the  count of odd number is : {odd}")
print(f"the  count of even number is : {even}")
print(f"the  count of zero number is : {zero}")
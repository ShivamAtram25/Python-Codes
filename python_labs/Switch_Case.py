days = int(input("Enter the number  0 for Monday, 1 for Tuesday, 2 for Wednesday, 3 for Thursday, 4 for Friday, 5 for Saturday, 6 for Sunday : "))

match days:
    case 0:
        print("Today is Monday")
        
    case 1:
        print("Today is Tuesday")
        
    case 2:
        print("Today is Wednesday")
        
    case 3:
        print("Today is Thursday")
        
    case 4:
        print("Today is Friday")
        
    case 5:
        print("Today is Saturday")
        
    case 6:
        print("Today is Sunday")
        
    case default:
        print("Please enter the number betweeen 0 - 6 for days of the week")
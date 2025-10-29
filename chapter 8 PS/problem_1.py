def greatestOf3(num1 , num2 , num3):

    if(num1 > num2 and num1 > num3):
        print(f"{num1} is the greatest")
    if(num2 > num1 and num2 > num3):
        print(f"{num2} is the greatest")    
    else:
        print(f"{num3} is the greatest")



greatestOf3(2,4,5)
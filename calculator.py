print(" ")
print('-------- Calculator -----------')
print('Select an operation to perform :')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

operation = input("Enter:")

if operation == "1":
        num1 = input("Enter the 1st number:")
        num1 = int(num1)
        num2 = input("Enter the 2nd number:")
        num2 = int(num2)
        print("Their sum is " + str(num1 + num2))
        


elif operation =="2":
        num1 = input("Enter the 1st number:")
        num1 = int(num1)
        num2 = input("Enter the 2nd number:")
        num2 = int(num2)
        print("Their subtraction is " + str(num1 - num2))
        
    
elif operation =="3":
        num1 = input("Enter the 1st number:")
        num1 = int(num1)
        num2 = input("Enter the 2nd number:")
        num2 = int(num2)
        print("Their product is  " + str(num1 * num2))
        
    
elif operation =="4":
        num1 = input("Enter the 1st number:")
        num1 = int(num1)
        num2 = input("Enter the 2nd number:")
        num2 = int(num2)
        print("Their division is " + str(num1/num2))
        
else:
    print("Invalid entry!")
        
        

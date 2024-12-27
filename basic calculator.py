print ("calculator")

num1 = float(input("Enter first number here: "))
num2 = float(input("Enter second number here: "))
print ("press 1 for addition \npress 2 for subtraction \npress 3 for multiplication \npress 4 for division")

choice = int(input("Enter your choice from 1-4 : "))

if choice ==1:
    print ("The additon of defined two number is",num1 + num2)
elif choice == 2:
    print("The subtraction of defined two number is",num1 - num2)
elif choice == 3:
        print ("The multiplication of defined two number is",num1 * num2)
elif choice == 4:
    print ("The division of defined two number is",num1 / num2) 
else :
        print ("Invalid input")      
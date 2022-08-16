number1 = float(input("Enter number 1:"))
number2 = float(input("Enter number 2:"))

if number1 > number2:
    print(number1, "is bigger than", number2)
elif number1 < number2:
    print(number2, "is bigger than", number1)
else:
    print("The two numbers are equal"
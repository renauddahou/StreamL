string1 = input("Enter a string:")
string2 = input("Enter a second string:")
how = input("How to compare these 2 strings?\nChoose between: '1' for comaraison based on ASCII or '2' for comparison based on their length: ")

if how == '1':
    first = string1 > string2
    second = string1 < string2

elif how == '2':
    first = len(string1) > len(string2)
    second = len(string1) < len(string2)
    

if first:
    print("The first string is bigger")

elif second:
    print("The first string is smaller")

else:
    print("These 2 strings are equall")
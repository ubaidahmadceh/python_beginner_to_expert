number = input("Enter your number : ")

if number.isdigit():
    print("this is numeric (0-9)")
elif number.isalpha():
    print("this is string !!")
else:
    print("This is not numeric , this is symbol or alphabet")

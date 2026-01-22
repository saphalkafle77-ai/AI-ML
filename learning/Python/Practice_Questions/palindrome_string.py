string = input("enter the string:")
reversed_string = string[::-1]
if string == reversed_string:
    print("palindrome ")
else:
    print("non palindrome")
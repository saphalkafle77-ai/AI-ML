# conditional statement under conditional statement
username = input("enter username:")
password = input("enter password:")
age = input("enter age:")

if (username == "admin") and (password == "pass"):
    print("logged in successfully")
if age == 18:
    print("18")
else:
    if username != "admin":
        print("wrong username")
    else:
        print("wrong password")

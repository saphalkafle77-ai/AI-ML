username = input("enter username:")
password = input("enter password:")

if (username == "admin") and (password == "pass"):
    print("you can login!!")
elif (username != "admin") and (password != "pass"):
    print("both wrong")

elif username != "admin":
    print("wrong username!!")
elif password != "pass":
    print("wrong password")

while True:
    n = input("enter number:")
    if n == "quit":

        break
    n = int(n)
    if n > 0:
        print("positive number:")
    if n < 0:
        print("negative number:")

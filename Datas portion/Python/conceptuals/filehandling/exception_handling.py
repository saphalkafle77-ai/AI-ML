try:
    with open("assignment/data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("file not found!!")

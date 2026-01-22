# f = open("conceptual/filehandling/names.txt", "x")
with open("conceptual/filehandling/names.txt", "w") as f:
    f.write("saphal \n ram \n sita \n rita\n dugal")

with open("conceptual/filehandling/names.txt", "r") as f:
    print(f.read())

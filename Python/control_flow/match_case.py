# alternative of if elif and else
color = input("enter color:")

match color:
    case "green":
        print("go")
    case "red":
        print("stop")
    case "yellow":
        print("wait")
    case _:
        print("wrong color")

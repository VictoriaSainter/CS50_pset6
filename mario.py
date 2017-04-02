import cs50

complete = False

while complete == False:

    print("Height: ", end="")
    s = cs50.get_int()

    if s > 0 and s < 24:
        for i in range(s):
            print(" " * (s-(i+1)), end="")
            print("#" + "#" * (i+1))
            complete = True

def choose():
    key = 0
    while key != 1 or key != 2:
        key = input("please chose installation method:(input 1 or 2)\n"
                    "1) Semi-automatic installation(no web config)\n"
                    "2) Full automatic installation(auto web config)\n")
    if key == 1:
        return 1
    else:
        return 0



keylist = ['1','2']
def choose():
    key = '0'
    while key not in keylist:
        key = input("please chose installation method:(input 1 or 2)\n"
                    "1) Semi-automatic installation(no web config)\n"
                    "2) Full automatic installation(auto web config)\n")
    if key == '2':
        return 1
    else:
        return 0



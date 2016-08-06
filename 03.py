import random
def get_int(msg,minimum,default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            i = int(line)
            if i < minimum:
                print("must be >=",minimum)
            else:
                return i
        except ValueError as err:
            print(err)

rows = get_int("rows:",1,None)
columns = get_int("columns:",1,None)
mininum = get_int("minimum (or Enter for 0):",-1000000,0)

default = 1000
if default < mininum:
    default = 2 * mininum
maximum = get_int("maximum(or Enter for " + str(default) + "):",
                  mininum,default)

row = 0
while row < rows:
    line = ""
    column = 0
    while column < columns:
        i = random.randint(mininum,maximum)
        s = str(i)
        while len(s) < 10:
            s = "" + s
            line += s
            column += 1
        print(line)
        row += 1


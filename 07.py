valid = False
count = 3
while count > 0:
    input = input('Enter password')
    for eachPasswd in passwdList:
        if input == eachPasswd:
            valid = True
            break
    if not valid:
        print('Invalid input')
        count -= 1
        continue
    else:
        break

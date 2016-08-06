def showNaxFactor(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            print('largest factor of %d is %d ' %\
                  (num,count))
            break
        count -= 1
    else:
        print(num,'is prime')

for eacnNum in range(10,21):
    showNaxFactor(eacnNum)

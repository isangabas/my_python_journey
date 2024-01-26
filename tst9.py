c0 = int(input(""" enter two digits such that:
               the integer is positive 
               it is not a factor of 10: """))

while c0 % 10 == 0:
    print("that's not right ! \n try again")
    c0 = int(input(": "))
else:
    print("let's get tricky with numbers")
    count = 0
    while c0 != 1 :
        count += 1
        if c0 % 2 == 0 :
            c0 /= 2
            print(c0)
        elif c0 % 2 == 1 :
            c0 = 3 * c0 + 1
            print(c0)
    else :
        print (c0)
print (count)


a = int(input("enter a number: "))
b = int(input("enter a number: "))
c = int(input("enter a number: "))

var_list = [a,b,c]

def calc_number() :
    total = 0
    for i in var_list :
        for j in (range(i)) :
            total += j
    print (total)

calc_number()



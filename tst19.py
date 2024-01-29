def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem
    return s    

lst = []
while len(lst) < 5 :
    user_input = int(input("enter a unique on number: "))
    lst.append(user_input)
print(lst)
print(list_sum(lst))




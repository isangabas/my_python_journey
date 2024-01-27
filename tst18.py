my_list = [1,2,4,4,1,3,2,1]
my_new_list = []

for i in my_list :
    for j in range(len(my_list)) :
        count = 0
        if i == my_list[j] :
            count += 1
            while count >= 2 :
                del my_list[j]
        else :
            my_new_list.append(i)
            continue
print(my_new_list)

            
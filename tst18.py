my_list = [1,2,4,4,1,3,2,1]
my_new_list = []

for i in range(len(my_list)) :
    for j in my_list :
        count = 0
        if j == my_list[i] :
            count += 1
            print(count)
            while count >= 1 :
                print(my_list)
        else :
            my_new_list.append(j)
            continue


my_list = [1, 2, 4, 4, 1, 3, 2, 1]

unique_list = []

for element in my_list:
    if element not in unique_list:
        unique_list.append(element)

print("Original List:", my_list)
print("List without Repetitions:", unique_list)







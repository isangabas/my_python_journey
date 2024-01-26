x = int(input("enter a number: \n"))
n = 1
count = 0
while x > 0 :
    x = x-n
    print(n)
    n += 1
    count += 1
    if x < n :
        
        break
print (count)
    

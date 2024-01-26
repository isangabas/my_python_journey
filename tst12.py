temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)
print (len(temps))

for d in temps :
    for h in d :
        h = float(input("Enter the temperature of the hour: "))
print(temps)



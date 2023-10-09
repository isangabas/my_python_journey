print('''
I am thinking of a number, can you guess the number?''')


g = input("Guess: ")
i = 0 #number of guesses
m = 3 #max guesses
x = str(5)

while i < m:
    i += 1
    while g != x:
        print("you guessed wrong, try again")
        g = input("Guess: ")
    else:
        print("wow you guessed correctly")
        break
else:
    print("you have exceeded your trials")







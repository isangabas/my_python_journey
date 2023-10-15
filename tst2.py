
while 1 == 1:
    cmd = input("enter a command> ")
    avlble = True
    if cmd == "quit":
        print("exiting game")
        break
    else:
        while avlble:
            if cmd == "help":
                print("input either of the following commands to play: start, stop, quit")
                avlble = False
            elif cmd == "start":
                print("car has started")
                avlble = False
            elif cmd == "stop":
                print("car has stopped")
                avlble = False
            else:
                print("you have entered a wrong input; enter 'help'")
                avlble = False
                


                


                
    


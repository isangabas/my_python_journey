try :
    school_class = {}
    def create_class_dataset() :
        while len(school_class.keys()) < 2 :
            # take name input and filter against invalid input
            name = input("Enter the name of the student: ")
            if name == "" :
                break
        
            # take score input and filter against invalid input
            score = int(input("Enter the student's score: "))
            if score not in range(0,11) : 
                break

            # add name, score input to dictionarys
            if name in school_class :
                school_class[name] += (score, )
            else :
                school_class[name] = (score, )

        return sorted(school_class)

    def avg_calculator(name) :
        #take name input
        name = input("Enter the name of the student: ")
        # check to see if name is in dictionary
        if name in sorted(school_class.keys()) :
            adding = 0
            counter = 0
            # if name is in dictionary, carry out average calculation
            for score in school_class[name] :
                adding += score
                counter += 1
            print(adding/score) 
        else :
            print("The name given is not in the database")

    create_class_dataset()
    avg_calculator("joe")

except :
    print("We'll try to fix the bug")



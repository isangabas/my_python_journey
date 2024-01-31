def is_prime(test_number):
    for n in range(2,test_number):
        mod_result = test_number % n
        if mod_result == 0 :
            print(mod_result)
            return False 
        else :
            return True
        
print(is_prime(19))


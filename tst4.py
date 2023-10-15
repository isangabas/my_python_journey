import random, math

def random_debugger():
    random.seed(0)
    for i in range(5):
        v = random.random()
        print(v)
        random.seed(v)
        print(random.random())
random_debugger()

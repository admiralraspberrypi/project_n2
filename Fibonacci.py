
def amount_get_fibanocci():
    c = int(input("How big the sequence? |  "))
    return c


def start_fibanocci():
    return int(input("Which number you want to start with? | "))


# Basic variables
fibanocci_list = []

# to run a loop
counter1 = 1
counter2 = amount_get_fibanocci()

x = start_fibanocci()
fibanocci_list.append(x)

# setting a loop for amount of/in range fibanocci numbers
for i in range(counter2):
# if statments to show exluding parts of fibanocci number such as firt two numbers thath must be the same
    if counter2 == 0:
        fibanocci_list = []
        print(fibanocci_list)
        break
    elif counter2 == 1:
        fibanocci_list = [x]
        print(fibanocci_list)
        break
    elif counter2 == 2:
        fibanocci_list = [x, x]
        print(fibanocci_list)
        break
    # if number is bigger than 2 than programs starts finding all fibanocci numbers
    elif counter2 > 2:
        # settings up those two first same fibanocci numbers to have something to start with
        fibanocci_list = [x, x]
        # counter1 is the way the loop knows to count 10 times.
        # counter2 is the answer we give for the question of how big the sequence we want it to be.
        while counter1 < (counter2-1):
            # if you are trying to understand it the run the code and try to match the pattern
            fibanocci_list.append(fibanocci_list[counter1] + fibanocci_list[counter1 -1])
            #loop hapening
            counter1 += 1
            print(fibanocci_list)
            # logic
            if counter1 > 1000:
                break



"""
def fibonacci():
    num = int(input("How many numbers that generates?:"))
    starter = int(input("What number to start with?"))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib
print(fibonacci())
input()
"""
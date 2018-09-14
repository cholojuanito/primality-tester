import random


def prime_test(N, k):
    # You will need to implements this function and change the return value.

    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.

    # Remember to ensure that all of your random values are unique

    # Should return one of three values: 'prime', 'composite', or 'carmichael'
    '''
        setOfNumsToTest = set()

        for x in range(k):
            setOfNumsToTest.add(random.random(1, N))

        # print(setOfNumsToTest)

        for x in range(len(setOfNumsToTest)):
            pass
    '''
    return 'prime'


def mod_exp(x, y, N):
    # You will need to implements this function and change the return value.

    return pow(x, y) % N


def probability(k):
    # The probability of being misled after multiple Fermat tests decreases expontentially
    # In fact it is along the lines of 2 ^ -k where k is the number of tests that are run

    return 1 / pow(2, k)


def is_carmichael(N, a):
    ''' 
    The algorithm follows these steps:
        1. Start the algorithm with an exponent value of N - 1
        2. Keep doing the following while the current exponent value, 'currExp' is divisible by 2:
            a. Calculate 'a ^ currExp % N' as 'e'
            b. Check if 'e' is equal to 1
                1) If true, do nothing this bad boy is prime
                2) Otherwise, check if 'e' is equal to N - 1
                    a) If true then set an 'isStillPrime' flag to True
                    b) Otherwise, check if the 'isStillPrime' flag is set to False
                        1. If set to False then return True, N is a Carmichael number
            c. Divide 'currExp' by 2 and continue
        3. If we reach this point then return False, N is a prime number
    '''
    nMinusOne = N - 1
    currExp = nMinusOne
    isStillPrime = False
    while (currExp % 2 == 0):
        e = mod_exp(a, currExp, N)
        if (e != 1):
            if (e == nMinusOne):
                isStillPrime = True
            else:
                if (isStillPrime != True):
                    return True

        currExp /= 2

    return False

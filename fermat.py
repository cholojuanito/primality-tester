import random
import math


def prime_test(N, k):
    '''
    Big-O time: O(n^3) because this function calls mod_exp which is a n^3
    Big-O space: O(k) because the largest aspect of this function is the set of size 'k' 

    prime_test algorithm steps:
        1. Create a set of numbers, size "k" in the range of 1 and N - 1
        2. Iterate through this set and use each number as "a" to do the following:
            a. Calculate 'a ^ currExp % N' as 'e'
            b. Check if e != 1
                1) If true, the number is composite. Return 'composite'
                2) Otherwise, check if the number is_carmichael
                    a) If true, the number is carmichael. Return 'carmichael'
                    b) Otherwise, the number is prime. Return 'prime'
    '''
    setOfNumsToTest = set()

    while (len(setOfNumsToTest) != k):
        randNum = random.randrange(1, N)
        setOfNumsToTest.add(randNum)

    for a in setOfNumsToTest:
        e = mod_exp(a, N - 1, N)

        if (e != 1):
            return 'compsite'

        if is_carmichael(N, a):
            return 'carmichael'

    return 'prime'


def mod_exp(x, y, N):
    '''
    n is the number of bits in 'N'
    Big-O time: O(n^3) because each iteration does a division operation which is a O(n^2). This leads to n * n^2 = n^3
    Big-O space: O(n) because space is allocated for the 'answer' var every recursive call and this is linear to 'n'

    mod_exp algorithm steps:
        1. If y == 0 then return 1
        2. Otherwise, divide 'y' by 2 and round down
        3. Recursively call mod_exp with the new 'y' value
        4. Once the recursion has reached the base case do the following:
            a. Check if y is divisible by 2
                1) If true, return 'answer ^ 2 % N' to the next level of recursion
                2) Otherwise, return ' x * answer ^ 2 % N' to the next level of recursion
    '''
    if (y == 0):
        return 1

    halfExp = math.floor(y / 2)
    answer = mod_exp(x,  halfExp, N)

    if (y % 2 == 0):
        return pow(answer, 2) % N
    else:
        return (x * pow(answer, 2)) % N


def probability(k):
    '''
    Big-O time: O(1) because k is constant and unrelated to the number of bits in 'N'
    Big-O space: O(1) 

    The probability of being misled after multiple Fermat tests decreases expontentially
    In fact, it is along the lines of 2 ^ -k where k is the number of tests that are run
    '''

    return 1 / pow(2, k)


def is_carmichael(N, a):
    '''
    y represents the exponent
    Big-O time: O(log(y)) because we divide y by 2 every iteration thus reducing the number of iterations logarithmically 
    Big-O space: O(y) because one 'area' in memory is made for 'e' after every recursive call, so it is linear to y

    is_carmichael algorithm  steps:
        1. Start the algorithm with an exponent value of N - 1
        2. Keep doing the following while the current exponent value, 'currExp' is divisible by 2:
            a. Calculate 'a ^ currExp % N' as 'e'
            b. Check if 'e' is NOT equal to 1 and also NOT equal to N - 1
                1) If true, check if the 'negOneModFlag' has been thrown
                    ***negOneModFlag*** indicates if there has been an 'e' that was equal to N - 1
                     at some point in the algorithm
                2) Otherwise, check if 'e' is equal to N - 1
                   a) If true, then throw the 'negOneModFlag' by setting it to True
            c. Divide 'currExp' by 2 and continue
        3. If we reach this point then return False, N is a prime number
    '''
    nMinusOne = N - 1
    currExp = nMinusOne
    negOneModFlag = False

    while (currExp % 2 == 0):
        e = mod_exp(a, currExp, N)
        if (e != 1 and e != nMinusOne):
            if (negOneModFlag == False):
                return True
        elif (e == nMinusOne):
            negOneModFlag = True

        currExp /= 2

    return False

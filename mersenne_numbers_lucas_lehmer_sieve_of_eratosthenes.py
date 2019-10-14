# mersenne number function

def mersenne_number(p):
    return (2 ** p) - 1

# an example of the implementation of the mersenne number function
mersenne_number(5)

# Mersenne numbers can only be prime if their exponent,  𝑝 , is prime

# here is a function to check if a number is a prime number
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# here is a function to obtain all the prime numbers between a and b        
def get_primes(a, b):
    prime_list = []
    for j in range(a, b):
        if is_prime(j):
            prime_list.append(j)
    return prime_list

# testing the get_primes function ...
primes = get_primes(3, 65)

# implementing mersenne_primes ...
mersenne_list = [mersenne_number(prime) for prime in primes]
print(mersenne_list)
print(len(mersenne_list))

# a dummy solution ...
n_start = 3
n_end = 65
mersennes = []
for number in range(n_start, n_end):
    if is_prime(number):
        mersenne_number = (2 ** number) - 1
        mersennes.append(mersenne_number)
print(mersennes)
print(len(mersennes))

# this function below generates the lucas lehmer sequence
def lucas_lehmer(p):
    lucas_lehmer_sequence = [4] * (p - 1) 
    for i in range(1, p - 1):
        lucas_lehmer_sequence[i] = (((lucas_lehmer_sequence[i - 1]) ** 2) - 2) % ((2 ** p) - 1)
    return lucas_lehmer_sequence

# an example implementing the lucas lehmer sequence function ...    
lucas_lehmer(17)

# For a given Mersenne number with exponent  𝑝 , the number is prime if the Lucas-Lehmer series is 0 at position  𝑝−2 
# The function below tests if a mersenne number with exponent p is prime
def lucas_lehmer(p):
    lucas_lehmer_sequence = [4] * (p - 1) 
    for i in range(1, p - 1):
        lucas_lehmer_sequence[i] = (((lucas_lehmer_sequence[i - 1]) ** 2) - 2) % ((2 ** p) - 1)
    if lucas_lehmer_sequence[p - 2] == 0:
        return 1
    else:
        return 0
    #return lucas_lehmer_sequence

# the example below tests if mersenne numbers with prime p between 3 and 65 are prime
# the final answer is a list of tuples consisting of (Mersenne exponent, 0) (or 1) for each Mersenne number that is tested, 
# where 0 and 1 are replacements for False and True respectively.
#lucas_lehmer(17)
my_logic = []
my_primes = get_primes(3, 65)
for idx in my_primes:
    my_logic.append(lucas_lehmer(idx))
print(list(zip(get_primes(3, 65), my_logic)))

# The primality check is_prime developed earlier is somewhat slow for large numbers.
# This is because a ton of extra work is done checking every possible factor of the tested number.
# Two optimizations will be made to implement a is_prime_fast function.
# The first optimization takes advantage of the fact that two is the only even prime.
# The second optimization takes advantage of the fact that when checking factors, only odd factors up to the square root of a number need to be checked.
import math

def is_prime_fast(number):
    if number <= 1:
        return False
    if number % 2 == 0:
        if number > 2:
            return False
    for factor in range(3, int(math.sqrt(number)) + 1, 2):
        if number % factor == 0:
            return False
    return True

# comparing is_prime and is_prime_fast ...
fast_list = []
for n in range(10000):
    fast_list.append(is_prime_fast(n))

slow_list = []
for n in range(10000):
    slow_list.append(is_prime(n))
    
slow_list == fast_list

# run this to ascertain the same primes are generated
for n in range(10000):
    assert is_prime(n) == is_prime_fast(n)

# a function which finds all prime numbers up to and including n
def get_primes_fast(n):
    my_list = []
    for number in range(n):
        if is_prime_fast(number):
            my_list.append(number)
    return my_list

# an example to test the function ...        
get_primes_fast(20)

# SIEVE OF ERATOSTHENES
# The sieve works as follows:
# 1. Generate a list of all numbers between 0 and N; mark the numbers 0 and 1 to be not prime
# Develop a list_true function: Make a list of true values of length  𝑛+1  where the first two values are false (this corresponds with step 1 of the algorithm above)
def list_true(n):
    my_list = []
    for i in range(n + 1):
        if i <= 1:
            my_list.append(False)
        if i >= 2:
            my_list.append(True)
    return my_list

# testing the function ...
list_true(6)

# asserting the function ...
assert len(list_true(20)) == 21
assert list_true(20)[0] is False
assert list_true(20)[1] is False

# 2. Starting with  𝑝=2  (the first prime) mark all numbers of the form  𝑛𝑝  where  𝑛>1  and  𝑛𝑝<=𝑁  to be not prime (they can't be prime since they are multiples of 2!)
# Develop a mark_false function: It takes a list of booleans and a number  𝑝 . Mark all elements  2𝑝,3𝑝,...𝑛  false (this corresponds with step 2 of the algorithm above)
def mark_false(bool_list, p):
    for i in range(2, len(bool_list)):
        if (p * i) < len(bool_list):
            bool_list[p * i] = False
    return bool_list

# asserting the function ...
assert mark_false(list_true(6), 2) == [False, False, True, True, False, True, False]

# 3. Find the smallest number greater than  𝑝  which is not marked and set that equal to  𝑝 , then go back to step 2. Stop if there is no unmarked number greater than  𝑝  and less than  𝑁+1
# Develop a find_next function: Find the smallest True element in a list which is greater than some  𝑝  (has index greater than  𝑝  (this corresponds with step 3 of the algorithm above)
def find_next(bool_list, p):
    for i in range(len(bool_list)):
        if (bool_list[i] == True) and i > p:
            return i

# asserting the function
assert find_next([True, True, True, True], 2) == 3
assert find_next([True, True, True, False], 2) is None

# Now given a list of True and False, return the index of the true values.
def prime_from_list(bool_list):
    index_true = []
    for i in range(len(bool_list)):
        if bool_list[i] == True:
            index_true.append(i)
    return index_true

# asserting the function
assert prime_from_list([False, False, True, True, False]) ==  [2, 3]

# incorporting the sieve of eratosthenes:
def sieve(n):
    bool_list = list_true(n)
    p = 2
    while p is not None:
        bool_list = mark_false(bool_list, p)
        p = find_next(bool_list, p)
    return prime_from_list(bool_list)

# asserting the function ...
assert sieve(1000) == get_primes(0, 1000)
import math

# To analyze
# 1/ Does the number of steps increase if input increases?
# 2/ Go Line by Line, figure out Big-O of each line and add
# 3/ If loop:
#       3.1/  Look at code inside loop and repeat step 2
#       3.2/ Calculate how many times the loop will run
#       3.3/ result of 3.1 x result of 3.2


from math import sqrt


# constant time == O(1)
def mult_2(n):
    print(n)  # O(1)
    if n == 5:  # O(1)
        print("horray")  # O(1)
    return n * 2  # O(1)


# O(1) + O(1) = O(2) => O(1)


# Linear time
def foo(n):  # O(1) + O(n) = O(2) => O(n)

    for i in range(0, n):  # O(n)
        print(i)  # O(1)


# Quadratic time (Polynomial Time)
def bar(n):  # O(1) + O(n^2) + O(1) ==> O(n^2)
    s = 0  # o(1)

    # O(n) * O(n) = O(n^2)
    for i in range(0, n):  # O(n)
        for j in range(0, n):  # O(n) * O(1) = O(n) this loop runs in linear time
            s += i * j  # o(1)
    return s  # o(1)


# O(n) * O(sqrt(n)) == O(n * sqrt n) || O(n^1.5)
# also a variant of O(n) * log(n)
def baz(n):
    s = 0

    for i in range(n):  # O(n)
        for j in range(int(sqrt(n))):  # O(sqrt(n)) || O(n^0.5)
            s += i * j  # O(1)

    return s


# When the input is halved (or another division) every step of the loop
# Think logarithmic!
# log(n)
# Logarithmic time
def divider(n):
    while n >= 1:  # O(log(n))
        print(n)  # O(1)
        n = n // 2  # O(1)

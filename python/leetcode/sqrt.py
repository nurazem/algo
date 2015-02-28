# -*- coding: utf-8 -*-
## calculates the square root of a positive number
## with the passed in precision
def sqrtWithPrecision(x, precision):
    assert(precision > 0, str(precision), 'is not a valid value, it must be a positive integer')
    assert x > 0, 'root can not be a negative number'
    low = 0
    high = max(x, 1)
    counter = 0
    guess= (low + high) /2.0
    while abs (guess ** 2 -x) > precision and counter <= 100:
        if(guess ** 2 < x):
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
        counter += 1
    assert counter <= 100, '100 iterations done and no good answer'
    ## printing the number of iterations,
    ## in productive code, you might want to remove the next line
    print 'Num of iterations:', counter, 'Estimate:', guess
    return guess
sqrtWithPrecision(9, 1)

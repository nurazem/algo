# Implement division using bitwise operators

def divide_bitwise(dividend, divisor):

    remainder = divisor;
    current = 1;
    answer=0;

    if (remainder > dividend):
        return 0

    if (remainder == dividend):
        return 1

    while (remainder <= dividend):
        remainder <<= 1
        current <<= 1

    remainder >>= 1
    current >>= 1

    while (current!=0):
        if (dividend >= remainder):
            dividend -= remainder
            answer |= current
        current >>= 1
        remainder >>= 1

    print remainder
    return answer

print divide_bitwise(10, 3)

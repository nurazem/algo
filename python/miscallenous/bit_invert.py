# Complete the function below.


def  getIntegerComplement(n):
    num_bits = n.bit_length()
    result = 0

    for i in range(num_bits):
        if n & (1 << i):
            result |= 1 << (num_bits - 1 - i)
    return result

print getIntegerComplement(100)

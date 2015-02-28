def longest_nonrepeated_substring(input):
    i, j = 0, 0
    exists = {}
    potential = 0
    while(j < len(input)):
        if input[j] in exists:
            potential = max(potential, j - i)
            while(input[i] != input[j]):
                exists[input[i]] = False
                i += 1
            i += 1
            j += 1
        else:
            exists[input[j]] = True
            j += 1
    return max(potential, len(input) - i)

print longest_nonrepeated_substring('tmmzuxt')

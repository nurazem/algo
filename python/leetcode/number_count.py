def next_num_str(s):
    result = []
    i = 0
    while i < len(s):
        c_count = 1
        j = i
        while j < len(s) - 1 and s[j] == s[j+1]:
            c_count += 1
            j += 1
        result.append(s[i])
        result.append(str(c_count))
        i += c_count
    return ''.join(result)

print next_num_str('1122')

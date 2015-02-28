def parse(s):
    for operator in ["+-", "*/"]:
        depth = 0
        for p in xrange(len(s) - 1, -1, -1):
            if s[p] == ')': depth += 1
            if s[p] == '(': depth -= 1
            if not depth and s[p] in operator:
                return [s[p]] + parse(s[:p]) + parse(s[p+1:])
    s = s.strip()
    if s[0] == '(':
        return parse(s[1:-1])
    return [s]

def ordering(users):
    return [x[0] for x in sorted(users, reverse=True, cmp=lambda a, b: cmp(a[1], b[1]) or cmp(b[0][0], a[0][0]))]

# def main():
users = [('John', 10), ('Bob', 1), ('Carlos', 5), ('Alice', 5), ('Donald', 7)]
print ordering(users)
# print parse('(10) + (20*30)')

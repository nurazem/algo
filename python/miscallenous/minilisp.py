#Use stack

def parse(exp):
    result = exp.replace('(', '( ').replace(')', ' )')
    return result.split(' ')

def tokenizer(exp):
    current = exp.pop(0)
    expressions = {'add': True, 'mult': True, 'let': True}
    if current == '(':
        stack = []
        while exp[0] != ')':
            stack.append(tokenizer(exp))
        exp.pop(0)
        return stack
    elif current in expressions:
        return current
    else:
        try: return int(current)
        except ValueError:
            return current

def replace(arr, x, y):
    for i, e in enumerate(l):
        if e == x:
            arr.pop(i)
            arr.insert(i, y)

def evaluator(exp):
    stack = []
    if isinstance(exp, list) and exp[0] == 'let':
        exp.reverse()

    for i in range(len(exp) - 1, -1, -1):
        if isinstance(exp[i], list):
            stack.append(evaluator(exp[i]))
        else:
            if exp[i] == 'add':
                first = stack.pop()
                second = stack.pop()
                stack.append(first + second)
            elif exp[i] == 'mult':
                first = stack.pop()
                second = stack.pop()
                stack.append(first * second)
            elif exp[i] == 'let':
                x = exp[i - 1]
                first = 0
                if isinstance(exp[i - 2], list):
                    first = evaluator(exp[i - 2])
                else:
                    first = exp[i - 2]
                replace(exp[i - 3], x, first)
                stack.append(evaluator(exp[i - 3]))
            else:
                stack.append(exp[i])
    return stack[0]

import sys
inputs = []
for line in sys.stdin:
    inputs.append(line.rstrip())

for exp in inputs:
    print evaluator(tokenizer(parse(exp)))

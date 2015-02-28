# Enter your code here. Read input from STDIN. Print output to STDOUT

def max_consecutive_streaks(arr):
    i = 0
    max_streak = 0
    while i < len(inputs):
        current_streak = 0
        if is_success(inputs[i]):
            current_streak += 1
            i += 1
        max_streak = max(max_streak, current_streak)
        i += 1
    return max_streak


def is_success(arr):
    budget = int(arr[0])
    breakfast = int(arr[1])
    lunch = int(arr[2])
    dinner = int(arr[3])
    return breakfast + lunch + dinner <= budget

import sys
inputs = []
for line in sys.stdin:
    input = line.split(',')
    inputs.append(input)
#print inputs
print max_consecutive_streaks(inputs)

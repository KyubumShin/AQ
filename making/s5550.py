T = int(input())
howl_dic = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}

for test_case in range(1, T + 1):
    howl = input()
    howl_part = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
    answer = 0
    before = -1
    for c in howl:
        howl_part[c] += 1
        if not howl_part['c'] >= howl_part['r'] >= howl_part['o']>= howl_part['a'] >= howl_part['k']:
            answer = -1
            break
        if c == 'c' and 0 not in howl_part.values():
            for j in howl_part.keys():
                howl_part[j] -= 1
    if not howl_part['c'] == howl_part['r'] == howl_part['o'] == howl_part['a'] == howl_part['k']:
        answer = -1
    else:
        answer = howl_part['c']
    print('#{} {}'.format(test_case, answer))

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
howl_dic = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
for i in range(1, 1+n):
    howl = input().strip()
    howl_part = [0] * 5
    answer = 0
    before = -1
    for c in howl:
        howl_part[howl_dic[c]] += 1
        if howl_dic[c] > 0 and howl_part[howl_dic[c]] > howl_part[howl_dic[c]-1]:
            answer = -1
            break
        if howl_dic[c] == 4:
            answer += 1
        if howl_dic[c] == 0 and answer != 0:
            for j in range(5):
                howl_part[j] -= 1
            answer -= 1
    if sum(howl_part)/5 != howl_part[0]:
        answer = -1
    print(i, answer)

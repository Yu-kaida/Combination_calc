from itertools import combinations

balls = list(map(int, input().split()))
num = int(input())

res = list(combinations(balls, num))
print("----------------------------------")
print("答え：" + str(len(res)) + "通り")
print("----------------------------------")
n = int(input())
mas = list(map(int, input().split()))

min_1 = 2 * 10**9 + 1
min_2 = 2 * 10**9 + 1
prev_min = 2 * 10**9 + 1

for i in range(n):
    if mas[i] < min_2:
        min_2 = mas[i]

    if min_1 > min_2:
        prev_min = min_1
        min_1 = min_2
        min_2 = prev_min

print(min_1, min_2)
n = int(input())
mas = list(map(int, input().split()))

max = -1001

for i in range(n):
    if mas[i] > max:
        max = mas[i]

print(max)
n = int(input())
mas = list(map(int, input().split()))
x = int(input())

diff = 100_000_000
nearest = 0

for i in range(n):
    if abs(mas[i] - x) < diff:
        diff = abs(mas[i] - x)
        nearest = mas[i]

print(nearest)
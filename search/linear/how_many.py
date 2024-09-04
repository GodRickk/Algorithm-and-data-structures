n = int(input())
mas = list(map(int, input().split()))
x = int(input())
count = 0

for i in range(n):
    if mas[i] == x:
        count += 1

print(count)
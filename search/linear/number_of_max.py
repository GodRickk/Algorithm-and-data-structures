n = int(input())
mas = list(map(int, input().split()))

max = -1001
num_of_max = 0

for i in range(n):
    if mas[i] > max:
        max = mas[i]
        num_of_max = i + 1

print(num_of_max)
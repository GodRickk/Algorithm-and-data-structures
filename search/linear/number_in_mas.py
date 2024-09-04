n = int(input())
mas = list(map(int, input().split()))
x = int(input())
numbers_of_equals = []


for i in range(n):
    if mas[i] == x:
        numbers_of_equals.append(i + 1)


if len(numbers_of_equals) != 0:
    print(*sorted(numbers_of_equals))
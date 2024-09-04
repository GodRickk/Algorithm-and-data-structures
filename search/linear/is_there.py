def is_in_mas(array):
    for i in range(len(array)):
        if array[i] == x:
            return "YES"
    return "NO"


n = int(input())
mas = list(map(int, input().split()))
x = int(input())

print(is_in_mas(mas))
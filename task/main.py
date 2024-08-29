n = int(input())
dividend = n
divider = 2

debug_mas = []
count = 0

while dividend != 1:
    if dividend % 2 == 0:
        dividend = dividend // 2
        debug_mas.append(2)
        continue
    else:
        while dividend % divider != 0:
            divider += 1
        dividend = dividend // divider
        debug_mas.append(divider)

print(*debug_mas)
#print(len(debug_mas))
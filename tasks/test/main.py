for i in range(1001):
    thousands = i // 1000 % 10
    hundreds = i // 100 % 10
    tens = i // 10 % 10
    units = i % 10
    digits_sum = thousands + hundreds + tens + units
    if i % 3 == 0 and i % 5 != 0 and digits_sum < 10:
        print(i)
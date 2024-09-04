import sys


def main():
    """
    есть строка S из английских букв в произвольном порядке, и есть набор С - английских букв,
    не повторяющихся. Надо найти минимальную подстроку в строке S состоящую из символов набора С

    Вход: 
    accb
    cab

    Выход:
    4
    
    """
    s = input()
    c = input()
    list_str = list()
    str_length = [] # массив для записи минимальных длин найденных строк

    

    count = 0
    min_str = ""

    # проверка все ли символы из мн-ва есть в строке
    for j in c:
        if s.find(j) == -1:
            return print(0)


    for i in range(len(s)):
        for j in range(len(c)):
            """if s.find(j) == -1:
                min_str = ""
                break"""

            # если текущего символа из строки нет в мн-ве, тогда искомая строка обнуляется
            if c.find(s[i]) == -1:
                min_str = ""
                break
                    
            # если в строке S текущий элемент равен элементу из множества C, то
            # в минимальную строку заносим этот элемент и прекращаем сравнение символа из строки S с символом из мн-ва C
            if s[i] == c[j]:
                min_str += c[j]
                print(min_str)
                break

                """ if len(min_str) == len(c):
                    print(min_str)
                    return print(len(min_str))"""


    # print(count)

    pass


if __name__ == '__main__':
    main()
a = int(input('値を入力してください: '))
b = int(input('値を入力してください: ')) #aはbよりも大きい値を入力する。

if a % 2 == 0:
    sum = a + 1
    print('奇数は', sum)
    for k in range(sum,b):
        sum = sum + 1

        if sum % 2 != 0:
            print('奇数は', sum)


else:
    sum = a
    print('奇数は', sum)
    for k in range(sum,b):
        sum = sum + 1

        if sum % 2 != 0:
            print('奇数は', sum)

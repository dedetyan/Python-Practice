a = int(input('値を入力してください: '))
b = int(input('値を入力してください: ')) #aはbよりも大きい値を入力する。

if a % 2 == 0:
    for k in range(a,b):
        a = a + 1
        if a % 2 != 0:
            print('奇数は', a)

else:
    print('奇数は', a)
    for k in range(a,b):
        a = a + 1
        if a % 2 != 0:
            print('奇数は', a)

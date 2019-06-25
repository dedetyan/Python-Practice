a = int(input('値を入力してください: '))
b = int(input('値を入力してください: ')) #aはbよりも大きい値を入力する。

for k in range(a,b):
    if k % 2 != 0:
        print('奇数は', k)

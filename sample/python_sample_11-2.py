n = int(input('入力する値の個数を指定してください:'))
max = 0

if n > 0:
    for i in range(1,n+1):
        num = int(input('値を入力:'))
        if num > max:
            max = num
            print(i, '回目までの値の最大値は', max, 'です')
        else:
            print(i, '回目までの値の最大値は', max, 'です')


else:
    print('入力値が不正です。')

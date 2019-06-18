num = int(input('数字を入力してください: '))

if num >= 2:
    sum = 1
    for k in range(1,num):
        sum = sum * (k + 1)
    print(num, 'の階乗は', sum, 'です。')

else:
    print('入力された値は不正です。')

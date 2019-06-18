num = int(input('底の値を入力してください: '))
index = int(input('指数の値を入力してください: '))

sum = 1
for k in range(1,(index+1)):
    sum = sum * num
print(num, 'の', index, '乗は', sum, 'です。')

n = int(input('自然数を入力してください:'))

if n > 1:
    for i in range(2,n):
        if n % i == 0:
            print(n, 'は素数でない')
            break
    else:
        print(n, 'は素数です')

else:
    if n == 1:
        print(n, 'は素数でない')

    else:
        print(n, 'は不正な値です。')

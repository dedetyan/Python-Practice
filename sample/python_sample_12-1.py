n = int(input('最終項の分母の値を入力:'))
pai = 1

if n > 0: #値は1以上か
    if n % 2 == 0: #偶数奇数判定
        n = n + 1 #偶数の場合。nを奇数にする
        for k in range(3,n+2,2):
            if (k-1)%4 == 0: #加算減算判定
                pai = pai + (1/k) #加算の場合

            else: #減算の場合
                pai = pai - (1/k)
    else: #奇数の場合
        for k in range(3,n+2,2):
            if (k-1)%4 == 0: #加算減算判定
                pai = pai + (1/k) #加算の場合

            else: #減算の場合
                pai = pai - (1/k)
else:
    print('入力値が不正です') #値が0以下の場合
pai = pai * 4

print('円周率', pai)
print('誤差', pai-3.1415926535897932) #標準円数率との差を出力

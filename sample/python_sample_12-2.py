for i in range(1,11): #10回繰り返し

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

            print(i, '回目') #繰り返し回数を表示
            print('円周率=', '{:.16f}'.format(pai*4)) #小数点以下16桁で表示
            print('誤差　=', '{:.16f}'.format(pai*4-3.1415926535897932)) #標準円数率との差を出力

        else: #奇数の場合
            for k in range(3,n+2,2):
                if (k-1)%4 == 0: #加算減算判定
                    pai = pai + (1/k) #加算の場合

                else: #減算の場合
                    pai = pai - (1/k)

            print(i, '回目') #繰り返し回数を表示
            print('円周率=', '{:.16f}'.format(pai*4)) #小数点以下16桁で表示
            print('誤差　=', '{:.16f}'.format(pai*4-3.1415926535897932)) #標準円数率との差を出力


    else:
        if n == 0:
            print('プログラムを終了します')
            break #0を入力された場合に繰り返しから離脱

        else:
            print('入力値が不正です') #値が0以下の場合,次の処理へ移行

print('end')

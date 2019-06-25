sum = 0
ave = 0
for i in range(1,11):
    num = int(input('値を入力:'))
    sum = sum + num
    ave = sum / i
    print(i, '回目までの合計は', sum)
    print(i, '回目までの平均は', ave)

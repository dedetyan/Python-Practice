t = int(input('t: '))

h = t//3600
i = t%3600
m = i//60
s = i%60

print('{0:02}時間{1:02}分{2:02}秒'.format(h,m,s))

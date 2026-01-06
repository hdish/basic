#两值比较
a,b = 3,6
max = a if a>b else b
print(f'最大值为{max}')

#三值比较
c,d,e = 6,34,18
#            c和e比          c和d比          d和e比
max1 = (c if c>e else e) if c>d else (d if d>e else e)
print(f'最大值为{max1}')
n=5
for row in range(1,n+1):
    for space in range(1,row):
        print(' ',end='')
    for star in range(5,row-1,-1):
        print('*',end='')
    print() 
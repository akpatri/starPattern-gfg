n=4
for row in range(1,n+1):
        for space in range(1,n+1-row):
            print(' ',end='')
        for star in range(1,row*2):
            if(star%2==0):
                print(' ',end='')
            else:
                print('*',end='')
        print()
for row in range(n-1,0,-1):
    for space in range(row,n):
        print(' ',end='')
    for star in range(1,row*2):
        if(star%2==0):
            print(' ',end='')
        else:
            print('*',end='')
    print()
    
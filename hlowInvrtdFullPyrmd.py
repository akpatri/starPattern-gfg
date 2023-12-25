n=5
for row in range(n,0,-1):
    for space in range(0,n-row):
        print(' ',end='')
    for star in range(1,row*2):
        if(row==n):
            if(star%2==0):
                print(' ',end='')
            else:
                print('*',end='')
        else:
            if(star==1 or star==2*row-1):
                print('*',end='')
            else:
                print(' ',end='')
    print()
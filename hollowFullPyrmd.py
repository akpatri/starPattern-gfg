n=6
for row in range(1,n+1):
    for space in range(0,n+1-row):
        print(' ',end='')
    for star in range(1,row*2):
        if(row==n):
            if(star%2==0):
                print(' ',end='')
            else:
                print('*',end='')
        elif(star==1 or star==row*2-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()
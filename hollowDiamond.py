n=4
for row in range(1,n+1):
    for space in range(0,n-row):
        print(' ',end='')
    for star in range(1,row*2):
        if(star==1 or star==row*2-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()
for row in range(n-1,0,-1):
    for space in range(0,n-row):
        print(' ',end='')
    for star in range(1,row*2):
        if(star==1 or star==row*2-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()
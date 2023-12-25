n=4
for row in range(n,0,-1):
    for space in range(0,n-row):
        print(' ',end='')
    for star in range(1,row*2):
        if(star%2==0):
            print(' ',end='')
        else:
            print('*',end='')
    print()
for row in range(2,n+1):
    for space in range(0,n-row):
        print(' ',end='')
    for star in range(1,2*row):
        if(star%2==0):
            print(' ',end='')
        else:
            print('*',end='')
    print()
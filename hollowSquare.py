n=5
for row in range(1,n+1):
    for col in range(1,n+1):
        if(row==1 or row==n):
            print('*',end=' ')
        else:
            if(col==1 or col==5):
                print('*',end=' ')
            else:
                print(' ',end=' ')
    print()
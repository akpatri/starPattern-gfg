n=5
for row in range(1,n+1):
    for col in range(n+1-row,0,-1):
        print('*',end='')
    print()
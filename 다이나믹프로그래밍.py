from array import array
from cgitb import reset


for i  in range(int(input())):


    n,m=map(int,input().split())
    array = list(map(int,input().split()))


    dp = []
    index = 0

    for x in range(n):
        dp.append(array[index:index+m])
        index += m

    for j in range(1,m):
        for x in range(n):

            if x == 0: left_up = 0
            else: left_up = dp[x-1][j-1]

            if x == n-1: left_down = 0
            else:left_down = dp[x+1][j-1]

            left =dp[x][j-1]
            dp[x][j] = dp[x][j] + max(left_up,left_down, left)
            result = 0
            for x in range(n):
                result = max(result ,dp[x][m-1])
            print(result)





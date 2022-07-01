n = int(input())
array = list(map(int , input().split()))


tc = [1] *n

for i in range(1,n):
    for j in range (0,i):
        if array [j] < array[i]:
            tc[i] = max(tc[i], tc[j] +1)


print(n-max(tc))
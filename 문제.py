# 식량 창고 n개에 대한 정보가 주어졌을때 얻을수 있는 식량의 최대값을 구하시오
# 최소 한칸 이상 떨어져 식량창고를 약탈해야한다

# ex) n = 4 최적의 해는 8이다

n = int(input())
food = list(map(int, input().split()))
d = [0] * 101
 
d[0] = food[0]
d[1] = max(food[0], food[1])
 
for i in range(2, n):    
    d[i] = max(food[i] + d[i - 2], d[i - 1])
 
print(d[n - 1])
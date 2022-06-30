# 손님이 왔을때 요청한 총 길이가 m 일때 적어도 m 만큼의 떡을 얻기 위해 절단기에 설정할수 있는 높이의 최대값을 구하는 프로그램을 작성

from array import array


n , m = list(map(int , input(). split()))

array= list(map(int , input(). split()))

start = 0
end = max(array)


result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:

        if x > mid:
            total += x-mid

    if total < m:
        end = mid -1

    else:
        result =mid
        start = mid+1

print(result)
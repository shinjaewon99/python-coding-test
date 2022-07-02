import heapq
import sys
input = sys.stdin.readline

# 무한을 의미하는 값으로 10억을 설정
INF = int(1e9)

# 노드의 갯수 , 간선의 갯수를 입력받기
n, m = map(int , input(). split())

start = int(input())

graph = [[] for i in range(n+1)]

# 최단거리 테이블을 모두 무한으로 초기화

distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기

for _ in range(m):
    a,b,c = map(int , input().split())

    # a 번 노드에서 b 번 노드로 가는 비용이 c 라는 의미

    graph[a].append((b,c))

def dijkstra(satrt):
    q = []

    # 시작 노드로 가기 위한 최단 거리는 0 으로 설정하여 , 큐에 삽입

    heapq.heappush(q,(0,start))

    distance[start] = 0

    while q:  #큐가 비어있지 않다면

        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기

        dist , now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이있는 노드라면 무시

        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인

        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드를거쳐서 , 다른 노드로 이동하는 거리가 더 짧은경우

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))


dijkstra(start)


for i in range(1,n+1):

    # 도달할 수 없는 경우 무한(infinity) 라고 출력

    if distance[i] == INF:
        print("infinity")

    # 도달할 수 있는 경우 거리를 출력

    else:
        print(distance[i])



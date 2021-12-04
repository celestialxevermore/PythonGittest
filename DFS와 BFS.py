# N : 정점의 개수
# M : 간선의 개수 
# V : 탐색을 시작할 정점의 번호 





def DFS(V,visited,mapp):

    for i in range(len(mapp[V])):

        if mapp[V][i]!=0 and i not in visited1:
            visited1.append(i)
            DFS(i,visited,mapp)
    


def BFS(queue,visited,mapp):

    while queue:
        cur = queue[0]
        del queue[0]
        for i in range(len(mapp[cur])):

            if mapp[cur][i]!=0 and i not in visited2:
                visited2.append(i)
                queue.append(i)











# 입력 받기
N,M,V = map(int,input().split())

# 지도 그리기
mapp = [[0]*1001 for _ in range(1001)]

for i in range(M):
    start,end = map(int,input().split())
    mapp[start][end]=1
    mapp[end][start]=1



visited1 = [V]
visited2 = [V] 
queue=[V]




#print("DFS \n\n")
DFS(V,visited1,mapp)

for i in range(len(visited1)):
    print(visited1[i], end=' ')

#print('\n\n')

#print("BFS \n\n")

BFS(queue,visited2,mapp)
print()
for i in range(len(visited2)):
    print(visited2[i], end=' ')
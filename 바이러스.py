# 컴퓨터의 수 100 이하 

# 1번부터 차례대로 숫자가 먹여진다. 




def BFS(queue,visited,mapp):

    while queue:
        cur = queue[0]
        
        del queue[0]

        for i in range(len(mapp[cur])):

            if mapp[cur][i]!=0 and i not in visited:
                visited.append(i)
                queue.append(i)









Computers = int(input())

N = int(input())


mapp = [[0]*101 for _ in range(101)]

for i in range(N):
    start,end = map(int,input().split())
    mapp[start][end]=1
    mapp[end][start]=1


visited=[1]
queue=[1]

BFS(queue,visited,mapp)


print(len(visited)-1)







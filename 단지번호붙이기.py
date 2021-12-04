





N = int(input())

mapp=[[0]*N for _ in range(N)]





for i in range(N):
    list_=input()

    for ii in range(len(list_)):
        mapp[i][ii]=int(list_[ii])
        


dx=[1,-1,0,0]
dy=[0,0,1,-1]





def BFS(queue,curvisited,mapp):
    
    while queue:
        curx,cury = queue[0][0],queue[0][1]
        #print("current x :",curx,"current y :",cury)
        del queue[0]

        for i in range(4):
            nextx,nexty = curx+dx[i],cury+dy[i]

            if nextx>=0 and nexty>=0 and nextx<N and nexty<N and mapp[nextx][nexty]==1 and (nextx,nexty) not in curvisited:
                visited.append((nextx,nexty))
                curvisited.append((nextx,nexty))
                queue.append((nextx,nexty))
    
    return 1,len(curvisited)






queue=[]
danjicnt=0
res=[]
visited=[]
for i in range(N):
    for ii in range(N):
         
        if mapp[i][ii]==1 and (i,ii) not in visited:
            #print("start x :",i,"start y :",ii)
            curvisited=[]
            curvisited.append((i,ii))
            visited.append((i,ii))
            queue.append((i,ii))
            tmp,cnt= BFS(queue,curvisited,mapp)
            danjicnt+=tmp
            res.append(cnt)
        
        

print(danjicnt)
res.sort()

for i in range(len(res)):
    print(res[i])

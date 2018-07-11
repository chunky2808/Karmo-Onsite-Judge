def topo():
    for i in xrange(1,r+1):
        if visited[i] == 0:
            dfs(i)
    return
 
def dfs(x):
    visited[x] = 1
    maxi=0
    for i in arr[x]:
        if visited[i[0]] == 0:
            maxi=max(maxi,2+i[1]+dfs(i[0]))
        else:
            maxi=max(maxi,2+i[1]+vals[i[0]])
    stack.append(x)
    vals[x]=maxi
    return maxi
 
stack = []
r, p = map(int, raw_input().split())
visited = []
vals=[]
arr = []
for i in xrange(r + 1):
    arr.append([])
    visited.append(0)
    vals.append(-1)
 
for i in xrange(p):
    q = map(int, raw_input().split())
    arr[q[0]].append([q[1], q[2]])
topo()
print max(vals)

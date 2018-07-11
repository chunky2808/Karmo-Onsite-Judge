
def dfs(N):
    time = 2
    max_time = time
    if edges[N] == []:
        return 0
    for t in edges[N]:
        max_time = max(time + t[1] + dfs(t[0]), max_time)
    return max_time
    
inp = input().split()
N = int(inp[0])
V = int(inp[1])
 
edges = [[] for i in range(N)]
 
for v in range(V):
    inp = input().split()
    r1 = int(inp[0])-1
    r2 = int(inp[1])-1
    t = int(inp[2])
    edges[r1].append([r2, t])
 
max_time = 0
for n in range(N):
    max_time = max(dfs(n), max_time)
print(max_time)

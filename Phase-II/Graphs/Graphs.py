d = {
    1:[2,3],
    2:[1,4,5],
    3:[1,4,6],
    4:[2,3],
    5:[2],
    6:[3],
    7:[8],
    8:[7]
    }
# def bfs(graph):
#     Q = [7]
#     vis = [False]*len(graph)
#     while Q:
#         curr = Q.pop(0)
#         if not vis[curr]:
#             print(curr,end=" ")
#             vis[curr] = True
#             for i in graph[curr]:
#                 if vis[i] == False:
#                     Q.append(i)
# def dfs(graph):
#     vis = [False]*(9)
#     def f(curr,graph,vis):
#         if not vis[curr]:
#             vis[curr] = True
#             print(curr,end=' ')
#             for i in graph[curr]:
#                 f(i,graph,vis)
#     f(7,graph,vis)
d2 = {
    1:[2,3],
    2:[1,4,5],
    3:[1,4,6],
    4:[2,3],
    5:[2],
    6:[3],
    7:[8,5],
    8:[7]
    }
graph = {
    'A' : ['B','C'],
    'B' : ['A','C','D'],
    'C' : ['A','B','E'],
    'D' : ['B','E'],
    'E' : ['C','D']
}
def Bfs(start,graph):
    visited = [start]
    q = [start]
    while q:
        ele = q.pop(0)
        for i in graph[ele]:
            if i not in visited:
                q.append(i)
                visited.append(i)
    return visited
def Dfs(start,graph,visited = []):
    visited.append(start)
    for ele in graph[start]:
        if ele not in visited:
            Dfs(ele,graph,visited)
    return visited
# print(Bfs(3,d2))
print(Dfs('E',graph))

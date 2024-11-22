graph = [
    [2, 3],
    [1, 3, 10, 11, 12],
    [2, 1, 4, 7],
    [3, 5, 6],
    [4, 6],
    [4, 5, 7],
    [6, 3],
    [9],
    [8],
    [2],
    [2],
    [2],
    []
]

def get_components(g): # алгоритм поиска компонент связности
    n = len(g)
    k = 0 # количество найденных компонент связности
    comp = [None] * n # компонента связности для каждой вершины
    
    def dfs(v):
        comp [v - 1] = k
        
        for u in g[v - 1]:
            if comp[u - 1] is None:
                dfs(u)
    
    for v in range(1, n + 1):
        if comp[v - 1] is None:
            k += 1
            dfs(v)
    
    components = [[] for _ in range(k)] # компоненты связности
    
    for v in range(1, n + 1):
        components [comp [v - 1] - 1].append(v)
    
    return components

print( *get_components(graph), sep='\n')

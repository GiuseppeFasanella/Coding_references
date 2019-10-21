from collections import defaultdict
from collections import deque

def dfs(graph, start='A', end='D'): ## DFS e' una LIFO
    queue = [start]
    
    while len(queue):
        node = queue.pop() #dfs prende l'ultimo elemento della queue.
        
        for next_node in graph[node]:
            if next_node == end:
                return True
            else:
                queue.append(next_node)
    return False #destination not found

def bfs(graph, start='A', end='D'): ## BFS e' una FIFO
    queue = deque([start])
    
    while len(queue):
        node = queue.popleft() #prende il primo elemento della queue.
        
        for next_node in graph[node]:
            if next_node == end:
                return True
            else:
                queue.append(next_node)
    return False #destination not found

def dfs_with_visited(graph, start='A', end='F'): ## DFS e' una LIFO
    queue = [start]
    visited = set()
    
    while len(queue):
        node = queue.pop() #dfs prende l'ultimo elemento della queue.
        visited.add(node)
        
        for next_node in graph[node]:
            if next_node in visited:
                continue
            if next_node == end:
                return True
            else:
                queue.append(next_node)
    return False #destination not found

def bfs_with_visited(graph, start='A', end='F'): ## BFS e' una FIFO
    queue = deque([start])
    visited = set()
    
    while len(queue):
        node = queue.popleft() #prende il primo elemento della queue.
        visited.add(node)
        
        for next_node in graph[node]:
            if next_node in visited:
                continue
            if next_node == end:
                return True
            else:
                queue.append(next_node)
    return False #destination not found

graph = defaultdict(list)
graph['A'] = ['B','C']
graph['B'] = ['A']
graph['D'] = []

#      A
#    // \
#    B  C       D

from collections import deque

def dfs_best_path(graph, start, end):
    queue = [(start, [start])]
    best_path = []
    best_score = 1000 #some ini value
    while queue:
        (node, path) = queue.pop() # DFS e' una LIFO
        
        for next_node in graph[node]:
            if next_node == end and len(path + [end])<best_score:
                best_path = path + [end]
                best_score = len(path)
            else:
                ## Fare questo check dopo, vuol dire che un path ciclico che inizia e finisce dallo stesso nodo e' ammissibile. Non ci devono pero' essere nodi rivisitati in mezzo al path.
                if next_node in path: # no need for a visited set
                    continue
                else:
                    queue.append((next_node, path + [next_node]))

    return best_path

def bfs_all_paths(graph, start, end):
    queue = deque([(start, [start])])
    best_path = []
    best_score = 1000 #some ini value
    while queue:
        (node, path) = queue.popleft() # BFS e' una FIFO
        
        for next_node in graph[node]:
            if next_node == end and len(path + [end])<best_score:
                best_path = path + [end]
                best_score = len(path)
            else:
                ## Fare questo check dopo, vuol dire che un path ciclico che inizia e finisce dallo stesso nodo e' ammissibile. Non ci devono pero' essere nodi rivisitati in mezzo al path.
                if next_node in path: # no need for a visited set
                    continue
                else:
                    queue.append((next_node, path + [next_node]))

    return best_path
                

graph = {}
graph['A'] = ['B','F']
graph['B'] = ['D']
graph['D'] = ['F']
graph['F'] = []

#       A
#      / \
#      B  |
#      |  |
#      D  |
#       \/
#        F
print(dfs_best_path(graph=graph, start='A', end='F')) 
print(bfs_all_paths(graph=graph, start='A', end='F'))

from collections import deque

def dfs_all_paths(graph, start, end):
    queue = [(start, [start])]
    all_paths = []
    while queue:
        (node, path) = queue.pop() # DFS e' una LIFO
        
        for next_node in graph[node]:
            if next_node == end:
                all_paths.append(path + [end])
            else:
                ## Fare questo check dopo, vuol dire che un path ciclico che inizia e finisce dallo stesso nodo e' ammissibile. Non ci devono pero' essere nodi rivisitati in mezzo al path.
                if next_node in path: # no need for a visited set
                    continue
                else:
                    queue.append((next_node, path + [next_node]))

    return all_paths

def bfs_all_paths(graph, start, end):
    queue = deque([(start, [start])])
    all_paths = []
    while queue:
        (node, path) = queue.popleft() # BFS e' una FIFO
        
        for next_node in graph[node]:
            if next_node == end:
                all_paths.append(path + [end])
            else:
                ## Fare questo check dopo, vuol dire che un path ciclico che inizia e finisce dallo stesso nodo e' ammissibile. Non ci devono pero' essere nodi rivisitati in mezzo al path.
                if next_node in path: # no need for a visited set
                    continue
                else:
                    queue.append((next_node, path + [next_node]))

    return all_paths
                

graph = {}
graph['A'] = ['B','C']
graph['B'] = ['D']
graph['D'] = ['F']
graph['C'] = ['E']
graph['E'] = ['F']

#       A
#      / \
#      B  C
#      |  |
#      D  E
#       \/
#        F
print(dfs_all_paths(graph=graph, start='A', end='F')) 
# [['A', 'C', 'E', 'F'], ['A', 'B', 'D', 'F']]
print(bfs_all_paths(graph=graph, start='A', end='F'))

graph = {}
graph['A'] = ['B']
graph['B'] = ['A']

#       A
#      // 
#      B  
print(dfs_all_paths(graph=graph, start='A', end='A'))
print(bfs_all_paths(graph=graph, start='A', end='A'))
#[[A,B,A]]

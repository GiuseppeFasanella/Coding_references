from collections import defaultdict
from collections import deque

## Problema 1.1 :-> Esiste un  path da start a end? Caso Directed Acyclic Graph
graph = defaultdict(list)
graph['A'] = ['B','C']
graph['B'] = ['D']
graph['D'] = ['F']
graph['C'] = ['E']

#       A
#      / \
#      B  C
#      |  |
#      D  E
#      |
#      F


def dfs(graph, start='A', end='F'):
    queue = [start]
    while len(queue):
        node = queue.pop() #dfs prende l'ultimo elemento della queue.
        ##print(node) #Giusto per vedere come tocco i nodi
        
        for next_node in graph[node]:
            if next_node == end:
                return True
            else:
                queue.append(next_node)
    return False #destination not found

def bfs(graph, start='A', end='F'):
    ## Una bfs che si rispetta ha una queue e un path
    queue = deque([start])
    while len(queue):
        ## Sostanzialmente QUESTA e' l'unica diff tra DFS e BFS
        node = queue.popleft() #prende il primo elemento della queue.
        ##print(node)
        
        for next_node in graph[node]:
            if next_node == end:
                return True
            else:
                queue.append(next_node)
    return False #destination not found
                
# print(bfs(graph))
# print(dfs(graph))

##################################################
## Problema 1.2 :-> Esiste un  path da start a end? Caso Graph CON cicli connesso
## DFS che NON si blocca in loop
graph = defaultdict(list)
graph['A'] = ['B','C']
graph['B'] = ['A','D']
#       A
#      //\
#      B  C
#      |  
#      D  

#print(dfs(graph,start='A',end='D'))

## DFS che SI blocca in loop
graph = defaultdict(list)
graph['A'] = ['B','C']
graph['C'] = ['A']
graph['B'] = ['D']
#       A
#      /\\
#      B  C
#      |  
#      D 

#print(dfs(graph,start='A',end='D'))



### Se ho un grafo connesso la BFS, anche senza visited funziona lo stesso
### Il problema si pone quando il grafo NON e' connesso, allora se tu parti da un punto
## che non puo' raggiungere la end position e non marchi il fatto che hai gia' visitato alcuni nodi --> e beh continua a rigirare tra quegli stessi nodi senza arrivare mai alla end e ti incastri in un loop infinito.
### Percio' un esempio che rompe la BFS e':
graph = defaultdict(list)
graph['A'] = ['B','C']
graph['B'] = ['A']
graph['D'] = []
#       A
#      / \
#      B  C       D

## La BFS invece non incappa in loop infiniti SE il grafo (anche con cicli) e' connesso
## Se invece gli si da' un grafo non connesso con cicli, se parto da uno start che non puo' raggiungere end, 
## la BFS non trova mai end e continua a girare a vuoto tra nodi gia' visitati andando il infinite loop.

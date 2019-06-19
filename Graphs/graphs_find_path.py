## create a graph as a dictionary                                                                                                                                                
g = { "a" : ["d", "f"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : ["d"]
    }
#g = { "a" : ["d"],                                                                                                                                                              
#      "b" : ["c"],                                                                                                                                                              
#      "c" : ["b", "c", "d", "e"],                                                                                                                                               
#      "d" : ["a", "c"],                                                                                                                                                         
#      "e" : ["c"],                                                                                                                                                              
#      "f" : []                                                                                                                                                                  
#    }                                                                                                                                                                           


## question1: trova un path (il primo che riesce a trovare) da 'a' a 'b'.                                                                                                        
## question2: trova tutti i possibile path da 'a' a 'b'.                                                                                                                         

## recursion                                                                                                                                                                     
def find_path(graph, start_vertex, end_vertex, path=[]):
    ### L'idea e' di spostare sempre lo start_point fino a quando start_point == end_point                                                                                       
    path = path + [start_vertex]
    if start_vertex == end_vertex: #pop-out condition                                                                                                                            
        return path
    if start_vertex not in graph: #safe-out condition                                                                                                                            
        return None
    for vertex in graph[start_vertex]: #This is a BFS Breadth First Search                                                                                                       
        if vertex not in path: #If you have not already visited that vertex                                                                                                      
            extended_path = find_path(graph,vertex, end_vertex, path)
            if extended_path:
                return extended_path

def find_all_paths(graph, start_vertex, end_vertex, path=[]):
    path = path + [start_vertex]
    if start_vertex == end_vertex:
        return [path]
    if start_vertex not in graph:
        return []
    paths = []
    for vertex in graph[start_vertex]:
        if vertex not in path:
            extended_paths = find_all_paths(graph, vertex, end_vertex, path)
            ## Difference w.r.t above: find_paths al primo match returna, questo stora tutti i possibili path                                                                    
            for p in extended_paths:
                paths.append(p)
    return paths


print(find_path(g, "a", "b"))
print(find_all_paths(g,"c","c"))

'''                                                                                                                                                                              
"Note on find_all_paths: it fails to find all c->c path in a graph like this:                                                                                                    
g = { "a" : ["d", "f"],                                                                                                                                                          
      "b" : ["c","e"],                                                                                                                                                           
      "c" : ["b", "c", "d", "e"],                                                                                                                                                
      "d" : ["a", "c"],                                                                                                                                                          
      "e" : ["c"],                                                                                                                                                               
      "f" : ["d"]                                                                                                                                                                
    }                                                                                                                                                                            
'''

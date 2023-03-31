import queue
graph = {
    'A' : ['B' , 'C'],
    'B' : ['E' , 'D' , 'A'],
    'C' : ['D' , 'F' , 'A'],
    'D' : ['E' , 'F' , 'B'],
    'E' : ['F' , 'B'],
    'F' : ['D' , 'E' , 'C' , 'H'],
    'G' : ['H' , 'I'],
    'H' : ['G' , 'I' , 'F'],
    'I' : ['G' , 'H']
}
q = queue.Queue()
q.put(list(graph.keys())[0])
v_count = len(graph)
visited = []
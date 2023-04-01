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
first_v = list(graph.keys())[0]
q.put(first_v)
v_count = len(graph)
visited = [first_v]
current_v = first_v
destinations = graph[first_v]
while(not q.empty()):
    current_v = q.get()
    destinations = graph[current_v]
    for i in range(len(destinations)):
        if(not destinations[i] in visited):
            q.put(destinations[i])
            visited.append(destinations[i])
            print(current_v , ' - ' , destinations[i])
import sys
graph = [
    [ 0 ,6.7,5.2,2.8,5.6,3.6] ,
    [6.7, 0 ,5.7,7.3,5.1,3.2] ,
    [5.2,5.7, 0 ,3.4,8.5,4.0] ,
    [2.8,7.3,3.4, 0 , 8 ,4.4] ,
    [5.6,5.1,8.5, 8 , 0 ,4.6] ,
    [3.6,3.2, 4 ,4.4,4.6, 0 ]
]
labels = ['1' , '2' , '3', '4', '5', '6']
vertices_count = len(labels)
selected_edges_count = 0
selected = [False for _ in labels]
selected[0] = True
while selected_edges_count < vertices_count - 1:
    min = sys.maxsize
    temp_from = -1
    temp_to = -1
    for r in range(vertices_count):
        if(selected[r]== True):
            for c in range(vertices_count):
                if(selected[c] == False and graph[r][c] != 0 and graph[r][c] < min):
                    min = graph[r][c]
                    temp_from = r 
                    temp_to = c
    selected[temp_to] = True
    selected_edges_count += 1
    print(labels[temp_from] , ' - ' , labels[temp_to] , min)
from collections import namedtuple
labels = ['A' , 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
data = [
    [0,2,4,3,0,0,0,0,0,0],
    [0,0,0,0,7,4,6,0,0,0],
    [0,0,0,0,3,2,4,0,0,0],
    [0,0,0,0,4,1,5,0,0,0],
    [0,0,0,0,0,0,0,1,4,0],
    [0,0,0,0,0,0,0,6,3,0],
    [0,0,0,0,0,0,0,3,3,0],
    [0,0,0,0,0,0,0,0,0,3],
    [0,0,0,0,0,0,0,0,0,4],
    [0,0,0,0,0,0,0,0,0,0],
]
length = len(data)
state = namedtuple('State' , ['From' , 'To' , 'Cost'])
states = []
states[length-1] = state(From = 'J' ,To = 'J' ,Cost = 0)
rowIndex = length - 2
while(rowIndex >= 0):
    for columnIndex in range(rowIndex+1,length):
        if data[rowIndex][columnIndex] == 0: continue
        states[rowIndex] = state(From=labels[rowIndex],To=labels[columnIndex],Cost=100000)
    rowIndex -=1

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
states = list(zip(labels, labels, labels))
states[length-1] = state(From = 'J' ,To = 'J' ,Cost = 0)
rowIndex = length - 2
while(rowIndex >= 0):
    states[rowIndex] = state(From=labels[rowIndex],To=labels[rowIndex+1],Cost=100000)
    for columnIndex in range(rowIndex+1,length):
        if data[rowIndex][columnIndex] == 0: continue
        newCost = data[rowIndex][columnIndex] + states[columnIndex].Cost
        if newCost < states[rowIndex].Cost:
            states[rowIndex].To = labels[columnIndex]
            states[rowIndex].Cost = newCost 
    rowIndex -=1

print(states[0].Cost)
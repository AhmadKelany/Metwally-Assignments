from collections import namedtuple
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
data = [
    [0, 2, 4, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 4, 6, 0, 0, 0],
    [0, 0, 0, 0, 3, 2, 4, 0, 0, 0],
    [0, 0, 0, 0, 4, 1, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 6, 3, 0],
    [0, 0, 0, 0, 0, 0, 0, 3, 3, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
length = len(data)
state = namedtuple('State', ['From', 'To', 'Cost'])

states = [state(l, l, 0) for l in labels]
states[length-1] = state(From='J', To='J', Cost=0)
rowIndex = length - 2
while (rowIndex >= 0):
    fromLabel = labels[rowIndex]
    toLabel = ''
    cost = 100000
    for columnIndex in range(rowIndex+1, length):
        if data[rowIndex][columnIndex] == 0:
            continue
        newCost = data[rowIndex][columnIndex] + states[columnIndex].Cost
        if newCost < cost:
            toLabel = labels[columnIndex]
            cost = newCost
    states[rowIndex] = state(fromLabel, toLabel, cost)
    rowIndex -= 1

path = ['A']
totalCost = 0
stateIndex = 0
pathIndex = 0
while stateIndex < len(states)-1:
    if states[stateIndex].From == path[pathIndex]:
        path.append(states[stateIndex].To)
        totalCost += states[stateIndex].Cost
        pathIndex += 1
    stateIndex += 1

print('Shortest Path: ', path)
print('Minimun cost= ', totalCost)

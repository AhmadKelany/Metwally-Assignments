import math
n = int(input("How many data pairs do you want?"))
print("Please enter data pairs in the format : x,y")
sumX = 0
sumY = 0
x = [0] * n
y = [0] * n
for i in range(n):
    v = input('\tpair #%d: ' % i)
    s = v.split(',')
    x[i] = int(s[0])
    y[i] = int(s[1])
    sumX += x[i]
    sumY += y[i]

meanX = sumX / n
meanY = sumY / n

dXsquareSum = 0
dYsquareSum = 0
dXdYProductSum = 0

for i in range(n):
    dx = x[i] - meanX
    dy = y[i] - meanY
    dXsquareSum += (dx*dx)
    dYsquareSum += (dy*dy)
    dXdYProductSum += (dx*dy)

correlation = dXdYProductSum / math.sqrt(dXsquareSum * dYsquareSum)
print(correlation)

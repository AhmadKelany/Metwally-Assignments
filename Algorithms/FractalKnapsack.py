from collections import namedtuple
Item = namedtuple('Item' , ['Name' , 'Profit' , 'Weight'])
def GetMaxProfit(items: list,maxWeight:int):
    sortedItems = sorted(items , key=lambda d:d.Profit/d.Weight , reverse= True) 
    result = []
    i = 0
    while maxWeight > 0:
        weight = maxWeight if sortedItems[i].Weight >= maxWeight else sortedItems[i].Weight
        item = (sortedItems[i].Name , weight * sortedItems[i].Profit/sortedItems[i].Weight , weight)
        result.append(item) 
        maxWeight -= sortedItems[i].Weight
        i+=1
    return result 

items = [Item(0,4,1) ,Item(1,9,2) ,Item(2,12,10),Item(3,11,4),Item(4,6,3),Item(5,5,5) ]
solution = GetMaxProfit(items , 12)
print(solution)
print('total profit: ' , sum(s[1] for s in solution))

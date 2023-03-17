from collections import namedtuple
Item = namedtuple('Item', ['Name', 'Profit', 'Weight'])


def GetItemsProfitTable(items: list, maxWeight: int):
    table = [[0 for _ in range(maxWeight+1)] for _ in range(len(items)+1)]
    columns = len(table[0])
    rows = len(table)

    for c in range(columns):
        for r in range(rows):
            if (r == 0 or c == 0):
                table[r][c] == 0
            elif (items[r-1].Weight <= c):

                table[r][c] = max(table[r-1][c], items[r-1].Profit +
                                  table[r-1][c - items[r-1].Weight])
            else:
                table[r][c] = table[r-1][c]

    return table


def GetItemsWithMaxProfit(items, table, maxWeight):
    c = len(table[0])-1
    r = len(table)-1
    solution = []
    remainingWeight = maxWeight
    while (remainingWeight >= 0 and c > 0):

        if (table[r][c] > table[r-1][c]):
            item = items[r-1]
            solution.append(item.Name)
            remainingWeight -= item.Weight
            c = remainingWeight
            r -= 1
        else:
            r -= 1
    return solution


items = [Item('#1', 4, 1), Item('#2', 9, 3),
         Item('#3', 12, 5), Item('#4', 11, 4), ]
maxWeight = 8
table = GetItemsProfitTable(items, maxWeight)
solution = GetItemsWithMaxProfit(items, table, maxWeight)
print(solution)

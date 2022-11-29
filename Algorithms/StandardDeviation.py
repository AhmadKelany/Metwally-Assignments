def GetMean(a):
    s = 0
    for x in a:
        s += x
    return s/len(a)


print(GetMean([2,3,6,8,9,10]))
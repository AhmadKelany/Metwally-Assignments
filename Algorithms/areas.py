def GetParallelogramArea(base , height):
    return base * height

def GetTrapezoidArea(base1 , base2 , height):
    return height * ((base1+base2)/2)

print(GetParallelogramArea(10,12))
print(GetParallelogramArea(16,9))
print(GetTrapezoidArea(16,9 , 5))
print(GetTrapezoidArea(35,42 , 15))

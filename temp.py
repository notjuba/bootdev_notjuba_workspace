import copy
l = [[1],2,3,4,5]
l2 = copy.copy(l)
l2[0][0] = 100
print(l, l2)
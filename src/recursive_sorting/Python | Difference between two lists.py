def Diff(list_one, list_two):
    list_difference = [item for item in list_one +
                       list_two if item not in list_one or item not in list_two]
    return list_difference


li1 = [10, 15, 20, 25, 30, 35, 40]
li2 = [25, 40, 35]
li3 = Diff(li1, li2)
print(li3)

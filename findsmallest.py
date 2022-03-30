#smallest element in list

#function
def smallest(list):
    small = list[0]
    for i in list:
        if i<small:
            small=i
    return small
#list
list=[3, 9, 7, 3, 6, 5, 7, 24, 6]
print("smallest in ",list,"is")
print(smallest(list))


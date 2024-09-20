list1 = [1,2,3,4,5,6,3,4,5,7,6,5,4,3,4,5,4,3, 'Привіт', 'анаконда']

def getList(list1):
    list2 = []
    for item in list1:
        if item not in list2:
            list2.append(item)
    return list2

def getSortList():
    int chisla=[]
    str text=[]
     for item in list2:
    chisla.append(item)
    text.append(text)
    chisla.sort()
    text.sort()
    
    sorted_list = chisla + text
    return sorted_list
res = getList(list1)
sorted_list = getSortList(res)
print("Список без повторень:", res)
print("Відсортований список:", sorted_list)

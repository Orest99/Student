list1 = [1,2,3,4,5,6,3,4,5,7,6,5,4,3,4,5,4,3, 'Привіт', 'анаконда']

def getList(list1):
    dubl = set(list1)
    poslidovnist = list(dubl)
    return poslidovnist
    
def getSortList():
     chisla=[]
     text=[]
for item in poslidovnist:
    if type(item) == int:
        chisla.append(item)
    elif type(item) == str:
        text.append(item)

    chisla.sort()
    text.sort()
    sorted_list = chisla + text
    return sorted_list
poslidovnist = getList(list1)#без повторів
sorted_list = getSortList(poslidovnist)

print("Список без повторень:", poslidovnist)
print("Відсортований список:", sorted_list)

text = "Hello World"
f_name = "Orest"
l_name = "Yakobchuk"
age = 17
list1 = []
list1.append(text)
list1.append(f_name)
list1.append(l_name)
list1.append(age)

for item in list1:
    print (item)
    print(type(item))
#------------------------------------------------------------    
for item in list1:
    if type(item) == str and f_name in item and l_name in item:
        print("Однакове:",item)
    print(item)
    print(type(item))
#------------------------------------------------------------    
if type(age) == int:
    print("Тип даних віку:",type(age))
    if age == 17:
        print("Вік: ",{age}, "тип: ",type(age))
#------------------------------------------------------------
list2 = []
for item2 int list2:
    print(item2)
    print (type(item2))
#-------------------------------------------------------------


#------------------------------------------------------------        
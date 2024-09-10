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
    list1.clear()
    print("Clearning",list1)
#------------------------------------------------------------    
for item in list1:
    if type(item) == str and f_name in item and l_name in item:
        print("Однакове:",item)
    print(item)
    print(type(item))
    list1.clear()
    print ("Clearning",list1)
#------------------------------------------------------------    
if type(age) == int:
    print("Тип даних віку:",type(age))
    if age == 17:
        print("Вік: ",{age}, "тип: ",type(age))
#------------------------------------------------------------
list3= []
text2= "Hello world"
f_n= "Orest"
l_n= "Yakobchuk"
list3.append(f_n)
list3.append(l_n)
list3.append(text2)
info= " ".join(list(text2))
list3.append(info)
print (list3)
list3.clear()
print("Clearning",list3)
#------------------------------------------------------------

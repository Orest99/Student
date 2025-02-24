class Orest:
    def __init__(self, first_name=None, last_name=None, birth_year=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

        if self.first_name is None:
            self.first_name = "None"
        if self.last_name is None:
            self.last_name = "None"
        if self.birth_year is None:
            self.birth_year = "None"

    def course(self):
        if self.birth_year != "None":
            return 2025 - int(self.birth_year)
        else:
            return None

    def name_list(self):
        list1_name = []
        if self.first_name != "None":
            list1_name.append(self.first_name)
        if self.last_name != "None":
            list1_name.append(self.last_name)
        return list1_name
class Student(Orest):
    def __init__(self, first_name=None, last_name=None, birth_year=None,city=None,email=None,ph_num=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.city = city
        self.email = email
        self.ph_num = ph_num
    def _check_city(self):
        enter = input("Enter the city name: ")
        if enter == "Lutsk":
            return "Complete"
        else:
            if self.city != "Lutsk":
                return "What your city?"
    def __check_ph(self):
        ph = input("Enter your phone number: ")
        if ph != "None" and ph.startswith("+380"):
            return "Complete"
        else:
            return "What your phone number?"

    def check_phone_number(self):
        return self.__check_ph()
    def _email(self):
        inf = input("Enter your email: ")
        lst1 = []
        if inf != "None":
            lst1.append(inf)
            print(lst1)
        else:
           return "Eror"



info = Orest("Orest", "Yakobchuk", 2007)
info2 = Student("Orest", "Yakobchuk", 2007)
lst1 = []
lst1.append(info2.course())
print(info.course())
print(info.name_list())
print(info2._check_city())
print(info2._email())
print(info2.check_phone_number())

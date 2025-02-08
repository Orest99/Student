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

info = Orest("Orest", "Yakobchuk", 2007)
print(info.course())
print(info.name_list())

no_info = Orest()
print(no_info.course())
print(no_info.name_list())

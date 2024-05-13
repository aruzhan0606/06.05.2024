class Person:
    def _init_(self, name, age, surname):
        self.name = name
        self.age = age
        self.surname = surname

    def my_method(self):
        print("Менің атым " + self.name, "жасым ", self.age, "және тегім ", self.surname, "де")

p1 = Person("Аружан", 18, "Бекбатыр")
p1.my_method()



class Person:
    def _init_(self, name, age, surname=""):
        self.name = name
        self.age = age
        self.surname=surname

        
    def my_method(self):
        if self.surname:
            print("Менің атым "+ self.name, self.surname ,"жасым ", self.age, )
            
        else:
            print("Менің атым "+ self.name,"жасым " ,self.age, "де " )
       

p1 = Person("Аружан",18,"Бекбатыр")
p1.my_method()
p1 = Person("Аружан",18,"")
p1.my_method()

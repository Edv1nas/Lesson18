# class Person:

#     def __init__(self, name: str, surname: str) -> None:
#         self.name = name
#         self.surname = surname

#     def fullname(self):
#         print(self.name, self.surname)

# class Student(Person):

#     def __init__(self, name: str, surname: str, education: str) -> None:
#         super().__init__(name, surname)
#         self.education = education

#     def full_info(self):
#         print(self.name,self.surname,self.education)

# student = Student("Tadas","Blinda","None")
# student.full_info()


class Fruits:
    def __init__(self, quantity: float)-> None:
        self.quantity = quantity

    
    def get_quantity(self):
        return self.quantity
    
class Orange(Fruits):
    ORANGE_PRICE = 2.45

    def get_full_price(self)->float:
        return round(self.ORANGE_PRICE * self.quantity, 2)
        
    
class Kiwi(Fruits):
    KIWI_PRICE = 1.89

    def get_full_price(self)->float:
        return round(self.KIWI_PRICE * self.quantity, 2)

        
        
orange_fruit = Orange(quantity = 1.5)
kiwi_fruit = Kiwi(quantity = 2)


print(f'Orange price for {orange_fruit.quantity}kg is {orange_fruit.get_full_price()} Euro')
print(f'Kiwi price for {kiwi_fruit.quantity}kg is {kiwi_fruit.get_full_price()} Euro')

kiwi_cost = kiwi_fruit.get_full_price()
orange_cost = kiwi_fruit.get_full_price()
total_cost = kiwi_cost + orange_cost
print(f'Total fruits price: {total_cost} Euro')

        






    

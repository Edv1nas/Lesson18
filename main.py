# class Names:
#     """This is a class our forgotten friend Antanas"""

#     def __init__(self, name: str, surname: str, age: int):
#         self.name = name
#         self._surname = surname
#         self.__age = age

#     def print_out_name(self ) ->None:
#         print(self.name)

#     def change_name(self, name: str):
#         self.name = name


# my_name = Names(name="Antanas", surname="Mindaugas", age=22)
# print(my_name.name)

# # my_name.name = "minde"
# # print(my_name.name)

# print(my_name._surname)
# print(my_name.__age)

# class Car:
#     def __init__(self, make_year: int, cost: float, color: str) -> None:
#         self.make_year = make_year
#         self.cost = cost
#         self.color = color
#         self.full_info = f" Full info: {cost} linero - {make_year} years - {color}..."

#     def get_car_color(self) -> None:
#         print(f"My car color: {self.color}")

#     def get_cost(self) -> float:
#         return self.cost
    
#     def get_full_info(self):
#         print(f'My full info: {self.full_info}')


class Car:
    def __init(self) -> None:
        self._check_this_one: int =1
        self._check_another_one: int =2

    def get_car_color(self, color: str) -> None:
        print(f"My car color: {self.color}")

    def get_cost(self, cost: float) -> float:
        return self.cost
    
    def get_full_info(self, full_info: str):
        print(f'My full info: {self.full_info}')

class Ferrari(Car):
    SPEED_CONSTANT = 20.5

    def __init__(self, hp: int) -> None:
        super().__init__()
        self.hp = hp


    def get_max_speed(self) -> float:
        return self.hp * self.SPEED_CONSTANT
    
    def get_cost(self, cost: float) -> float:
        print(f"cool not cool: {cost}")
    

my_uber_car = Ferrari(hp = 450)
print(f"Max speed: {my_uber_car.get_max_speed()}")
# my_uber_car.get_car_color("White")
my_uber_car.get_cost(cost=25000)
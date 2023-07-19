# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.


class Animal:
    def __init__(self, name: str):
        self.name = name

    def show_spec(self):
        pass


class Fish(Animal):
    LITTLE = 10
    HIGHT = 100

    def __init__(self, name: str, long: int):
        super().__init__(name)
        self.long = long

    def show_spec(self):
        if self.long < self.LITTLE:
            return "Мелководная рыба"
        elif self.long > self.HIGHT:
            return "Глубоководная рыба"
        else:
            return "Средне-водная рыба"


class Bird(Animal):
    def __init__(self, name: str, length: int):
        super().__init__(name)
        self.length = length

    def show_spec(self):
        return self.length * 2


fish1 = Fish('акула', 50)
bird1 = Bird('орел', 15)
animal_list = [fish1, bird1]
for animal in animal_list:
    print(animal.show_spec())








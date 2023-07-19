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

    def __init__(self, name: str, length: int):
        super().__init__(name)
        self.length = length

    def show_spec(self):
        if self.length < self.LITTLE:
            return "Мелководная рыба"
        elif self.length > self.HIGHT:
            return "Глубоководная рыба"
        else:
            return "Средне-водная рыба"


class Bird(Animal):
    def __init__(self, name: str, wingspan: int):
        super().__init__(name)
        self.wingspan = wingspan

    def show_spec(self):
        return self.wingspan * 2


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str, name: str, **kwargs):
        if animal_type == "Fish":
            return Fish(name, kwargs.get("length"))
        elif animal_type == "Bird":
            return Bird(name, kwargs.get("wingspan"))
        else:
            raise ValueError("Invalid animal type")


fish1 = Fish('акула', 50)
bird1 = Bird('орел', 15)
animal_list = [fish1, bird1]

# Использование класса-фабрики для создания экземпляров животных
animal_factory = AnimalFactory()
fish2 = animal_factory.create_animal("Fish", "карась", length=20)
bird2 = animal_factory.create_animal("Bird", "сокол", wingspan=30)
animal_list.extend([fish2, bird2])

for animal in animal_list:
    print(animal.show_spec())
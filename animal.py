class Animal:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

class DomesticAnimal(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        self.commands = ["Сидеть", "Лежать"]

class PackAnimal(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        self.commands = ["Идти", "Тянуть"]

# Класс для учета животных
class AnimalRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_commands(self, animal):
        return animal.commands

    def menu(self):
        while True:
            print("Меню:")
            print("1. Завести новое животное")
            print("2. Выход")
            choice = input("Введите выбор: ")
            if choice == '1':
                name = input("Введите имя животного: ")
                birth_date = input("Введите дату рождения (YYYY-MM-DD): ")
                type_of_animal = input("Введите тип животного (домашнее/вьючное): ")
                if type_of_animal == "домашнее":
                    self.add_animal(DomesticAnimal(name, birth_date))
                else:
                    self.add_animal(PackAnimal(name, birth_date))
            elif choice == '2':
                break
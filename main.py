import mysql.connector
from mysql.connector import Error

class Animal:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    def commands(self):
        return []

class DomesticAnimal(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        self._commands = ["Sit", "Lie down"]

    def commands(self):
        return self._commands

class PackAnimal(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        self._commands = ["Walk", "Pull"]

    def commands(self):
        return self._commands

class Register:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_commands(self, animal):
        return animal.commands()

# Функции для работы с базой данных

def create_connection():
    """ Создание подключения к базе данных """
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Замените на ваше имя пользователя
            password='your_password',  # Замените на ваш пароль
            database='pet_registry'  # Замените на имя вашей базы данных
        )
    except Error as e:
        print(f"Ошибка: '{e}'")

    return connection

def create_table(connection):
    """ Создание таблиц """
    query = """
    CREATE TABLE IF NOT EXISTS domestic_animals (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        commands VARCHAR(255),
        birth_date DATE
    );
    """
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

# Пример использования

connection = create_connection()
create_table(connection)

register = Register()
dog = DomesticAnimal("Bobik", "2018-01-01")
horse = PackAnimal("Trus", "2019-05-05")

register.add_animal(dog)
register.add_animal(horse)

print(f"{dog.name} can: {register.show_commands(dog)}")
print(f"{horse.name} can: {register.show_commands(horse)}")

# Закрытие соединения
if connection.is_connected():
    cursor.close()
    connection.close()
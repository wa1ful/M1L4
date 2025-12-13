from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = self.get_hp()
        self.attack = self.get_attack()
        self.defense = self.get_defense()
        self.special_attack = self.get_special_attack()
        self.special_defense = self.get_special_defense()
        self.speed = self.get_speed()

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['sprites']['front_default']
        else:
            return data['sprites']['front_default']
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    def get_hp(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for stat in data['stats']:
                if stat['stat']['name'] == 'hp':
                    return stat['base_stat']
        return 50

    def get_attack(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for stat in data['stats']:
                if stat['stat']['name'] == 'attack':
                    return stat['base_stat']
        return 50

    def get_defense(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for stat in data['stats']:
                if stat['stat']['name'] == 'defense':
                    return stat['base_stat']
        return 50

    def get_special_attack(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for stat in data['stats']:
                if stat['stat']['name'] == 'special-attack':
                    return stat['base_stat']
        return 50

    def get_special_defense(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for stat in data['stats']:
                if stat['stat']['name'] == 'special-defense':
                    return stat['base_stat']
        return 50

    def get_speed(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for stat in data['stats']:
                if stat['stat']['name'] == 'speed':
                    return stat['base_stat']
        return 50

    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покемона: {self.name}\nHP: {self.hp}\nАтака: {self.attack}\nЗащита: {self.defense}\nСпец. атака: {self.special_attack}\nСпец. защита: {self.special_defense}\nСкорость: {self.speed}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
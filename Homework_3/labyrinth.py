import random
import os

class Map():
    def __init__(self, seed, height, width):
        self.seed = seed
        self.height = height
        self.width = width
        self.grid = []
        self.generate_map()
    '''
    def map(self):
        wall = '#'
        cloud = '*'
        room_none = ' '
        room_locker = 'g'
        room_monster = '!'
        room_trap = '&'
        room_key = 'k'
        room_portal_exit = 'e'
        room_portal_map = 'm'
    '''
    def generate_map(self):
        rnd = random.Random(self.seed)
        wall = '#'
        room_none = ' '
        features = ['g', '!', '&', 'k', 'e', 'm']

        for y in range(self.height):
            row = []
            for x in range(self.width):
                if y == 0 or y == self.height - 1 or x == 0 or x == self.width - 1:
                    row.append(row)
                else:
                    c = rnd.random()
                    if c < 0.2:
                        row.append(wall)
                    elif c < 0.6:
                        row.append(rnd.c(features))
                    else:
                        row.append(room_none)
            self.grid.append(row)
    def draw(self, player_coordinates):
        os.system('cls' if os.name == 'nt' else 'clear')

        px, py = player_coordinates
        print('Лабиринт: ' + self.seed)
        print("-"*self.width)

        for y in range(self.height):
            line = ""
            for x in range(self.width):
                if x == px and y == py:
                    line += "P"
                else:
                    line += self.grid[y][x]
            print(line)
        print("-"*self.width)

class Inventory():
    def __init__(self, capacity):
        self.capacity = capacity
        self.items_list = []
    def items(self):
        return self.items_list
    def food(self):
        if "food" in self.items_list:
            self.items_list.remove("food")
            return True
        return False
    def sorting(self):
        self.items_list.sort()
        print('Инвентарь отсортирован')
    def throw_away(self, item):
        if item in self.items_list:
            self.items_list.remove(item)
            print('Вы выбросили: '+ item)
        else:
            print('Вам нечего выбрасывать')
    def to_take_away(self, item):
        if len(self.items_list) < self.capacity:
            self.items_list.append(item)
            print('Вы взяли: '+ item)
            return True
        print('Инвентарь полон!')
        return False
    def enchanted_books(self):
        return [item for item in self.items_list if "book" in item]
    def collection(self):
        return list(set(self.items_list))
    def plot_items(self):
        print('Ваши предметы: '+ self.items_list)

class Gamer():
    def __init__(self, name, strength, mana, health, coordinates, inventory):
        self.name = name
        self.strength = strength
        self.mana = mana
        self.health = health
        self.coordinates = coordinates
        self.inventory = Inventory(capacity=5)
    def damage(self):
        return self.damage*2
    def heal(self):
        if self.inventory.food():
            self.health = min(100, self.health + 30)
            print('Ваше здоровье: '+self.health)
        else:
            print('Еды не осталось')
    def get_hurt(self, amount):
        self.health -= amount
        print('- '+amount+' хп')
    def enchant(self):
        if self.mana >= 20:
            self.mana -= 20
            self.strength += 5
            print('Магия силы применена')
        else:
            print('Вам не хватает маны')
    def coordinator(self):
        return self.coordinates

class Safe():
    def __init__(self, seed, map):
        self.seed = seed
        self.map = map

class Movement():
    def __init__(self, coordinates):
        self.coordinates = coordinates
    def forward(self):
        pass
    def backward(self):
        pass
    def right(self):
        pass
    def left(self):
        pass

game = True
while game:
    pass
        
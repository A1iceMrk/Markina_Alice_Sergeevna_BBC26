import random
import os

class Map():
    def __init__(self, seed, height, width):
        self.seed = str(seed)
        self.height = height
        self.width = width
        self.grid = []
        self.visited = set()
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
                    row.append(wall)
                elif x == 1 and y == 1:
                    row.append(room_none)
                else:
                    c = rnd.random()
                    if c < 0.2:
                        row.append(wall)
                    elif c < 0.45:
                        row.append(rnd.choice(features))
                    else:
                        row.append(room_none)
            self.grid.append(row)

    def reveal_around(self, player_coordinates):
        px, py = player_coordinates
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                self.visited.add((px + dx, py + dy))

    def draw(self, player_coordinates):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.reveal_around(player_coordinates)

        px, py = player_coordinates
        print('Лабиринт: ' + str(self.seed))
        print("-" * self.width)

        for y in range(self.height):
            line = ""
            for x in range(self.width):
                if x == px and y == py:
                    line += "P"
                elif (x, y) in self.visited or x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1:
                    line += self.grid[y][x]
                else:
                    line += "*"
            print(line)
        print("-" * self.width)


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
            print('Вы выбросили: ' + item)
        else:
            print('Вам нечего выбрасывать')

    def to_take_away(self, item):
        if len(self.items_list) < self.capacity:
            self.items_list.append(item)
            print('Вы взяли: ' + item)
            return True
        print('Инвентарь полон!')
        return False

    def enchanted_books(self):
        return [item for item in self.items_list if "book" in item]

    def collection(self):
        return list(set(self.items_list))

    def plot_items(self):
        print('Ваши предметы: ' + ', '.join(self.items_list) if self.items_list else 'Инвентарь пуст')


class Gamer():
    def __init__(self, name, strength, mana, health, coordinates, inventory=None):
        self.name = name
        self.strength = strength
        self.mana = mana
        self.health = health
        self.coordinates = coordinates
        self.inventory = inventory if inventory is not None else Inventory(capacity=5)

    def damage(self):
        return self.strength * 2

    def heal(self):
        if self.inventory.food():
            self.health = min(100, self.health + 30)
            print('Ваше здоровье: ' + str(self.health))
        else:
            print('Еды не осталось')

    def get_hurt(self, amount):
        self.health -= amount
        print('-' + str(amount) + ' хп')

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
    def __init__(self, seed, game_map):
        self.seed = seed
        self.map = game_map
        self.loot_pool = ["food", "magic_book", "gold_coin", "health_potion"]

    def open_locker(self, player):
        if "key" in player.inventory.items():
            player.inventory.throw_away("key")
            rnd = random.Random(str(self.seed) + str(player.coordinates))
            loot = rnd.choice(self.loot_pool)
            print("Вы открыли сундук (g) ключом!")
            player.inventory.to_take_away(loot)
            return True
        else:
            print("Сундук заперт! Нужен ключ (k).")
            return False


class Movement():
    def __init__(self, coordinates):
        self.coordinates = list(coordinates)

    def _can_move(self, new_x, new_y, game_map):
        if 0 <= new_y < game_map.height and 0 <= new_x < game_map.width:
            if game_map.grid[new_y][new_x] != '#':
                return True
        print("Там стена (#)!")
        return False

    def forward(self, game_map):
        nx, ny = self.coordinates[0], self.coordinates[1] - 1
        if self._can_move(nx, ny, game_map):
            self.coordinates = [nx, ny]

    def backward(self, game_map):
        nx, ny = self.coordinates[0], self.coordinates[1] + 1
        if self._can_move(nx, ny, game_map):
            self.coordinates = [nx, ny]

    def right(self, game_map):
        nx, ny = self.coordinates[0] + 1, self.coordinates[1]
        if self._can_move(nx, ny, game_map):
            self.coordinates = [nx, ny]

    def left(self, game_map):
        nx, ny = self.coordinates[0] - 1, self.coordinates[1]
        if self._can_move(nx, ny, game_map):
            self.coordinates = [nx, ny]


def handle_room(player, game_map, safe):
    x, y = player.coordinates
    cell = game_map.grid[y][x]

    if cell == 'k':
        print("Вы нашли ключ!")
        if player.inventory.to_take_away("key"):
            game_map.grid[y][x] = ' '

    elif cell == 'g':
        if safe.open_locker(player):
            game_map.grid[y][x] = ' '

    elif cell == '&':
        print("Вы наступили в ловушку (&)!")
        player.get_hurt(15)
        game_map.grid[y][x] = ' '

    elif cell == '!':
        print("На вас напал монстр (!)!")
        monster_hp = 20
        while monster_hp > 0 and player.health > 0:
            dmg = player.damage()
            monster_hp -= dmg
            print(f"Вы ударили монстра на {dmg} урона.")
            if monster_hp > 0:
                player.get_hurt(10)
        if player.health > 0:
            print("Монстр повержен! Вы нашли еду.")
            player.inventory.to_take_away("food")
            game_map.grid[y][x] = ' '

    elif cell == 'm':
        print("Вы активировали портал карты (m)! Весь лабиринт открыт.")
        for ry in range(game_map.height):
            for rx in range(game_map.width):
                game_map.visited.add((rx, ry))
        game_map.grid[y][x] = ' '

    elif cell == 'e':
        print("Вы нашли портал выхода (e)! Победа!")
        return False

    return True


# --- Инициализация и игровой цикл ---
current_seed = input("Введите сид лабиринта: ") or "dungeon_1"
game_map = Map(seed=current_seed, height=12, width=22)
safe = Safe(seed=current_seed, game_map=game_map)
mover = Movement([1, 1])
player = Gamer(name="Герой", strength=5, mana=40, health=100, coordinates=mover.coordinates)
player.inventory.to_take_away("food")

game = True
while game:
    game_map.draw(player.coordinates)
    print(f"Игрок: {player.name} | HP: {player.health} | Мана: {player.mana} | Сила: {player.strength}")
    player.inventory.plot_items()
    print("\nУправление: [w/a/s/d] - идти | [h] - поесть | [e] - магия силы | [sort] - сортировка | [q] - выход")

    cmd = input("Ваш ход: ").strip().lower()

    if cmd == 'w':
        mover.forward(game_map)
    elif cmd == 's':
        mover.backward(game_map)
    elif cmd == 'a':
        mover.left(game_map)
    elif cmd == 'd':
        mover.right(game_map)
    elif cmd == 'h':
        player.heal()
        input("Нажмите Enter...")
        continue
    elif cmd == 'e':
        player.enchant()
        input("Нажмите Enter...")
        continue
    elif cmd == 'sort':
        player.inventory.sorting()
        input("Нажмите Enter...")
        continue
    elif cmd == 'q':
        print("Вы покинули игру.")
        break
    else:
        continue

    player.coordinates = mover.coordinates
    game = handle_room(player, game_map, safe)

    if player.health <= 0:
        print("\nВы погибли! Игра окончена.")
        game = False

    if game and game_map.grid[player.coordinates[1]][player.coordinates[0]] == ' ':
        pass
    elif game:
        input("Нажмите Enter, чтобы продолжить...")

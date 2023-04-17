class Monster:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f'{self.name} - Health: {self.health} | Attack: {self.attack} | Defense: {self.defense}'

    def attack_player(self, player):
        damage = self.attack - player.defense
        if damage < 0:
            damage = 0
        player.health -= damage
        print(f'{self.name} attacks {player.name} for {damage} damage!')
        
    def generate_monster():
        monster_types = ['Goblin', 'Orc', 'Troll']
        monster_type = random.choice(monster_types)
        if monster_type == 'Goblin':
            return Monster('Goblin', 50, 10, 5)
        elif monster_type == 'Orc':
            return Monster('Orc', 75, 15, 10)
        else:
            return Monster('Troll') #<-come back to here 
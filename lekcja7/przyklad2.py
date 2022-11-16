from random import randint


class Character:
    def __init__(self, name, hp, max_damage, attack_bonus):
        self.name = name
        self.hp = hp
        self.max_damage = max_damage
        self.attack_bonus = attack_bonus
        self.ac = 10

    def get_damage(self):
        return randint(1, self.max_damage)

    def attack(self, target):
        attack_roll = randint(1, 20) + self.attack_bonus
        target.get_hit(attack_roll, self.get_damage())

    def get_hit(self, attack_result, damage):
        if attack_result >= self.ac:
            print(self.name + " got hit for " + str(damage) + " damage")
            self.hp = self.hp - damage
        else:
            print("miss!")




def get_fight_status(hero, foe):
    print(hero.name + ":" + str(hero.hp) + " " + foe.name + ":" + str(foe.hp))


hero = Character("Hero", 100, 10, 5)
goblin = Character("Goblin", 20, 1, 1)

get_fight_status(hero, goblin)
while goblin.hp > 0 and hero.hp > 0:
    hero.attack(goblin)
    goblin.attack(hero)
    get_fight_status(hero, goblin)
print("goblin died")
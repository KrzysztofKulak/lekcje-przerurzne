player_1 = {"name": "Player", "hit_points": 10, "damage_output": 2, "is_alive": True}
enemy_1 = {"name": "small goblin", "hit_points": 5, "damage_output": 1, "is_alive": True}


def hit(attacker, target):
    if not attacker["is_alive"]:
        print(attacker["name"] + " cannot attack because they're dead!")
        return
    target["hit_points"] = target["hit_points"] - attacker["damage_output"]
    if target["hit_points"] <= 0:
        print(target["name"] + " has been slained by " + attacker["name"])
        target["is_alive"] = False
    else:
        print(target["name"] + " has been hit by " +
          attacker["name"] + " and has " + str(target["hit_points"]) + " HP left")


hit(player_1, enemy_1)
hit(enemy_1, player_1)
hit(player_1, enemy_1)
hit(enemy_1, player_1)
hit(player_1, enemy_1)
hit(enemy_1, player_1)
print(player_1)
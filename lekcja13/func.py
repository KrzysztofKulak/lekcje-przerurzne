
def tri_field(a, h):
    field = a * h / 2 * 0.39
    return field

tri_0 = {
    "a": 123,
    "h": 12
}
tri_1 = {
    "a": 12,
    "h": 9
}
tri_2 = {
    "a": 14,
    "h": 10
}
tri_3 = {
    "a": 15,
    "h": 16
}

field_tri_0 = tri_field(tri_0["a"], tri_0["h"])
field_tri_1 = tri_field(tri_1["a"], tri_1["h"])
field_tri_2 = tri_field(tri_2["a"], tri_2["h"])

print(field_tri_0, field_tri_1, field_tri_2)


class Triangle:
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def calc_field(self):
        field = self.a * self.h / 2 * 0.39
        return field


tri_0 = Triangle(123, 12)
tri_1 = Triangle(12, 9)
tri_2 = Triangle(14, 10)

field_tri_0 = tri_0.calc_field()
field_tri_1 = tri_1.calc_field()
field_tri_2 = tri_2.calc_field()

print(field_tri_0, field_tri_1, field_tri_2)

print(type(tri_0))
print(type(tri_2))
print(type(1))


class Hero:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp_current = hp
        self.hp_max = hp


class Bed:
    def __init__(self, quality=1.0):
        self.quality = quality

    def provide_sleep(self, hero):
        hero.hp_current += (hero.hp_max - hero.hp_current) * self.quality

hero = Hero(name=None)
bed_in_czerwona_latarnia = Bed(quality=0.5)

hero.hp_current = 50
print(hero.hp_current)
while hero.hp_current != hero.hp_max:
    bed_in_czerwona_latarnia.provide_sleep(hero)
    print(hero.hp_current)
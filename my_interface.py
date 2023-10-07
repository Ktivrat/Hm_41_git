from my_interface import Poison

class PotionInterface:
    def __init__(self):
        self.potions = []

    def create_potion(self, name, cost, ingredients):
        potion = Poison(name, cost, ingredients)
        self.potions.append(potion)

    def delete_potion(self, name):
        self.potions = [potion for potion in self.potions if potion.name != name]

# Интерфейс для создания и удаления зелий
potion_interface = PotionInterface()

potion_interface.create_potion("Целебный отвар", 100, {"подорожник": 5})
potion_interface.create_potion("Приятель", 150, {"Петрушка": 2, "подорожник": 3})
potion_interface.create_potion("Прилив сил", 200, {"Черемух": 4, "Петрушка": 3, "подорожник2_0": 2})

print("Созданные зелья:", [potion.name for potion in potion_interface.potions])
potion_interface.delete_potion("Приятель")
print("Созданные зелья после удаления:", [potion.name for potion in potion_interface.potions])
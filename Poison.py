class Poison:
    def __init__(self, name, cost, ingredients):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients

    def check_description(self, description):
        if description == "Целебный отвар":
            return self.ingredients.get("подорожник", 0) >= 3
        elif description == "Приятель":
            return self.ingredients.get("Петрушка", 0) >= 1 and self.ingredients.get("подорожник", 0) >= 2
        elif description == "Прилив сил":
            return (
                self.ingredients.get("Черемух", 0) >= 3
                and self.ingredients.get("Петрушка", 0) >= 2
                and self.ingredients.get("подорожник", 0) >= 1
            )
        else:
            return False
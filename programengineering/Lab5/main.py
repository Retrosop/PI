class Burger:
    def __init__(self, name="Бургер"):
        self.name = name
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def __str__(self):
        ingredients = ', '.join(self.ingredients)
        return f"{self.name}: {ingredients}"


class BurgerBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        """Сбрасывает состояние строителя, создавая новый объект Burger."""
        self.burger = Burger()

    def set_name(self, name):
        self.burger.name = name
        return self

    def add_lettuce(self):
        self.burger.add_ingredient("Салат")
        return self

    def add_tomato(self):
        self.burger.add_ingredient("Помидор")
        return self

    def add_cheese(self):
        self.burger.add_ingredient("Сыр")
        return self

    def add_patty(self):
        self.burger.add_ingredient("Котлета")
        return self

    def get_burger(self):
        """Возвращает текущий бургер и сбрасывает состояние строителя."""
        burger = self.burger
        self.reset()
        return burger


class BurgerDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_cheeseburger(self):
        """Строит стандартный чизбургер."""
        return (
            self.builder
            .set_name("Чизбургер")
            .add_lettuce()
            .add_tomato()
            .add_cheese()
            .add_patty()
            .get_burger()
        )

    def build_simple_burger(self):
        """Строит простой бургер без сыра."""
        return (
            self.builder
            .set_name("Бургер")
            .add_lettuce()
            .add_tomato()
            .add_patty()
            .get_burger()
        )



if __name__ == "__main__":
    builder = BurgerBuilder()
    director = BurgerDirector(builder)

    cheeseburger = director.build_cheeseburger()
    print(cheeseburger)

    simple_burger = director.build_simple_burger()
    print(simple_burger)

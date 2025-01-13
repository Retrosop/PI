import copy

class GameCharacter:
    def __init__(self, name, health, strength, skills=None):
        self.name = name
        self.health = health
        self.strength = strength
        self.skills = skills if skills else []

    def clone(self):
        """Создает глубокую копию объекта."""
        return copy.deepcopy(self)

    def __str__(self):
        skills = ", ".join(self.skills) if self.skills else "нет навыков"
        return (f"Персонаж: {self.name}, Здоровье: {self.health}, "
                f"Сила: {self.strength}, Навыки: {skills}")



if __name__ == "__main__":
    original_character = GameCharacter(name="Воин", health=100, strength=50, skills=["Меч", "Щит"])
    print("Оригинальный персонаж:")
    print(original_character)

    cloned_character = original_character.clone()
    cloned_character.name = "Клон Воина"
    cloned_character.skills.append("Магия")  

    print("\nКлон персонажа:")
    print(cloned_character)

    print("\nОригинальный персонаж после клонирования:")
    print(original_character)

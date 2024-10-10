# (Л)утченко -> (Л)агман
# (А)ртем -> (А)зу по-татарски

class Ingredient:
    """Класс, описывающий ингредиент."""

    def __init__(self, name: str, raw_weight: float, final_weight: float, cost: float) -> None:
        """Инициализация объекта ингредиента."""
        self.name = name
        self.raw_weight = raw_weight
        self.final_weight = final_weight
        self.cost = cost

    def __repr__(self):
        return f"Ingredient({self.name}, {self.raw_weight}g, {self.final_weight}g, {self.cost}р)"


class Receipt:
    """Класс, описывающий рецепт."""

    def __init__(self, name: str, ingredients_list: list[tuple[str, float, float, float]]) -> None:
        """Инициализация объекта рецепта."""
        self.name = name
        self.ingredients = [Ingredient(*ingredient) for ingredient in ingredients_list]

    def calc_cost(self, portions: int = 1) -> float:
        """Рассчитать общую себестоимость рецепта."""
        total_cost = sum(ingredient.cost for ingredient in self.ingredients)
        return total_cost * portions

    def calc_weight(self, portions: int = 1, raw: bool = True) -> float:
        """Рассчитать общий вес рецепта."""
        if raw:
            total_weight = sum(ingredient.raw_weight for ingredient in self.ingredients)
        else:
            total_weight = sum(ingredient.final_weight for ingredient in self.ingredients)
        return total_weight * portions

    def __str__(self) -> str:
        """Строковое представление рецепта."""
        return f"Рецепт '{self.name}' с {len(self.ingredients)} ингредиентами."


# Проверка работы классов
if __name__ == '__main__':
    # Данные из API для Лагмана
    receipt_from_api = {
        "title": "Лагман",
        "ingredients_list": [
            ('Говядина', 400, 300, 450),
            ('Лапша', 200, 180, 150),
            ('Морковь', 100, 90, 40),
            ('Перец болгарский', 100, 90, 50),
            ('Томат', 100, 80, 30)
        ],
    }

    # Создание объекта рецепта
    receipt = Receipt(receipt_from_api['title'], receipt_from_api['ingredients_list'])

    # Самопроверка методов класса Receipt
    print(receipt)
    print(f"Общий вес сырого продукта: {receipt.calc_weight(raw=True)} г")
    print(f"Общий вес готового продукта: {receipt.calc_weight(raw=False)} г")
    print(f"Общая себестоимость: {receipt.calc_cost()} р")

    # Аналогично можно создать второй рецепт для "Азу по-татарски"
    azu_receipt_data = {
        "title": "Азу по-татарски",
        "ingredients_list": [
            ('Говядина', 400, 300, 500),
            ('Картофель', 300, 270, 70),
            ('Морковь', 150, 130, 50),
            ('Лук', 80, 75, 15),
            ('Томатная паста', 50, 50, 30),
            ('Огурец солёный', 100, 90, 40)
        ],
    }
    azu_receipt = Receipt(azu_receipt_data['title'], azu_receipt_data['ingredients_list'])
    
    # Самопроверка второго рецепта
    print(azu_receipt)
    print(f"Общий вес сырого продукта: {azu_receipt.calc_weight(raw=True)} г")
    print(f"Общий вес готового продукта: {azu_receipt.calc_weight(raw=False)} г")
    print(f"Общая себестоимость: {azu_receipt.calc_cost()} р")

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

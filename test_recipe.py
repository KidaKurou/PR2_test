import unittest
from recipe import Ingredient, Receipt

class TestRecipe(unittest.TestCase):
    """Тесты для классов Ingredient и Receipt."""

    @classmethod
    def setUpClass(cls):
        """Настройка перед всеми тестами."""
        print(">>> Начало тестирования Receipt и Ingredient")
        cls.lagman_data = {
            "title": "Лагман",
            "ingredients_list": [
                ('Говядина', 400, 300, 450),
                ('Лапша', 200, 180, 150),
                ('Морковь', 100, 90, 40),
                ('Перец болгарский', 100, 90, 50),
                ('Томат', 100, 80, 30)
            ],
        }
        cls.azu_data = {
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

    @classmethod
    def tearDownClass(cls):
        """Действия после завершения всех тестов."""
        print(">>> Завершение тестирования Receipt и Ingredient")

    def setUp(self):
        """Настройка перед каждым тестом."""
        self.lagman = Receipt(self.lagman_data['title'], self.lagman_data['ingredients_list'])
        self.azu = Receipt(self.azu_data['title'], self.azu_data['ingredients_list'])

    def tearDown(self):
        """Очистка после каждого теста."""
        self.lagman = None
        self.azu = None

    def test_ingredient_repr(self):
        """Тест метода __repr__ для класса Ingredient."""
        ingredient = Ingredient('Говядина', 400, 300, 450)
        expected_repr = "Ingredient(Говядина, 400g, 300g, 450р)"
        self.assertEqual(repr(ingredient), expected_repr)

    def test_ingredient_initialization(self):
        """Тест инициализации ингредиента."""
        ingredient = Ingredient('Говядина', 400, 300, 450)
        self.assertEqual(ingredient.name, 'Говядина')
        self.assertEqual(ingredient.raw_weight, 400)
        self.assertEqual(ingredient.final_weight, 300)
        self.assertEqual(ingredient.cost, 450)

    # def test_invalid_ingredient(self):
    #     """Тест для обработки неверных данных в ингредиенте."""
    #     with self.assertRaises(ValueError):
    #         Ingredient('Говядина', -400, 300, 450)  # Отрицательный вес должен вызывать ошибку

    def test_ingredient_creation(self):
        """Тест создания ингредиентов."""
        ingredients = [
            ('Говядина', 400, 300, 450),
            ('Лапша', 200, 180, 150),
            ('Морковь', 100, 90, 40)
        ]
        for name, raw_weight, final_weight, cost in ingredients:
            with self.subTest(ingredient=name):
                ingredient = Ingredient(name, raw_weight, final_weight, cost)
                self.assertEqual(ingredient.name, name)
                self.assertEqual(ingredient.raw_weight, raw_weight)
                self.assertEqual(ingredient.final_weight, final_weight)
                self.assertEqual(ingredient.cost, cost)
    
    def test_receipt_initialization_lagman(self):
        """Тест инициализации рецепта 'Лагман'."""
        self.assertEqual(self.lagman.name, 'Лагман')
        self.assertEqual(len(self.lagman.ingredients), 5)

    def test_receipt_cost_calculation_lagman(self):
        """Тест расчёта себестоимости рецепта 'Лагман'."""
        expected_cost = sum([450, 150, 40, 50, 30])  # Сумма стоимости всех ингредиентов
        self.assertEqual(self.lagman.calc_cost(), expected_cost)

    def test_receipt_weight_calculation_raw_lagman(self):
        """Тест расчёта веса сырого продукта рецепта 'Лагман'."""
        expected_raw_weight = sum([400, 200, 100, 100, 100])  # Сумма сырого веса всех ингредиентов
        self.assertEqual(self.lagman.calc_weight(raw=True), expected_raw_weight)

    def test_receipt_weight_calculation_final_lagman(self):
        """Тест расчёта веса готового продукта рецепта 'Лагман'."""
        expected_final_weight = sum([300, 180, 90, 90, 80])  # Сумма готового веса всех ингредиентов
        self.assertEqual(self.lagman.calc_weight(raw=False), expected_final_weight)

    def test_receipt_initialization_azu(self):
        """Тест инициализации рецепта 'Азу по-татарски'."""
        self.assertEqual(self.azu.name, 'Азу по-татарски')
        self.assertEqual(len(self.azu.ingredients), 6)

    def test_receipt_cost_calculation_azu(self):
        """Тест расчёта себестоимости рецепта 'Азу по-татарски'."""
        expected_cost = sum([500, 70, 50, 15, 30, 40])  # Сумма стоимости всех ингредиентов
        self.assertEqual(self.azu.calc_cost(), expected_cost)

    def test_receipt_weight_calculation_raw_azu(self):
        """Тест расчёта веса сырого продукта рецепта 'Азу по-татарски'."""
        expected_raw_weight = sum([400, 300, 150, 80, 50, 100])  # Сумма сырого веса всех ингредиентов
        self.assertEqual(self.azu.calc_weight(raw=True), expected_raw_weight)

    def test_receipt_weight_calculation_final_azu(self):
        """Тест расчёта веса готового продукта рецепта 'Азу по-татарски'."""
        expected_final_weight = sum([300, 270, 130, 75, 50, 90])  # Сумма готового веса всех ингредиентов
        self.assertEqual(self.azu.calc_weight(raw=False), expected_final_weight)

    def test_str_method(self):
        """Тест строкового представления рецепта."""
        self.assertEqual(str(self.lagman), "Рецепт 'Лагман' с 5 ингредиентами.")
        self.assertEqual(str(self.azu), "Рецепт 'Азу по-татарски' с 6 ингредиентами.")


if __name__ == '__main__':
    unittest.main()

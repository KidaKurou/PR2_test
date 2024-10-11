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
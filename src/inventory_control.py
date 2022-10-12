class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.current_inventory = self.MINIMUM_INVENTORY.copy()
        self.orders = []

    def add_new_order(self, customer, order, day):
        dish_ingredients = self.INGREDIENTS[order]
        for item in dish_ingredients:
            if self.current_inventory[item] == 0:
                return False
        for item in dish_ingredients:
            self.current_inventory[item] -= 1
        self.orders.append({
            "name": customer,
            "dish": order,
            "weekday": day,
        })

    def get_quantities_to_buy(self):
        quantities_to_buy = {}
        # https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/
        for key, value in self.current_inventory.items():
            quantities_to_buy[key] = self.MINIMUM_INVENTORY[key] - value

        return quantities_to_buy

    def get_available_dishes(self):
        available_dishes = set()
        missing_elements = list()

        for dish, ingredients in self.INGREDIENTS.items():
            for ingredient in ingredients:
                if self.current_inventory[ingredient] == 0:
                    missing_elements.append(ingredient)
            if len(missing_elements) == 0:
                available_dishes.add(dish)
            missing_elements = []
        return available_dishes

import unittest
import os
import json
from FinalProject import Fragrance, FragranceManager, ShoppingList, ShoppingListManager

class TestFragranceManager(unittest.TestCase):
    def setUp(self):
        self.manager = FragranceManager()
        self.fragrance = Fragrance("Lavender", 2021, "Spring", "I Like This One")
        self.manager.add_fragrance(self.fragrance)

    def test_add_fragrance(self):
        self.assertEqual(len(self.manager.fragrances), 1)
        self.assertEqual(self.manager.fragrances[0].name, "Lavender")

    def test_remove_fragrance(self):
        self.manager.remove_fragrance("Lavender")
        self.assertEqual(len(self.manager.fragrances), 0)

    def test_remove_non_existent_fragrance(self):
        self.manager.remove_fragrance("NonExistent")
        self.assertEqual(len(self.manager.fragrances), 1)

    def test_update_status(self):
        self.manager.update_status("Lavender", "SHOPPING LIST")
        self.assertEqual(self.manager.fragrances[0].status, "SHOPPING LIST")

    def test_update_status_non_existent_fragrance(self):
        self.manager.update_status("NonExistent", "SHOPPING LIST")
        self.assertEqual(self.manager.fragrances[0].status, "I Like This One")

    def test_save_and_load_from_json(self):
        filename = "test_fragrances.json"
        self.manager.save_to_json(filename)
        new_manager = FragranceManager.load_from_json(filename)
        self.assertEqual(len(new_manager.fragrances), 1)
        self.assertEqual(new_manager.fragrances[0].name, "Lavender")
        os.remove(filename)

class TestShoppingListManager(unittest.TestCase):
    def setUp(self):
        self.manager = ShoppingListManager()
        self.shopping_list = ShoppingList("Christmas List", 2023, "Holiday", ["Candle", "Soap"])
        self.manager.shopping_lists.append(self.shopping_list)

    def test_create_list(self):
        self.manager.create_list("Birthday List", 2023, "Birthday", ["Perfume", "Lotion"])
        self.assertEqual(len(self.manager.shopping_lists), 2)
        self.assertEqual(self.manager.shopping_lists[1].name, "Birthday List")

    def test_edit_list(self):
        self.manager.edit_list("Christmas List", new_items=["Candle", "Soap", "Diffuser"])
        self.assertEqual(self.manager.shopping_lists[0].items, ["Candle", "Soap", "Diffuser"])

    def test_edit_non_existent_list(self):
        self.manager.edit_list("NonExistent", new_items=["Candle", "Soap", "Diffuser"])
        self.assertEqual(self.manager.shopping_lists[0].items, ["Candle", "Soap"])

    def test_export_list(self):
        self.assertTrue(self.manager.export_list("Christmas List", "christmas_list.txt"))
        with open("christmas_list.txt", "r") as f:
            content = f.read()
        self.assertEqual(content, "Candle\nSoap\n")
        os.remove("christmas_list.txt")

    def test_export_non_existent_list(self):
        self.assertFalse(self.manager.export_list("NonExistent", "non_existent.txt"))

    def test_save_and_load_from_json(self):
        filename = "test_shopping_lists.json"
        self.manager.save_to_json(filename)
        new_manager = ShoppingListManager.load_from_json(filename)
        self.assertEqual(len(new_manager.shopping_lists), 1)
        self.assertEqual(new_manager.shopping_lists[0].name, "Christmas List")
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()
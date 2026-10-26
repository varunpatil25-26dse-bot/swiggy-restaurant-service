import unittest
from restaurant_service import search_restaurants


class TestRestaurantSearch(unittest.TestCase):

    def test_search_by_name(self):
        results = search_restaurants(query="Truffles")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Truffles")

    def test_search_by_cuisine(self):
        results = search_restaurants(query="South Indian")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "A2B - Adyar Ananda Bhavan")

    def test_veg_filter(self):
        results = search_restaurants(veg_only=True)
        self.assertTrue(all(r["is_veg"] for r in results))

    def test_min_rating_filter(self):
        results = search_restaurants(min_rating=4.3)
        self.assertTrue(all(r["rating"] >= 4.3 for r in results))


if __name__ == "__main__":
    unittest.main()

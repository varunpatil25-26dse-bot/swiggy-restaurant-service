RESTAURANT_CATALOG = [
    {
        "id": 1,
        "name": "Meghana Foods",
        "cuisine": ["Biryani", "Andhra"],
        "rating": 4.5,
        "is_veg": False,
    },
    {
        "id": 2,
        "name": "A2B - Adyar Ananda Bhavan",
        "cuisine": ["South Indian", "Sweets"],
        "rating": 4.2,
        "is_veg": True,
    },
    {
        "id": 3,
        "name": "Truffles",
        "cuisine": ["Burgers", "American"],
        "rating": 4.4,
        "is_veg": False,
    },
    {
        "id": 4,
        "name": "Bikanervala",
        "cuisine": ["North Indian", "Street Food"],
        "rating": 4.0,
        "is_veg": True,
    },
]


def search_restaurants(
    query: str = "", min_rating: float = 0.0, veg_only: bool = False
) -> list:
    """Searches restaurants by keyword (name or cuisine) and applies filters."""
    query = query.strip().lower()
    results = []

    for r in RESTAURANT_CATALOG:
        # Match name or cuisine
        name_match = query in r["name"].lower()
        cuisine_match = any(query in c.lower() for c in r["cuisine"])

        # Filter criteria
        passes_query = (not query) or name_match or cuisine_match
        passes_rating = r["rating"] >= min_rating
        passes_veg = (not veg_only) or r["is_veg"]

        if passes_query and passes_rating and passes_veg:
            results.append(r)

    return results


if __name__ == "__main__":
    print("Searching for Biryani:")
    print(search_restaurants(query="biryani"))
    print("\nSearching Pure-Veg with rating >= 4.0:")
    print(search_restaurants(veg_only=True, min_rating=4.0))

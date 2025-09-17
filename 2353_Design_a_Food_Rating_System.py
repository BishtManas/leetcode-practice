import heapq
from collections import defaultdict

class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_to_heap = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating
            heapq.heappush(self.cuisine_to_heap[cuisine], (-rating, food))

    def changeRating(self, food, newRating):
        self.food_to_rating[food] = newRating
        cuisine = self.food_to_cuisine[food]
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        heap = self.cuisine_to_heap[cuisine]
        while True:
            rating, food = heap[0]
            if -rating == self.food_to_rating[food]:
                return food
            heapq.heappop(heap)

# --- Example Test Case (same as LeetCode sample) ---
if __name__ == "__main__":
    foodRatings = FoodRatings(
        ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
        ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
        [9, 12, 8, 15, 14, 7]
    )

    print(foodRatings.highestRated("korean"))    # Output: "kimchi"
    print(foodRatings.highestRated("japanese"))  # Output: "ramen"
    foodRatings.changeRating("sushi", 16)
    print(foodRatings.highestRated("japanese"))  # Output: "sushi"
    foodRatings.changeRating("ramen", 16)
    print(foodRatings.highestRated("japanese"))  # Output: "ramen"

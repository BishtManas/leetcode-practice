from collections import defaultdict
from sortedcontainers import SortedList
from typing import List


class MovieRentingSystem:
    """
    Implements a movie rental system with efficient search, rent, drop, and report functionalities.
    """

    def __init__(self, n: int, entries: List[List[int]]):
        """
        Initializes the data structures.
        - self.prices: For O(1) price lookup of a movie at a shop.
        - self.unrented_movies: Stores available copies, sorted by price then shop.
        - self.rented_movies: Stores rented movies, sorted by price, shop, then movie.
        """
        # Structure: {shop: {movie: price}}
        self.prices = defaultdict(dict)

        # Structure: {movie: SortedList[(price, shop)]}
        self.unrented_movies = defaultdict(SortedList)

        # Structure: SortedList[(price, shop, movie)]
        self.rented_movies = SortedList()

        for shop, movie, price in entries:
            self.prices[shop][movie] = price
            self.unrented_movies[movie].add((price, shop))

    def search(self, movie: int) -> List[int]:
        """
        Finds the 5 cheapest shops that have an unrented copy of a given movie.
        Time Complexity: O(log K), where K is the number of unrented copies for the movie.
        """
        if movie not in self.unrented_movies:
            return []

        # Get the sorted list of available copies.
        available_copies = self.unrented_movies[movie]

        # Take the first 5 cheapest copies and extract their shop IDs.
        cheapest_shops = [shop for price, shop in available_copies[:5]]

        return cheapest_shops

    def rent(self, shop: int, movie: int) -> None:
        """
        Rents a movie, moving it from the unrented collection to the rented collection.
        Time Complexity: O(log K + log R), where K is unrented copies and R is total rented.
        """
        price = self.prices[shop][movie]

        # Remove from unrented collection.
        self.unrented_movies[movie].remove((price, shop))

        # Add to rented collection.
        self.rented_movies.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        """
        Drops off a movie, moving it from the rented collection back to the unrented one.
        Time Complexity: O(log R + log K).
        """
        price = self.prices[shop][movie]

        # Remove from rented collection.
        self.rented_movies.remove((price, shop, movie))

        # Add back to unrented collection.
        self.unrented_movies[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        """
        Returns the 5 cheapest rented movies.
        Time Complexity: O(1), as we only access the first 5 elements.
        """
        # Take the first 5 cheapest from the sorted list of rented movies.
        cheapest_rented = self.rented_movies[:5]

        # Format the output as [[shop, movie], ...].
        return [[shop, movie] for price, shop, movie in cheapest_rented]


if __name__ == "__main__":
    # Example usage
    entries = [
        [0, 1, 5],
        [0, 2, 6],
        [0, 3, 7],
        [1, 1, 4],
        [2, 1, 5]
    ]

    obj = MovieRentingSystem(3, entries)

    print("Search movie 1:", obj.search(1))  # [1, 0, 2]
    obj.rent(0, 1)
    obj.rent(1, 1)
    print("Report:", obj.report())  # [[1, 1], [0, 1]]
    obj.drop(1, 1)
    print("Report after drop:", obj.report())  # [[0, 1]]

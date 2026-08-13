"""Command-line entry point for the media tracker."""

from models import Media




from models import Book, Movie, Game

book = Book(
    "The Hobbit",
    status="finished",
    rating=5,
    pages=310,
    author="J. R. R. Tolkien"
)

movie = Movie(
    "Inception",
    status="watched",
    rating=4,
    runtime_minutes=148,
    director="Christopher Nolan"
)

game = Game(
    "Minecraft",
    status="in-progress",
    rating=5,
    hours_played=42,
    platform="PC"
)

print(book)
print()
print(movie)
print()
print(game)
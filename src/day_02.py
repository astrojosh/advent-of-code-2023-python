"""Module for implementing the solution to the problem set on day 2."""

import math
import operator
from dataclasses import dataclass
from enum import Enum
from functools import partial, reduce
from typing import Iterator, Self


@dataclass
class Cube:
    max_amount: int


class Cubes(Enum):
    RED = Cube(max_amount=12)
    GREEN = Cube(max_amount=13)
    BLUE = Cube(max_amount=14)


@dataclass
class CubeCollection:
    cube: Cube
    amount: int

    def __post_init__(self) -> None:
        self.possible = self.amount <= self.cube.max_amount

    @classmethod
    def from_string(cls, string: str) -> Self:
        amount, colour = string.split(" ")
        cube = Cubes[colour.upper()].value
        return cls(cube, int(amount))


@dataclass
class Set:
    cube_collections: list[CubeCollection]

    def __post_init__(self) -> None:
        self.possible = int(all(cube.possible for cube in self.cube_collections))

    @classmethod
    def from_string(cls, string: str) -> Self:
        return cls([CubeCollection.from_string(cube) for cube in string.split(", ")])


@dataclass
class Game:
    number: int
    sets: list[Set]

    def __post_init__(self) -> None:
        self.possible = int(all(set.possible for set in self.sets))
        nested_cube_collections = (set.cube_collections for set in self.sets)
        self.cube_collections = reduce(operator.add, nested_cube_collections)

    @classmethod
    def from_string(cls, string: str) -> Self:
        info, game = string.split(": ")
        number = int(info.split(" ")[1])
        sets = [Set.from_string(set) for set in game.split("; ")]
        return cls(number, sets)

    @staticmethod
    def filter_cube_to_colour(
        coloured_cube: Cube, cube_collection: CubeCollection
    ) -> Iterator[CubeCollection]:
        if cube_collection.cube is coloured_cube:
            yield cube_collection

    def filter_cubes_to_colour(self, coloured_cube: Cube) -> Iterator[CubeCollection]:
        filter_cube_to_colour = partial(self.filter_cube_to_colour, coloured_cube)
        for cube_collection in self.cube_collections:
            yield from filter_cube_to_colour(cube_collection)

    def max_amount(self, coloured_cube: Cube) -> int:
        cube_collections = self.filter_cubes_to_colour(coloured_cube)
        return max(cube_collection.amount for cube_collection in cube_collections)

    @property
    def power(self) -> int:
        return math.prod(self.max_amount(cube.value) for cube in Cubes)


def create_games(input_data: str) -> list[Game]:
    return [Game.from_string(game) for game in input_data.splitlines()]


def part_1_answer(input_data: str) -> int:
    games = create_games(input_data)
    return sum(game.number * game.possible for game in games)


def part_2_answer(input_data: str) -> int:
    games = create_games(input_data)
    return sum(game.power for game in games)

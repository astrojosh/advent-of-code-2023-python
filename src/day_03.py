"""Module for implementing the solution to the problem set on day 3."""

import math
import re
from dataclasses import dataclass
from typing import Iterator, Self


@dataclass
class Number:
    number: int

    def __hash__(self) -> int:
        return id(self)


Element = Number | str | None


@dataclass
class Symbol:
    gear: bool
    adjacent_elements: set[Element]

    @property
    def adjacent_numbers(self) -> list[int]:
        return [
            adjacent_element.number
            for adjacent_element in self.adjacent_elements
            if isinstance(adjacent_element, Number)
        ]

    @property
    def part_number(self) -> int:
        return sum(self.adjacent_numbers)

    @property
    def gear_ratio(self) -> int:
        if self.gear and len(self.adjacent_numbers) == 2:
            return math.prod(self.adjacent_numbers)
        return 0


@dataclass
class Grid:
    grid: list[list[Element]]

    @classmethod
    def from_string(cls, input_data: str) -> Self:
        return cls([cls.process_line(line) for line in input_data.splitlines()])

    @staticmethod
    def process_string(string: str) -> Iterator[Element]:
        if len(string) == 0:
            return

        if string == ".":
            yield None
            return

        if not string.isdigit():
            yield string
            return

        number = Number(int(string))
        for _ in string:
            yield number

    @classmethod
    def process_line(cls, line: str) -> list[Element]:
        split_line = re.split("([^0-9])", line)
        return [
            processed_string
            for string in split_line
            for processed_string in cls.process_string(string)
        ]

    def process_symbol(
        self, element: Element, row_index: int, column_index: int
    ) -> Symbol:
        gear = element == "*"

        adjacent_indices = [
            (row_index - 1, column_index - 1),
            (row_index - 1, column_index),
            (row_index - 1, column_index + 1),
            (row_index, column_index - 1),
            (row_index, column_index + 1),
            (row_index + 1, column_index - 1),
            (row_index + 1, column_index),
            (row_index + 1, column_index + 1),
        ]

        adjacent_elements = {
            self.grid[adjacent_row_index][adjacent_column_index]
            for adjacent_row_index, adjacent_column_index in adjacent_indices
        }

        return Symbol(gear, adjacent_elements)

    @property
    def symbols(self) -> list[Symbol]:
        return [
            self.process_symbol(element, row_index, column_index)
            for row_index, row in enumerate(self.grid)
            for column_index, element in enumerate(row)
            if isinstance(element, str)
        ]


def part_1_answer(input_data: str) -> int:
    grid = Grid.from_string(input_data)
    return sum(symbol.part_number for symbol in grid.symbols)


def part_2_answer(input_data: str) -> int:
    grid = Grid.from_string(input_data)
    return sum(symbol.gear_ratio for symbol in grid.symbols)

"""Module for implementing the solution to the problem set on day 4."""

from dataclasses import dataclass
from functools import cached_property
from typing import Self


@dataclass
class Card:
    id: int
    numbers: list[int]
    winning_numbers: list[int]

    def __post_init__(self) -> None:
        self.winning_cards: list[Self] | None = None

    @classmethod
    def from_line(cls, line: str) -> Self:
        card_info, number_info = line.split(": ")
        card_id = int(card_info.split(" ")[-1])
        number_strings = number_info.split(" | ")
        numbers, winning_numbers = [
            cls.process_number_string(number_string) for number_string in number_strings
        ]
        return cls(card_id, numbers, winning_numbers)

    @staticmethod
    def process_number_string(numbers: str) -> list[int]:
        return [int(number) for number in numbers.split(" ") if number]

    @property
    def matching_numbers(self) -> list[int]:
        return [number for number in self.numbers if number in self.winning_numbers]

    @property
    def num_matches(self) -> int:
        return len(self.matching_numbers)

    @property
    def score(self) -> int:
        if self.num_matches == 0:
            return 0
        return 2 ** (self.num_matches - 1)

    @property
    def winning_card_ids(self) -> list[int]:
        return [self.id + i + 1 for i in range(self.num_matches)]

    def calculate_winning_cards(self, cards: list[Self]) -> None:
        self.winning_cards = [cards[card_id - 1] for card_id in self.winning_card_ids]

    @cached_property
    def num_winning_cards(self) -> int:
        if self.winning_cards is None:
            raise ValueError
        nested_matches = sum(card.num_winning_cards for card in self.winning_cards)
        return self.num_matches + nested_matches


def part_1_answer(input_data: str) -> int:
    cards = (Card.from_line(line) for line in input_data.splitlines())
    return sum(card.score for card in cards)


def part_2_answer(input_data: str) -> int:
    cards = [Card.from_line(line) for line in input_data.splitlines()]
    for card in cards:
        card.calculate_winning_cards(cards)
    return sum(1 + card.num_winning_cards for card in cards)

"""Module for implementing the solution to the problem set on day 6."""

import math
import re


def process_digits(digits: list[str], combine_digits: bool) -> list[int]:
    if combine_digits:
        digits = ["".join(digit for digit in digits)]
    return [int(digit) for digit in digits]


def winning_races(time: int, distance: int) -> int:
    discriminant = math.sqrt(time**2 - 4 * distance)
    least_time = math.floor((time - discriminant) / 2 + 1)
    most_time = math.ceil((time + discriminant) / 2 - 1)
    return most_time - least_time + 1


def total_winning_races(input_data: str, combine_digits: bool = False) -> int:
    digits = [re.findall("[0-9]+", line) for line in input_data.splitlines()]
    processed_digits = [process_digits(digit, combine_digits) for digit in digits]
    races_won = [winning_races(*race_params) for race_params in zip(*processed_digits)]
    return math.prod(races_won)


def part_1_answer(input_data: str) -> int:
    return total_winning_races(input_data)


def part_2_answer(input_data: str) -> int:
    return total_winning_races(input_data, combine_digits=True)

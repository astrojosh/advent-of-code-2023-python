"""Module for implementing the solution to the problem set on day 1."""

DIGIT_NAMES = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def remove_letters(string: str) -> str:
    return "".join(character for character in string if not character.isalpha())


def calculate_digit_sum(input_data: str) -> int:
    digits = [remove_letters(line) for line in input_data.splitlines()]
    first_and_last_digits = [int(digit[0] + digit[-1]) for digit in digits]
    return sum(first_and_last_digits)


def convert_digit_names(input_data: str) -> str:
    processed_input = input_data

    for digit, digit_name in enumerate(DIGIT_NAMES):
        replace_text = digit_name + str(digit) + digit_name
        processed_input = processed_input.replace(digit_name, replace_text)

    return processed_input


def part_1_answer(input_data: str) -> int:
    return calculate_digit_sum(input_data)


def part_2_answer(input_data: str) -> int:
    processed_input = convert_digit_names(input_data)
    return calculate_digit_sum(processed_input)

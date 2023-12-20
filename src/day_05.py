"""Module for implementing the solution to the problem set on day 5."""

from dataclasses import dataclass
from functools import partial
from typing import Self


@dataclass
class Range:
    start: int
    end: int
    offset: int

    @classmethod
    def from_string(cls, string: str) -> Self:
        destination_start, source_start, range_length = string.split(" ")
        start = int(source_start)
        end = start + int(range_length) - 1
        offset = int(destination_start) - start
        return cls(start, end, offset)

    def inverse(self) -> Self:
        destination_start = self.start + self.offset
        destination_end = self.end + self.offset
        return self.__class__(destination_start, destination_end, -self.offset)


@dataclass
class Mapping:
    ranges: list[Range]

    @classmethod
    def from_strings(cls, range_strings: list[str]) -> Self:
        return cls([Range.from_string(range_string) for range_string in range_strings])

    def map_number(self, input_number: int) -> int:
        for mapping_range in self.ranges:
            if mapping_range.start <= input_number <= mapping_range.end:
                return input_number + mapping_range.offset
        return input_number

    def inverse(self) -> Self:
        inverse_ranges = [mapping_range.inverse() for mapping_range in self.ranges]
        return self.__class__(inverse_ranges)

    @property
    def critical_points(self) -> list[int]:
        return [
            critical_point
            for mapping_range in self.ranges
            for critical_point in (mapping_range.start, mapping_range.end)
        ]


@dataclass
class Almanac:
    mappings: list[Mapping]
    seeds: list[int]

    @classmethod
    def from_string(cls, input_data: str, seed_range: bool = False) -> Self:
        seeds_string, *mappings_strings = input_data.split("\n\n")
        mapping_range_strings = (
            mapping_strings.splitlines()[1:] for mapping_strings in mappings_strings
        )

        mappings = [
            Mapping.from_strings(range_strings)
            for range_strings in mapping_range_strings
        ]
        seeds = cls.process_seeds(mappings, seeds_string, seed_range)
        return cls(mappings, seeds)

    @classmethod
    def process_seeds(
        cls, mappings: list[Mapping], seeds_string: str, seed_range: bool
    ) -> list[int]:
        seeds = [int(seed) for seed in seeds_string.split(" ")[1:]]

        if not seed_range:
            return seeds

        seed_ranges = [
            (start, start + seed_range - 1)
            for start, seed_range in zip(seeds[::2], seeds[1::2])
        ]

        inverse_mappings = [mapping.inverse() for mapping in reversed(mappings)]
        _map_back_to_seed = partial(cls.map_back_to_seed, inverse_mappings)

        critical_mapping_points = [
            _map_back_to_seed(critical_point, mapping_layer)
            for mapping_layer, mapping in enumerate(mappings)
            for critical_point in mapping.critical_points
        ]

        critical_points = seeds + critical_mapping_points

        seeds = [
            seed
            for seed in critical_points
            for seed_start, seed_end in seed_ranges
            if seed_start <= seed <= seed_end
        ]

        return seeds

    @staticmethod
    def map_seed_to_location(mappings: list[Mapping], seed: int) -> int:
        for mapping in mappings:
            seed = mapping.map_number(seed)
        return seed

    @classmethod
    def map_back_to_seed(
        cls, inverse_mappings: list[Mapping], seed: int, mapping_layer: int
    ) -> int:
        return cls.map_seed_to_location(inverse_mappings[-mapping_layer:], seed)

    @property
    def critical_locations(self) -> list[int]:
        return [self.map_seed_to_location(self.mappings, seed) for seed in self.seeds]

    @property
    def closest_location(self) -> int:
        return min(self.critical_locations)


def part_1_answer(input_data: str) -> int:
    almanac = Almanac.from_string(input_data)
    return almanac.closest_location


def part_2_answer(input_data: str) -> int:
    almanac = Almanac.from_string(input_data, seed_range=True)
    return almanac.closest_location

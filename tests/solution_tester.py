"""Module for defining the structure of the tests of the solutions to the problems."""

import importlib
import os
from abc import ABC, abstractmethod
from types import ModuleType
from typing import Any


class SolutionTester(ABC):
    """Abstract base class for defining the structure of the tests of the
    solutions to the problems.

    Attributes
    ----------
    day: str
        The day of the problem.

    module: ModuleType
        The module containing the solution to the problem set on that day.

    example_input_data: str
        The example input data if it is used in both parts of the problem.

    example_part_1_input: str
        The example input data for part 1 of the problem.

    example_part_2_input: str
        The example input data for part 2 of the problem.

    input_data: str
        The input data if it is used in both parts of the problem.

    part_1_input: str
        The input data for part 1 of the problem.

    part_2_input: str
        The input data for part 2 of the problem.

    example_part_1_output: Any
        The solution to the example part 1 of the problem.

    part_1_output: Any
        The solution to part 1 of the problem.

    example_part_2_output: Any
        The solution to the example part 2 of the problem.

    part_2_output: Any
        The solution to part 2 of the problem.
    """

    @property
    @abstractmethod
    def day(self) -> str:
        """The day of the problem.

        Abstract method to be defined in implementations of this class.

        Returns
        -------
        str: The day of the problem.
        """

    @property
    def module(self) -> ModuleType:
        """The module containing the solution to the problem set on that day.

        Returns
        -------
        ModuleType: The module containing the solution to the problem set on that day.
        """
        return importlib.import_module(f"src.{self.day}")

    def file_path(self, file_name: str) -> str:
        """The file path of the data with the associated file name.

        Parameters
        ----------
        file_name: str
            The file name of the data.

        Returns
        -------
        str: The file path of the data with the associated file name.
        """
        return f"data/{self.day}/{file_name}.txt"

    def load_data(self, file_name: str) -> str:
        """Loads in the data from the file.

        Parameters
        ----------
        file_name: str
            The file name of the data.

        Returns
        -------
        str: The data in the file.
        """
        with open(self.file_path(file_name), encoding="utf-8") as f:
            data = f.read()
        return data.rstrip()

    def file_exists(self, file_name: str) -> bool:
        """Checks if the file name exists.

        Parameters
        ----------
        file_name: str
            The file name of the data.

        Returns
        -------
        bool: True if the file name exists, False if not.
        """
        return os.path.isfile(self.file_path(file_name))

    @property
    def example_input_data(self) -> str:
        """The example input data if it is used in both parts of the problem.

        Returns
        -------
        str: The example input data if it is used in both parts of the problem.
        """
        return self.load_data("example_input")

    @property
    def example_part_1_input(self) -> str:
        """The example input data for part 1 of the problem.

        Returns
        -------
        str: The example input data for part 1 of the problem.
        """
        if self.file_exists("example_part_1_input"):
            return self.load_data("example_part_1_input")
        return self.example_input_data

    @property
    def example_part_2_input(self) -> str:
        """The example input data for part 2 of the problem.

        Returns
        -------
        str: The example input data for part 2 of the problem.
        """
        if self.file_exists("example_part_2_input"):
            return self.load_data("example_part_2_input")
        return self.example_input_data

    @property
    def input_data(self) -> str:
        """The input data if it is used in both parts of the problem.

        Returns
        -------
        str: The input data if it is used in both parts of the problem.
        """
        return self.load_data("input")

    @property
    def part_1_input(self) -> str:
        """The input data for part 1 of the problem.

        Returns
        -------
        str: The input data for part 1 of the problem.
        """
        if self.file_exists("part_1_input"):
            return self.load_data("part_1_input")
        return self.input_data

    @property
    def part_2_input(self) -> str:
        """The input data for part 2 of the problem.

        Returns
        -------
        str: The input data for part 2 of the problem.
        """
        if self.file_exists("part_2_input"):
            return self.load_data("part_2_input")
        return self.input_data

    @property
    def example_part_1_output(self) -> Any:
        """The solution to the example part 1 of the problem.

        Returns
        -------
        Any: The solution to the example part 1 of the problem.
        """
        return self.module.part_1_answer(self.example_part_1_input)

    @property
    def part_1_output(self) -> Any:
        """The solution to part 1 of the problem.

        Returns
        -------
        Any: The solution to part 1 of the problem.
        """
        return self.module.part_1_answer(self.part_1_input)

    @property
    def example_part_2_output(self) -> Any:
        """The solution to the example part 2 of the problem.

        Returns
        -------
        Any: The solution to the example part 2 of the problem.
        """
        return self.module.part_2_answer(self.example_part_2_input)

    @property
    def part_2_output(self) -> Any:
        """The solution to part 2 of the problem.

        Returns
        -------
        Any: The solution to part 2 of the problem.
        """
        return self.module.part_2_answer(self.part_2_input)

    @abstractmethod
    def test_example_part_1(self) -> None:
        """Tests that the solution to the example part 1 of the problem
        matches the expected output.

        Abstract method to be defined in implementations of this class.

        Returns
        -------
        None
        """

    @abstractmethod
    def test_part_1(self) -> None:
        """Tests that the solution to part 1 of the problem matches the
        expected output.

        Abstract method to be defined in implementations of this class.

        Returns
        -------
        None
        """

    @abstractmethod
    def test_example_part_2(self) -> None:
        """Tests that the solution to the example part 2 of the problem
        matches the expected output.

        Abstract method to be defined in implementations of this class.

        Returns
        -------
        None
        """

    @abstractmethod
    def test_part_2(self) -> None:
        """Tests that the solution to part 2 of the problem matches the
        expected output.

        Abstract method to be defined in implementations of this class.

        Returns
        -------
        None
        """

    @classmethod
    def display_outputs(cls) -> None:
        """Displays the solutions to all parts of the problem.

        Returns
        -------
        None
        """
        solutions = cls()
        print("Part 1:")
        print((solutions.example_part_1_output, solutions.part_1_output))
        print("\nPart 2:")
        print((solutions.example_part_2_output, solutions.part_2_output))

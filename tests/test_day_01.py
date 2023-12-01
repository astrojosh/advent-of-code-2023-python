"""Module for testing the solution to the problem set on day 1."""

from .solution_tester import SolutionTester


class TestDay01(SolutionTester):
    """Class for testing the solution to the problem set on day 1."""

    @property
    def day(self) -> str:
        return "day_01"

    def test_example_part_1(self) -> None:
        assert self.example_part_1_output == 142

    def test_part_1(self) -> None:
        assert self.part_1_output == 54877

    def test_example_part_2(self) -> None:
        assert self.example_part_2_output == 281

    def test_part_2(self) -> None:
        assert self.part_2_output == 54100


if __name__ == "__main__":
    TestDay01.display_outputs()

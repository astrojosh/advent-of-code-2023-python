"""Module for testing the solution to the problem set on day 4."""

from .solution_tester import SolutionTester


class TestDay04(SolutionTester):
    """Class for testing the solution to the problem set on day 4."""

    @property
    def day(self) -> str:
        return "day_04"

    def test_example_part_1(self) -> None:
        assert self.example_part_1_output == 13

    def test_part_1(self) -> None:
        assert self.part_1_output == 18653

    def test_example_part_2(self) -> None:
        assert self.example_part_2_output == 30

    def test_part_2(self) -> None:
        assert self.part_2_output == 5921508


if __name__ == "__main__":
    TestDay04.display_outputs()

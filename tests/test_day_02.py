"""Module for testing the solution to the problem set on day 2."""

from .solution_tester import SolutionTester


class TestDay02(SolutionTester):
    """Class for testing the solution to the problem set on day 2."""

    @property
    def day(self) -> str:
        return "day_02"

    def test_example_part_1(self) -> None:
        assert self.example_part_1_output == 8

    def test_part_1(self) -> None:
        assert self.part_1_output == 2149

    def test_example_part_2(self) -> None:
        assert self.example_part_2_output == 2286

    def test_part_2(self) -> None:
        assert self.part_2_output == 71274


if __name__ == "__main__":
    TestDay02.display_outputs()

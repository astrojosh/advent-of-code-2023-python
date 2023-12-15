"""Module for testing the solution to the problem set on day 3."""

from .solution_tester import SolutionTester


class TestDay03(SolutionTester):
    """Class for testing the solution to the problem set on day 3."""

    @property
    def day(self) -> str:
        return "day_03"

    def test_example_part_1(self) -> None:
        assert self.example_part_1_output == 4361

    def test_part_1(self) -> None:
        assert self.part_1_output == 527446

    def test_example_part_2(self) -> None:
        assert self.example_part_2_output == 467835

    def test_part_2(self) -> None:
        assert self.part_2_output == 73201705


if __name__ == "__main__":
    TestDay03.display_outputs()

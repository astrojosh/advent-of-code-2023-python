"""Module for testing the solution to the problem set on day 6."""

from .solution_tester import SolutionTester


class TestDay06(SolutionTester):
    """Class for testing the solution to the problem set on day 6."""

    @property
    def day(self) -> str:
        return "day_06"

    def test_example_part_1(self) -> None:
        assert self.example_part_1_output == 288

    def test_part_1(self) -> None:
        assert self.part_1_output == 281600

    def test_example_part_2(self) -> None:
        assert self.example_part_2_output == 71503

    def test_part_2(self) -> None:
        assert self.part_2_output == 33875953


if __name__ == "__main__":
    TestDay06.display_outputs()

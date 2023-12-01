"""Module for testing the solution to the problem set on day x."""

from .solution_tester import SolutionTester


class TestDayX(SolutionTester):
    """Class for testing the solution to the problem set on day x."""

    @property
    def day(self) -> str:
        return "day_x"

    def test_example_part_1(self) -> None:
        assert self.example_part_1_output == 0

    def test_part_1(self) -> None:
        assert self.part_1_output == 0

    def test_example_part_2(self) -> None:
        assert self.example_part_2_output == 0

    def test_part_2(self) -> None:
        assert self.part_2_output == 0


if __name__ == "__main__":
    TestDayX.display_outputs()

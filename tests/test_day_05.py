"""Module for testing the solution to the problem set on day 5."""

from .solution_tester import SolutionTester


class TestDay05(SolutionTester):
    """Class for testing the solution to the problem set on day 5."""

    @property
    def day(self) -> str:
        return "day_05"

    def test_example_part_1(self) -> None:
        assert self.example_part_1_output == 35

    def test_part_1(self) -> None:
        assert self.part_1_output == 825516882

    def test_example_part_2(self) -> None:
        assert self.example_part_2_output == 46

    def test_part_2(self) -> None:
        assert self.part_2_output == 136096660


if __name__ == "__main__":
    TestDay05.display_outputs()

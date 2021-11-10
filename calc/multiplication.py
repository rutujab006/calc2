"""This is multiplication operation object"""

from calc.calculations.calculation import Calculation

class Multiplication(Calculation):
    """This is multiplication class"""
    def get_result(self):
        """This is multiplication class"""
        return self.value_a * self.value_b

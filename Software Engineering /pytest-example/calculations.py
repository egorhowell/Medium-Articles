class Calculations:
    def __init__(self, a: float, b: float) -> None:
        """
        Initialize the Calculation object with two numbers.

        :param a: The first number.
        :param b: The second number.
        """
        self.a = a
        self.b = b

    def sum(self) -> float:
        """
        Calculate the sum of the two numbers.

        :return: The sum of the two numbers.
        """
        return self.a + self.b

    def multiply(self) -> float:
        """
        Calculate the product of the two numbers.

        :return: The product of the two numbers.
        """
        return self.a * self.b

    def divide(self) -> float:
        """
        Calculate the quotient of the two numbers.

        :return: The quotient of the two numbers.
        """
        return self.a / self.b

class Fraction:
    """The Fraction class creates a fraction using a numerator and denominator. It contains
    methods to do simple operations with fractions """

    def __init__( self, numerator, denominator ):
        """This method initializes the numerator and denominator of a fraction"""
        self.numerator = numerator
        if denominator == 0:
            raise ValueError("The denominator cannot be 0")
        self.denominator = denominator

    def addition( self, two_frac ):
        """This method adds 2 fractions"""
        my_denom = self.denominator * two_frac.denominator
        add_numer = (self.numerator * two_frac.denominator) + (two_frac.numerator * self.denominator)
        result = Fraction(add_numer, my_denom)
        return result

    def subtraction( self, two_frac ):
        """This method subtracts 2 fractions"""
        my_denom = self.denominator * two_frac.denominator
        sub_numer = (self.numerator * two_frac.denominator) - (two_frac.numerator * self.denominator)
        result = Fraction(sub_numer, my_denom)
        return result

    def multiplication( self, two_frac ):
        """This method multiplies 2 fractions"""
        my_numer = self.numerator * two_frac.numerator
        my_denom = self.denominator * two_frac.denominator
        result = Fraction(my_numer, my_denom)
        return result

    def division( self, two_frac ):
        """This method divides 2 fractions"""
        my_numer = self.numerator * two_frac.denominator
        my_denom = self.denominator * two_frac.numerator
        if (my_denom == 0):
            print("The denominator cannot be 0")
        else:
            result = Fraction(my_numer, my_denom)
            return result

    def equal( self, two_frac ):
        """This method determines whether 2 fractions are equal"""
        my_numer = self.numerator * two_frac.denominator
        my_denom = self.denominator * two_frac.numerator
        if my_numer == my_denom:
            return True
        else:
            return False

    def __str__( self ):
        """This method returns a string representation of a fraction"""
        return str(self.numerator) + "/" + str(self.denominator)


class FractionCalculator:
    """The Fraction Calculator Class asks the user for 2 fractions and an operator and
    then prints the result"""

    def get_number( self, my_input ):
        """This method ensures that the user entered in the correct input. It will
        be repeated until the valid input is entered """
        again = True
        while again:
            str_1 = input(my_input)
            try:
                int_1 = int(str_1)
                again = False
            except ValueError:
                print("Expected a number but got " + str_1)
        return int_1

    def get_fraction( self ):
        """This method ensures that the user types in a valid fraction. It makes sure
        that the denominator does not equal to 0"""
        again = True
        while again:
            frac_num = self.get_number("Please enter your numerator: ")
            frac_den = self.get_number("Please enter your denominator: ")
            try:
                my_frac = Fraction(frac_num, frac_den)
                again = False
            except ValueError as e:
                print(e)
        return my_frac

    def get_operator( self ):
        """This method asks the user for an operator. If an invalid operator is entered,
         the user will be asked to enter again"""
        again = True
        while again:

            my_operator = input("Please enter your operator (+, -, *, /, ==): ")
            if my_operator in ['+', '-', '*', '/', '==']:
                again = False

        return my_operator

    def calculation( self ):
        """This method asks the user for 2 fractions and an operator. The result will be
        based on the operator selected by the user"""
        first = self.get_fraction()
        my_operator = self.get_operator()
        second = self.get_fraction()

        if my_operator == "+":
            result = first.addition(second)
        elif my_operator == "-":
            result = first.subtraction(second)
        elif my_operator == "*":
            result = first.multiplication(second)
        elif my_operator == "/":
            result = first.division(second)
        elif my_operator == "==":
            result = first.equal(second)

        print(first, my_operator, second, "=", result)


class Testing:
    """This class tests the operations within the Fraction Class"""

    def test_addition( self ):
        """This method tests the addition operation"""
        f12 = Fraction(1, 2)
        f34 = Fraction(3, 4)
        f44 = Fraction(4, 4)

        f1234 = Fraction(10, 8)
        f1212 = Fraction(4, 4)
        f1244 = Fraction(12, 8)
        f123444 = Fraction(72, 32)

        result1 = f12.addition(f34)

        result2 = f12.addition(f12)

        result3 = f12.addition(f44)

        result4 = f12.addition(f34.addition(f44))

        print(f12, '+', f34, '=', result1, "[", f1234, "]")
        print(f12, '+', f12, '=', result2, "[", f1212, "]")
        print(f12, '+', f44, '=', result3, "[", f1244, "]")
        print(f12, '+', f34, '+', f44, '=', result4, "[", f123444, "]")

    def test_subtraction( self ):
        """This method tests the subtraction operation"""

        f12 = Fraction(1, 2)
        f34 = Fraction(3, 4)
        f44 = Fraction(4, 4)

        f1234 = Fraction(-2, 8)
        f1244 = Fraction(-4, 8)

        result1 = f12.subtraction(f34)

        result2 = f12.subtraction(f44)

        print(f12, '-', f34, '=', result1, "[", f1234, "]")
        print(f12, '-', f44, '=', result2, '[', f1244, ']')

    def test_multiplication( self ):
        """This method tests the multiplication operation"""

        f12 = Fraction(1, 2)
        f34 = Fraction(3, 4)
        f44 = Fraction(4, 4)

        f1234 = Fraction(3, 8)
        f3444 = Fraction(12, 16)

        result1 = f12.multiplication(f34)

        result2 = f34.multiplication(f44)

        print(f12, '*', f34, '=', result1, "[", f1234, "]")
        print(f34, '*', f44, '=', result2, "[", f3444, "]")

    def test_division( self ):
        """This method tests the multiplication operation"""

        f12 = Fraction(1, 2)
        f34 = Fraction(3, 4)
        f44 = Fraction(4, 4)

        f1234 = Fraction(4, 6)
        f4412 = Fraction(8, 4)

        result1 = f12.division(f34)

        result2 = f44.division(f12)

        print(f12, '/', f34, '=', result1, "[", f1234, "]")
        print(f44, '/', f12, '=', result2, "[", f4412, "]")

    def test_equal( self ):
        """This method tests whether 2 fractions are equal"""
        f12 = Fraction(1, 2)
        f34 = Fraction(3, 4)
        f128 = Fraction(12, 8)
        f32 = Fraction(3, 2)

        result1 = f12.equal(f34)

        result2 = f128.equal(f32)

        print("With", f12, "and", f34, "the result is", result1, "[False]")
        print("With", f128, "and", f32, "the result is", result2, "[True]")


def main( ):
    """This method executes the Fraction Calculator"""
    print("This is a Fraction Calculator. You must type in numbers")
    my_calc = FractionCalculator()
    my_calc.calculation()


def test_main( ):
    """This method executes Testing"""
    my_test = Testing()
    my_test.test_addition()
    my_test.test_subtraction()
    my_test.test_multiplication()
    my_test.test_division()
    my_test.test_equal()


main()
test_main()

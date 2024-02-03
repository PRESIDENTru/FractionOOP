import math


class Fraction:
    def __init__(self, numerator, denominator=1):
        if type(numerator) is str:
            if numerator.count("/") == 0:
                self.num = int(numerator)
                self.den = denominator
            else:
                n = numerator.split("/")
                self.num = int(n[0])
                self.den = int(n[-1])
        else:
            self.num = numerator
            self.den = denominator
        self.__delen()

    def numerator(self, number=None):
        if number is None:
            return abs(self.num)
        else:
            self.num = number * self.__sign()
            self.__delen()

    def denominator(self, denominator=None):
        if denominator is None:
            return self.den
        else:
            self.den = denominator
            self.__delen()

    def __add__(self, other):
        return self.__operations(other, "+")

    def __sub__(self, other):
        return self.__operations(other, "-")

    def __iadd__(self, other):
        return self.__operations(other, "+=")

    def __isub__(self, other):
        return self.__operations(other, "-=")

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __repr__(self):
        return "Fraction(\'" + str(self.num) + "/" + str(self.den) + "\')"

    def __neg__(self):
        return Fraction(-self.num, self.den)

    def __mul__(self, other):
        return self.__operations(other, "*")

    def __truediv__(self, other):
        return self.__operations(other, "/")

    def __imul__(self, other):
        return self.__operations(other, "*=")

    def __itruediv__(self, other):
        return self.__operations(other, "/=")

    def __radd__(self, other):
        other = Fraction(other, 1)
        return other.__operations(self, "+")

    def __rsub__(self, other):
        other = Fraction(other, 1)
        return other.__operations(self, "-")

    def __rmul__(self, other):
        other = Fraction(other, 1)
        return other.__operations(self, "*")

    def __rtruediv__(self, other):
        other = Fraction(other, 1)
        return other.__operations(self, "/")

    def __lt__(self, other):
        return self.__operations(other, "<")

    def __le__(self, other):
        return self.__operations(other, "<=")

    def __eq__(self, other):
        return self.__operations(other, "==")

    def __ne__(self, other):
        return self.__operations(other, "!=")

    def __gt__(self, other):
        return self.__operations(other, ">")

    def __ge__(self, other):
        return self.__operations(other, ">=")

    def reverse(self):
        return Fraction(self.den, self.num)

    def __operations(self, other, operation):
        if type(other) is not Fraction:
            other = Fraction(other)
        copy = self.den
        copyOther = other.den
        den = self.den * other.den
        numSelf = self.num * copyOther
        numOther = other.num * copy

        if operation == "+":
            num = (self.num * copyOther) + (other.num * copy)
            return Fraction(num, den)
        elif operation == "-":
            num = (self.num * copyOther) - (other.num * copy)

            return Fraction(num, den)
        elif operation == "+=":
            self.den *= other.den
            self.num = (self.num * copyOther) + (other.num * copy)

            self.__delen()
            return self
        elif operation == "-=":
            self.den = self.den * other.den
            self.num = (self.num * copyOther) - (other.num * copy)

            self.__delen()
            return self
        elif operation == "*":
            den = self.den * other.den
            num = self.num * other.num

            return Fraction(num, den)
        elif operation == "/":
            den = self.den * other.num
            num = self.num * other.den

            return Fraction(num, den)
        elif operation == "*=":
            self.den *= other.den
            self.num *= other.num

            self.__delen()
            return self
        elif operation == "/=":
            self.den *= other.num
            self.num *= other.den

            self.__delen()
            return self
        elif operation == "<":
            if numSelf < numOther:
                return True
            else:
                return False
        elif operation == ">":
            if numSelf > numOther:
                return True
            else:
                return False
        elif operation == ">=":
            if numSelf >= numOther:
                return True
            else:
                return False
        elif operation == "<=":
            if numSelf <= numOther:
                return True
            else:
                return False
        elif operation == "==":
            if numSelf == numOther:
                return True
            else:
                return False
        elif operation == "!=":
            if numSelf != numOther:
                return True
            else:
                return False

    def __sign(self):
        return -1 if self.num < 0 else 1

    def __delen(self):
        while math.gcd(int(self.num), int(self.den)) != 1:
            n = math.gcd(self.num, self.den)
            self.num = int(self.num / n)
            self.den = int(self.den / n)
        if int(self.num) < 0 and int(self.den) < 0:
            self.num = abs(self.num)
            self.den = abs(self.den)
        elif int(self.num) > 0 and int(self.den) < 0:
            self.num = -self.num
            self.den = abs(self.den)


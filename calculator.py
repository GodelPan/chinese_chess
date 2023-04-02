class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def plus(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def multiple(self):
        return self.a * self.b

    def mod(self):
        remainder = self.a % self.b
        quotient = (self.a - self.b) / self.b
        return quotient, remainder

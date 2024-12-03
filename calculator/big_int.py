class BigInt:
    def __init__(self, value):
        # Remove leading zeros and ensure the value is valid
        self.value = self._normalize(value)

    @staticmethod
    def _normalize(value):
        if not value.isdigit():
            raise ValueError("Only non-negative integers are supported.")
        return value.lstrip('0') or '0'

    def __str__(self):
        return self.value

    def add(self, other):
        x, y = self.value[::-1], other.value[::-1]
        carry, result = 0, []
        for i in range(max(len(x), len(y))):
            digit_x = int(x[i]) if i < len(x) else 0
            digit_y = int(y[i]) if i < len(y) else 0
            total = digit_x + digit_y + carry
            result.append(total % 10)
            carry = total // 10
        if carry:
            result.append(carry)
        return BigInt(''.join(map(str, result[::-1])))

    def subtract(self, other):
        if self.compare(other) < 0:
            raise ValueError("Result would be negative, not supported in this implementation.")
        x, y = self.value[::-1], other.value[::-1]
        borrow, result = 0, []
        for i in range(len(x)):
            digit_x = int(x[i])
            digit_y = int(y[i]) if i < len(y) else 0
            total = digit_x - digit_y - borrow
            if total < 0:
                total += 10
                borrow = 1
            else:
                borrow = 0
            result.append(total)
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return BigInt(''.join(map(str, result[::-1])))

    def multiply(self, other):
        x, y = self.value[::-1], other.value[::-1]
        product = [0] * (len(x) + len(y))
        for i in range(len(x)):
            for j in range(len(y)):
                product[i + j] += int(x[i]) * int(y[j])
                if product[i + j] >= 10:
                    product[i + j + 1] += product[i + j] // 10
                    product[i + j] %= 10
        while len(product) > 1 and product[-1] == 0:
            product.pop()
        return BigInt(''.join(map(str, product[::-1])))

    def divide(self, other):
        if other.value == '0':
            raise ZeroDivisionError("Division by zero.")
        quotient, remainder = BigInt('0'), BigInt(self.value)
        while remainder.compare(other) >= 0:
            temp_y = other
            multiple = BigInt('1')
            while remainder.compare(temp_y.add(temp_y)) >= 0:
                temp_y = temp_y.add(temp_y)
                multiple = multiple.add(multiple)
            remainder = remainder.subtract(temp_y)
            quotient = quotient.add(multiple)
        return quotient, remainder

    def factorial(self):
        if self.value == '0' or self.value == '1':
            return BigInt('1')
        result = BigInt('1')
        current = BigInt('1')
        while current.compare(self) <= 0:
            result = result.multiply(current)
            current = current.add(BigInt('1'))
        return result

    def compare(self, other):
        x, y = self.value.lstrip('0'), other.value.lstrip('0')
        if len(x) > len(y):
            return 1
        if len(x) < len(y):
            return -1
        return (x > y) - (x < y)

# Example REPL
def repl():
    print("Arbitrary Precision Calculator")
    print("Supported operations: +, -, *, /, !")
    print("Type 'exit' to quit the REPL.")
    while True:
        expr = input(">> ").strip()
        if expr.lower() == 'exit':
            break
        try:
            if '!' in expr:
                n = BigInt(expr.replace('!', '').strip())
                print(n.factorial())
            elif '+' in expr:
                x, y = map(str.strip, expr.split('+'))
                print(BigInt(x).add(BigInt(y)))
            elif '-' in expr:
                x, y = map(str.strip, expr.split('-'))
                print(BigInt(x).subtract(BigInt(y)))
            elif '*' in expr:
                x, y = map(str.strip, expr.split('*'))
                print(BigInt(x).multiply(BigInt(y)))
            elif '/' in expr:
                x, y = map(str.strip, expr.split('/'))
                q, r = BigInt(x).divide(BigInt(y))
                print(f"Quotient: {q}, Remainder: {r}")
            else:
                print("Unsupported operation.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()

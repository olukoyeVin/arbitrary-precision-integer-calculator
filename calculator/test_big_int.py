import unittest
from big_int import BigInt

class TestBigInt(unittest.TestCase):
    def test_addition(self):
        # Basic cases
        self.assertEqual(str(BigInt('123').add(BigInt('456'))), '579')
        self.assertEqual(str(BigInt('999999').add(BigInt('1'))), '1000000')
        self.assertEqual(str(BigInt('0').add(BigInt('0'))), '0')
        # Large numbers
        self.assertEqual(
            str(BigInt('987654321987654321').add(BigInt('123456789123456789'))),
            '1111111111111111110'
        )

    def test_subtraction(self):
        # Basic cases
        self.assertEqual(str(BigInt('456').subtract(BigInt('123'))), '333')
        self.assertEqual(str(BigInt('1000').subtract(BigInt('1'))), '999')
        # Edge cases
        with self.assertRaises(ValueError):
            BigInt('123').subtract(BigInt('456'))

    def test_multiplication(self):
        # Basic cases
        self.assertEqual(str(BigInt('123').multiply(BigInt('456'))), '56088')
        self.assertEqual(str(BigInt('0').multiply(BigInt('9999'))), '0')
        # Large numbers
        self.assertEqual(
            str(BigInt('123456789').multiply(BigInt('987654321'))),
            '121932631112635269'
        )

    def test_division(self):
        # Basic division
        q, r = BigInt('100').divide(BigInt('3'))
        self.assertEqual(str(q), '33')
        self.assertEqual(str(r), '1')

        q, r = BigInt('999').divide(BigInt('10'))
        self.assertEqual(str(q), '99')
        self.assertEqual(str(r), '9')

        # Edge cases
        with self.assertRaises(ZeroDivisionError):
            BigInt('123').divide(BigInt('0'))

    def test_factorial(self):
        # Basic cases
        self.assertEqual(str(BigInt('5').factorial()), '120')
        self.assertEqual(str(BigInt('0').factorial()), '1')
        self.assertEqual(str(BigInt('1').factorial()), '1')
        # Large factorial
        self.assertEqual(
            str(BigInt('10').factorial()), '3628800'
        )

    def test_comparison(self):
        # Basic comparisons
        self.assertEqual(BigInt('123').compare(BigInt('456')), -1)
        self.assertEqual(BigInt('456').compare(BigInt('123')), 1)
        self.assertEqual(BigInt('123').compare(BigInt('123')), 0)
        # Large numbers
        self.assertEqual(
            BigInt('987654321').compare(BigInt('123456789')), 1
        )

    def test_normalization(self):
        # Leading zeros
        self.assertEqual(str(BigInt('000123').add(BigInt('000007'))), '130')
        self.assertEqual(str(BigInt('0000').add(BigInt('0'))), '0')

    def test_edge_cases(self):
        # Large inputs and zero handling
        self.assertEqual(str(BigInt('1').add(BigInt('999999999999999999'))), '1000000000000000000')
        self.assertEqual(str(BigInt('999999999999999999').multiply(BigInt('0'))), '0')
        self.assertEqual(str(BigInt('1000000000000').subtract(BigInt('999999999999'))), '1')

if __name__ == '__main__':
    unittest.main()

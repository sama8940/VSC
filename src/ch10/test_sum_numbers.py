# sum_numbres 関数のテストコード
import unittest
from code_sum_numbers import sum_numbers

class TestSumNumbers(unittest.TestCase):
    def test_sum_numbers(self):
        assert sum_numbers('10,20,30') == 60
        assert sum_numbers('10,20,30,40') == 'error'
        assert sum_numbers('10,20,thirty') == 'error'
        assert sum_numbers('10,20') == 'error'
        assert sum_numbers('10') == 'error'
        assert sum_numbers('') == 'error'

    def test_error(self) :
        assert sum_numbers('x,y,z') == 'error'

if __name__ == '__main__':
    unittest.main()

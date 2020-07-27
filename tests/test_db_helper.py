from unittest import TestCase
from src.db_helper import DbHelper
from unittest.mock import patch

class TestSalary(TestCase):
    def setUp(self):
        self.sal = DbHelper()

    @patch('src.db_helper.DbHelper')
    def test_sum_with_mocking(self, MockCalculator):
        mockcal = MockCalculator()  
        
        mockcal.get_maximum_salary.return_value = 46342.0
        mockcal.get_minimum_salary.return_value = 2134.0
        max_sal = mockcal.get_maximum_salary()
        min_sal = mockcal.get_minimum_salary()
        self.assertGreater(max_sal, min_sal)
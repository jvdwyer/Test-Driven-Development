import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #demonstrating that this is run at the beginning of testing
        print('setupClass')
    
    @classmethod
    def tearDownClass(cls):
        #demonstrating that this is run at the end of testing
        print('teardownClass')

    def setUp(self):
        #run before each test
        self.emp_1 = Employee('John', 'Dwyer', 50000)
        self.emp_2 = Employee('Maddie', 'Wall', 65000)
    
    def tearDown(self):
        #run after each test
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'John.Dwyer@email.com')
        self.assertEqual(self.emp_2.email, 'Maddie.Wall@email.com')

        self.emp_1.first = 'Jon'
        self.emp_2.first = 'Madds'

        self.assertEqual(self.emp_1.email, 'Jon.Dwyer@email.com')
        self.assertEqual(self.emp_2.email, 'Madds.Wall@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'John Dwyer')
        self.assertEqual(self.emp_2.fullname, 'Maddie Wall')

        self.emp_1.first = 'Jon'
        self.emp_2.first = 'Madds'

        self.assertEqual(self.emp_1.fullname, 'Jon Dwyer')
        self.assertEqual(self.emp_2.fullname, 'Madds Wall')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 68250)
    
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('December')
            mocked_get.assert_called_with('http://yourcompany.com/Dwyer/December')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('April')
            mocked_get.assert_called_with('http://yourcompany.com/Wall/April')
            self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
    unittest.main()

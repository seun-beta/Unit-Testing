import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee('Jason', 'Bourne', 1000)
        self.emp_2 = Employee('Charles', 'Severance', 3000)

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Jason.Bourne@gmail.com')
        self.assertEqual(self.emp_2.email, 'Charles.Severance@gmail.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Bruno'

        self.assertEqual(self.emp_1.email, 'John.Bourne@gmail.com')
        self.assertEqual(self.emp_2.email, 'Bruno.Severance@gmail.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Jason Bourne')
        self.assertEqual(self.emp_2.fullname, 'Charles Severance')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Bourne')
        self.assertEqual(self.emp_2.fullname, 'Jane Severance')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 1030)
        self.assertEqual(self.emp_2.pay, 3090)


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch 
import website

class TestWebsite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def test_monthly_schedule(self):
        with patch('website.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = website.monthly_schedule('Seunfunmi', 'March')
            mocked_get.assert_called_with('http://company.com/Seunfunmi/March')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False
            schedule = website.monthly_schedule('Seunfunmi', 'March')
            mocked_get.assert_called_with('http://company.com/Seunfunmi/March')
            self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
    unittest.main()

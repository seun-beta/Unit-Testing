import unittest
import fish


class TestFish(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.fish_1 = fish.Fish('Jake')
        self.fish_2 = fish.Fish('Vanessa')

    def tearDown(self):
        print('tearDown')
        pass

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.fish_1.fullname(), 'Jake Fish')
        self.assertEqual(self.fish_2.fullname(), 'Vanessa Fish')

        self.fish_1.first_name = 'John'

        self.assertEqual(self.fish_1.fullname(), 'John Fish')
        self.assertEqual(self.fish_1.eyelids, False)
        self.assertEqual(self.fish_1.skeleton, 'bone')

        self.fish_1.skeleton = 'cartilage'
        self.assertEqual(self.fish_1.skeleton, 'cartilage')

    def test_swim(self):
        print('test_swim')

        self.assertEqual(self.fish_1.swim(), 'The fish is swimming.')


if __name__ == '__main__':
    unittest.main()

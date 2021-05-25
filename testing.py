from logging import exception
from main import main
import unittest, labels

class testImage(unittest.TestCase):

    def test_vehicle(self):
        label = main()
        try:
            self.assertEqual(labels.match_labels(label), True)
        except AssertionError:
            raise Exception("{0} is not inside the function.".format(label))

if __name__ == '__main__':
    unittest.main()
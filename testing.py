from main import main
import unittest, labels

class testImage(unittest.TestCase):

    def test_vehicle(self):
        label = main()
        self.assertEqual(labels.match_labels(label), True, "{0} is not inside the function.".format(label))

if __name__ == '__main__':
    unittest.main()
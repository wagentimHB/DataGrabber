import unittest#
from driver.driver import Selenium

class TestSelenium(unittest.TestCase):

    def test_initialBrowser(self):
        obj = Selenium()

        with self.assertRaises(ValueError):
            obj.initial_browser("")

        self.assertEqual(obj.initial_browser("firefox"), "firefox")
        self.assertEqual(obj.initial_browser("edge"), "edge")
        self.assertEqual(obj.initial_browser("chrome"), "chrome")

if __name__ == '__main__':
    unittest.main()
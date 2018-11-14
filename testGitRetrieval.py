import unittest
from gitRetrieval import calculate_language_total
 
class TestGitRetrieval(unittest.TestCase):

    def test_total_lines_in_language(self):
        list = [{"Java": 100, "Python": 95}, {"Perl": 5, "Java" : 25}, {"Haskell": 200}, {"Java":220}, {"JavaScript":550, "Java":100}]
        total_code_usage = calculate_language_total(list)
        self.assertEqual(total_code_usage, {"Java": 445, "Perl": 5, "Python": 95, "Haskell": 200, "JavaScript":550})
        print total_code_usage

if __name__ == '__main__':
    unittest.main()


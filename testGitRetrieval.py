import unittest
from gitRetrieval import calculate_language_total, convert_to_json
import json
 
class TestGitRetrieval(unittest.TestCase):

    def test_total_lines_in_language(self):
        list = [{"Java": 100, "Python": 95}, {"Perl": 5, "Java" : 25}, {"Haskell": 200}, {"Java":220}, {"JavaScript":550, "Java":100}]
        total_code_usage = calculate_language_total(list)
        self.assertEqual(total_code_usage, {"Java": 445, "Perl": 5, "Python": 95, "Haskell": 200, "JavaScript":550})
        languages_json = convert_to_json(total_code_usage)
        self.assertEqual(languages_json, json.dumps([{"linesOfCode": 95, "language": "Python"}, {"linesOfCode": 200, "language": "Haskell"}, 
        {"linesOfCode": 445, "language": "Java"}, {"linesOfCode": 550, "language": "JavaScript"}, {"linesOfCode": 5, "language": "Perl"}]))

        

if __name__ == '__main__':
    unittest.main()
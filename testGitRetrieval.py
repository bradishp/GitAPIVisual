import unittest
from gitRetrieval import GitLanguagesRetrieval
import json
 
class TestGitRetrieval(unittest.TestCase):

    def test_total_lines_in_language(self):
        testLanguages = GitLanguagesRetrieval("XanthusXX")  #dummy value, will be overwritten
        list = [{"Java": 100, "Python": 95}, {"Perl": 5, "Java" : 25}, {"Haskell": 200}, {"Java":220}, {"JavaScript":550, "Java":100}]

        total_code_usage = testLanguages.calculate_language_total(list)
        self.assertEqual(total_code_usage, {"Java": 445, "Other": 5, "Python": 95, "Haskell": 200, "JavaScript":550})
        languages_json = testLanguages.convert_to_json(total_code_usage, "linesOfCode")

        self.assertEqual(languages_json, json.dumps([{"linesOfCode": 95, "language": "Python"}, {"linesOfCode": 200, "language": "Haskell"}, 
        {"linesOfCode": 445, "language": "Java"}, {"linesOfCode": 550, "language": "JavaScript"}, {"linesOfCode": 5, "language": "Other"}]))

        self.assertEqual(testLanguages.get_minor_languages(), json.dumps([{"linesOfCode": 5, "language": "Perl"}]))

        self.assertEqual(testLanguages.get_languages_appearences(), json.dumps([{ "language": "Python", "numberOfRepos": 1}, {"language": 
        "Haskell", "numberOfRepos": 1}, {"language": "Java", "numberOfRepos": 4}, {"language": "JavaScript", "numberOfRepos": 1}, 
        {"language": "Perl", "numberOfRepos": 1}]))
        

if __name__ == '__main__':
    unittest.main()
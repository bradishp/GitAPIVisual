import unittest
from gitRetrieval import GitUserInfo, calculate_language_percent
 
class TestGitRetrieval(unittest.TestCase):

    # Tests that github is being accessed and data is being retrieved
    #def test_git_retrieval(self):
        # Make sure Github can be accessed.
        #gitUser = GitUserInfo("bbbbce0775c88233af65f275dadf6662e5531562")
       # gitUser.display_developers_info()

    def test_total_lines_in_language(self):
        list = [{"Java": 100, "Python": 95}, {"Perl": 5, "Java" : 25}, {"Haskell": 200}, {"Java":220}, {"JavaScript":550, "Java":100}]
        calculate_language_percent(list)
        total_code_usage = calculate_language_percent(list)
        self.assertEqual(total_code_usage, {"Java": 445, "Perl": 5, "Python": 95, "Haskell": 200, "JavaScript":550})
        print total_code_usage

if __name__ == '__main__':
    unittest.main()


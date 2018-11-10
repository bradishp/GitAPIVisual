import unittest
from gitRetrieval import GitUserInfo
 
class TestGitRetrieval(unittest.TestCase):

    # Tests that github is being accessed and data is being retrieved
    def test_git_retrieval(self):
        # Make sure Github can be accessed.
        gitUser = GitUserInfo("bbbbce0775c88233af65f275dadf6662e5531562")
        gitUser.display_developers_info()

if __name__ == '__main__':
    unittest.main()


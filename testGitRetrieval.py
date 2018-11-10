import unittest
from gitRetrieval import GitUserInfo
 
class TestGitRetrieval(unittest.TestCase):

    # Tests that github is being accessed and data is being retrieved
    def test_git_retrieval(self):
        # Make sure Github can be accessed.
        gitUser = GitUserInfo("bbbbce0775c88233af65f275dadf6662e5531562")
        assert(gitUser.display_developer_repos(), True) 
        assert(gitUser.gather_info_on_collaborators(), True)

if __name__ == '__main__':
    unittest.main()


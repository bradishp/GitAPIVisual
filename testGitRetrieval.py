import unittest
from gitRetrieval import *
 
class TestGitRetrieval(unittest.TestCase):

    # Tests that github is being accessed and data is being retrieved
    def test_git_retrieval(self):
        # Make sure Github can be accessed.
        self.assertEqual(get_info_on_developer(), True) 

if __name__ == '__main__':
    unittest.main()


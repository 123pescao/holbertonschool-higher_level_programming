import unittest

if __name__ == '__main__':
    # Discover and run all tests in the current directory.
    tests = unittest.TestLoader().discover('.')
    unittest.TextTestRunner().run(tests)

import unittest
import StringIO
import sys

# class {{ cookiecutter.project_slug|title }}Test(unittest.TestCase):
class Test(unittest.TestCase):

    # A class method called before tests in an individual class run
    @classmethod
    def setUpClass(cls):
        print "called once before any tests in class"

    # Method called to prepare the test fixture.This is called immediately before
    # calling the test method
    def setUp(self):
        pass

    # Method called immediately after the test method has been called and the
    # result recorded. This is called even if the test method raised an exception,
    def tearDown(self):
        pass

    # A class method called after tests in an individual class have run.
    @classmethod
    def tearDownClass(cls):
        print "\ncalled once after all tests in class"

    def _getTargetClass(self):
        import {{ cookiecutter.project_slug }}
        return {{ cookiecutter.project_slug }}

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()

    def test_main(self):
        {{ cookiecutter.project_slug }} = self._makeOne()
        captured_output = StringIO.StringIO()
        sys.stdout = captured_output
        {{ cookiecutter.project_slug }}.main()
        sys.stdout = sys.__stdout__
        console_out = captured_output.getvalue()
        self.assertEqual("hello world\n", console_out)

if __name__ == '__main__':
    unittest.main()

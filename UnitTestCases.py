
from logging import raiseExceptions
import unittest
from stringcolor import *
def sum(self):
    return self**2
def test_your_name(self):
    self.x=input("enter your name")
    return self.x
class teststing(unittest.TestCase):
    def setUp(self):
        self.widget = ('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')


    def test_string(self):
        self.assertEqual('foo'.upper(),'FOO')
    @unittest.skip(cs("this test has been skip","red"))
    def test_int(self):# this test will fail
        
        self.assertEqual(200,20)

    def test_again(self):
        s = 'hello world as'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
def test_the_sum_fun():
    try:
        assert sum(12)==24
    except:
        print(cs("THE FOLLWOING TEST IS FAIL","red"))
def test_name():
    x=None
    try:
        assert test_your_name(x)=="zain"
    except:
        print(cs("this test is fail","yellow"))

def suite():
    suite=unittest.TestCase
    suite.addTest(teststing('teststing'))
if __name__ == '__main__':
    #runner = unittest.TextTestRunner()
    #runner.run(suite())
    #test_the_sum_fun()
    #test_name()
    teststing
    unittest.main()
    #print(cs("all is done","red"))
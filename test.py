import unittest
from pipeto import *
from random import randint

def inc(x): return x + 1
def double(x): return x * 2
def neg(x): return 0 - x

class TestPipeto(unittest.TestCase):
    def setUp(self):
        self.true = self.assertTrue

    def test_pipe(self):
        for i in range(1, 100):
            arg = randint(1, 1000000)
            self.true(pipe(arg) | inc | done == inc(arg))
            self.true(pipe(arg) | double | done == double(arg))
            self.true(pipe(arg) | double | inc | neg | done ==  neg(inc(double(arg))))

    def test_to(self):
        for i in range(1, 100):
            arg = randint(1, 1000000)
            self.true(arg | to(inc) == inc(arg))
            self.true(arg | to(inc) | to(double) == double(inc(arg)))
            self.true(arg | to(inc) | to(double) | to(neg) == neg(double(inc(arg))))

    def test_compose(self):
        fn = compose(inc) | double | neg
        for i in range(1, 100):
            arg = randint(1, 1000000)
            self.true(neg(double(inc(arg))) == fn(arg))


if __name__ == '__main__':
    unittest.main()

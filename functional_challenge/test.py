import unittest, random, secrets, string, os, re
from functional_challenge import ChallengeNotAttempted

class SkipIfNotAttempted:
    def __init__(self, test):
        self.test = test
    
    def __enter__(self): pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == ChallengeNotAttempted:
            self.test.skipTest("Challenge not attempted")
            return True


class TestAll(unittest.TestCase):
    
    def test_self_introduction(self):
        from functional_challenge import self_introduction
        with SkipIfNotAttempted(self):
            random.seed()  # reset the seed
            name = secrets.token_hex(2)
            age = random.randint(2, 200)
            self.assertEqual("Hi my name is {} and I'm {} years old".format(name, age), self_introduction(name, age))
    
    def test_add(self):
        from functional_challenge import add
        
        with SkipIfNotAttempted(self):
            a = random.random() + random.randint(-1000, 1000)
            b = random.random() + random.randint(-1000, 1000)
            self.assertAlmostEqual(a + b, add(a, b))
    
    def test_concat(self):
        from functional_challenge import concat
        
        with SkipIfNotAttempted(self):
            a = secrets.token_hex(10)
            b = secrets.token_hex(10)
            self.assertEqual(a + b, concat(a, b))
    
    def test_add_to_list(self):
        from functional_challenge import add_to_list
        
        with SkipIfNotAttempted(self):
            l = random.sample(range(1000), 501)
            self.assertEqual(l, add_to_list(l[:500], l[500]))
    
    def test_third_element(self):
        from functional_challenge import third_element
        
        with SkipIfNotAttempted(self):
            l = random.sample(range(1000), 5)
            self.assertEqual(l[3], third_element(l))
    
    def test_int_to_str(self):
        from functional_challenge import int_to_str
        
        with SkipIfNotAttempted(self):
            i = random.randint(-1000, 1000)
            self.assertEqual(str(i), int_to_str(i))
    
    def test_sum(self):
        from functional_challenge import sum
        import builtins
        
        with SkipIfNotAttempted(self):
            i = random.randint(11, 9999)
            l = random.sample(range(-i, i), random.randint(10, i - 1))
            
            self.assertEqual(builtins.sum(l), sum(*l))
    
    def test_max(self):
        from functional_challenge import max
        import builtins
        
        with SkipIfNotAttempted(self):
            i = random.randint(11, 9999)
            l = random.sample(range(-i, i), random.randint(10, i - 1))
            
            self.assertEqual(builtins.max(l), max(*l))
    
    def test_flatten(self):
        from functional_challenge import flatten
        import random
        i = random.randint(100, 500)
        s = random.sample(range(i), random.randint(100, i - 1))
        
        def crumble(l):
            if len(l) == 1:
                return l
            s = random.randint(0, len(l) - 1)
            e = random.randint(0, len(l) - 1)
            if s < e:
                l[s] = l[s:e]
            for i in range(s + 1, e):
                l.pop(s + 1)
            
            mid = len(l) // 2
            return crumble(l[:mid]) + crumble(l[mid:])
        
        t = crumble(s[:])
        
        with SkipIfNotAttempted(self):
            self.assertEqual(s, flatten(t))
    
    def test_create_dict(self):
        from functional_challenge import create_dict
        
        with SkipIfNotAttempted(self):
            i = random.randint(1001, 9999)
            l = random.sample(range(i), random.randint(1000, i - 1))
            d = {j: random.randint(-9999, 9999) for j in l}
            self.assertEqual(d, create_dict(*d.items()))

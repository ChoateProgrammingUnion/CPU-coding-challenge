import unittest, secrets, random, string, os, re
from oop_challenge import ChallengeNotAttempted


class Level0(unittest.TestCase):
    def setUp(self):
        from oop_challenge import Basic
        try:
            Basic()
        except ChallengeNotAttempted:
            self.skipTest("Challenge 0 not attempted")
    
    def test_is_basic(self):
        from oop_challenge import Basic
        b = Basic()
        self.assertTrue(b.is_basic)
    
    def test_say_hi(self):
        from oop_challenge import Basic
        b = Basic()
        self.assertEqual(b.say_hi(), "Hi")


class Level1(unittest.TestCase):
    def setUp(self):
        from oop_challenge import Person
        try:
            Person("Mike", 18)
        except ChallengeNotAttempted:
            self.skipTest("Challenge 1 not attempted")
    
    def test_age(self):
        from oop_challenge import Person
        
        random.seed()  # reset the seed
        age = random.randint(2, 200)
        p = Person(secrets.token_hex(4), age)
        self.assertEqual(p.age, age)
    
    def test_name(self):
        from oop_challenge import Person
        
        random.seed()  # reset the seed
        
        name = secrets.token_hex(4)
        p = Person(name, random.randint(2, 200))
        self.assertEqual(p.name, name)
    
    def test_introduction_type(self):
        from oop_challenge import Person
        
        self.assertEqual(type(Person.introduction), property)
    
    def test_overall(self):
        from oop_challenge import Person
        
        random.seed()  # reset the seed
        name = secrets.token_hex(4)
        age = random.randint(2, 200)
        p = Person(name, age)
        self.assertEqual(p.name, name)
        self.assertEqual(p.age, age)
        self.assertEqual(p.introduction, "Hi my name is {} and I'm {} years old".format(name, age))
        self.assertEqual(str(p), "{}, age {}".format(name, age))
        name = secrets.token_hex(4)
        age = random.randint(2, 200)
        p.name = name
        p.age = age
        self.assertEqual(p.introduction, "Hi my name is {} and I'm {} years old".format(name, age))
        self.assertEqual(str(p), "{}, age {}".format(name, age))


class Level2(unittest.TestCase):
    def setUp(self):
        from oop_challenge import WeirdNumber
        try:
            WeirdNumber()
        except ChallengeNotAttempted:
            self.skipTest("Challenge 2 not attempted")
    
    def test_addition(self):
        from oop_challenge import WeirdNumber
        random.seed()
        
        n = random.randint(1, 1000)
        w = WeirdNumber()
        self.assertEqual(w + n, w)
        self.assertEqual(w + w, w)
    
    def test_subtraction(self):
        from oop_challenge import WeirdNumber
        random.seed()
        
        n = random.randint(1, 1000)
        w = WeirdNumber()
        self.assertEqual(w - n, w)
        self.assertEqual(w - w, 0)
    
    def test_multiplication(self):
        from oop_challenge import WeirdNumber
        import math
        random.seed()
        
        n = random.randint(1, 1000)
        w = WeirdNumber()
        self.assertEqual(w * n, w)
        self.assertTrue(math.isnan(w * w))
        self.assertEqual(w * 0, 0)
    
    def test_division(self):
        from oop_challenge import WeirdNumber
        import math
        random.seed()
        
        n = random.randint(1, 1000)
        w = WeirdNumber()
        self.assertEqual(w / w, 1)
        self.assertEqual(w / n, w)
        self.assertTrue(math.isnan(w / 0))
    
    def test_comparison(self):
        from oop_challenge import WeirdNumber
        random.seed()
        
        n = random.randint(1, 1000)
        w = WeirdNumber()
        self.assertGreater(w, n)
        self.assertFalse(w > w)
    
    def test_equality(self):
        from oop_challenge import WeirdNumber
        random.seed()
        
        n = random.randint(1, 1000)
        w = WeirdNumber()
        self.assertEqual(w, WeirdNumber())
        self.assertNotEqual(w, n)
    
    def test_subclass(self):
        from oop_challenge import Dictionary
        import builtins
        
        self.assertIs(Dictionary.__mro__[1], builtins.object)  # protect against global namespace pollution


class Level3(unittest.TestCase):
    def setUp(self):
        from oop_challenge import Dictionary
        try:
            Dictionary()
        except ChallengeNotAttempted:
            self.skipTest("Challenge 3 not attempted")
    
    def test_insertion(self):
        from oop_challenge import Dictionary
        d = Dictionary()
        d[secrets.token_hex(4)] = secrets.token_hex(4)

    
    def test_access(self):
        from oop_challenge import Dictionary
        d = Dictionary()
        with self.assertRaises(KeyError):
            d[secrets.token_hex(4)]
    
    def test_deletion(self):
        from oop_challenge import Dictionary
        d = Dictionary()
        with self.assertRaises(KeyError):
            del d[secrets.token_hex(4)]
    
    def test_data_integrity(self):
        from oop_challenge import Dictionary
        d = Dictionary()
        key = secrets.token_hex(5)
        data = secrets.token_hex(5)
        d[key] = data
        self.assertEqual(d[key], data)
        for i in range(1000):
            d[secrets.token_hex(4)] = secrets.token_hex(5)
        self.assertEqual(d[key], data)
        d[key] = secrets.token_hex(6)
        self.assertNotEqual(d[key], data)
        del d[key]
        with self.assertRaises(KeyError):
            d[key]
    
    def test_subclass(self):
        from oop_challenge import Dictionary
        import builtins
        
        self.assertIs(Dictionary.__mro__[1], builtins.object)  # protect against global namespace pollution


class Level4(unittest.TestCase):
    def setUp(self):
        from oop_challenge import JavascriptObject
        try:
            JavascriptObject()
        except ChallengeNotAttempted:
            self.skipTest("Challenge 4 not attempted")
    
    def test_insertion(self):
        from oop_challenge import JavascriptObject
        d = JavascriptObject()
        d[random.choice(string.ascii_letters) + secrets.token_hex(4)] = secrets.token_hex(4)

    def test_assignment(self):
        from oop_challenge import JavascriptObject
        d = JavascriptObject()
        setattr(d,random.choice(string.ascii_letters) + secrets.token_hex(4),secrets.token_hex(4))
    
    def test_access(self):
        from oop_challenge import JavascriptObject
        d = JavascriptObject()
        with self.assertRaises(KeyError):
            d[random.choice(string.ascii_letters) + secrets.token_hex(4)]
        with self.assertRaises(AttributeError):
            getattr(d, random.choice(string.ascii_letters) + secrets.token_hex(4))
    
    def test_deletion(self):
        from oop_challenge import JavascriptObject
        d = JavascriptObject()
        with self.assertRaises(KeyError):
            del d[random.choice(string.ascii_letters) + secrets.token_hex(4)]
    
    def test_data_integrity(self):
        from oop_challenge import JavascriptObject
        d = JavascriptObject()
        key = random.choice(string.ascii_letters) + secrets.token_hex(4)
        data = secrets.token_hex(5)
        d[key] = data
        
        self.assertEqual(data, d[key])
        self.assertEqual(data, getattr(d, key))
        
        for i in range(1000):
            d[random.choice(string.ascii_letters) + secrets.token_hex(4)] = secrets.token_hex(5)
        
        self.assertEqual(data, d[key])
        self.assertEqual(data, getattr(d, key))
        
        setattr(d,key, secrets.token_hex(6))
        
        self.assertNotEqual(data, d[key])
        self.assertNotEqual(data,getattr(d, key))
        
        del d[key]
        with self.assertRaises(KeyError):
            d[key]
            getattr(d, key)
    
    
    
    def test_subclass(self):
        from oop_challenge import JavascriptObject
        import builtins
        
        self.assertIs(JavascriptObject.__mro__[1], builtins.object)  # protect against global namespace pollution
    
    def test_attribute_access(self):
        
        from oop_challenge import JavascriptObject
        
        a = random.choice(string.ascii_letters) + secrets.token_hex(4)
        
        with self.assertRaises(AttributeError):
            o = JavascriptObject()
            getattr(o, a)
        
        with self.assertRaises(KeyError):
            o = JavascriptObject()
            o[a]


class Level5(unittest.TestCase):
    def setUp(self):
        from oop_challenge import ErrorSuppressor
        try:
            ErrorSuppressor()
        except ChallengeNotAttempted:
            self.skipTest("Challenge 5 not attempted")
    
    def test_context(self):
        from oop_challenge import ErrorSuppressor
        try:
            with ErrorSuppressor():
                pass
        except:
            self.fail("Your object does not work as a context manager")
    
    def test_attr(self):
        from oop_challenge import ErrorSuppressor
        suppressor = ErrorSuppressor()
        try:
            suppressor.error_count
            suppressor.errors_list,
            suppressor.last_error
        except AttributeError:
            self.fail("Your object does not have required attributes")
    
    def test_functionality(self):
        from oop_challenge import ErrorSuppressor
        random.seed()
        
        errors_list = []
        for i in range(random.randint(100, 200)):
            errors_list.append(random.choice(string.ascii_letters) + secrets.token_hex(4))
        
        suppressor = ErrorSuppressor()
        for err_name in errors_list:
            with self.subTest("Raising exception {}".format(err_name)):
                with suppressor:
                    raise type(err_name, (Exception,), {})
                self.assertEqual(suppressor.last_error.__name__, err_name)

        
        self.assertEqual(errors_list, list(map(lambda e: e.__name__, suppressor.errors_list)))
        self.assertEqual(len(errors_list), suppressor.error_count)

    def test_subclass(self):
        from oop_challenge import ErrorSuppressor
        import builtins
    
        self.assertIs(ErrorSuppressor.__mro__[1], builtins.object)  # protect against global namespace pollution


class Level6(unittest.TestCase):
    def setUp(self):
        from oop_challenge import SingletonWithNew
        try:
            SingletonWithNew()
        except ChallengeNotAttempted:
            self.skipTest("Challenge 6 not attempted")
    
    def test_identity(self):
        from oop_challenge import SingletonWithNew
        self.assertIs(SingletonWithNew(), SingletonWithNew())
        self.assertIs(type(SingletonWithNew()),SingletonWithNew)
    
    def test_meta(self):
        from oop_challenge import SingletonWithNew
        import builtins
        
        self.assertIs(builtins.type(SingletonWithNew), builtins.type, "You used a metaclass")

    def test_subclass(self):
        from oop_challenge import SingletonWithNew
        import builtins
    
        self.assertIs(SingletonWithNew.__mro__[1], builtins.object)  # protect against global namespace pollution


class Level7(unittest.TestCase):
    def setUp(self):
        from oop_challenge import SingletonWithMeta
        try:
            SingletonWithMeta()
        except ChallengeNotAttempted:
            self.skipTest("Challenge 7 not attempted")
    
    def test_identity(self):
        from oop_challenge import SingletonWithMeta
        import builtins
        
        SingletonWithMeta.__new__ = builtins.object.__new__
        # replace the __new__ method in case it was overridden
        
        self.assertIs(SingletonWithMeta(), SingletonWithMeta())
    
    def test_meta(self):
        from oop_challenge import SingletonWithMeta
        import builtins
        
        self.assertNotEqual(builtins.type(SingletonWithMeta), builtins.type, 'You are not using a metaclass')

    def test_subclass(self):
        from oop_challenge import SingletonWithMeta
        import builtins
    
        self.assertIs(SingletonWithMeta.__mro__[1], builtins.object)  # protect against global namespace pollution


class Level8(unittest.TestCase):
    def setUp(self):
        from oop_challenge import SuperDictionary
        try:
            SuperDictionary()
        except ChallengeNotAttempted:
            self.skipTest("Challenge 8 not attempted")
    
    def test_identity(self):
        from oop_challenge import SuperDictionary
        
        self.assertIs(SuperDictionary(), SuperDictionary())
    
    def test_attribute_access(self):
        
        from oop_challenge import SuperDictionary
        
        a = random.choice(string.ascii_letters) + secrets.token_hex(2)
        
        with self.assertRaises(AttributeError):
            o = SuperDictionary()
            getattr(o, a)
        
        with self.assertRaises(KeyError):
            o = SuperDictionary()
            o[a]
    
    def test_class_attribute_access(self):
        
        from oop_challenge import SuperDictionary
        
        a = random.choice(string.ascii_letters) + secrets.token_hex(2)
        
        with self.assertRaises(AttributeError):
            getattr(SuperDictionary, a)
        
        with self.assertRaises(KeyError):
            o = SuperDictionary()
            SuperDictionary[a]
    
    def test_attribute_assignment_on_instance(self):
        from oop_challenge import SuperDictionary
        
        k = random.choice(string.ascii_letters) + secrets.token_hex(2)
        v = secrets.token_hex(4)
        d = SuperDictionary()
        
        setattr(d, k, v)
        self.assertEqual(v, getattr(d, k))
        self.assertEqual(v, d[k])
    
    def test_attribute_assignment_on_class(self):
        from oop_challenge import SuperDictionary
        
        k = random.choice(string.ascii_letters) + secrets.token_hex(2)
        v = secrets.token_hex(4)
        d = SuperDictionary
        
        setattr(d, k, v)
        self.assertEqual(v, getattr(d, k))
        self.assertEqual(v, d[k])
    
    def test_insertion_on_instance(self):
        from oop_challenge import SuperDictionary
        d = SuperDictionary()
        d[random.choice(string.ascii_letters) + secrets.token_hex(2)] = secrets.token_hex(2)
    
    def test_insertion_on_class(self):
        from oop_challenge import SuperDictionary
        d = SuperDictionary
        
        d[random.choice(string.ascii_letters) + secrets.token_hex(2)] = secrets.token_hex(2)
    
    def test_access_on_instance(self):
        from oop_challenge import SuperDictionary
        d = SuperDictionary()
        with self.assertRaises(KeyError):
            d[random.choice(string.ascii_letters) + secrets.token_hex(2)]
        with self.assertRaises(AttributeError):
            getattr(d, random.choice(string.ascii_letters) + secrets.token_hex(2))
    
    def test_access_on_class(self):
        from oop_challenge import SuperDictionary
        d = SuperDictionary
        with self.assertRaises(KeyError):
            d[random.choice(string.ascii_letters) + secrets.token_hex(2)]
        with self.assertRaises(AttributeError):
            getattr(d, random.choice(string.ascii_letters) + secrets.token_hex(2))
    
    def test_deletion_on_instance(self):
        from oop_challenge import SuperDictionary
        d = SuperDictionary()
        with self.assertRaises(KeyError):
            del d[random.choice(string.ascii_letters) + secrets.token_hex(2)]
    
    def test_deletion_on_class(self):
        from oop_challenge import SuperDictionary
        d = SuperDictionary
        with self.assertRaises(KeyError):
            del d[random.choice(string.ascii_letters) + secrets.token_hex(2)]
    
    def test_data_integrity_on_instance(self):
        from oop_challenge import SuperDictionary
        random.seed()
        
        d = SuperDictionary()
        key = random.choice(string.ascii_letters) + secrets.token_hex(4)
        data = secrets.token_hex(5)
        d[key] = data
        
        self.assertEqual(d[key], data)
        self.assertEqual(getattr(d, key), data)
        
        for i in range(1000):
            d[random.choice(string.ascii_letters) + secrets.token_hex(4)] = secrets.token_hex(5)
        
        self.assertEqual(d[key], data)
        self.assertEqual(getattr(d, key), data)
        
        d[key] = secrets.token_hex(6)
        
        self.assertNotEqual(d[key], data)
        self.assertNotEqual(getattr(d, key), data)
        
        del d[key]
        with self.assertRaises(KeyError):
            d[key]
        with self.assertRaises(AttributeError):
            getattr(d, key)

    
    def test_data_integrity_on_class(self):
        from oop_challenge import SuperDictionary
        random.seed()
        
        d = SuperDictionary
        key = random.choice(string.ascii_letters) + secrets.token_hex(4)
        data = secrets.token_hex(5)
        d[key] = data
        
        self.assertEqual(getattr(SuperDictionary, key), data)
        self.assertEqual(SuperDictionary[key], data)
        
        for i in range(1000):
            d[random.choice(string.ascii_letters) + secrets.token_hex(4)] = secrets.token_hex(5)
        
        self.assertEqual(getattr(SuperDictionary, key), data)
        self.assertEqual(SuperDictionary[key], data)
        
        d[key] = secrets.token_hex(6)
        
        self.assertNotEqual(getattr(SuperDictionary, key), data)
        self.assertNotEqual(SuperDictionary[key], data)
        
        del d[key]
        with self.assertRaises(KeyError):
            d[key]
        
        with self.assertRaises(AttributeError):
            getattr(d, key)
    
    def test_data_integrity_overall(self):
        from oop_challenge import SuperDictionary
        random.seed()
        
        key = random.choice(string.ascii_letters) + secrets.token_hex(4)
        value = secrets.token_hex(4)
        SuperDictionary[key] = value
        self.assertEqual(value, SuperDictionary[key])
        self.assertEqual(value, SuperDictionary()[key])
        self.assertEqual(value, getattr(SuperDictionary, key))
        self.assertEqual(value, getattr(SuperDictionary(), key))
        
        key = random.choice(string.ascii_letters) + secrets.token_hex(4)
        value = secrets.token_hex(4)
        SuperDictionary()[key] = value
        self.assertEqual(value, SuperDictionary[key])
        self.assertEqual(value, SuperDictionary()[key])
        self.assertEqual(value, getattr(SuperDictionary, key))
        self.assertEqual(value, getattr(SuperDictionary(), key))
        
        key = random.choice(string.ascii_letters) + secrets.token_hex(4)
        value = secrets.token_hex(4)
        setattr(SuperDictionary, key, value)
        self.assertEqual(value, SuperDictionary[key])
        self.assertEqual(value, SuperDictionary()[key])
        self.assertEqual(value, getattr(SuperDictionary, key))
        self.assertEqual(value, getattr(SuperDictionary(), key))
        
        key = random.choice(string.ascii_letters) + secrets.token_hex(4)
        value = secrets.token_hex(4)
        setattr(SuperDictionary(), key, value)
        self.assertEqual(value, SuperDictionary[key])
        self.assertEqual(value, SuperDictionary()[key])
        self.assertEqual(value, getattr(SuperDictionary, key))
        self.assertEqual(value, getattr(SuperDictionary(), key))
        
        key = random.choice(string.ascii_letters) + secrets.token_hex(4)
        value = secrets.token_hex(4)
        setattr(SuperDictionary(), key, value)
        self.assertEqual(value, SuperDictionary[key])
        self.assertEqual(value, SuperDictionary()[key])
        self.assertEqual(value, getattr(SuperDictionary, key))
        self.assertEqual(value, getattr(SuperDictionary(), key))
        del SuperDictionary[key]
        with self.assertRaises(AttributeError):
            getattr(SuperDictionary, key)
        with self.assertRaises(AttributeError):
            getattr(SuperDictionary(), key)
        with self.assertRaises(KeyError):
            SuperDictionary[key]
        with self.assertRaises(KeyError):
            SuperDictionary()[key]
        
        key = random.choice(string.ascii_letters) + secrets.token_hex(4)
        value = secrets.token_hex(4)
        setattr(SuperDictionary, key, value)
        self.assertEqual(value, SuperDictionary[key])
        self.assertEqual(value, SuperDictionary()[key])
        self.assertEqual(value, getattr(SuperDictionary, key))
        self.assertEqual(value, getattr(SuperDictionary(), key))
        del SuperDictionary()[key]
        with self.assertRaises(AttributeError):
            getattr(SuperDictionary, key)
        with self.assertRaises(AttributeError):
            getattr(SuperDictionary(), key)
        with self.assertRaises(KeyError):
            SuperDictionary[key]
        with self.assertRaises(KeyError):
            SuperDictionary()[key]

    def test_subclass(self):
        from oop_challenge import SuperDictionary
        import builtins
    
        self.assertIs(SuperDictionary.__mro__[1], builtins.object)  # protect against global namespace pollution

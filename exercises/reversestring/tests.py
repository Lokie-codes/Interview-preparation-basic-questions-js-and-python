#testing file for reverse string function defined in main file

import unittest
from main import reverse

class TestReverse(unittest.TestCase):

    def if_reverse_is_a_function(self):
        self.assertTrue(callable(reverse))

    # testing the examples given in the main.py file
    def test_reverse(self):
        self.assertEqual(reverse('apple'), 'elppa')
        self.assertEqual(reverse('hello'), 'olleh')
        self.assertEqual(reverse('Greetings!'), '!sgniteerG')
    
    # tesing some more edge cases
    def test_reverse_edge_cases(self):
        self.assertEqual(reverse(''), '')
        self.assertEqual(reverse('ab  '), '  ba')
        self.assertEqual(reverse('#!@#$%^&*()'), ')(*&^%$#@!#')
        self.assertEqual(reverse('1234567890'), '0987654321')
        self.assertEqual(reverse('a'), 'a')

    # testing some unique test cases
    def test_reverse_unique_cases(self):
        self.assertEqual(reverse('a b c d e f g h i j k l m n o p q r s t u v w x y z'), 'z y x w v u t s r q p o n m l k j i h g f e d c b a')
        self.assertEqual(reverse('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'), 'Z Y X W V U T S R Q P O N M L K J I H G F E D C B A')
        self.assertEqual(reverse('!@#$%^&*()_+'), ('+_)(*&^%$#@!'))


if __name__ == '__main__':
    unittest.main()

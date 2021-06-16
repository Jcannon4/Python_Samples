import unittest
import cap

class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')
    
    def test_mult_words(self):
        test = 'lebron james'
        result = cap.cap_text(test)
        self.assertEqual(result, 'Lebron James')
if __name__ == '__main__':
    unittest.main()
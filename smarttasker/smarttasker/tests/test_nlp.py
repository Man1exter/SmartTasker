import unittest
from smarttasker.nlp_utils import extract_date, extract_category, extract_priority

class TestNlpUtils(unittest.TestCase):
    def test_extract_date(self):
        self.assertEqual(extract_date("spotkanie jutro o 10"), "2024-08-01T10:00:00") #Założyłem date na 2024-08-01
        self.assertEqual(extract_date("kup mleko"), None)

    def test_extract_category(self):
        self.assertEqual(extract_category("praca - zrób projekt"), "praca")
        self.assertEqual(extract_category("obiad w domu"), "dom")
        self.assertEqual(extract_category("zakupy na urodziny"), "zakupy")
        self.assertEqual(extract_category("spotkanie z kolega"), "uncategorized")
    
    def test_extract_priority(self):
         self.assertEqual(extract_priority("pilne wyslac maila"), "pilne")
         self.assertEqual(extract_priority("ważne spotkanie z szefem"), "ważne")
         self.assertEqual(extract_priority("kupic banany"), "normal")

if __name__ == '__main__':
    unittest.main()
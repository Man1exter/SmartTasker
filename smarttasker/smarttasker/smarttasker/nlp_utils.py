import nltk
from nltk.tokenize import word_tokenize
import dateparser

nltk.download('punkt', quiet=True)

def extract_date(text):
    date_result = dateparser.parse(text)
    if date_result:
        return date_result.isoformat()
    return None

def extract_category(text):
    tokens = word_tokenize(text.lower())
    if "praca" in tokens:
        return "praca"
    elif "dom" in tokens:
        return "dom"
    elif "zakupy" in tokens:
        return "zakupy"
    else:
        return "uncategorized"

def extract_priority(text):
    tokens = word_tokenize(text.lower())
    if "pilne" in tokens:
        return "pilne"
    elif "ważne" in tokens:
        return "ważne"
    else:
        return "normal"
from os import lseek
from src.ner import ner

def test_ner():
    sentence = "I went to New York to speak French"
    results = ner(sentence)

    assert "New York" in results
    assert "French" in results
    assert "to" not in results
    print(results)
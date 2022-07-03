from dataclasses import dataclass
from src.parse_to_pages.parse_to_pages import Page
from src.ner import ner

@dataclass
class SentenceWithNE:
    sentence: str
    nes: list[str]

    def display_nes(self):
        return " ".join([f"[[{ne}]]" for ne in self.nes])

    def __repr__(self):
        newline = "\n"
        if len(self.nes) > 0:
            return f"{self.sentence}{newline}        - {self.display_nes()}"
        return self.sentence

class PageWithNE(Page):
    def display_sentences(self):
        return self.sentence_joiner.join([sentence.__repr__() for sentence in self.sentences])

    sentences: SentenceWithNE

def add_ne_to_page(page: Page):
    sentences = [SentenceWithNE(sentence, ner(sentence)) for sentence in page.sentences]
    return PageWithNE(page.number, sentences)

    

from asyncore import read
from dataclasses import dataclass
import re
import nltk

nltk.download('punkt')

@dataclass
class Page:
    number: int
    sentences: list[str]
    sentence_joiner = '\n    - '

    def display_sentences(self):
        return self.sentence_joiner.join(self.sentences)

    def __repr__(self):
        return f"""

Page {self.number}

- Text
    - {self.display_sentences()}
- Metadata
    - Activity summary
    - Place
    - Narrator
    - People present
    - People mentioned
    - Other



"""

def parse_text_to_pages(text: str, page_separator) -> list[Page]:
    raw_pages = re.split(page_separator, text)
    pages = [[sentence.strip().replace("\n", "") for sentence in nltk.sent_tokenize(raw_page)] for raw_page in raw_pages]
    return [Page(i+1, page) for i, page in enumerate(pages)]
    


from asyncore import read
from dataclasses import dataclass
import nltk

nltk.download('punkt')

@dataclass
class Page:
    number: int
    sentences: list[str]

def parse_text_to_pages(text: str) -> list[Page]:
    raw_pages = text.split("")
    pages = [nltk.sent_tokenize(raw_page) for raw_page in raw_pages]
    return [Page(i, page) for i, page in enumerate(pages)]

pages = parse_text_to_pages(open("upload_to_roam/data/1800180799FGBVC-_1_ (1).txt").read())
print(pages)


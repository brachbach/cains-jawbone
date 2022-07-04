from src.parse_to_pages.parse_to_pages import parse_text_to_pages
from src.add_ne_to_page import add_ne_to_page

pages = parse_text_to_pages(open("data/Cain's Jawbone (slideshow).txt").read(), r"\[ \d* ]\nNOTES")
print(len(pages))
pages_with_ne = [add_ne_to_page(page) for page in pages]
for page in pages_with_ne:
    print(page)
open("data/parsed_for_roam_with_ne.txt", "w").write("\n\n".join([str(page) for page in pages_with_ne]))
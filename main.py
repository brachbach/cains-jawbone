from src.parse_to_pages.parse_to_pages import parse_text_to_pages
from src.add_ne_to_page import add_ne_to_page

pages = parse_text_to_pages(open("data/1800180799FGBVC-_1_ (1).txt").read())
pages_with_ne = [add_ne_to_page(page) for page in pages]
open("data/parsed_for_roam_with_ne.txt", "w").write("\n\n".join([str(page) for page in pages_with_ne]))
## Starting file

[This Reddit post](https://www.reddit.com/r/CainsJawbone/comments/qkiog1/free_digital_copy_of_cains_jawbone/) is the only source I've find of digital files of the book.

There are a PDF, EPUB, and slideshow there. All seem to be a of a different edition of the book that has some typos that are absent in Gina's print edition

I added the PDF and EPUB to the data folder.

## Parsing to easily-machine-readable format

I quickly tried some parsing options for both PDF and EPUB and settled on [Convertio](https://convertio.co/download/fdeded8c02945500e24ea1df7b7dfc81906647/), converting PDF to txt.

The resulting text is in the data folder.

## Parsing to pages with sentences

I used nltk. See parse_to_pages.py

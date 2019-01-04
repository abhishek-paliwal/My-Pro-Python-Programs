## THIS PROGRAM NEEDS PYTHON3 TO RUN: (I TESTED ON PYTHON 3.7)
## FILENAME: demo-mercury-web-parser.py
## RUN AS > python3 demo-mercury-web-parser.py
from mercury_parser import ParserAPI

mercury = ParserAPI(api_key='DhPT0GswRlGDeZIFLCYhtqfmCjdHFdsHdCxAKORS')

p = mercury.parse('http://www.bbc.com/capital/story/20181204-how-austerity-memes-helped-the-internet-generation-cope')

# Available attributes FOR PRINTING:
print(p.title)
#print(p.content)
print(p.date_published)
print(p.lead_image_url)
print(p.dek)
print(p.url)
print(p.domain)
print(p.excerpt)
print(p.word_count)
print(p.direction)
print(p.total_pages)
print(p.rendered_pages)
print(p.next_page_url)

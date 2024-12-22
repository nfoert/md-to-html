import datetime
import os

import markdown
from bs4 import BeautifulSoup
import argparse

from styles import styles

parser = argparse.ArgumentParser(
    prog='tab-discord-weekly-recap',
    description='Generate a weekly recap for the TAB Discord',
    epilog='Text at the bottom of help')

parser.add_argument("-d", "--dev", help="Run in dev mode and store output files to index.html instead", action="store_true")

args = parser.parse_args()

# Get markdown file
# Turn into html
with open("body.md", "r") as f:
    html = markdown.markdown(f.read())

# Embed needed css
soup = BeautifulSoup(html, 'html.parser')

for tag, style in styles.items():
    for element in soup.find_all(tag):
        try:
            element['style'] = element['style'] + style
        except KeyError:
            element['style'] = style

# Create an empty bs4 document
body = BeautifulSoup(features="html.parser")
new_div = body.new_tag('div')
new_div['style'] = styles["body_content"]
new_div.append(soup)
body.append(new_div)

# Get default header and footer html
# Embed css into header and footer
with open("header.html", "r") as f:
    header = f.read()

    header_soup = BeautifulSoup(header, 'html.parser')

    for tag, style in styles.items():
        for element in header_soup.find_all(tag):
            try:
                element['style'] = element['style'] + style
            except KeyError:
                element['style'] = style

    header = str(header_soup)

with open("footer.html", "r") as f:
    footer = f.read()

    footer_soup = BeautifulSoup(footer, 'html.parser')

    for tag, style in styles.items():
        for element in footer_soup.find_all(tag):
            try:
                element['style'] = element['style'] + style
            except KeyError:
                element['style'] = style

    footer = str(footer_soup)

with open("head.html", "r") as f:
    head = f.read()

    head_soup = BeautifulSoup(head, 'html.parser')

    head = str(head_soup)

# Assemble final pages
final = header + str(body) + footer
# Add <!DOCTYPE html> to the top of the final document
final = "<!DOCTYPE html><html>"+ head + "<body>" + final + "</body></html>"

final_soup = BeautifulSoup(final, 'html.parser')
final_soup.body['style'] = styles["body"]
final = str(final_soup.prettify())

now = datetime.datetime.now()

if not args.dev:
    if not os.path.exists("./output"):
        os.makedirs("./output")

    with open(f"./output/{now.year}-{now.month}-{now.day}.html", "w") as f:
        f.write(final)
else:
    with open("index.html", "w") as f:
        f.write(final)
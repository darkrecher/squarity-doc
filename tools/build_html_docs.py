"""
blah
"""

from pathlib import Path
from markdown_it import MarkdownIt
from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.anchors import anchors_plugin

text = """
---
a: 1
---

## Pouet !

### Pouet mais de niveau 3

## Pouet !

a | b
- | -
1 | 2

Osef de ta footnote
"""

text = open("../user_manual/main_doc_v2.md").read()

def main():

    # https://mdit-py-plugins.readthedocs.io/en/latest/#heading-anchors
    md = (
        MarkdownIt('commonmark', {'breaks':True,'html':True})
        .use(front_matter_plugin)
        .use(
            anchors_plugin,
            max_level=5,
            permalink=True,
            permalinkSymbol="&#x1F517;"
        )
        .enable('table')
    )

    tokens = md.parse(text)
    html_text = md.render(text)

    Path("output.html").write_text(html_text)


from html.parser import HTMLParser

TITLE_TAGS = ("h1", "h2", "h3", "h4", "h5")

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag == "html":
            self.stored_titles = []
            self.in_title = None
            self.first_title_data = None
        elif tag in TITLE_TAGS:
            print("Encountered a start title tag:", tag)
            self.in_title = tag
        elif tag == "a" and self.in_title:
            dict_attrs = dict(attrs)
            print(dict_attrs["href"])
            self.stored_titles.append(
                (self.in_title, self.first_title_data, dict_attrs["href"])
            )

    def handle_endtag(self, tag):
        if tag in TITLE_TAGS:
            self.in_title = None
            self.first_title_data = None

    def handle_data(self, data):
        if self.in_title and self.first_title_data is None:
            self.first_title_data = data
            print("Encountered some data in the title:", data)


def main_test():

    parser = MyHTMLParser()
    html_text = open("output.html").read()
    parser.feed(html_text)
    for stored_title in parser.stored_titles:
        print(stored_title)


if __name__ == "__main__":
    main_test()

"""
start:
<h2 id="configuration-json">Configuration json <a class="header-anchor" href="#configuration-json">&#x1F517;</a></h2>

end:
<a href="#configuration-json"><h2>Configuration json</h2></a>

"""
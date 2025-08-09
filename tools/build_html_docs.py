"""
Petit script pour générer les docs HTML à partir de doc MarkDown,
avec leurs sommaires (Table Of Content (Toc)).

Par défaut, les fichiers générés sont placés dans squarity-code/src/components/docarticles
Il faut activer le virtual env "venv_squarity" avant de lancer le script.
J'ai pas mis poetry, parce que flemme.
"""

from pathlib import Path
from markdown_it import MarkdownIt
from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.anchors import anchors_plugin
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


class HtmlContentGenerator():

    def __init__(self, markdown_text, html_content_filepath):
        self.markdown_text = markdown_text
        self.html_content_filepath = html_content_filepath

    def generate(self):
        # https://mdit-py-plugins.readthedocs.io/en/latest/#heading-anchors
        md = (
            MarkdownIt('commonmark', {'breaks':True, 'html':True})
            .use(front_matter_plugin)
            .use(
                anchors_plugin,
                max_level=5,
                permalink=True,
                permalinkSymbol="&#x1F517;"
            )
            .enable('table')
        )
        # tokens = md.parse(text)
        self.html_content = md.render(self.markdown_text)

    def get_html_content(self):
        return self.html_content

    def write_html_content_file(self):
        self.html_content_filepath.write_text(self.html_content)


class HtmlTocGenerator():

    def __init__(self, stored_titles):
        self.stored_titles = stored_titles
        self.html_toc = ""

    def html_code_from_title_data(self, title_data):
        tag, title_text, title_id = title_data
        html_title = f'<a href="{title_id}"><{tag}>{title_text}</{tag}></a>\n'
        return html_title

    def generate(self):
        # TODO: il faut imbriquer les titres dans des divs.
        # Comme ça on pourrait faire du CSS plus sympa avec des décalages, des cadres imbriqués, etc.
        for title_data in self.stored_titles:
            self.html_toc += self.html_code_from_title_data(title_data)


class ArticleGenerator():

    OUT_PATH = Path(
        "..",
        "..",
        "squarity-code",
        "src",
        "components",
        "docarticles",
    )

    def __init__(self, markdown_filepath, article_name):
        self.markdown_filepath = Path(markdown_filepath)
        self.article_name = article_name

    def generate_all(self):
        self._compute_out_filepaths()
        self._read_markdown()
        html_content_generator = HtmlContentGenerator(
            self.markdown_text,
            self.html_content_filepath
        )
        html_content_generator.generate()
        self.html_content = html_content_generator.get_html_content()
        html_content_generator.write_html_content_file()

    def _compute_out_filepaths(self):
        content_filename = self.article_name + ".vue"
        toc_filename = self.article_name + "Toc.vue"
        out_path = ArticleGenerator.OUT_PATH
        self.html_content_filepath = out_path / content_filename
        self.html_toc_filepath = out_path / toc_filename

    def _read_markdown(self):
        self.markdown_text = self.markdown_filepath.read_text()


def main_old():

    parser = MyHTMLParser()
    html_text = open("output.html").read()
    parser.feed(html_text)
    #for stored_title in parser.stored_titles:
    #    print(stored_title)
    html_toc_generator = HtmlTocGenerator(parser.stored_titles)
    html_toc_generator.generate()
    print(html_toc_generator.html_toc)

def main():
    article_generator = ArticleGenerator("../user_manual/main_doc_v2.md", "PouetDoc")
    article_generator.generate_all()

if __name__ == "__main__":
    main()

"""
start:
<h2 id="configuration-json">Configuration json <a class="header-anchor" href="#configuration-json">&#x1F517;</a></h2>

end:
<a href="#configuration-json"><h2>Configuration json</h2></a>

"""

"""
Petit script pour générer les docs HTML à partir de doc MarkDown,
avec leurs sommaires (Table Of Content (Toc)).

Par défaut, les fichiers générés sont placés dans squarity-code/src/components/docarticles
Il faut activer le virtual env "venv_squarity" avant de lancer le script.
J'ai pas mis poetry, parce que flemme.
"""

# TODO : quand c'est des liens externes, on met target=_blank. Sinon, on laisse comme ça.
# et si possible, on met une petite icône de flèche pour indiquer que c'est un lien externe.

from pathlib import Path
import re
from markdown_it import MarkdownIt
from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.anchors import anchors_plugin
from html.parser import HTMLParser


class HtmlContentGenerator():

    COMPONENT_START = (
        "<template>\n"
        "    <div class=\"doc-article\">\n"
        "\n"
    )

    COMPONENT_END = (
        "\n"
        "    </div>\n"
        "</template>\n"
        "\n"
        "<style lang=\"css\" scoped src=\"@/styles/docArticle.css\"></style>\n"
    )

    PATH_TO_IMG = "../../assets/doc_img/"

    def __init__(self, markdown_text, html_content_filepath):
        self.markdown_text = markdown_text
        self.html_content_filepath = html_content_filepath

    def generate(self):
        self._modify_img_links()
        # https://mdit-py-plugins.readthedocs.io/en/latest/#heading-anchors
        md = (
            MarkdownIt("commonmark", {"breaks":True, "html":True})
            .use(front_matter_plugin)
            .use(
                anchors_plugin,
                max_level=5,
                permalink=True,
                permalinkSymbol="&#x1F517;"
            )
            .enable("table")
        )
        # tokens = md.parse(text)
        self.html_content = md.render(self.markdown_text)

    def get_html_content(self):
        return self.html_content

    def write_html_content_file(self):
        html_content_as_component = (
            HtmlContentGenerator.COMPONENT_START +
            self.html_content +
            HtmlContentGenerator.COMPONENT_END
        )
        self.html_content_filepath.write_text(html_content_as_component)

    def _modify_img_links(self):
        """
        Modifie le lien de toutes les images, en gardant le nom du fichier
        mais en remplaçant tout ce qu'il y a avant par un chemin fixe,
        adapté au site Squarity.
        """
        # C'est fait de manière très moche, mais c'est pas grave.
        markdown_imgs = re.findall(
            "(!\\[[^\\]]*\\]\\([^\\)]*\\))",
            self.markdown_text
        )
        for markdown_img in markdown_imgs:
            markdown_img_strip = markdown_img[2:-1]
            alt_text, img_link = markdown_img_strip.split("](")
            img_filename = img_link.split("/")[-1]
            # TODO : en même temps, il faudrait copier les images du repository de doc
            # vers le repository de code. Pour être sûr de les avoir à jour.
            new_img_link = HtmlContentGenerator.PATH_TO_IMG + img_filename
            new_markdown_img = f"![{alt_text}]({new_img_link})"
            self.markdown_text = self.markdown_text.replace(
                markdown_img,
                new_markdown_img
            )


class MyHTMLParser(HTMLParser):

    TITLE_TAGS = ("h1", "h2", "h3", "h4", "h5")

    def handle_starttag(self, tag, attrs):
        if tag == "html":
            self.stored_titles = []
            self.in_title = None
            self.first_title_data = None
        elif tag in MyHTMLParser.TITLE_TAGS:
            self.in_title = tag
        elif tag == "a" and self.in_title:
            dict_attrs = dict(attrs)
            self.stored_titles.append(
                (self.in_title, self.first_title_data, dict_attrs["href"])
            )

    def handle_endtag(self, tag):
        if tag in MyHTMLParser.TITLE_TAGS:
            self.in_title = None
            self.first_title_data = None

    def handle_data(self, data):
        if self.in_title and self.first_title_data is None:
            self.first_title_data = data


class HtmlTocGenerator():
    """
    Récupère tous les tags de titre, convertit ceci:
    <h2 id="configuration-json">Configuration json <a class="header-anchor" href="#configuration-json">&#x1F517;</a></h2>
    en ceci:
    <a href="#configuration-json"><h2>Configuration json</h2></a>
    """

    COMPONENT_START = (
        "<template>\n"
        "    <div class=\"doc-toc\">\n"
        "\n"
    )

    COMPONENT_END = (
        "\n"
        "    </div>\n"
        "</template>\n"
        "\n"
        "<style lang=\"css\" scoped src=\"@/styles/docToc.css\"></style>\n"
    )

    HREF_FIRST_TOC_LINK = "#doc-start"

    def __init__(self, html_content, html_toc_filepath):
        self.html_content = html_content
        self.html_toc_filepath = html_toc_filepath
        self.html_toc = ""

    def generate(self):
        parser = MyHTMLParser()
        html_content_as_html = "<html>" + self.html_content + "</html>"
        parser.feed(html_content_as_html)
        self.stored_titles = parser.stored_titles
        # Le premier lien dans le sommaire doit avoir un href spécial.
        tag, title_text, _ = self.stored_titles[0]
        self.stored_titles[0] = (
            tag,
            title_text,
            HtmlTocGenerator.HREF_FIRST_TOC_LINK
        )
        # TODO: il faut imbriquer les titres dans des divs.
        # Comme ça on pourrait faire du CSS plus sympa avec des décalages, des cadres imbriqués, etc.
        for title_data in self.stored_titles:
            self.html_toc += self._html_code_from_title_data(title_data)

    def write_html_toc_file(self):
        html_toc_as_component = (
            HtmlTocGenerator.COMPONENT_START +
            self.html_toc +
            HtmlTocGenerator.COMPONENT_END
        )
        self.html_toc_filepath.write_text(html_toc_as_component)

    def _html_code_from_title_data(self, title_data):
        tag, title_text, title_id = title_data
        html_title = f'<a href="{title_id}"><{tag}>{title_text}</{tag}></a>\n'
        return html_title


class ArticleGenerator():

    OUT_PATH = Path(
        "..",
        "..",
        "squarity-code",
        "src",
        "components",
        "docarticles",
    )

    def __init__(self, markdown_filepath, article_name, generate_toc=True):
        self.markdown_filepath = Path(markdown_filepath)
        self.article_name = article_name
        self.generate_toc = generate_toc

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
        if self.generate_toc:
            html_toc_generator = HtmlTocGenerator(
                self.html_content,
                self.html_toc_filepath
            )
            html_toc_generator.generate()
            html_toc_generator.write_html_toc_file()

    def _compute_out_filepaths(self):
        content_filename = self.article_name + ".vue"
        toc_filename = self.article_name + "Toc.vue"
        out_path = ArticleGenerator.OUT_PATH
        self.html_content_filepath = out_path / content_filename
        self.html_toc_filepath = out_path / toc_filename

    def _read_markdown(self):
        self.markdown_text = self.markdown_filepath.read_text()


def main():
    DOCS_TO_GENERATE = (
        ("../user_manual/main_doc_v2.md", "MainDocV2", True),
        ("../user_manual/share_your_game.md", "ShareYourGame", False),
        ("../user_manual/choose_version.md", "ChooseVersion", True),
        ("../user_manual/main_doc_v1.md", "MainDocV1", True),
        ("../user_manual/tutoriel_sokoban.md", "TutorielSokobanV1", True),
    )
    for markdown_filepath, article_name, generate_toc in DOCS_TO_GENERATE:
        article_generator = ArticleGenerator(
            markdown_filepath,
            article_name,
            generate_toc,
        )
        article_generator.generate_all()
    print("It is done")

if __name__ == "__main__":
    main()

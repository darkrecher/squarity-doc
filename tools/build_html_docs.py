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

    md = (
        MarkdownIt('commonmark', {'breaks':True,'html':True})
        .use(front_matter_plugin)
        .use(anchors_plugin, max_level=5, permalink=True)
        .enable('table')
    )

    tokens = md.parse(text)
    html_text = md.render(text)

    Path("output.html").write_text(html_text)


if __name__ == "__main__":
    main()

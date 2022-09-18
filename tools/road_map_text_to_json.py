import os
import logging
import json

PATH_FILE_SOURCE = os.path.join("..", "road_map.md")
PATH_FILE_DEST = os.path.join(
    "..", "..", "squarity-code", "public", "road_map_data.json"
)

INDEXES_CHAPTER_TO_SKIP = [0]

ID_FROM_CHAPTER_TITLES = {
    "IDE, Environnement de développement": "i",
    "Éditeur de niveaux, gestion des tilesets": "l",
    "Moteur du jeu": "g",
    '"Effets spéciaux"': "e",
    "Tutoriels, manuels, conseils": "t",
    "Contenu et promotion": "c",
    "Social et site web": "s",
    "Auto-formation, Optimisation": "o",
}

MAP_SQUARES = [
    "    ... g11 ... ... g14 ... ... ... ... ...",
    "... ... g10 g07 g12 g08 ... ... ... ... ...",
    "... e06 g05 g06 g16 g03 g15 i03 i05 ... ...",
    "... e05 e02 g17 g13 G02 i06 i07 ... ... ...",
    "e08 e07 e03 e01 g09 G01 g04 i04 i02 ... ...",
    "... ... t04 e04 e00 g00 i00 i01 i08 l04 l05",
    "... t05 t02 T01 t00 #00 l00 l01 l02 l03 ...",
    "... ... ... t03 c00 s00 o00 l06 l07 l08 ...",
    "... ... C04 c02 C01 s01 O01 o02 o03 ... ...",
    "... ... ... c03 s05 s02 s03 o04 o05 ... ...",
    "... ... ... s08 s06 s10 s04 o06 ... ... ...",
    "... ... ... ... s09 ... s07 s11 ... ... ...",
    "... ... ... ... ... ... s12 ... ... ... ...",
]

HTML_CLASS_FROM_ID = {
    "g": "game-engine",
    "s": "social",
    "e": "special-effect",
    "i": "ide",
    "t": "tuto",
    "l": "level",
    "c": "promo",
    "o": "optim",
}

HARDCODED_SQUARE_DEFINITIONS = [
    {
        "key": "#00",
        "rank": "origin",
        "html_class": "road-map-origin",
        "description": ""
        "C'est la road-map de Squarity. Elle n'est pas linéaire.\n"
        'C\'est une "road-square-map".\n\n'
        "Cliquez sur les autres carrés pour avoir des précisions sur les fonctionnalités prévues.\n",
        "link_url": "https://github.com/darkrecher/squarity-doc/blob/master/road_map.md",
        "link_text": 'Lien vers la road-map version "document normal".',
    },
    {
        "key": "e00",
        "rank": "superior",
        "html_class": "special-effect superior-square",
        "title": '\n"Effets spéciaux"',
        "gif_vision": "dancing-banana-gif-moving-5.gif",
    },
    {
        "key": "g00",
        "rank": "superior",
        "html_class": "game-engine superior-square",
        "title": "\nMoteur du jeu",
        "gif_vision": "dancing-banana-gif-moving-5.gif",
    },
    {
        "key": "i00",
        "rank": "superior",
        "html_class": "ide superior-square",
        "title": "Environnement de dév. intégré",
        "gif_vision": "dancing-banana-gif-moving-5.gif",
    },
    {
        "key": "t00",
        "rank": "superior",
        "html_class": "tuto superior-square",
        "title": "Tutoriels\n\nDocs\n\nExemples",
        "gif_vision": "dancing-banana-gif-moving-5.gif",
    },
    {
        "key": "l00",
        "rank": "superior",
        "html_class": "level superior-square",
        "title": "Éditeur de niveaux\n\nGestion des tilesets",
        "gif_vision": "dancing-banana-gif-moving-5.gif",
    },
    {
        "key": "c00",
        "rank": "superior",
        "html_class": "promo superior-square",
        "title": "Contenu\n\nJeux\n\nPromotion",
        "gif_vision": "dancing-banana-gif-moving-5.gif",
    },
    {
        "key": "s00",
        "rank": "superior",
        "html_class": "social superior-square",
        "title": "\nSocial\n\nSite web",
        "gif_vision": "dancing-banana-gif-moving-5.gif",
    },
    {
        "key": "o00",
        "rank": "superior",
        "html_class": "optim superior-square",
        "title": "Auto-formation\n\nOptimisation",
        "gif_vision": "dancing-banana-gif-moving-5.gif",
    },
]


class RoadMapConverter:
    def __init__(self, html_class_from_id, map_squares, hardcoded_square_definitions):
        logging.basicConfig(level=logging.INFO)
        self.html_class_from_id = html_class_from_id
        self.map_squares = map_squares
        self.hardcoded_square_definitions = hardcoded_square_definitions

        all_sub_ids = " ".join(map_squares)
        self.done_sub_chapter_ids = [
            sub_chapter_id.lower()
            for sub_chapter_id in all_sub_ids.split()
            if sub_chapter_id[0].isupper()
        ]
        logging.info(f"done_sub_chapter_ids : {self.done_sub_chapter_ids}")
        all_sub_ids = set(all_sub_ids.lower().split())
        self.all_sub_ids = all_sub_ids

    def generate_one_subchapter_json(self, subchapter_text, complete_sub_id):
        title, new_line, sub_chapter_text = subchapter_text.partition("\n")
        html_class = self.html_class_from_id[complete_sub_id[0]]
        if complete_sub_id not in self.done_sub_chapter_ids:
            html_class += "-undone"

        subchapter_json_data = {
            "key": complete_sub_id,
            "rank": "normal",
            "html_class": html_class,
            "title": title.strip(),
            "description": sub_chapter_text.strip(),
        }
        return subchapter_json_data

    def generate_one_chapter_json(self, chapter_text, id_chapter):
        sub_id_index = 1
        subchapters_json_data = []
        subchapters = chapter_text.split("\n### ")
        # On supprime systématiquement le premier élément, qui n'est pas un sub-chapter,
        # mais un bout de texte avec
        # le titre principal, une description de la "vision" principale du chapitre, et rien de plus.
        subchapters = subchapters[1:]
        for subchapter in subchapters:

            complete_sub_id = f"{id_chapter}{sub_id_index:02d}"
            if complete_sub_id not in self.all_sub_ids:
                raise Exception(
                    f"L'identifiant de sous-chapitre {complete_sub_id} n'est pas dans la map_square."
                )
            subchapter_json_data = self.generate_one_subchapter_json(
                subchapter, complete_sub_id
            )
            subchapters_json_data.append(subchapter_json_data)
            sub_id_index += 1

        return subchapters_json_data

    def generate_map_squares(self):
        outputted_map_squares = [line.lower() for line in self.map_squares]
        return outputted_map_squares

    def convert_markdown_to_json(self, path_file_source, path_file_dest):

        all_subchapters_json_data = list(self.hardcoded_square_definitions)
        str_road_map_markdown = open(path_file_source, encoding="utf-8").read()

        chapters = str_road_map_markdown.split("\n## ")
        # On supprime systématiquement le premier élément, qui n'est pas un chapter,
        # mais un bout de texte avec le titre principal et rien de plus.
        chapters = chapters[1:]
        # Et ensuite on supprime les chapters qui ne décrivent pas la roadmap.
        chapters = [
            chap
            for index_chap, chap in enumerate(chapters)
            if index_chap not in INDEXES_CHAPTER_TO_SKIP
        ]
        logging.info(f"Nombre de chapitres principaux : {len(chapters)}")
        assert len(chapters) == 8

        for chapter in chapters:
            title, new_line, chapter_text = chapter.partition("\n")
            assert new_line
            title = title.strip()
            if title not in ID_FROM_CHAPTER_TITLES:
                raise Exception(
                    f"Le titre de chapitre {title} n'est pas dans la correspondance des titre <-> id."
                )
            id_chapter = ID_FROM_CHAPTER_TITLES[title]
            logging.info(f"Chapitre : {title}, id : {id_chapter}.")
            current_subchapters_json_data = self.generate_one_chapter_json(
                chapter_text, id_chapter
            )
            all_subchapters_json_data.extend(current_subchapters_json_data)

        final_data = {
            "map_squares": self.generate_map_squares(),
            "unordered_road_squares": all_subchapters_json_data,
        }
        file_dest = open(path_file_dest, "w", encoding="utf-8")
        file_dest.write(json.dumps(final_data, indent=2))
        file_dest.close()
        logging.info("Génération du json terminée.")


def main():
    road_map_converter = RoadMapConverter(
        HTML_CLASS_FROM_ID, MAP_SQUARES, HARDCODED_SQUARE_DEFINITIONS
    )
    road_map_converter.convert_markdown_to_json(PATH_FILE_SOURCE, PATH_FILE_DEST)


if __name__ == "__main__":
    main()

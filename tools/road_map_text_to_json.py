import os
import logging
import json

PATH_FILE_SOURCE = os.path.join("..", "road_map.md")

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
    "... e99 g05 g06 g16 g03 g15 i99 i99 ... ...",
    "... e99 e99 g17 g13 G02 i99 i99 ... ... ...",
    "e99 e99 e99 e99 g09 G01 g04 i99 i99 ... ...",
    "... ... t99 e99 e00 g00 i00 i01 i99 l99 l99",
    "... t99 t99 t99 t00 #00 l00 l99 l99 l99 ...",
    "... ... ... t99 c00 s00 o00 l99 l99 l99 ...",
    "... ... c99 c99 c99 s01 o99 o99 o99 ... ...",
    "... ... ... c99 s05 s02 s03 o99 o99 ... ...",
    "... ... ... s08 s06 s10 s04 o99 ... ... ...",
    "... ... ... ... s09 ... s07 s12 ... ... ...",
    "... ... ... ... ... ... s11 ... ... ... ...",
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


class RoadMapConverter:
    def __init__(self, html_class_from_id, map_squares):
        logging.basicConfig(level=logging.INFO)
        self.html_class_from_id = html_class_from_id
        self.map_squares = map_squares

        all_sub_ids = " ".join(map_squares)
        self.done_sub_chapter_ids = [
            sub_chapter_id
            for sub_chapter_id in all_sub_ids.split()
            if sub_chapter_id.isupper()
        ]
        all_sub_ids = set(all_sub_ids.lower().split())
        self.all_sub_ids = all_sub_ids
        # TODO : faudra générer un map_squares avec tout en lower.

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

    def convert_markdown_to_json(self, path_file_source):

        all_subchapters_json_data = []
        str_road_map_markdown = open(PATH_FILE_SOURCE, encoding="utf-8").read()

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
            # TODO crap un seul pour le moment.
            if id_chapter in ("g", "s"):
                current_subchapters_json_data = self.generate_one_chapter_json(
                    chapter_text, id_chapter
                )
                all_subchapters_json_data.extend(current_subchapters_json_data)
        print(json.dumps(all_subchapters_json_data))

        logging.info("Génération du json terminée.")


def main():
    road_map_converter = RoadMapConverter(HTML_CLASS_FROM_ID, MAP_SQUARES)
    road_map_converter.convert_markdown_to_json(PATH_FILE_SOURCE)


if __name__ == "__main__":
    main()

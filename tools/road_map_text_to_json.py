"""
Ce script ne prend pas de paramètres. Les emplacements des fichiers d'entrée et de sortie sont
définis en dur, parce que pas besoin de plus.

Ce script lit le fichier markdown "road_map.md", qui est présent dans la racine du repository squarity-doc.

Il écrit le fichier json road_map_data.json, qui est présent dans le repository squarity-code.
Ce fichier json est nécessaire au site Squarity, pour afficher la road-map.

Les titres de niveau 3 du fichier markdown et les textes des chapitre sont utilisés pour définir
les carrés de la road-map (titre et description).

Si la dernière ligne d'un texte de chapitre est une url (débute par "http"), alors la description
du carré correspondant comportera un lien, placé à la fin.

 - La dernière ligne du texte du chapitre est utilisée pour l'url du lien
 - L'avant-dernière ligne du texte du chapitre est utilisée pour le texte du lien.

Le premier titre de niveau 2 et tout son contenu ne sont pas lus par ce script. On peut y mettre
tout ce qu'on veut, ça restera dans le markdown.

Le "carré original" (celui qui est placé au milieu de la road-map), et les 8 carrés "superior"
ne sont pas définis par le markdown, mais par des infos en dur définies dans ce code
(voir variable HARDCODED_SQUARE_DEFINITIONS).

Pour des infos plus détaillées sur la disposition des carrés dans la road-map, et sur la
manière dont le fichier markdown doit être écrit, voir les commentaires des variables
ID_FROM_CHAPTER_TITLES, MAP_SQUARES, VISION_GIF_FILES.
"""

import os
import logging
import json

PATH_FILE_SOURCE = os.path.join("..", "road_map.md")
PATH_FILE_DEST = os.path.join(
    "..", "..", "squarity-code", "public", "road_map_data.txt"
)

INDEXES_CHAPTER_TO_SKIP = [0]

# Correspondance entre les titres de chapitre et leurs identifiants internes
# Attention, ces titres de chapitre doivent correspondre exactement aux titres de niveau 2
# qui sont écrits dans le fichier markdown. Sinon ça lève une vilaine exception.
ID_FROM_CHAPTER_TITLES = {
    "IDE, Environnement de développement": "i",
    "Éditeur de niveaux, gestion des tilesets": "l",
    "Moteur du jeu": "g",
    '"Effets spéciaux"': "e",
    "Tutoriels, docs, exemples": "t",
    "Contenu et promotion": "c",
    "Social et site web": "s",
    "Auto-formation, Optimisation": "o",
}

# Carte des carrés tels qu'ils seront représentés dans la road-map du site.
# La première lettre correspond à la catégorie du carré (voir dictionnaire ID_FROM_CHAPTER_TITLES),
# si la lettre est minuscule, le carré est considéré comme non fait (sa couleur sera terne),
# en majuscule, le carré est fait (couleur vive).
# Le numéro juste après permet d'identifier le carré dans sa catégorie.
# 00 : le "superior square" indiquant la catégorie concernée.
# une valeur supérieure à 1 : index du sous-chapitre (en comptant à partir de 1),
# dans le fichier markdown contenant les données d'entrée.
MAP_SQUARES = [
    "... ... g11 ... ... g14 ... ... ... ... ...",
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

# Nom des images gif pour les carrés spéciaux affichant des "visions", au lieu d'une description.
VISION_GIF_FILES = {
    "i05": "test_vision",
    "l08": "test_vision",
    "g05": "test_vision",
    "g11": "test_vision",
    "e07": "test_vision",
    "s04": "test_vision",
}

HARDCODED_SQUARE_DEFINITIONS = [
    {
        "key": "#00",
        "rank": "origin",
        "html_class": "road-map-origin",
        "description": ""
        "Squarity est développé par une équipe d'une seule personne. "
        "Il est donc difficile d'annoncer des dates de réalisation, ou même d'ordonner les priorités. "
        "C'est pourquoi la road-map est sous forme d'un quadrillage, où chaque carré représente une fonctionnalité. "
        "Aucun ordre précis ne peut être déduit.\n\n"
        "Les carrés de couleurs vives sont des fonctionnalités déjà faites (pour l'instant, il y en a assez peu...). "
        "Ceux de couleurs ternes sont des fonctionnalités à développer.\n\n"
        "Certains carrés afficheront des gif animés montrant des screenshot hypothétique de Squarity.\n"
        "Pour l'instant ces gifs ne sont pas finis, il faudra attendre encore un peu.\n"
        "La première étape de la road-map est de finir la road-map.\n\n",
        "link_url": "https://github.com/darkrecher/squarity-doc/blob/master/road_map.md",
        "link_text": "Lien vers la road-map en version texte, pour une lecture détaillée plus facile.",
    },
    {
        "key": "e00",
        "rank": "superior",
        "html_class": "special-effect superior-square",
        "title": '\n"Effets spéciaux"',
        "gif_vision": "special_effect",
    },
    {
        "key": "g00",
        "rank": "superior",
        "html_class": "game-engine superior-square",
        "title": "\nMoteur du jeu",
        "gif_vision": "game_engine",
    },
    {
        "key": "i00",
        "rank": "superior",
        "html_class": "ide superior-square",
        "title": "Environnement de dév. intégré",
        "gif_vision": "ide",
    },
    {
        "key": "t00",
        "rank": "superior",
        "html_class": "tuto superior-square",
        "title": "Tutoriels\n\nDocs\n\nExemples",
        "gif_vision": "tuto",
    },
    {
        "key": "l00",
        "rank": "superior",
        "html_class": "level superior-square",
        "title": "Éditeur de niveaux\n\nGestion des tilesets",
        "gif_vision": "level_editor",
    },
    {
        "key": "c00",
        "rank": "superior",
        "html_class": "promo superior-square",
        "title": "Contenu\n\nJeux\n\nPromotion",
        "gif_vision": "test_vision",
    },
    {
        "key": "s00",
        "rank": "superior",
        "html_class": "social superior-square",
        "title": "\nSocial\n\nSite web",
        "gif_vision": "test_vision",
    },
    {
        "key": "o00",
        "rank": "superior",
        "html_class": "optim superior-square",
        "title": "Auto-formation\n\nOptimisation",
        "gif_vision": "test_vision",
    },
]


class RoadMapConverter:
    def __init__(
        self,
        html_class_from_id,
        map_squares,
        vision_gif_files,
        hardcoded_square_definitions,
    ):
        logging.basicConfig(level=logging.INFO)
        self.html_class_from_id = html_class_from_id
        self.map_squares = map_squares
        self.vision_gif_files = vision_gif_files
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

        if title.startswith("Vision :"):
            title = title[len("Vision :") :]
            gif_vision = self.vision_gif_files[complete_sub_id]
            subchapter_json_data = {
                "key": complete_sub_id,
                "rank": "vision",
                "html_class": html_class,
                "title": title.strip(),
                "gif_vision": gif_vision,
            }
        else:
            description = sub_chapter_text.strip()
            subchapter_json_data = {
                "key": complete_sub_id,
                "rank": "normal",
                "html_class": html_class,
                "title": title.strip(),
                "description": description,
            }

            descrip_lines = description.split("\n")
            last_line = descrip_lines[-1]
            if last_line.startswith("http") and "//" in last_line:
                index_line_descrip = len(descrip_lines) - 2
                before_last_line = None
                while before_last_line is None:
                    if descrip_lines[index_line_descrip].strip():
                        before_last_line = descrip_lines[index_line_descrip].strip()
                    index_line_descrip -= 1
                subchapter_json_data["link_text"] = before_last_line
                subchapter_json_data["link_url"] = last_line
                subchapter_json_data["description"] = "\n".join(
                    descrip_lines[:index_line_descrip] + [""]
                )

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
        HTML_CLASS_FROM_ID, MAP_SQUARES, VISION_GIF_FILES, HARDCODED_SQUARE_DEFINITIONS
    )
    road_map_converter.convert_markdown_to_json(PATH_FILE_SOURCE, PATH_FILE_DEST)


if __name__ == "__main__":
    main()

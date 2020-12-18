# squarity.fr/#fetchez_githubgist_darkrecher/197b2c33e75a99763810e0a8c49e88bc/raw/sokopunk.txt

LEVEL_1 = (
    ".....####...........",
    "######..############",
    "######......#..#####",
    "###O##..###...O#####",
    "###+###.###.#O.#####",
    "#..O....+..O########",
    "#.#.#.....#.########",
    "#.#.################",
    "#..O...###..........",
    "#.#.#...............",
    "#...######..........",
    "####################",
    "....................",
    "....................",
)

class Ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.electrified = False
        self.char = "O"

    def __str__(self):
        return "Ball:%s,%s - %s" % (self.x, self.y, self.electrified)

    def electrify(self):
        self.electrified = True
        self.char = "*"

    def unelectrify(self):
        self.electrified = False
        self.char = "O"


class BoardModel():

    def __init__(self):
        self.w = 20 # width (largeur) : 20 cases
        self.h = 14 # height (hauteur) : 14 cases
        self.balls = []
        self.tiles = []
        for y in range(self.h):
            line = []
            for x in range(self.w):
                char_map = LEVEL_1[y][x]
                if char_map == "O":
                    line.append(["."])
                    self.balls.append(Ball(x, y))
                elif char_map == "+":
                    line.append([".", char_map])
                else:
                    line.append([char_map])
            self.tiles.append(line)
        self.arcs = [
            [
                []
                for x
                in range(self.w)
            ]
            for y in range(self.h)
        ]
        self.lady_coord = [6, 8]
        self.warn_about_arcs = True
        self.electrify_all_balls()

    def get_size(self):
        return self.w, self.h

    def get_tile_gamobjs(self, x, y):
        return self.tiles[y][x]

    def export_all_tiles(self):
        exported_tiles = [
            [
                self.tiles[y][x] + self.arcs[y][x]
                for x
                in range(self.w)
            ]
            for y in range(self.h)
        ]
        for ball in self.balls:
            exported_tiles[ball.y][ball.x].append(ball.char)
        x, y = self.lady_coord
        exported_tiles[y][x].append("lady")
        return exported_tiles

    def check_push_ball(self, ball_to_push, move_coord):
        ball_new_coord = (
            ball_to_push.x + move_coord[0],
            ball_to_push.y + move_coord[1],
        )
        x, y = ball_new_coord
        if x < 0 or x >= self.w or y < 0 or y >= self.h:
            return False
        dest_gamobjs = self.get_tile_gamobjs(*ball_new_coord)
        if {"#", "+"}.intersection(set(dest_gamobjs)):
            return False
        for ball in self.balls:
            if x == ball.x and y == ball.y:
                return False
        return True

    def check_no_wall_line_horiz(self, x_1, x_2, y):
        for x in range(x_1, x_2):
            if "#" in self.get_tile_gamobjs(x, y):
                return False
        return True

    def check_no_wall_line_vertic(self, x, y_1, y_2):
        for y in range(y_1, y_2):
            if "#" in self.get_tile_gamobjs(x, y):
                return False
        return True

    def check_electrification(self, ball):
        """
        Renvoie None si la balle à checker n'a pas à être électrifiée.
        Sinon, renvoie un tuple de 0, 1 ou 2 éléments :
          Chaque élément est un sous-tuple de 3 éléments :
            - la balle initiale
            - l'autre balle qui est sur la même ligne ou la même colonne
            - indication "horiz" ou "vertic" selon le type d'électrification.
        """
        elec_result = []

        # Liste de tuple de 2 sous-éléments :
        #  - distance entre la balle à vérifier et l'autre balle sur la même colonne.
        #  - l'objet Ball de l'autre balle sur la même colonne.
        balls_on_same_col = []
        # Pareil, mais pour les balles sur une même ligne.
        balls_on_same_line = []

        for other_ball in self.balls:

            # check horizontal.
            if ball.x == other_ball.x and ball.y < other_ball.y:
                if self.check_no_wall_line_vertic(ball.x, ball.y+1, other_ball.y):
                    balls_on_same_col.append((other_ball.y-ball.y, other_ball))

            # check vertical.
            if ball.y == other_ball.y and ball.x < other_ball.x:
                if self.check_no_wall_line_horiz(ball.x+1, other_ball.x, ball.y):
                    balls_on_same_line.append((other_ball.x-ball.x, other_ball))

        if balls_on_same_col:
            dist, other_ball_col = min(balls_on_same_col, key=lambda e:e[0])
            ball.electrify()
            other_ball_col.electrify()
            elec_result.append((ball, other_ball_col, "vertic"))

        if balls_on_same_line:
            dist, other_ball_line = min(balls_on_same_line, key=lambda e:e[0])
            ball.electrify()
            other_ball_line.electrify()
            elec_result.append((ball, other_ball_line, "horiz"))

        return tuple(elec_result)

    def electrify_all_balls(self):
        # On déselectrifie toutes les boules.
        for ball in self.balls:
            ball.unelectrify()
        # On enlève tous les arcs.
        self.arcs = [
            [
                []
                for x
                in range(self.w)
            ]
            for y in range(self.h)
        ]
        # On re-electrifie
        for ball in self.balls:
            elec_result = self.check_electrification(ball)
            for ball_1, ball_2, elec_dir in elec_result:
                if elec_dir == "horiz":
                    for x in range(ball_1.x+1, ball_2.x):
                        self.arcs[ball_1.y][x].append("l_horiz")
                else:
                    for y in range(ball_1.y+1, ball_2.y):
                        self.arcs[y][ball_1.x].append("l_vertic")


    def on_game_event(self, event_name):
        # print("on_game_event", event_name)
        if event_name in ("action_1", "action_2"):
            print("Les boutons d'actions ne servent à rien dans ce jeu")
            return

        move_coord = squarity.MOVE_FROM_DIR.get(event_name)
        if move_coord is None:
            return

        lady_new_coord = (
            self.lady_coord[0] + move_coord[0],
            self.lady_coord[1] + move_coord[1],
        )
        x, y = lady_new_coord
        if x < 0 or x >= self.w or y < 0 or y >= self.h:
            return
        dest_gamobjs = self.get_tile_gamobjs(*lady_new_coord)
        if {"#", "+"}.intersection(set(dest_gamobjs)):
            return
        if self.arcs[y][x]:
            if self.warn_about_arcs:
                print("Vous ne pouvez pas vous déplacer dans les arcs électriques")
                self.warn_about_arcs = False
            return

        ball_to_push = None
        can_push_ball = False
        for ball in self.balls:
            if x == ball.x and y == ball.y:
                ball_to_push = ball
                break

        if ball_to_push:
            can_push_ball = self.check_push_ball(ball_to_push, move_coord)
            if not can_push_ball:
                return

        self.lady_coord = lady_new_coord

        if can_push_ball:
            ball_to_push.x += move_coord[0]
            ball_to_push.y += move_coord[1]
            self.electrify_all_balls()



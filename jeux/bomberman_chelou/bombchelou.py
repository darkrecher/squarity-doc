# https://i.imgur.com/YVPdCXR.png
"""
{
    "tile_size": 320,
    "img_coords": {
        "herbe": [0, 0],
        "mur": [320,0],
        "boite": [640,0],
        "joueur": [0,320],
        "cible": [320,320],
        "feu": [640,320]
    }
}
"""

import re

# Vous vous déplacez, des cibles apparaissent derrière vous de plus en plus vite, si vous marchez sur une cible vous perdez de la vie.
# Vous pouvez poser des bombes, qui sont dangereuses, mais qui suppriment les cibles sur le sol.
# Plus vous tenez longtemps, plus vous avez un bon score.
# Bonne chance.

class Bomb():

    bombId = 0

    def __init__(self, x, y, ticks):
        print("New Bomb !" + str(self.bombId))
        self.id = self.bombId
        Bomb.bombId += 1
        self.x = x
        self.y = y
        self.ticks = ticks

class GameModel():

    def __init__(self):

        self.w = 20 # width (largeur) : 10 cases
        self.h = 14 # height (hauteur) : 10 cases
        self.tiles = []
        self.startPosX = 1
        self.startPosY = 1
        self.health = 10
        self.start = True
        self.alive = True

        self.score = 0

        for y in range(self.h):
            line = []
            for x in range(self.w):
                game_objects = ["herbe"]
                line.append(game_objects)
            self.tiles.append(line)

        self.curr_posX = self.startPosX
        self.curr_posY = self.startPosY
        self.tiles[self.curr_posY][self.curr_posX].append("joueur")

        self.bombes = []

    def export_all_tiles(self):
        return self.tiles

    def clampPos(self, rawPos, direction):
        if direction == "X":
            return min(max(0, rawPos), self.w - 1)
        elif direction == "Y":
            return min(max(0, rawPos), self.h - 1)

    def plantBomb(self):
        if "boite" in self.tiles[self.curr_posY][self.curr_posX]:
            print("Il y a déjà une bombe")
        elif len(self.bombes) >= 3:
            print("Vous n'avez plus de bombes pour l'instant")
        else:
            b = Bomb(self.curr_posX, self.curr_posY, 5)
            self.bombes.append(b)
            self.tiles[b.y][b.x].append("boite")
            print("Planting Bomb")
            return """{ "delayed_actions": [ {"name": "bombtick_""" + str(b.id) + """", "delay_ms": 500} ] }"""

    def tickBomb(self, id):
        bombe = None
        for b in self.bombes:
            if str(b.id) == str(id):
                bombe = b

        if bombe is None:
            return None

        bombe.ticks -= 1
        if bombe.ticks > 0:
            return """{ "delayed_actions": [ {"name": "bombtick_""" + str(bombe.id) + """", "delay_ms": 500} ] }"""
        else:
            self.tiles[bombe.y][bombe.x].remove("boite")
            self.bombes.remove(bombe)
            return self.deflagration(bombe)

    def deflagration(self, bombe):
        for i in range(0,self.h):
            self.tiles[i][bombe.x].append("feu")
        for i in range(0,self.w):
            self.tiles[bombe.y][i].append("feu")
        return """{ "delayed_actions": [ {"name": "explosionVanish_""" + str(bombe.x) + ":" + str(bombe.y)+ """", "delay_ms": 2000} ] }"""

    def on_game_event(self, event_name):
        # Décommentez la ligne ci-dessous pour afficher une ligne d'info
        # à chaque fois que le joueur appuie sur une touche.
        # print("on_game_event", event_name)
        # print("player tile", self.tiles[self.curr_posY][self.curr_posX])

        if not self.alive:
            for y in range(self.h):
                for x in range(self.w):
                    self.tiles[y][x] = ["mur"]
            return None


        if self.start:
            self.start = False
            self.previousPos_X = self.curr_posX
            self.previousPos_Y = self.curr_posY
            return """{ "delayed_actions": [ {"name": "tickMove_400", "delay_ms": 400} ] }"""

        if re.search("tickMove_\d+", event_name):
            self.score += 1
            self.tiles[self.previousPos_Y][self.previousPos_X].append("cible")
            self.previousPos_X = self.curr_posX
            self.previousPos_Y = self.curr_posY
            prevDelay = int(re.search("\d+", event_name)[0])
            self.score += 1
            return """{ "delayed_actions": [ {"name": "tickMove_""" + str(prevDelay - 1) + """", "delay_ms": """ + str(prevDelay - 1) + """} ] }"""


        if "cible" in self.tiles[self.curr_posY][self.curr_posX] or "feu" in self.tiles[self.curr_posY][self.curr_posX]:
            self.health -= 1
            print("Vie restante : " + str(self.health))
            if self.health <= 0:
                print("You Lost !")
                print("Your score is " + str(self.score))
                self.alive = False

        nextPosX_Raw = self.curr_posX
        nextPosY_Raw = self.curr_posY
        hasMoved = False

        if re.search("explosionVanish_", event_name):
            explosionCoordinates = re.search("\d+:\d+", event_name)[0].split(":")
            for i in range(0,self.h):
                self.tiles[i][int(explosionCoordinates[0])] = list(filter(lambda a: a not in ["cible", "feu"], self.tiles[i][ int(explosionCoordinates[0]) ]))
            for i in range(0,self.w):
                self.tiles[int(explosionCoordinates[1])][i] = list(filter(lambda a: a not in ["cible", "feu"], self.tiles[ int(explosionCoordinates[1]) ][i]))

        if re.search("bombtick_\d+", event_name):
            return self.tickBomb(re.search("\d+", event_name)[0])

        if event_name == "action_1":
            a = self.plantBomb()
            # For Debug
            # print(a)
            return a

        if event_name in ["U","D","R","L"]:
            hasMoved = True
            if event_name == "U":
                nextPosY_Raw -= 1
            if event_name == "D":
                nextPosY_Raw += 1
            if event_name == "L":
                nextPosX_Raw -= 1
            if event_name == "R":
                nextPosX_Raw += 1

        nextPosX = self.clampPos(nextPosX_Raw, "X")
        nextPosY = self.clampPos(nextPosY_Raw, "Y")


        # Déplacer le joueur
        if hasMoved:
            self.tiles[self.curr_posY][self.curr_posX].remove("joueur")

            self.curr_posX = nextPosX
            self.curr_posY = nextPosY

            self.tiles[self.curr_posY][self.curr_posX].append("joueur")

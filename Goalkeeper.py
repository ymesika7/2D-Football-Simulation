from Player import Player


# Change the color to be different from the other players
def getDarkerColor(color):
    dark_color = ''.join(str(color))
    x = dark_color[dark_color.index('(') + 1:dark_color.index(',')]
    sub_str = dark_color[dark_color.index(',') + 1:dark_color.index(')') + 1]
    z = sub_str[sub_str.index(',') + 2:-1]
    newColor = (int(x), 255, int(z))
    return newColor


class Goalkeeper(Player):
    def __init__(self, locations, color):
        Player.__init__(self, locations, getDarkerColor(color))

from Ball import Ball
from Team import Team as Team
from constants import Color


class FieldManagement:
    def __init__(self, filename):
        team1, team2, ball = [], [], []
        checkIndex = -1

        with open(filename, 'r') as file:  # Copy the data from the file to temporary list
            for line in file:
                if checkIndex >= 0:
                    if checkIndex % self._numOfPlayers < teamSize:
                        team1.append(line[:-1])
                    elif (self._numOfPlayers - 1) > (checkIndex % self._numOfPlayers) >= teamSize:
                        team2.append(line[:-1])
                    else:
                        ball.append(line[:-1])
                else:
                    self._numOfPlayers = int(line[:-1])
                    teamSize = (self._numOfPlayers - 1) / 2
                    teamSize = int(teamSize)

                checkIndex += 1

        if team1.__len__() == 0 or team2.__len__() == 0 or ball.__len__() == 0:
            print("failed open file")
            return None

        self._objects = []
        self._objects.append(Team(Color.FIRST_TEAM, teamSize, team1))
        self._objects.append(Team(Color.SEC_TEAM, teamSize, team2))
        self._objects.append(Ball(Color.BALL, ball))

    def isNotEmpty(self):
        """ Check if any of the objects in the list(self._objects) reach to his end.
                :returns False : If none of the objects reach to his end
                         True : Otherwise
            """
        for i in range(self._objects.__len__()):
            if not self._objects[i].isNotEmpty():
                return False
        return True

    def updateField(self, frame):
        """ Print all the current data to the field sketch.
            :param frame: (cv2.frame) empty copy of the field sketch
            :return frame : the frame after all of the objects was printed
        """
        for i in range(self._objects.__len__()):
            frame = self._objects[i].printObj(frame)
        return frame

import cv2
from constants import Color


class DrawableObjects:
    def __init__(self, color, size=14, arrow_color=Color.BLACK):
        self._size = size
        self._color = color
        self._arrow_color = arrow_color

    def printObject(self, frame, current_location):
        """ Print the current data of the object to the field sketch.
                :param current_location: Current location of the object
                :param frame: (cv2.frame) copy of the field sketch
                :return frame : the frame after the object was printed
            """
        cv2.circle(frame, eval(current_location), self._size, self._color, -1)
        cv2.circle(frame, eval(current_location), self._size, Color.BLACK, 1)
        return frame

    def printObjectDirection(self, frame, start_point, end_point):
        """ Print arrow that indicate on the movement of the object to the field sketch.
                :param start_point: Start point to draw the arrow
                :param end_point: End point to draw the arrow
                :param frame: (cv2.frame) copy of the field sketch
                :return frame : the frame after the object was printed
            """
        cv2.arrowedLine(frame, start_point, end_point,
                        self._arrow_color, 2, tipLength=3)
        return frame

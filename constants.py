# Constants for the project


# Used all over the project
class Color(object):
    FIRST_TEAM = (220, 83, 61)
    SEC_TEAM = (40, 74, 255)
    BALL = (255, 255, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)


# Used to fix deviation from the video to the sketch field (xGAnalytic.py)
class SHIFTING(object):
    X_SHIFTING = 90
    Y_SHIFTING = 200


# How to use the app, starting instruction (xGAnalytic.py)
HOW_TO = "\n\n[IMPORTANT] HowTo:" + \
         "\nNote: To to approve your object selection please press twice on the SPACE bar.\n" + \
         "       You have to choose equal number of players from each team.\n\n" + \
         "       1. Mark the goalkeeper of the first team\n" + \
         "       2. Mark the field players of the first team\n" + \
         "       3. Repeat the last two steps for the second team\n" + \
         "       4. Mark the ball\n" + \
         "       5. Press SPACE bar and then 'q' to quit selecting boxes and start tracking\n"
        

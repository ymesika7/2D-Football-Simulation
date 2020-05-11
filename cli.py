import argparse
import logging
from players_detection import DetectThePlayers



class Cli:

    def __init__(self):
        self.args = None
        logger = logging.getLogger(__name__)
        self.logger=logger


    def parse_arguments_advanced(self):
        """ Processing and storing the arguments of the program
            returns an argparse.Nampespace object, depicting and store the input arguments
            according to the defined flags
        """
        self.logger.info(f"parsing arguments")
        parser = argparse.ArgumentParser(
            description="Script Description"
        )
        parser.add_argument("-i", "--input", required=True,help="path to input video")
        self.args = parser.parse_args()

    def args_handel(self):
        """ The function handles the arguments """
        video_path = self.args.input
        detection = DetectThePlayers(video_path,self.logger)
        detection.run()
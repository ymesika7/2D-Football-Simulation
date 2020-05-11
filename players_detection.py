import sys
import cv2
import time
import tryModel
from constants import SHIFTING, HOW_TO
import os


class DetectThePlayers(object):
    def __init__(self, video_path, logger):
        self.logger = logger
        self._videoPath = video_path
        self._filename = "players_locations" + time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime()) + ".txt"
        self._outputPath = self._videoPath[:-4] + "_To2D_" + time.strftime("%Y-%m-%d-%H-%M-%S",
                                                                        time.gmtime()) + ".mp4"
        self._cap = None


    def check_validity_input(self):
        self.logger.info("check_validity_input")
        if self._videoPath is None:
            self.logger.error("""no input file was recognized, please repeat and enter valid game file name"
                     including .mp4 suffix""")
            sys.exit()
        elif not str(self._videoPath).endswith(".mp4"):
            self.logger.error("game file has to mp4 format,please repeat and enter valid game file")
            sys.exit()
        elif not os.path.exists(self._videoPath):
            self.logger.error("game file is not exist, check the name you entered")
            sys.exit()
        else:
            self.logger.info("input is valid")
            return

    def set_capture_object(self):
        self.logger.info("set capture_object from the given game file")
        try:
            # Create a video capture object to read videos
            self._cap = cv2.VideoCapture(self._videoPath)
            # Read first frame
            success, self._frame = self._cap.read()
            # quit if unable to read the video file
            if not success:
                sys.exit('Failed to read video')
        except:
            self.logger.error("can't read the given file")
            sys.exit()



    def run(self):
        self.check_validity_input()
        self.set_capture_object()
        self.logger.info("running the program")
        with open(self._filename, 'w') as file:
            # Select boxes
            bboxes = []
            self.logger.info(HOW_TO)

            # OpenCV's selectROI function doesn't work for selecting multiple objects in Python
            # So we will call this function in a loop till we are done selecting all objects
            while True:
                # draw bounding boxes over objects
                # selectROI's default behaviour is to draw box starting from the center
                # when fromCenter is set to false, you can draw box starting from top left corner
                bbox = cv2.selectROI('MultiTracker', self._frame)
                bboxes.append(bbox)
                k = cv2.waitKey(0) & 0xFF
                if k == 113:  # q is pressed
                    if bboxes.__len__() > 2:
                        break
                    else:
                        self.logger.error("\n--At least three objects have to be marked to continue--\n")
            cv2.destroyAllWindows()
            if bboxes.__len__() % 2 == 0:
                self.logger.error("\n--Illegal input. pleas try again.")
                sys.exit(1)

            self.info('Selected bounding boxes {}'.format(bboxes))

            # Create MultiTracker object
            multiTracker = cv2.MultiTracker_create()

            # Initialize MultiTracker
            for bbox in bboxes:
                multiTracker.add(cv2.TrackerCSRT_create(), self._frame, bbox)

            # Write the number of bbox the user choose
            file.write(str(bboxes.__len__()) + "\n")
            firstFrame = True
            tic = time.perf_counter()
            # Process video and track objects
            while self._cap.isOpened():
                success, frame = self._cap.read()
                if not success:
                    break

                # get updated location of objects in subsequent frames
                success, boxes = multiTracker.update(frame)
                # draw tracked objects
                for i, newbox in enumerate(boxes):
                    center = ((int(newbox[0] + (int(newbox[2]) / 2))) - SHIFTING.X_SHIFTING,
                              (int(newbox[1] + (int(newbox[3]) / 2))) - SHIFTING.Y_SHIFTING)
                    file.write(str(center) + "\n")

                # some information on processing single frame
                if firstFrame:
                    firstFrame = False
                    toc = time.perf_counter()
                    totalFrames = int(self._cap.get(cv2.CAP_PROP_FRAME_COUNT))
                    self.logger.info("single frame took %.4f seconds" % (toc - tic))
                    self.logger.info(f"{totalFrames} total frames in video")
                    self.logger.info("Estimated time to finish: {}".format(
                        time.strftime('%H:%M:%S', time.gmtime((toc - tic) * totalFrames))))

        file.close()
        toc = time.perf_counter()
        self.logger.info("Finish detection in {}".format(time.strftime('%H:%M:%S', time.gmtime((toc - tic)))))
        tryModel.tryModel(self._filename, self._outputPath)
        toc = time.perf_counter()
        self.logger.info("Finish model in {}".format(time.strftime('%H:%M:%S', time.gmtime((toc - tic)))))

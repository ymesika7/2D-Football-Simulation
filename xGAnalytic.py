import argparse
import sys
import time as t
import cv2
import time
import tryModel
from constants import SHIFTING, HOW_TO


class DetectThePlayers(object):
    def __init__(self):
        # construct the argument parse and parse the arguments
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--input", required=True,
                        help="path to input video")
        args = vars(ap.parse_args())

        # Set video to load
        self._videoPath = args["input"]
        # Create a video capture object to read videos
        self._cap = cv2.VideoCapture(self._videoPath)
        # Read first frame
        success, self._frame = self._cap.read()
        # quit if unable to read the video file
        if not success:
            print('Failed to read video')
            sys.exit(1)

        self._filename = "players_locations" + t.strftime("%Y-%m-%d-%H-%M-%S", t.gmtime()) + ".txt"
        self._outputPath = self._videoPath[:-4] + "_To2D_" + t.strftime("%Y-%m-%d-%H-%M-%S", t.gmtime()) + ".mp4"

    """ The main function executes the program """

    def run(self):
        with open(self._filename, 'w') as file:
            # Select boxes
            bboxes = []
            print(HOW_TO)

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
                        print("\n--At least three objects have to be marked to continue--\n")
            cv2.destroyAllWindows()
            if bboxes.__len__() % 2 == 0:
                print("\n[Error] Illegal input. pleas try again.")
                sys.exit(1)

            print('Selected bounding boxes {}'.format(bboxes))

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
                    print("\n[INFO] single frame took %.4f seconds" % (toc - tic))
                    print("[INFO] {} total frames in video".format(totalFrames))
                    print("[INFO] Estimated time to finish: {}".format(
                        time.strftime('%H:%M:%S', time.gmtime((toc - tic) * totalFrames))))

        file.close()
        toc = time.perf_counter()
        print("[INFO] Finish detection in {}".format(time.strftime('%H:%M:%S', time.gmtime((toc - tic)))))
        tryModel.tryModel(self._filename, self._outputPath)
        toc = time.perf_counter()
        print("[INFO] Finish model in {}".format(time.strftime('%H:%M:%S', time.gmtime((toc - tic)))))


if __name__ == '__main__':
    DetectThePlayers().run()

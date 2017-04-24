import os
import cv2
import tempfile
import numpy as np
import pytesseract
from PIL import Image
from resizeimage import resizeimage


class CaptureUtil:
    """
    Wrapper class for pytesseract and binary.

    """
    def __init__(self):
        """
        Constructor takes no argument.
        """
        self.path = tempfile.mkdtemp()

    def get_string(self, img_path):
        """
        Return all strings in an image as a string.

        """
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kernel = np.ones((1, 1), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)
        cv2.imwrite(os.path.join(self.path, "removed_noise.png"), img)
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY, 11, 2)
        cv2.imwrite(os.path.join(self.path, "thres.png"), img)
        result = pytesseract.image_to_string(Image.open(os.path.join(self.path, "thres.png")))
        return result

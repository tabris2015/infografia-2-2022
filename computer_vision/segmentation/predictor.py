import cv2
import mediapipe as mp
import numpy as np
from PIL import Image


class SelfiePredictor:
    def __init__(self, bg_color=(192, 192, 192)):
        self.bg_color = bg_color
        self.mp_draw = mp.solutions.drawing_utils
        self.selfie_segmentation = mp.solutions.selfie_segmentation.SelfieSegmentation(model_selection=0)

    def predict_file(self, file):
        img = np.array(Image.open(file))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.selfie_segmentation.process(img)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
        bg_image = np.zeros(img.shape, dtype=np.uint8)
        bg_image[:] = self.bg_color
        output_image = np.where(condition, img, bg_image)
        return output_image

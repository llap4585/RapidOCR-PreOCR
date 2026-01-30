# -*- coding: utf-8 -*-
# @Author: llap4585
# @Project: RapidOCR-PreOCR
# @License: Apache-2.0
# @GitHub: https://github.com/llap4585/RapidOCR-PreOCR

import cv2
from rapidocr import RapidOCR

def preprocess_for_rapidocr(img_path, save_path=None):
    img = cv2.imread(img_path)

    # 1. Grayscale conversion
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2. Slight denoising (without destroying edges)
    denoised = cv2.GaussianBlur(gray, (3, 3), 0)

    # 3. Gentle contrast enhancement (Critical step)
    clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(16, 16))
    enhanced = clahe.apply(denoised)

    if save_path:
        cv2.imwrite(save_path, enhanced)

    return enhanced


if __name__ == "__main__":
    img_path = ""  # Enter your input image path here
    pre_path = ""  # Enter your output image path here

    preprocess_for_rapidocr(img_path, pre_path)

    engine = RapidOCR()
    result = engine(pre_path)

    print(result)
    result.vis("vis_safe.jpg")

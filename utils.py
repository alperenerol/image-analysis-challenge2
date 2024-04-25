import base64
from io import BytesIO
from PIL import Image
import numpy as np
import cv2

# Functions for encoding and decoding
def pil_image_to_b64_str(img_pil:Image, img_format:str) -> str:
    buffered = BytesIO()
    img_pil.save(buffered, format=img_format)
    img_bytes = buffered.getvalue()
    img_b64_bytes = base64.b64encode(img_bytes)
    img_b64_str = img_b64_bytes.decode('ascii')
    return img_b64_str

def base64_to_cv2array(image_b64) -> np.ndarray:
    im_bytes = base64.b64decode(image_b64)  # im_bytes is a binary image
    im_arr = np.frombuffer(im_bytes, dtype=np.uint8)  # im_arr is one-dim Numpy array
    img_cv2_arr = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
    return img_cv2_arr

def base64_to_pilimage(image_b64) -> Image:
    im_bytes = base64.b64decode(image_b64)  # im_bytes is a binary image
    img_file = BytesIO(im_bytes)  # convert image to file-like object
    img_pil = Image.open(img_file)   # img is now PIL Image object
    return img_pil
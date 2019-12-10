import cv2


def process_image(original_image):
    # convert to gray scale
    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # edge detection, this is useless for now
    processed_image = cv2.Canny(processed_image, threshold1=200, threshold2=300)
    return processed_image

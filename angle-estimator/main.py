import cv2
import numpy as np
import math
def find_length(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)
    max_length = 0
    longest_line = None
    for line in lines:
        x1, y1, x2, y2 = line[0]
        length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        if length > max_length:
            max_length = length
            longest_line = line
    x1, y1, x2, y2 = longest_line[0]
    length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    return length

if __name__ == "__main__":
    lengthBaseImg = find_length('skeleton-ref.png')
    lengthTestImg = find_length('skeleton-short.png')

    # assuming the device is parallel to a vertical wall
    angle = math.acos(lengthTestImg/lengthBaseImg)
    print("Angle made with the wall as reference: ", angle, "degree")


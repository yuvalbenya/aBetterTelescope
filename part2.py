import cv2
import matplotlib.pyplot as plt
import glob
import numpy as np

def images_paths():
    """
    :rtype: list of file paths for all image files in the img directory.
    """
    return glob.glob("./db/*.jpg") + glob.glob("./db/*.png")

def print_picture(path, index):

    img = cv2.imread(path)
    if img is None:
        print('Error: Failed to load image', path)
        return False

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(img, contours, -1, (255, 0, 0), 3)

    number_stars = len(contours)

    if number_stars == 0:
        print('No stars found in image', path)
        return False

    print(f"Number of stars in picture {index}: {number_stars}")
    for cnt in contours:
        (x, y), radius = cv2.minEnclosingCircle(cnt)
        brightness = np.mean(gray[int(y) - 2:int(y) + 2, int(x) - 2:int(x) + 2])
        print(f"Star: x={x}, y={y}, radius={radius}, brightness={brightness}")
    print("\n")
    plt.imshow(img)
    plt.show()
    return True


def run_process():
    paths = images_paths()
    print("Number of pictures: ", len(paths))
    for index, path in enumerate(paths, start=1):
        print(path)
        print_picture(path=path, index=index)

if __name__ == '__main__':
    run_process()
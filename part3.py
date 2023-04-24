import cv2
import part2
import random


def show_matches(picture1_path, picture2_path):
    """
    print the math coordinate for every img between to the other img
    show the mathes with line from star to star.
    :rtype: return False if cant load some pic else return true
    """
    # Load the two images
    img1 = cv2.imread(picture1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(picture2_path, cv2.IMREAD_GRAYSCALE)

    if img1 is None or img2 is None:
        print("cant load one of the pictures")
        return False

    img1 = cv2.resize(img1, (0, 0), fx=0.5, fy=0.5)
    img2 = cv2.resize(img2, (0, 0), fx=0.5, fy=0.5)

    # Initialize the feature detector
    detector = cv2.SIFT_create()

    # Find the keypoints and descriptors in both images
    kp1, desc1 = detector.detectAndCompute(img1, None)
    kp2, desc2 = detector.detectAndCompute(img2, None)

    # Initialize the matcher
    matcher = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

    # Match the descriptors between the images
    matches = matcher.match(desc1, desc2)

    # Print the coordinates of the matched keypoints
    for match in matches:
        img1_idx = match.queryIdx
        img2_idx = match.trainIdx
        (x1, y1) = kp1[img1_idx].pt
        (x2, y2) = kp2[img2_idx].pt
        print('Matched Keypoint in Image 1 (x, y):', x1, y1)
        print('Matched Keypoint in Image 2 (x, y):', x2, y2)

    # Sort the matches by distance
    matches = sorted(matches, key=lambda x: x.distance)
    print('Number of matches:', len(matches))

    # Draw the matches between the images with stars
    img_matches = cv2.drawMatches(img1, kp1, img2, kp2, matches, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Create a resizable window
    cv2.namedWindow('Matches', cv2.WINDOW_NORMAL)

    # Display the matched keypoints
    cv2.imshow('Matches', img_matches)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return True


if __name__ == '__main__':

    # get the paths to all the pictures
    paths = part2.images_paths()

    # random 2 pictures from paths
    random_number1 = random.randint(0, 11)
    random_number2 = random.randint(0, 10)

    # print the matches stars coordinates and show the lines
    show_matches(picture1_path=paths.pop(random_number1), picture2_path=paths.pop(random_number2))

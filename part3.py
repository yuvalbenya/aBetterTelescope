import cv2
import part2
import random


def show_matches(picture1_path, picture2_path):
    img1 = cv2.imread(picture1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(picture2_path, cv2.IMREAD_GRAYSCALE)

    if None in (img1, img2):
        print("Couldn't load one or both of the images.")
        return False

    img1, img2 = cv2.resize(img1, None, fx=0.5, fy=0.5), cv2.resize(img2, None, fx=0.5, fy=0.5)

    detector, matcher = cv2.SIFT_create(), cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
    kp1, desc1 = detector.detectAndCompute(img1, None)
    kp2, desc2 = detector.detectAndCompute(img2, None)
    matches = matcher.match(desc1, desc2)

    for match in matches:
        x1, y1 = kp1[match.queryIdx].pt
        x2, y2 = kp2[match.trainIdx].pt
        print(f"Matched Keypoint in Image 1 (x, y): {x1}, {y1}")
        print(f"Matched Keypoint in Image 2 (x, y): {x2}, {y2}")

    matches = sorted(matches, key=lambda x: x.distance)
    print(f"Number of matches: {len(matches)}")

    img_matches = cv2.drawMatches(img1, kp1, img2, kp2, matches, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.namedWindow("Matches", cv2.WINDOW_NORMAL)
    cv2.imshow("Matches", img_matches)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return True


if __name__ == "__main__":
    paths = part2.images_paths()
    random_numbers = random.sample(range(len(paths)), 2)
    picture1_path, picture2_path = paths.pop(random_numbers[0]), paths.pop(random_numbers[1])
    show_matches(picture1_path, picture2_path)

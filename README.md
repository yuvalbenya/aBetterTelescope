Question 1:

Write a simple and effective algorithm to match two pictures - one with hundreds of stars and the other with 10-20 stars. Choose the simplest existing method in this section.

Input: Two images containing stars

Output: Transformed positions of stars in the second image to match the positions in the first image

- Load the image and convert it to grayscale.
- Calculate the brightness threshold for the image.
- Convert the image to black and white based on the brightness threshold.
- Identify stars in both images using a star detection algorithm (Harris Corner Detector, Laplacian of Gaussian (LoG))
- For each star in the first image, compute its feature vector using a feature extraction algorithm. 
- Compute the feature vector for each star in the second image using the same algorithm.
- Use a feature matching algorithm to match the feature vectors of stars in both images, accounting for differences in brightness, color, and orientation.
- Derive a transformation matrix that maps the coordinates of the matched stars in the second image to their corresponding positions in the first image using a method such as Least-Squares Estimation
- Apply the transformation matrix to the coordinates of all stars in the second image to obtain their new positions in the first image.
- Validate the accuracy of the matching algorithm by comparing the positions of the stars in the first image to their expected positions based on the database of star positions.

For the feature extraction algorithm task, Scale-Invariant Feature Transform (SIFT) or Speeded Up Robust Features (SURF) algorithms can be utilized. Those algorithms will get as information about the star's color, brightness, orientation, and texture as mentioned.

For the feature matching algorithm, we use a randomized algorithm, therefore sometimes it may fail and requires multiple runs to get a perfect match.

Part2:

in part2 we take as input all the images in the directory “db” and create a corresponding csv file for each pictures with all the stars coordinates

Part3:
in this part we use the csv to match between the stars in the images and create a new image with the match.
this part is implemented using open\_cv and star matching algorithms.




Running example:

here are 2 star pictures and their matches picture with the star matching algorithm 
 
![(http://https://github.com](https://raw.githubusercontent.com/yuvalbenya/aBetterTelescope/blob/main/star1.jpg)
![(http://https://github.com/](https://raw.githubusercontent.com/yuvalbenya/aBetterTelescope/blob/main/star2.jpg)

Match results:

![(http://https://github.com](https://raw.githubusercontent.com/yuvalbenya/aBetterTelescope/blob/main/mstar1.jpg)
![(http://https://github.com/](https://raw.githubusercontent.com/yuvalbenya/aBetterTelescope/blob/main/mstar2.jpg)



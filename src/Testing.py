import os

from VanishingPoint import *

outputDir = os.path.join('..','pictures','output')
if not os.path.exists(outputDir):
    os.makedirs(outputDir)

i = 0
for subdir, dirs, files in os.walk('../pictures/input'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".jpg"):
            print "Load Image" + filepath
            i += 1
            img = cv2.imread(filepath)

            hough_lines = hough_transform(img)
            if hough_lines:
                print "--got hough_lines"
                random_sample = sample_lines(hough_lines, 100)
                intersections = find_intersections(random_sample, img)
                if intersections:
                    print "--got intersections"
                    grid_size = min(img.shape[0], img.shape[1]) // 3
                    vanishing_point = find_vanishing_point(img, grid_size, intersections)

                    filename = os.path.join(outputDir, 'center' + str(i) + '.jpg')

                    cv2.imwrite(filename, img)

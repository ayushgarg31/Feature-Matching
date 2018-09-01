# Feature-Matching
These codes take in two images of same object/scene with slight variations like lighting changes, occlusions, angle change and try to find correspondences in the image pair. It is an important area of research due to its numerous applications in image processing and computer vision.

## Research objective
To imporve the accuracy of the state of the art feature matching algorithms namely ORB, FAST n BRIEF and SIFT.

## Prerequisites
* Python 3.7 (lower versions also work correctly)
* OpenCV
* Numpy
* Matplotlib
* opencv-contrib-python

## Getting Started
The function in each of the code takes 2 images of the same scene with slight differences (such as lighting change or angle change) as the input and the output will be an image showing the found correspondences between the two images.

## Arguments
* img1 - location/name of the image 1
* img2 - location/name of the image 2
* n - only the n best correspondences accoding to the algorthim will be displayed.

## Result
<img src="https://github.com/ayushgarg31/Feature-Matching/blob/master/images/orb_result.jpg" alt="drawing" height="280px" width="448px" style="float:left;"/> ORB result | <img src="https://github.com/ayushgarg31/Feature-Matching/blob/master/images/FAST%20n%20BRIEF.jpg" alt="drawing"  height="280px" width="448px" style="float:left;"/> FAST n BRIEF result
---------------------------------------------------------------|-------------------------------------------------------------------
<img src="https://github.com/ayushgarg31/Feature-Matching/blob/master/images/only%20SIFT.jpg" alt="drawing"  height="280px" width="448px" style="float:left;"/> SIFT result | <img src="https://github.com/ayushgarg31/Feature-Matching/blob/master/images/SIFT%20KNN%20BBS.jpg" alt="drawing"  height="280px" width="448px" style="float:left;"/> SIFT + KNN + BBS result

## Conclusion
We have found that the our algorithm performs much better than the current state of the art algorithms in feature matching as can be seen in the images.

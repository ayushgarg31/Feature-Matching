import cv2
import numpy as np
from matplotlib import pyplot as plt


def orb_feature_matching(img1, img2, n=1000):
    test1=cv2.imread(img1,0)
    test2=cv2.imread(img2,0)

    orb = cv2.ORB_create()

    kp1=orb.detect(test1,None)
    kp2=orb.detect(test2,None)

    mark1=cv2.drawKeypoints(test1,kp1,None,color=(0,0,255),flags=0)
    orient1=cv2.drawKeypoints(test1,kp1,None,color=(0,0,255),flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    mark2=cv2.drawKeypoints(test2,kp2,None,color=(255,0,0),flags=0)
    orient2=cv2.drawKeypoints(test2,kp2,None,color=(255,0,0),flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    kp1, des1 = orb.compute(test1, kp1)
    kp2, des2 = orb.compute(test2, kp2)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = bf.match(des1,des2)

    matches = sorted(matches, key = lambda x:x.distance)
    result = cv2.drawMatches(mark1,kp1,mark2,kp2,matches[:min(n, len(matches))],None,matchColor=[0,255,0], flags=2)

    plt.imshow(result, interpolation = 'bicubic')
    plt.axis('off')
    plt.show()

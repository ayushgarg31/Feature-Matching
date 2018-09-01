import cv2
import cv2.xfeatures2d as cv
import numpy
from matplotlib import pyplot as plt


def SIFT_KNN_BBS(img1, img2):
    t1 = cv2.imread(img1,0)
    t2 = cv2.imread(img2,0)


    sift=cv.SIFT_create()

    kp1, des1 = sift.detectAndCompute(t1, None)
    kp2, des2 = sift.detectAndCompute(t2, None)

    f=cv2.drawKeypoints(t1,kp1,None,[0,0,255],flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    nf=cv2.drawKeypoints(t2,kp2,None,[255,0,0],flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1,des2, k=2)

    good1 = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good1.append([m])

    matches = bf.knnMatch(des2,des1, k=2)

    good2 = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good2.append([m])

    good=[]

    for i in good1:
        img1_id1=i[0].queryIdx
        img2_id1=i[0].trainIdx

        (x1,y1)=kp1[img1_id1].pt
        (x2,y2)=kp2[img2_id1].pt

        for j in good2:
            img1_id2=j[0].queryIdx
            img2_id2=j[0].trainIdx

            (a1,b1)=kp2[img1_id2].pt
            (a2,b2)=kp1[img2_id2].pt

            if (a1 == x2 and b1 == y2) and (a2 == x1 and b2 == y1):
                good.append(i)


    result=cv2.drawMatchesKnn(t1,kp1,t2,kp2,good,None,[0,0,255],flags=2)

    plt.imshow(result, interpolation = 'bicubic')
    plt.axis('off')
    plt.show()

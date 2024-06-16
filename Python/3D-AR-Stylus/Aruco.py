#!/usr/bin/env python
# -*- coding: utf-8 -*
import cv2
from cv2 import aruco
import numpy as np

cap = cv2.VideoCapture(0)

dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
parameters = aruco.DetectorParameters()

# Change below value to match with the actual marker size
marker_size = 0.05  # in meter

parameters.cornerRefinementMethod = aruco.CORNER_REFINE_SUBPIX
detector = cv2.aruco.ArucoDetector(dictionary, parameters)

# Camera Matrix --- Change it with yours
cameraMatrix = np.array([
            [500.44308524, 0, 323.48347426],
            [0, 497.29888962, 239.35672106],
            [0, 0, 1]], dtype='double',)

# Distortion Matrix --- Change it with yours
distCoeffs = np.array([[-0.03020035], [0.26274676],  [0.00116514],  [-0.00079586],  [-0.461474]])

# Camera setting --- Change it with yours
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def decimal_round(value, digit):
    value_multiply = value * 10 ** digit
    value_float    = value_multiply.astype(int)/( 10 ** digit)
    return value_float

def estimatePose(corner, marker_size, mtx, distortion):
    marker_points = np.array([[-marker_size / 2, marker_size / 2, 0],
                              [marker_size / 2, marker_size / 2, 0],
                              [marker_size / 2, -marker_size / 2, 0],
                              [-marker_size / 2, -marker_size / 2, 0]], dtype=np.float32)

    # Method is based on the paper of Toby Collins and Adrien Bartoli. "Infinitesimal Plane-Based Pose Estimation" ([61]).
    # This method is suitable for marker pose estimation. It requires 4 coplanar object points (described above).
    # trash, rvecs, tvecs = cv2.solvePnP(marker_points, corner, mtx, distortion, False, cv2.SOLVEPNP_IPPE_SQUARE)

    # cv::SOLVEPNP_SQPNP Method is based on the paper "A Consistently Fast and Globally Optimal Solution to
    # the Perspective-n-Point Problem" by G. Terzakis and M.Lourakis ([267]). It requires 3 or more points.
    # trash, rvecs, tvecs = cv2.solvePnP(marker_points, corner, mtx, distortion, False, cv2.SOLVEPNP_SQPNP)

    # cv::SOLVEPNP_ITERATIVE Iterative method is based on a Levenberg-Marquardt optimization. In this case the function
    # finds such a pose that minimizes reprojection error, that is the sum of squared distances between the observed
    # projections "imagePoints" and the projected (using cv::projectPoints ) "objectPoints". Initial solution for
    # non-planar "objectPoints" needs at least 6 points and uses the DLT algorithm.
    trash, rvecs, tvecs = cv2.solvePnP(marker_points, corner, mtx, distortion, False, cv2.SOLVEPNP_ITERATIVE)

    return rvecs, tvecs, trash

def main():
    ret, frame = cap.read()
    while ret == True:
        ret, frame = cap.read()
        corners, ids, rejectedImgPoints = detector.detectMarkers(frame)
        aruco.drawDetectedMarkers(frame, corners, ids, (0,255,0))

        for i, corner in enumerate( corners ):
            # Draw polylines
            points = corner[0].astype(np.int32)
            cv2.polylines(frame, [points], True, (0,255,255))
            # Draw marker IDs
            cv2.putText(frame, str(ids[i][0]), tuple(points[0]), cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0), 1)
            # Draw marker corner no.
            for j in range(1,4):
                cv2.putText(frame, str(j) , points[j], cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
            # Calculate pose
            rvecs_new, tvecs_new, _objPoints = estimatePose(corner, marker_size, cameraMatrix, distCoeffs)
            (rotation_matrix, jacobian) = cv2.Rodrigues(rvecs_new)
            cv2.drawFrameAxes(frame, cameraMatrix, distCoeffs, rvecs_new, tvecs_new, 0.1)

        cv2.imshow('org', frame)
        key = cv2.waitKey(50)
        if key == 27: # ESC
            break

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
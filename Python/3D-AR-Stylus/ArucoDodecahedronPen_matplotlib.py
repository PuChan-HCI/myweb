#!/usr/bin/env python
# -*- coding: utf-8 -*
import cv2
from cv2 import aruco
import numpy as np
import pandas as pd
from collections import deque
import matplotlib.pyplot as plt
import io
from PIL import Image

# Setup the web camera
def setup_web_camera():
    # Open the webcam (built-in camera)
    cap = cv2.VideoCapture(0)
    # Camera setting --- Change it with yours
    cap.set(cv2.CAP_PROP_FPS, 30)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    # Camera Matrix --- Change it with yours
    cameraMatrix = np.array([
        [500.44308524, 0, 323.48347426],
        [0, 497.29888962, 239.35672106],
        [0, 0, 1]], dtype='double', )
    # Distortion Matrix --- Change it with yours
    distCoeffs = np.array([[-0.03020035], [0.26274676], [0.00116514], [-0.00079586], [-0.461474]])
    return cap, cameraMatrix, distCoeffs

# Set up the Aruco 
def setup_aruco():
    # Set up the Aruco dictionary
    dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    parameters = aruco.DetectorParameters()
    # Change below value to match with the actual marker size
    marker_size = 0.014  # in meter
    # Process markers' corners at subpixels
    parameters.cornerRefinementMethod = aruco.CORNER_REFINE_SUBPIX
    detector = cv2.aruco.ArucoDetector(dictionary, parameters)
    return detector, marker_size

# Passing graphics from matplotlib to cv images
def buffer_plot_and_get(figure):
    buf = io.BytesIO()
    figure.savefig(buf)
    buf.seek(0)
    pil_image = Image.open(buf)
    opencvImage = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    return opencvImage

# Estimate the pose information for each marker
def estimatePoseLocal(corner, marker_size, cameraMatrix, distCoeffs):
    marker_points = np.array([[-marker_size / 2, marker_size / 2, 0],
                              [marker_size / 2, marker_size / 2, 0],
                              [marker_size / 2, -marker_size / 2, 0],
                              [-marker_size / 2, -marker_size / 2, 0]], dtype=np.float32)
    trash, rvecs, tvecs = cv2.solvePnP(marker_points, corner, cameraMatrix, distCoeffs, False, cv2.SOLVEPNP_ITERATIVE)
    return rvecs, tvecs, trash

# Estimate the global information of the dodecahedron from detected markers
def estimatePoseGlobal(model_points, image_points, cameraMatrix, distCoeffs):
    trash, rvecs, tvecs = cv2.solvePnP(model_points, image_points, cameraMatrix, distCoeffs, False, cv2.SOLVEPNP_ITERATIVE)
    return rvecs, tvecs, trash

# Create a live 3D scatter plot
def live_plot3D():
    # Pen tip (-0.014943, -65.6512, 85.2906) as being measured using Blender 3D
    fig = plt.figure()
    plt.ion()       # Turn on interactive mode
    ax = fig.add_subplot(projection='3d')
    # Adjust axes
    ax.axes.set_xlim3d(-200,200)
    ax.axes.set_ylim3d(-200,100)
    ax.axes.set_zlim3d(bottom=-200, top=100)
    return fig, ax

# This is the main function
def main():

    # Setup the web camera --------------------------------
    cap, cameraMatrix, distCoeffs = setup_web_camera()
    ret, frame = cap.read()

    # Setup the Aruco marker ------------------------------
    detector, marker_size = setup_aruco()

    # Read Dodecahedron 3D coordinates --------------------
    data = pd.read_csv('markers/model_points_4x4.csv')    # Modified annotation (adjusted to each marker)
    row, column = data.shape                        # Check the number of row & column
    # Put data into a 2D-list
    cols_to_combine = ['x', 'y', 'z']
    model_points_2d_list = data[cols_to_combine].values.tolist()
    # Convert a 2D list to a 3D list using K-slice
    # initializing K-Slicing method
    K = 4                                           # Number of 2D data in a group
    tmp1 = iter(model_points_2d_list)
    tmp2 = [tmp1] * K
    model_points_3d_list = [list(ele) for ele in zip(*tmp2)]

    # Initialize the variable ----------------------------
    global_pose = False
    plot_pen_tip = False

    # Create a live 3D scatter plot ----------------------
    fig, ax = live_plot3D()
    plt_img = buffer_plot_and_get(fig)

    while ret == True:
        ret, frame = cap.read()
        height, width, channels = frame.shape
        corners, ids, rejectedImgPoints = detector.detectMarkers(frame)
        aruco.drawDetectedMarkers(frame, corners, ids, (0,255,0))

        # Use deque to append (faster)
        image_points_2d = deque()
        model_points_3d = deque()
        for i, corner in enumerate(corners):

            # Draw polylines (edge)
            points = corner[0].astype(np.int32)
            cv2.polylines(frame, [points], True, (0,255,255))

            # Draw marker IDs
            cv2.putText(frame, str(ids[i][0]), tuple(points[0]), cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0), 1)

            # Draw marker corner no.
            for j in range(1,4):
                cv2.putText(frame, str(j) , points[j], cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

            # Calculate the local pose of each AR marker
            rvecs, tvecs, _objPoints = estimatePoseLocal(corner, marker_size, cameraMatrix, distCoeffs)
            if not global_pose:
                cv2.drawFrameAxes(frame, cameraMatrix, distCoeffs, rvecs, tvecs, 0.01)
                overlay = frame.copy()
                # A filled line
                cv2.line(overlay, (20, 20), (250, 20), (0, 255, 0), 40)
                # Transparency factor.
                alpha = 0.4
                cv2.putText(frame, 'Mode: Local Pose Estimation', (20, 25),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)

            # Calculate only for #ID < 12
            # to avoid wrong ID detection
            if (ids[i][0] < 12):
                # Collect image points
                for j in range(4):
                    image_points_2d.append(corner[0][j].tolist())
                # Collect model points
                for j in range(4):
                    model_points_3d.append(model_points_3d_list[ids[i][0]][j])

        if ids is not None:
            # Convert to numpy array
            tmp = np.array(image_points_2d)
            image_points = tmp[np.newaxis, :]
            model_points = np.array(model_points_3d)
            if len(model_points>=4):
                rvecs_global, tvecs_global, _objPoints = estimatePoseGlobal(model_points, image_points, cameraMatrix, distCoeffs)
                (rotation_matrix, jacobian) = cv2.Rodrigues(rvecs_global)

                # Calculate the global pose of the dodecahedron
                if global_pose:
                    # Draw Axis, Line, Text
                    cv2.drawFrameAxes(frame, cameraMatrix, distCoeffs, rvecs_global, tvecs_global, 50)
                    overlay = frame.copy()
                    # A filled line
                    cv2.line(overlay, (20, 20), (250, 20), (255, 255, 0), 40)
                    # Transparency factor.
                    alpha = 0.4
                    cv2.putText(frame, 'Mode: Global Pose Estimation', (20, 25),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)

                    # Calculate and draw the trajectory of the 3D pen tip
                    if plot_pen_tip:
                        pen_tip_loc = np.array([[-0.014943], [-65.6512], [85.2906]])    # 3x1 array
                        pen_tip_loc_world = rotation_matrix @ pen_tip_loc + tvecs_global
                        ax.scatter3D(-pen_tip_loc_world[0],-pen_tip_loc_world[1],-pen_tip_loc_world[2])
                        plt.ioff()  # Turn off interactive mode
                        plt_img = buffer_plot_and_get(fig)

        frame = cv2.hconcat([frame, plt_img])
        cv2.imshow('org', frame)
        key = cv2.waitKey(50)
        if key == 27: # ESC
            break
        elif key == ord(' '):  # Space key to change between local/global pose estimation
            global_pose = not global_pose
        elif key == ord('p'):  # 'p' key to start/stop plotting
            if global_pose:
                plot_pen_tip = not plot_pen_tip
        elif key == ord('r'):  # 'r' key to reset the graph
            plt.cla()
            ax.axes.set_xlim3d(-200, 200)
            ax.axes.set_ylim3d(-200, 100)
            ax.axes.set_zlim3d(bottom=-200, top=100)
            plt_img = buffer_plot_and_get(fig)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
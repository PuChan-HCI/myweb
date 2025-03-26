import cv2
import numpy as np
import pywavefront

# Load the OBJ file
# This function uses pywavefront to load the OBJ file.
def load_obj(file_path):
    scene = pywavefront.Wavefront(file_path, collect_faces=True)
    return scene

# Draw the OBJ model
# This function projects the 3D vertices of the OBJ model onto 
# the 2D image using the camera matrix and the pose estimated from 
# the ArUco marker.
def draw_obj(scene, camera_matrix, rvec, tvec, image):
    # Project the 3D points to 2D
    # for name, mesh in scene.meshes.items():
    #     for face in mesh.faces:
    for name, material in scene.materials.items():
        # points = [mesh.vertices[i] for i in face]
        points = material.vertices
        # Convert 3D points to homogeneous coordinates
        points_3d = np.array(points)
        points_3d_homogeneous = np.hstack((points_3d, np.ones((points_3d.shape[0], 1))))

        # Apply rotation and translation
        R, _ = cv2.Rodrigues(rvec)
        transformed_points = (R @ points_3d_homogeneous[:, :3].T + tvec).T

        # Project to 2D
        projected_points = (camera_matrix @ transformed_points.T).T
        projected_points /= projected_points[:, 2].reshape(-1, 1)  # Normalize

        # Draw the edges
        for i in range(len(projected_points)):
            next_index = (i + 1) % len(projected_points)
            cv2.line(image, tuple(projected_points[i][:2].astype(int)), tuple(projected_points[next_index][:2].astype(int)), (0, 255, 0), 2)

# Main function
def main():
    # Load the camera parameters
    camera_matrix = np.array([[800, 0, 320], 
                              [0, 800, 240], 
                              [0, 0, 1]], 
                              dtype=np.float32)
    dist_coeffs = np.zeros((4, 1))  # Assuming no lens distortion

    # Load the OBJ file
    obj_file = '3D_Model/Test.obj'  # Replace with your OBJ file path
    scene = load_obj(obj_file)

    # Initialize the video capture
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to grayscale for ArUco detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Define the ArUco dictionary and parameters
        aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
        parameters = cv2.aruco.DetectorParameters()

        # Detect markers
        corners, ids, _ = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

        if ids is not None:
            # Estimate pose of each marker
            for i in range(len(ids)):
                rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(corners[i], 0.1, camera_matrix, dist_coeffs)
                draw_obj(scene, camera_matrix, rvec[0], tvec[0], frame)
                cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        # Show the frame
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

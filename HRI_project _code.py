""" Huaman Robot Interaction (HRI)
    Made by : Mariam Elsaid
    Description: Real-time joint control in CoppeliaSim using MediaPipe Face Mesh """

import cv2
import mediapipe as mp
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

def main():
    # Connect to Coppeliasim
    try:
        print("[-] initializing connection to coppeliasim..")
        client = RemoteAPIClient()
        sim = client.getObject('sim')

        # Target joint handle ( Check the name oh joint is matches the scene )
        target_joint = sim.getObject('/joint')
        print ('[+] Connection confirmed .Remote API is active!.')
    except Exception as error:
        print(f"[!] Error: Unable to connect to the simulator. {error}")
        return
    
    #Setup : MediaPipe face mesh configuration..
    mp_mesh = mp.solutions.face_mesh
    processor = mp_mesh.FaceMesh(
    max_num_faces = 1,
    refine_landmarks = True ,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5
        )

    # Camera Input
    video_stream = cv2.VideoCapture(0)
    print ("[+] Human Machine interface Started. Tracking head movement")

    #Start the Simulation Envirnoment
    sim.startSimulation()
    try:
        while video_stream.isOpened():
            success, frame = video_stream.read()
            if not success:
                print("[!] Warning: Camera connection lost!!.")
                break

             # Image processing for better tracking
            frame = cv2.flip (frame,1)
            rgb_data = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            inference_results = processor.process(rgb_data)
            if inference_results.multi_face_landmarks :
              for face_data in inference_results.multi_face_landmarks:
                # read out Nose Tip landmark (index 1)
                nose_coord_x = face_data.landmark[1].x

                #Unifying the coordinates : mapping ( 0 to 1) to radians (-1.5 to 1.5)
                #Adjusting the sensitivity factor (3.0) for smoother and better rotation
                control_signal = (nose_coord_x -0.5)*3.0

                #command the robotjoint
                sim.setJointTargetPosition(target_joint, control_signal)


                #Display the interface
                cv2.imshow(' HRI Control Interface_ Mariam Elsaid',frame)
                #Exit loop on 'ESC' key 
                key = cv2.waitKey(1) & 0xFF 
                if key == 27:
                    break

    finally:
        # resource cleanup
        print('[-] Finishing session and stopping Simulation ..')
        sim.stopSimulation()
        video_stream.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()            







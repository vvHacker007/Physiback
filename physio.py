from time import perf_counter
import streamlit as st
import cv2
import io
import mediapipe as mp
import numpy as np
import imageio

if 'video_captured' not in st.session_state:
    st.session_state.video_captured = False
if 'analysis_done' not in st.session_state:
    st.session_state.analysis_done = False

def videoCapture(src):
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    
    message = st.empty();
    message.warning('Started Capturing')
    
    def calculate_angle(a,b,c):
        a = np.array(a) # First
        b = np.array(b) # Mid
        c = np.array(c) # End
        
        radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
        angle = np.abs(radians*180.0/np.pi)
        
        if angle >180.0:
            angle = 360-angle
            
        return angle 

    k={"IMAGE":[],"KAI":[],'HKA':[], 'SHK':[],}
    cap = cv2.VideoCapture(src)
    screen = st.empty()

    webcam_timer = 30
    if src == 0:
        start_time = perf_counter()

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        message.success('Capturing now')
        
        while cap.isOpened():
            ret, frame = cap.read()
            if ret==False:
                break;
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            try:
                landmarks = results.pose_landmarks.landmark
                hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
                index = [landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].x,landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].y]
                shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                angle_foot=calculate_angle(knee,ankle,index)
                ankle_angle = calculate_angle(hip,knee,ankle)
                hip_angle = calculate_angle(shoulder,hip,knee)
                
                
                k['IMAGE'].append(frame)
                k['KAI'].append(angle_foot)
                k['HKA'].append(ankle_angle)
                k['SHK'].append(hip_angle)
                
                # Visualize angle
                cv2.putText(image, str(angle), 
                            tuple(np.multiply(elbow, [640, 480]).astype(int)), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                    )
            except:
                pass
            
            
            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                    mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                    )               
            
            screen.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
            
            if (src == 0 and (perf_counter()-start_time) > webcam_timer): #Timer if webcam is source
                cap.release()
        cap.release()
    
    screen.empty()
    message.success('Capturing Successful!')
    st.session_state.video_captured = True
    st.session_state.imgData = k

def analyseVideo():
    message = st.empty()
    
    if not st.session_state.video_captured:
        pass
    
    k = st.session_state.imgData
    message.warning("Analysing data")
    def rep_analyse(start_index,end_index, tot_KAI):
        min_HKA = k['HKA'][start_index]
        min_HKA_i = start_index
        tot_frames = end_index - start_index + 1
        avg_KAI = tot_KAI/tot_frames
        var_KAI = 0
        
        for i in range(start_index,end_index+1):
            if min_HKA >= k['HKA'][i]:
                min_HKA = k['HKA'][i]
                min_HKA_i = i
            var_KAI += (k['KAI'][i] - avg_KAI)**2
        
        squat_angle = int(min_HKA - 90)
        HKA_SHK_Diff = k['HKA'][min_HKA_i] - k['SHK'][min_HKA_i]
        var_KAI = var_KAI/(tot_frames-1)
        
        return squat_angle, HKA_SHK_Diff, var_KAI, tot_frames

    rep_start = False
    rep_mid = False
    tot_rep = 0
    tot_KAI = 0
    rep_report = {'start_i':[],'end_i':[],'squat_angle':[],'HKA_SHK_Diff':[],'var_KAI':[],'tot_frames':[]}
    for i in range(len(k['IMAGE'])):
        print("Reps start:", rep_start)
        print("Reps mid:", rep_mid)
        print(tot_rep)
        print(k['KAI'][i], k['HKA'][i], k['SHK'][i])
        
        if not rep_start:
            if(int(abs(k['HKA'][i]) - 160) < 5):
                rep_start = True
                rep_report['start_i'].append(i)
                tot_KAI = k['KAI'][i]
        else:
            tot_KAI += k['KAI'][i]
            if(int(abs(k['HKA'][i] - 150)) < 5 and rep_mid):
                rep_report['end_i'].append(i)
                squat_angle, HKA_SHK_Diff, var_KAI, tot_frames = rep_analyse(rep_report['start_i'][tot_rep],rep_report['end_i'][tot_rep],tot_KAI)
                rep_report['squat_angle'].append(squat_angle)
                rep_report['HKA_SHK_Diff'].append(HKA_SHK_Diff)
                rep_report['var_KAI'].append(var_KAI)
                rep_report['tot_frames'].append(tot_frames)
                tot_rep += 1
                rep_start = rep_mid = False
                tot_KAI = 0
            elif(int(abs(k['HKA'][i] - 95)) < 10 and rep_start):
                rep_mid = True          
                
    print(rep_report)
    if not rep_report['start_i']:
        st.error("No valid data points found")
        return
    
    #Generating Sugegstions based on rep_report:
    suggestions = []
    perfect_rep = 0
    for rep in range(0,tot_rep):
        rep_suggestion = []
        
        if(rep_report['squat_angle'][rep] > 15):
            rep_suggestion.append("Incomplete squat! Squat little lower")
        elif(rep_report['squat_angle'][rep] < -10):
            rep_suggestion.append("Too much sqautting! Squat little less")
            
        if(rep_report['tot_frames'][rep] < 50):
            rep_suggestion.append("Too fast! Squat slower")
        
        if(rep_report['HKA_SHK_Diff'][rep] < 0):
            rep_suggestion.append("Knee too much forward! Try to keep knee from leaning forward")
        elif(rep_report['HKA_SHK_Diff'][rep] > 15):
            rep_suggestion.append("Try to keep you back straight")
            
        if(rep_report['var_KAI'][rep] > 25):
            rep_suggestion.append("Your feet are shifting! Keep your legs planted")
            
        if not rep_suggestion:
            rep_suggestion.append("Perfect Squat!")
            perfect_rep += 1
            
        suggestions.append(rep_suggestion)
        
        with imageio.get_writer("rep_"+str(rep+1)+".gif", mode="I") as writer:
            for gif_frame,img_frame in enumerate(range(rep_report['start_i'][rep],rep_report['end_i'][rep]+1)):
                rgb_frame = cv2.cvtColor(k['IMAGE'][img_frame], cv2.COLOR_BGR2RGB)
                writer.append_data(rgb_frame)

    print("Suggestions and gif stored")
    print(suggestions)
    st.session_state.analysis_done = True
    message.success("Analysis Done!")
    st.session_state.analysisData = {'suggestions':suggestions, 'perfect_rep':perfect_rep, 'tot_rep':tot_rep}

nav = st.sidebar.radio("Navigate to",('About','Live Video Analysis'))
if nav == "About":
    st.title("About")
    #TO BE DONE

elif nav == "Live Video Analysis":
    st.title("Live Video Analysis")
    video_src = st.selectbox("Choose your video source :",('Built-in Camera (30sec)','Sample 1','Sample 2', 'Other video'))
    if video_src == 'Built-in Camera (30sec)':
        src = 0
    elif video_src == 'Sample 1':
        src = "squat_2.mp4"
    elif video_src == 'Sample 2':
        src = "squat_3.mp4"
    else:
        video = st.file_uploader("Upload .mp4 file",type=["mp4"])
        if video:
            byte_video = io.BytesIO(video.read())
            with open("uploaded_vid.mp4", 'wb') as out:
                out.write(byte_video.read())
            out.close()
            src = "uploaded_vid.mp4"

    start_button = st.empty()
    if start_button.button("Start"):
        start_button.empty()
        videoCapture(src)
    
    if st.session_state.video_captured:
        if not st.session_state.analysis_done:
            analyseVideo()
            if st.session_state.analysis_done:
                analysisData = st.session_state.analysisData

        #Attempt to export video from frames        
        # frames = st.session_state.imgData['IMAGE']
        # out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 60, (640,480))
        # for frame in frames:
        #     out.write(frame)
        # out.release()
        # with open('exercise.mp4') as f:
        #     if st.download_button("Export Video",f):
        #         st.success("Video Exported Successfuly")
    
    if st.session_state.analysis_done:
        perfect_rep = st.session_state.analysisData['perfect_rep']
        tot_rep = st.session_state.analysisData['tot_rep']
        suggestions = st.session_state.analysisData['suggestions']
        st.title("Score: " + str((perfect_rep/tot_rep)*100))
        st.title("Suggestions")
        for rep in range(0,tot_rep):
            st.header("Rep " + str(rep+1) + " :")
            for suggestion in suggestions[rep]:
                print(suggestion)
                if suggestion == "Perfect Squat!":
                    st.success(suggestion)
                else:
                    st.error(suggestion)
            st.image("rep_"+str(rep+1)+".gif")
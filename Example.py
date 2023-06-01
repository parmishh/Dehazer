import cv2
import moviepy.editor as mpy
from Dehaze_module import remove_haze
cap = cv2.VideoCapture("file.mp4")
frame_fps = int(cap.get(cv2.CAP_PROP_FPS))
    # specify a writer to write a processed video to a disk frame by frame
    
video_row=[]
while True:
    ret, frame = cap.read()
        # if frame is read correctly ret is True
    if not ret:
           
        break
        # some video processing here
    new = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray, haze_map = remove_haze(new, showHazeTransmissionMap=False)
        
        # write a processed frame to the list
        
    video_row.append(gray)

    ## Close video file
    cap.release()
    # create moviepy object from list with numpy frames and save it to a disk
    clip = mpy.ImageSequenceClip(video_row, fps=25)
    clip.write_videofile("new.mp4")
    # when video is fully saved to disk, open it as BytesIO and play with st.video()
    # result_video = open(temp_file_result, "rb")

    
    result_video = open(new.mp4, "rb")
 
    

import streamlit as st
import cv2
import tempfile
import moviepy.editor as mpy
from rembg import remove

video_data = st.file_uploader("Upload file", ['mp4','mov', 'avi'])

if video_data:
    # save uploaded video to disc
    temp_file_1 = tempfile.NamedTemporaryFile(delete=False,suffix='.mp4')
    temp_file_1.write(video_data.getbuffer())
    st.video(temp_file_1.name)
    # read it with cv2.VideoCapture(), so now we can process it with OpenCV functions
    cap = cv2.VideoCapture(temp_file_1.name)
    # grab some parameters of video to use them for writing a new, processed video
    frame_fps = int(cap.get(cv2.CAP_PROP_FPS))
    # specify a writer to write a processed video to a disk frame by frame
    temp_file_2 = tempfile.NamedTemporaryFile(delete=False,suffix='.mp4')
    # loop though a video, process each frame and save it to a list
    video_row=[]
    while True:
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            st.write("Video is ready! Now you can play it")
            break
        # some video processing here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        new=remove(gray)
        # write a processed frame to the list
        
        video_row.append(new)

    ## Close video file
    cap.release()
    # create moviepy object from list with numpy frames and save it to a disk
    clip = mpy.ImageSequenceClip(video_row, fps=25)
    clip.write_videofile(temp_file_2.name)
    # when video is fully saved to disk, open it as BytesIO and play with st.video()
    # result_video = open(temp_file_result, "rb")

    st.video(temp_file_2.name)
    result_video = open(temp_file_2.name, "rb")
    st.download_button(label="Download video file", data=result_video,file_name='video_clip.mp4')
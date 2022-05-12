video_capture = cv2.VideoCapture(CAM_REF)

# Initialize some variables
face_names = []
process_this_frame = True

# start
while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    # Resize frame of video to 1/4 size for faster face recognition
    # processing
    # small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    # Convert the image from BGR color (which OpenCV uses) to 
    # RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    # Only process every other frame of video to save time
    thread = threading.Thread(target=encodeThisFrameFaces, 
    args=(rgb_small_frame,))
    if process_this_frame:
        # encodeThisFrameFaces(rgb_small_frame)
        print("appActiveColor: ", appActiveColor, end="\t\t")
        thread.start()
        # thread.join()
    (...)
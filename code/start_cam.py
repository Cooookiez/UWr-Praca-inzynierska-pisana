video_capture = cv2.VideoCapture(CAM_REF)

# inicjacja zmiennych
face_names = []
process_this_frame = True

# start
while True:
    # wez klatke z kamerki
    ret, frame = video_capture.read()
    # zeskaluj klatke do 1/4 rozmiaru dla szybszego procesu
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    # konwertuj klatke z BGR (uzywanego przez OpenCV)
    # do RGB (uzywanego przez face_recognition)
    rgb_small_frame = small_frame[:, :, ::-1]
    # przetwarzaj tylko co druga klatke
    thread = threading.Thread(target=encodeThisFrameFaces, 
    args=(rgb_small_frame,))
    if process_this_frame:
        print("appActiveColor: ", appActiveColor, end="\t\t")
        thread.start()
    (...)
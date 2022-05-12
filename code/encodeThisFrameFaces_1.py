def encodeThisFrameFaces(frame):
    timeStart = time.time()
    # Find all the faces and face encodings in the current frame of
    # video
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, 
    face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(
        known_face["encodings"], face_encoding)
        name = UNKNOWN_NAME

        # Or instead, use the known face with the smallest distance
        # to the new face
        face_distances = face_recognition.face_distance(
        known_face["encodings"], face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face["names"][best_match_index]

        face_names.append(name)
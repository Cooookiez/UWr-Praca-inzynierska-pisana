def encodeThisFrameFaces(frame):
    timeStart = time.time()
    # znajdz wszystkie pozycje twarzy i encodowania twarzy
    # w biezadzej klatce
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, 
    face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # sprawdz czy twarz jest znana
        matches = face_recognition.compare_faces(
        known_face["encodings"], face_encoding)
        name = UNKNOWN_NAME
        
        # jak nie znana, to sprawdz najlepsze porownanie
        face_distances = face_recognition.face_distance(
        known_face["encodings"], face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face["names"][best_match_index]

        face_names.append(name)
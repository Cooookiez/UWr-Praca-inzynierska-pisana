# sprawdz czy osoba nie powtarza się zbyt często
face_names_to_alert = []
time_differences = {}
for regognized_face in face_names:
    if regognized_face in ALERT_PEOPLE.keys():
        # sprawdz czas ostatniego wykrycia
        time_difference = time.time() - ALERT_PEOPLE[
        regognized_face]
        time_differences[regognized_face] = time_difference
        ALERT_PEOPLE[regognized_face] = time.time()
        if time_difference >= ALERT_DELAY_IGNORE:
            # powiadom
            face_names_to_alert.append(regognized_face)
            pass
        else:
            # pomin
            pass
        pass
    else:
        # dodaj to ALERT_PEOPLE & powiadom
        ALERT_PEOPLE[regognized_face] = time.time()
        face_names_to_alert.append(regognized_face)
        pass
print(f"[{threading.active_count()}] ", *face_names_to_alert, 
f" ({(time.time() - timeStart):.4}s)\t\t\t{time_differences}")

for face in face_names_to_alert:
    say_hello(face)
pass
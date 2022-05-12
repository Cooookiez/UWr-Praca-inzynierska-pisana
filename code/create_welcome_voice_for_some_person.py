def create_welcome_voice_for_known_person(name, path2root=
PATH_TO_ROOT):
    person_dir_path = os.path.join(path2root, 
    KNOW_PEOPLE_DIR_PATH_NAME, name)
    welcomes_dir = os.path.join(person_dir_path, 
    WELCOMES_DIR_PATH_NAME)
    basic_welcome_file = os.path.join(welcomes_dir, 
    BASIC_WELCOME_FILE_NAME)
    create_and_save_welcome_message(f"Witaj {name}", 
    basic_welcome_file)

def create_welcome_voice_for_unknown_person(path2root=PATH_TO_ROOT):
    # stworz folder dla nieznanych osob
    unknowe_dir_name = f"{WELCOMES_DIR_PATH_NAME}_unknown"
    know_people_dir = os.path.join(path2root, 
    KNOW_PEOPLE_DIR_PATH_NAME)
    unknown_dir_path = os.path.join(know_people_dir, 
    unknowe_dir_name)
    if not os.path.isdir(unknown_dir_path):
        if os.path.isfile(unknown_dir_path):
            os.remove(unknown_dir_path)
        os.chdir(know_people_dir)
        os.mkdir(unknowe_dir_name)
    
    # stworz plik z wiadomoscia
    file_path = os.path.join(unknown_dir_path, 
    BASIC_WELCOME_FILE_NAME)
    create_and_save_welcome_message("Witaj nieznajomy nieznajoma", 
    file_path)
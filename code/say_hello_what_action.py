def say_hello(name, path2root=PATH_TO_ROOT):
    global addPersoneMode2queue
    
    appActiveName = name
    
    # pobierz folder z mp3
    mp3s = []
    path_to_welcomes_for_name = os.path.join(path2root, 
    KNOW_PEOPLE_DIR_PATH_NAME)
    if name == "Unknown":
        addPersoneMode2queue(Mods.UNKNOWN)
        path_to_welcomes_for_name = os.path.join(
        path_to_welcomes_for_name, "welcomes_unknown")
    else:
        addPersoneMode2queue(Mods.KNOWN, name)
        path_to_welcomes_for_name = os.path.join(
        path_to_welcomes_for_name, name, WELCOMES_DIR_PATH_NAME)
        
    # pobierz sciezki do plikow mp3
    for file in os.listdir(path_to_welcomes_for_name):
        print(file)
        extension = os.path.splitext(file)[1] # rozszerzenie pliku
        print(extension)
        if extension.lower() == ".mp3":
            mp3s.append(os.path.join(path_to_welcomes_for_name, 
            file))
    print(mp3s)        
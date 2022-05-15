def screenVisualization():
    global lastMods2Show
    global lGreeting
    global lName
    if len(mods2ShowQueue) > 0:
        mods2ShowQueue.sort()
        # sprawdzenie wykorzystania limitu czasu
        if time.time() > mods2ShowQueue[0].time_end:
            # pop
            mods2ShowQueue.pop(0)
            lGreeting.pack_forget()
            lName.pack_forget()
            screenVisualization()
        else:
            activeMode2show = mods2ShowQueue[0]
            # zmien tylko gdy mod2show jest nowy
            if activeMode2show != lastMods2Show:
                # kolor tła
                Tk.configure(background=
                    appBackground[activeMode2show.activeMode])
                lGreeting.configure(background=
                    appBackground[activeMode2show.activeMode])
                lName.configure(background=
                    appBackground[activeMode2show.activeMode])
                
                # zmien imie textu
                lName.config(text=activeMode2show.name)
                
                # wyswietl text
                lGreeting.pack()
                lName.pack()
                
                Tk.update()
                if activeMode2show.activeMode == Mods.UNKNOWN:
                    say_hello("Unknown")
                else:
                    say_hello(activeMode2show.name)
                lastMods2Show = activeMode2show
                appLastMode = activeMode2show.activeMode;
    else:
        # zmien na idle
        Tk.configure(background=appBackground[Mods.IDLE])
        Tk.update()
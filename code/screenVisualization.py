# # # # # # # # # # # # #
# TU SIE JESZCZE ZMIENI #
# # # # # # # # # # # # #

def screenVisualization():
    global appLastMode
    global lastMods2Show
    print(f"\t|{mods2ShowQueue}|")
    if len(mods2ShowQueue) > 0:
        mods2ShowQueue.sort()
        # czy termin waznosci nie minol
        if time.time() > mods2ShowQueue[0].time_end:
            mods2ShowQueue.pop(0)
            screenVisualization()
            pass
        else:
            activeMode2show = mods2ShowQueue[0]
            # zmien tylko gy mod2show jest nowy
            if activeMode2show != lastMods2Show:
                Tk.configure(background=appBackground[
                activeMode2show.activeMode])
                Tk.update()
                lastMods2Show = activeMode2show
                appLastMode = activeMode2show.activeMode;
                pass
            pass
        pass
    else:
        # zmien na idle (jesli juz nie jest)
        if appLastMode != Mods.IDLE:
            Tk.configure(background=appBackground[Mods.IDLE])
            Tk.update()
        appLastMode = Mods.IDLE;
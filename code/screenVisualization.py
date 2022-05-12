def screenVisualization():
    global appLastMode
    global lastMods2Show
    print(f"\t|{mods2ShowQueue}|")
    if len(mods2ShowQueue) > 0:
        mods2ShowQueue.sort()
        # is queue itme still valid
        if time.time() > mods2ShowQueue[0].time_end:
            # pop
            mods2ShowQueue.pop(0)
            screenVisualization()
            pass
        else:
            activeMode2show = mods2ShowQueue[0]
            # change only if mod2show is new
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
        # change to idle (expect it is not idle)
        if appLastMode != Mods.IDLE:
            Tk.configure(background=appBackground[Mods.IDLE])
            Tk.update()
        appLastMode = Mods.IDLE;
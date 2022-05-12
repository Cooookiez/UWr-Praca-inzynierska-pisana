# rand file to play
mp3_to_paly = random.choice(mp3s)
print(mp3_to_paly)

# play      
pygame.mixer.init()
pygame.mixer.music.load(mp3_to_paly)
pygame.mixer.music.play()
while pygame.mixer.get_busy() == True:
    continue
# back2idle()
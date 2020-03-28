import winsound
import time

winsound.Beep(700, 2000) # ( Força do som, Tempo do som)
time.sleep(3)
winsound.Beep(800 , 1000)

winsound.PlaySound('audio/audio.wav',winsound.SND_FILENAME + winsound.SND_ASYNC ) # + winsound.SND_LOOP para coloca mas paramentros, como o som em loop
# winsoud.SND_ASYNC deixa o audio tocando de fundo
print('Hello world')
time.sleep(60)

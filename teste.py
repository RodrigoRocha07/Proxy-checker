import numpy as np
import sounddevice as sd

def alertaSonoro():
    frequencia = 440  
    duração = 4.0
    amostra_rate = 44100
    t = np.linspace(0, duração, int(amostra_rate * duração), endpoint=False)
    onda = 0.5 * np.sin(2 * np.pi * frequencia * t)
    sd.play(onda, samplerate=amostra_rate)
    sd.wait()


alertaSonoro()
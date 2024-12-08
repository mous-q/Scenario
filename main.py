from text_control import Scenary
from vosk import Model, KaldiRecognizer
import os
import pyaudio
def main(scene: Scenary):

    

    model = Model(r"vosk-model-small")
    rec = KaldiRecognizer(model, 44100)
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16, 
        channels=1, 
        rate=44100, 
        input=True, 
        frames_per_buffer=44100
    )
    stream.start_stream()

    print(scene.show_current())

    while True:

        
        
        try:
            data = stream.read(44100)
            if rec.AcceptWaveform(data):
                txt = rec.Result()
            else:
                txt = rec.PartialResult()
            print(txt)
            if len(set(scene.markers[scene.current].split()) & set(txt.split())) >= len(scene.markers[scene.current].split())//2:
                scene.next()
            
        except IndexError:
            break

        except:
            pass

        finally:
            with open('current.txt', 'w', encoding='utf-8') as file:
                file.write(scene.show_current())

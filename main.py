from text_control import Scenary
from vosk import Model, KaldiRecognizer
import pyaudio
from multiprocessing import Queue

def main(scene: Scenary, q: Queue):

    q.put(scene.info())

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
    q.put([*scene.info()])

    while True:

        
        try:
            data = stream.read(44100)
            if rec.AcceptWaveform(data):
                txt = rec.Result()
            else:
                txt = rec.PartialResult()
            txt = ''.join([i for i in txt if i in set('йцукенгшщзхъфывапролджэячсмитьбю ')])
            print(txt)
            if len(set(scene.marker().split()) & set(txt.split())) >= (len(set(scene.marker().split()))//2):
                scene.next()
                q.put(scene.info())
            
        except IndexError:
            q.put(scene.info())
            break

        except:
            pass
        
        finally:
            if q.empty():
                q.put(scene.info())
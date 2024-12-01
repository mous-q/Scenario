from test_m import get_speech
from text_control import Scenary
def main(scene: Scenary):

    print(*scene.show_current())

    while True:
        

        
        txt = get_speech()
        
        try:
            if scene.markers[scene.current] in txt:
                scene.next()
            
        except IndexError:
            break

        except:
            pass

        finally:
            with open('current.txt', 'w', encoding='utf-8') as file:
                file.write(scene.show_current())


def main():

    import speech_recognition as sr
    import os
    from test_m import get_speech
    from text_control import create_markers, get_text, Scenary, cut


    scene = Scenary('test-scenary.txt')

    while True:
        

        print(*scene.show_current())
        txt = get_speech()
        
        try:
            if scene.markers[scene.current] in txt:
                scene.next()
                scene.show_current()
        except IndexError:
            scene.show_current()
            os._exit()

            
if __name__ == '__main__':
    main()


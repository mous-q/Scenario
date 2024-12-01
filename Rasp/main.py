
def main():

    import speech_recognition as sr
    from test_m import get_speech
    from text_control import create_markers, get_text, Scenary, cut


    scene = Scenary('Scenario/Rasp/test-scenary.txt')
    print(*scene.show_current())

    while True:
        

        
        txt = get_speech()
        
        try:
            if scene.markers[scene.current] in txt:
                scene.next()
                print(*scene.show_current())
        except IndexError:
            print(scene.show_current())
            break
        except:
            pass

            
if __name__ == '__main__':
    main()


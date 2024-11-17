
def create_markers():
    
    print("Input clasterizing phrases with '@;' as a delimiter:")
    markers = list(map(str.lower, input().split('@;')))
    return markers

def get_text(filename:str) -> str:
    
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().replace('\n', ' ').lower()
    
def cut(text:str, markers:list) -> list:
    
    parts = []

    for marker in markers:
        try:
            a = text.find(marker)
            parts.append([text[:a+len(marker)]])
            text = text[a:]
        except:
            pass
    return parts
            

class Scenary():
    def __init__(self, file):

        self.text = get_text(file)
        self.markers = create_markers()
        self.parts = cut(self.text, self.markers)
        self.current = 0

    def show_current(self):
        try:
            return self.parts[self.current]
        except IndexError:
            pass
    
    def next(self):
        self.current += 1

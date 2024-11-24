def get_text(filename:str) -> str:
    
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().replace('\n', ' ').lower()
    
def cut(text:str, markers:list) -> list:
    
    parts = []

    for marker in markers:
        try:
            a = text.find(marker)
            parts.append([text[:a+len(marker)]])
        except:
            pass
        
        text = text[a+len(marker):]
        
    parts.append(text)
    return parts
            

class Scenary():
    def __init__(self, file, markers):

        self.text = get_text(file)
        self.markers = markers
        self.parts = cut(self.text, self.markers)
        self.current = 0

    def show_current(self):
        try:
            return self.parts[self.current]
        except IndexError:
            pass
    
    def next(self):
        self.current += 1

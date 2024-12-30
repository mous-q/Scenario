from part_cls import Part

def get_text(filename:str) -> str:
    
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().replace('\n', ' ')
    
def cut(text:str, markers:list) -> list:
    
    parts: list[Part] = []
    roles: set[str] = set()

    for marker in markers:
        roles.clear()
        try:
            a = text.lower().find(marker)
            txt = text[:a+len(marker)]
            for word in txt.split():
                if word.upper() == word:
                    roles.add(word)
            part = Part(txt, marker, roles)
            parts.append(part)
        except:
            pass
    
    
    roles.clear()
    txt = text[a+len(markers[-1]):]
    for word in text.split():
        if word.upper() == word:
                roles.add(word)
    part = Part(txt, "", roles)

        
    parts.append(part)
    return parts
            

class Scenary():
    def __init__(self, file, markers):

        self.text = get_text(file)
        self.markers = markers
        self.parts = cut(self.text, self.markers)
        self._current = 0

    def info(self):
        try:
            part: Part = self.parts[self._current]
            next_part: Part = self.parts[self._current+1]
            return part.text, part.roles, next_part.roles
        except IndexError:
            part: Part = self.parts[-1]
            return part.text, part.roles, ''

    def marker(self) -> str:
        part: Part = self.parts[self._current]
        return part.marker
    
    def next(self):
        self._current += 1

from part_cls import Part
import sys
import os

def get_text(filename:str) -> str:
    
    try:
        with open(os.path.join(sys.path[0], os.path.normpath(f'scenaries/{filename}.txt')), 'r', encoding='utf-8') as file:
            return file.read()
    except:
        pass
    

def get_markers(filename: str) -> list[str]:

    try:
        with open(os.path.join(sys.path[0], os.path.normpath(f'scenaries/{filename}_mr.txt')), 'r', encoding='utf-8') as file:
            return file.read().split('@')
    except:
        pass

    
def cut(text:str, markers:list) -> list[Part]:
    
    parts: list[Part] = []
    roles: set[str] = set()

    try:
        for marker in markers:
            try:
                i: int = text.find(marker)

                part_text = text[:i+len(marker)].strip('.,;: !?- ')
                text = text[i+len(marker):].strip('.,;: !?- ')

                part = Part(text=part_text, marker=marker)

                parts.append(part)
            except:
                pass
    except:
        pass

        
    parts.append(Part(text, 'empty'))
    return parts
            

class Scenary():
    def __init__(self, file):

        self.text: str = get_text(file)
        self.markers: list[str] = get_markers(file)
        self.parts: list[Part] = cut(self.text, self.markers)
        self._current: int = 0


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

Scenary('New_Text_Document')

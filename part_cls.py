class Part():

    def __init__(self, text: str, marker: str, roles: list[str] = ['[error]']):
        self.text = text
        self.marker = marker
        self.roles = roles
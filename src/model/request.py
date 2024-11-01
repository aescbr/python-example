class Request:
    def __init__(self, name, files):
        self.name = name
        self.files = files
        self.steps = []
    
    def __str__(self):
        return f"Request:{self.name}, {self.steps}"
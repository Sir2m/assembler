class Reader:
    def __init__(self, file):
        self.file = file
    
    def __enter__(self):
        def purify(s:str):
            i = s.find("/")
            if i > -1:
                s = s[:i]
            s = s.strip()
            return s.split(" ")
        
        file = open(self.file, "r")
        data = list(map(purify, file))
        file.close()
        return data
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        ...
import json


class TextFile:
    def read(self, file):
        with open(file) as f:
            return f.read()
        pass

    def write(self, file, lines):
        pass
    
class JSONFile:
    def read(self, file):
        with open(file) as f:
            return json.load(f)

        pass

    def write(self, file, lines):
        pass

file_processor = JSONFile()

data = file_processor.read("data.json")
print(data)
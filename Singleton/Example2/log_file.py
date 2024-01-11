class LogFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, content):
        with open(self.file_path, 'a') as file:
            file.write(content)

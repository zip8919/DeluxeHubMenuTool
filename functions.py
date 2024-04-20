import os

class functions:
    def check_file(self, file_path):
        if os.path.exists(file_path):
            return True
        else:
            return False
    def crete(self, file_path, text):
            with open(file_path, 'w') as file:
                file.write(text)
import os


class SQLProvider:
    def __init__(self, files_path):
        self.scripts = {}
        for file in os.listdir(files_path):
            _sql = open(f'{files_path}/{file}').read()
            self.scripts[file] = _sql

    def get(self, filename):
        return self.scripts[filename]


import os
from pathlib import Path
import pathlib

class Colors:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RESET = '\033[0m'


class LineFeed():
    def __init__(self, path):
        self.path = path;
        self.WINDOWS_LINE_ENDING = b'\r\n'
        self.UNIX_LINE_ENDING = b'\n'
        self.tmpSelection = []
        self.selection = []
    

    def fetchFiles(self, ending):
        paths = []
        for root, d_names, f_names in os.walk('.'):
            for f in f_names:
                if '*' not in ending:
                    if ending in f:
                        paths.append(os.path.join(root, f))
                else:
                    paths.append(os.path.join(root, f))

        self.tmpSelection = paths;

    def printTemp(self):
        for path in self.tmpSelection:
            p1 = Path(path)
            full = self.path / p1
            
            if os.stat(full).st_size != 0:
                with open(full, 'rb') as open_file:
                    content = open_file.read()

                if self.WINDOWS_LINE_ENDING in content:
                    print(f'{Colors.OKBLUE}[WINDOWS]{Colors.RESET} {p1}')
                else:
                    print(f'{Colors.OKCYAN}[UNIX]{Colors.RESET} {p1}')
            else:
                print(f'{Colors.WARNING}[EMPTY]{Colors.RESET} {p1}')

            
    def printSelection(self):
        for path in self.selection:
            p1 = Path(path)
            full = self.path / p1
            
            if os.stat(full).st_size != 0:
                with open(full, 'rb') as open_file:
                    content = open_file.read()

                if self.WINDOWS_LINE_ENDING in content:
                    print(f'{Colors.OKBLUE}[WINDOWS]{Colors.RESET} {p1}')
                else:
                    print(f'{Colors.OKCYAN}[UNIX]{Colors.RESET} {p1}')
            else:
                print(f'{Colors.WARNING}[EMPTY]{Colors.RESET} {p1}')

    def changeLineEnding(self, lineending):
        for path in self.selection:
            p1 = Path(path)
            full = self.path / p1
            
            with open(full, 'rb') as open_file:
                content = open_file.read()

            if lineending == '1':
                if self.UNIX_LINE_ENDING in content:
                    content = content.replace(self.UNIX_LINE_ENDING, self.WINDOWS_LINE_ENDING)

                    with open(full, 'wb') as open_file:
                        open_file.write(content)

            if lineending == '2':
                if self.WINDOWS_LINE_ENDING in content:
                    content = content.replace(self.WINDOWS_LINE_ENDING, self.UNIX_LINE_ENDING)

                    with open(full, 'wb') as open_file:
                        open_file.write(content)

    def select(self):
        self.selection += self.tmpSelection
        self.tmpSelection = []


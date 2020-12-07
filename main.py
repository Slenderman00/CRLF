from linefeed import LineFeed
import os
from pathlib import Path
import pathlib

current = pathlib.Path(__file__).parent.absolute()
l1 = LineFeed(current)

ending = input("fileformat ('.*', '.py', ...): ")
l1.fetchFiles(ending)
l1.printTemp()

print("desired line ending: \n 1. Windows line ending \n 2. Unix line ending")
lineending = input(': ')
if lineending == '1' or lineending == '2':
    l1.select()
    l1.changeLineEnding(lineending)
    l1.printSelection()

else:
    exit(0)



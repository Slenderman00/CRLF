import os
from pathlib import Path
import pathlib

WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'

current = pathlib.Path(__file__).parent.absolute()

paths = []
for root, d_names, f_names in os.walk('.'):
    for f in f_names:
        if '.py' in f:
            paths.append(os.path.join(root, f))


for path in paths:
    p1 = Path(path)
    full = current / p1
    
    with open(full, 'rb') as open_file:
        content = open_file.read()

    if WINDOWS_LINE_ENDING in content:
        print('fixing: ' + str(full))
        content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

        with open(full, 'wb') as open_file:
            open_file.write(content)


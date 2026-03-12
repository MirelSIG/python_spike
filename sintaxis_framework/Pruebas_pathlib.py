from pathlib import Path
import os

path_os = os.getcwd()
path_pathlib = Path.cwd()

print(type(path_os))
print(type(path_pathlib))
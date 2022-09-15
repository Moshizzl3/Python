from fileinput import filename
from pathlib import Path
import os


def createDir(x):
    p = Path(str(x[1]))
    try:
        p.mkdir()
    except FileExistsError as exc:
        print(exc)


def createFile():
    fileName = open("test.txt", "w+")
    fileName.close()


def appenToFile(x):
    filename = open(x[1], "a+")
    filename.write(x[2])
    filename.write("\n")
    filename.close()


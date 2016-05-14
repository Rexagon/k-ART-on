import os
import sys
from PIL import Image

def resize(folder, fileName, height):
    filePath = os.path.join(folder, fileName)
    im = Image.open(filePath)
    w, h  = im.size
    factor = height / h
    newIm = im.resize((int(w*factor), int(height)), Image.ANTIALIAS)
    newIm.save(filePath)

def bulkResize(imageFolder, height):
    imgExts = ["png", "bmp", "jpg"]
    for path, dirs, files in os.walk(imageFolder):
        for fileName in files:
            ext = fileName[-3:].lower()
            if ext not in imgExts:
                continue

            resize(path, fileName, height)

if __name__ == "__main__":
    imageFolder=sys.argv[1]
    bulkResize(imageFolder, float(sys.argv[2]))

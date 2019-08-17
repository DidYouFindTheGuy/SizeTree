import sys
import os 


def getFolderSize(path):
    size = 0
    files = os.listdir(path)
    for file in files:
        fullpath = path + '/' + file
        if os.path.isdir(fullpath):
            size = size + getFolderSize(fullpath)
        else:
            if os.path.isfile(fullpath):
                statinfo = os.stat(fullpath)
                filesize = statinfo.st_size
                size = size + filesize
    return size 


def main(directory, depth):
    filelist = []
    files = os.listdir(directory)
    for file in files:
        fullpath = directory + '/' + file
        if os.path.isdir(fullpath):
            if depth > 0:
                filelist = filelist + main(fullpath, depth-1)
            else:
                sizedict = {'name':fullpath, 'size':getFolderSize(fullpath)}
                filelist.append(sizedict)
        else:
            if os.path.isfile(fullpath):
                statinfo = os.stat(fullpath)
                size = statinfo.st_size
                sizedict = {'name':fullpath, 'size':size}
                filelist.append(sizedict)
    return filelist


def sortOnSize(element):
    return element['size']



def bytesToGB(bytes):
    mega = bytes / 1000000
    if mega >= 1000:
        giga = mega / 1000
        giga = round(giga,2)
        return f"{giga} Gb"
    else:
        mega = round(mega, 2)
        return f"{mega} Mb"


def printSizes(fileslist):
    fileslist.sort(key=sortOnSize)
    for file in fileslist:
        print(f"\033[0;32m{bytesToGB(file['size'])} \033[0m\t {file['name']}")




if __name__ == "__main__":
    inputs = sys.argv
    directory = inputs[1]
    depth = int(inputs[2])
    filelist = main(directory, depth)
    printSizes(filelist)


    

#Organizador de la carpeta downloads 

from os import listdir, mkdir, rename
from os.path import isfile, join, splitext
from time import gmtime, strftime


download_path = '/home/faiya/Downloads'
destination_path = '/home/faiya/Documents'
dirs = {
    1: '/1 pictures',
    2: '/2 videos',
    3: '/3 documentos',
    4: '/4 zip',
    5: '/5 libros',
}

switcher = {
        "jpg": 1,
        "jpeg": 1,
        "png": 1,
        "mkv": 2,
        "mp4": 2,
        "webm": 2,
        "pdf": 3,
        "odt": 3,
        "doc": 3,
        "docx": 3,
        "txt": 3,
        "zip": 4,
        "rar": 4,
        "tar": 4,
        "epub": 5,
        "azw3": 5,
    }

def createDirectory(dirName):
    try:
        # Create target Directory
        mkdir(dirName)
        print("Creating directory %s" % (dirName))
    # the directory allready exists
    except FileExistsError as e:
        pass

def setup():
    createDirectory(download_path+'/1 pictures')
    createDirectory(download_path+'/2 videos')
    createDirectory(download_path+'/3 documentos')
    createDirectory(download_path+'/4 zip')
    createDirectory(download_path+'/5 libros')

def order_files(listfiles):
    for file in listfiles:
        # get filename and filextension
        filename, filextension = splitext(file)
        filextension = filextension.replace('.', '')
        # get the number of the switch depending of file extension
        switch = switcher.get(filextension, 0)

        if switch != 0:
            # create the paths
            filepath = download_path+"/"+file
            newpath = download_path+dirs.get(switch)+"/"+file
            # get the time
            time = strftime("[%Y-%m-%d %H:%M:%S]", gmtime())
            # log the action
            print("{:22} Moving {:<40.40} from Downloads to {:10} ".format(time,file,dirs.get(switch)))
            # move the file
            rename(filepath,newpath)

        
if __name__ == "__main__":
    # create the folders if they dont exist
    setup()

    listfiles = [f for f in listdir(download_path) if isfile(join(download_path, f))]

    order_files(listfiles)
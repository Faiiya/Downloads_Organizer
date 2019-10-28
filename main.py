#Organizador de la carpeta downloads 

from os import listdir, mkdir, rename
from os.path import isfile, join, splitext
from time import gmtime, strftime
from shutil import move

download_paths = ['/home/faiya/Downloads','/media/faiya/B80843F40843B064/Users/Trabajo/Downloads', '/media/faiya/B80843F40843B064/Users/faiya/Downloads']

destination_path = '/media/faiya/CAE2E37BE2E369E1/999. DOWNLOADS' #'/home/faiya/Documents'

dirs = {
    1: '/1 pictures',
    2: '/2 videos',
    3: '/3 documentos',
    4: '/4 zip',
    5: '/5 libros',
    6: '/6 executables'
}

switcher = {
        "jpg":  1,
        "jpeg": 1,
        "png":  1,
        "mkv":  2,
        "mp4":  2,
        "webm": 2,
        "pdf":  3,
        "odt":  3,
        "doc":  3,
        "docx": 3,
        "txt":  3,
        'json': 3,
        "zip":  4,
        "rar":  4,
        "tar":  4,
        "epub": 5,
        "azw3": 5,
        'exe':  6,
        'msi':  6,
        'torrent': 6,
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
    createDirectory(destination_path+'/1 pictures')
    createDirectory(destination_path+'/2 videos')
    createDirectory(destination_path+'/3 documentos')
    createDirectory(destination_path+'/4 zip')
    createDirectory(destination_path+'/5 libros')

def order_files(listfiles, path):
    for file in listfiles:
        # get filename and filextension
        filename, filextension = splitext(file)
        filextension = filextension.replace('.', '')
        # get the number of the switch depending of file extension
        switch = switcher.get(filextension.lower(), 0)

        if switch != 0:
            # create the paths
            filepath = path+"/"+file
            newpath = destination_path+dirs.get(switch)
            # get the time
            time = strftime("[%Y-%m-%d %H:%M:%S]", gmtime())
            # log the action
            print("{:22} Moving {:<40.40} from {:<20.20} to {:10} ".format(time, file, path, dirs.get(switch)))
            # move the file
            move(filepath,newpath)

            # print("[WARNING] File extension for {} not recognized".format(file))
        
if __name__ == "__main__":
    # create the folders if they dont exist
    setup()

    print("[INFO] Checking files")
    for path in download_paths: 
        listfiles = [f for f in listdir(path) if isfile(join(path, f))]
        order_files(listfiles, path)
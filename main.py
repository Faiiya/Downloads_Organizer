#Organizador de la carpeta downloads 

from os import listdir, mkdir, rename
import sys
from os.path import isfile, join, splitext, exists, dirname
from time import gmtime, strftime
from shutil import move
import re
import pickle

# list of paths to check on for files
checked_folders = ['/home/YOU/Downloads','/OTHER/FOLDER/PATH']

dest_folder = '/your/dest/folder'

pathname = dirname(sys.argv[0])     

not_recognized = []

# list of folders you want to create to organize
# you can add as much as you want or remove the ones you dont like
dirs = {
    1: '/1 pictures',
    2: '/2 videos',
    3: '/3 documentos',
    4: '/4 zip',
    5: '/5 libros',
    6: '/6 executables'
}

# list of fileextensions to folder
# to add an extension just put the name and the dest folder
# of dirs
switcher = {
        "jpg":  1,
        "jpeg": 1,
        "png":  1,
        "mkv":  2,
        "mp4":  2,
        "webm": 2,
        "pdf":  3,
        "odt":  3,
        'ods':  3,
        'ini':  3,
        "doc":  3,
        'log':  3,
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
        'jar':  6,
        'sh':   6,
        'apk':  6,
        'vce':  6,
        'iso':  6,
        'torrent': 6,
    }

def createDirectory(dirName):
    try:
        # Create target Directory
        mkdir(dirName)     
    # the directory allready exists
    except FileExistsError as e:
        pass

def move_rename(path,newpath,file):
    filename, filextension = splitext(file)

    # get the number of the switch depending of file extension
    switch = switcher.get(filextension.lower(), 0)

    tem_filename = filename
    old_name = path+"/"+file
    if "rename_" in filename:
        filename = re.sub('(\d+)(?!.*\d)', lambda x: str(int(x.group(0)) + 1), filename)
    else:
        filename = filename+" rename_1"
    filepath= path+"/"+filename+filextension

    # get the time
    time = strftime("[%Y-%m-%d %H:%M:%S]", gmtime())
    # log the action
    print("[INFO]{:22} Renaming {:<20.20} to {:<20.20}".format(time, tem_filename, filename))
    rename(old_name,filepath)
    try:
        print("[INFO]{:22} Moving {:<40.40} from {:<20.20} to {:10} ".format(time, filepath, path, dirs.get(switch)))
        move(filepath,newpath)
    except:
        move_rename(path,newpath,filename+filextension)

def setup():
    global not_recognized
    for key, value in dirs.items():
        createDirectory(dest_folder+value)
    try:
        with open(pathname+'/not_recognized.pkl', 'rb') as f:
            not_recognized = pickle.load(f)
    except FileNotFoundError:
        not_recognized = []

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
            newpath = dest_folder+dirs.get(switch)
            # check if directory exists before moving, otherwise in a rare case it can create a bug where
            # it creates a file and move files to it basically deleting your files.
            if not exists(newpath):
                createDirectory(newpath)
            # get the time
            time = strftime("[%Y-%m-%d %H:%M:%S]", gmtime())
            # log the action
            print("[INFO]{:22} Moving {:<40.40} from {:<20.20} to {:10} ".format(time, file, path, dirs.get(switch)))
            try:
                # move the file
                move(filepath,newpath)
            except:
                print("[WARNING]{:22} name allready exists {}".format(time, filename))
                move_rename(path,newpath,file)
        elif file not in not_recognized:
            # get the time
            time = strftime("[%Y-%m-%d %H:%M:%S]", gmtime())
            # log the action
            print("[WARNING]{:22} File extension for {} not recognized".format(time, file))
            not_recognized.append(file)
        
if __name__ == "__main__":
    # create the folders if they dont exist
    setup()

    time = strftime("[%Y-%m-%d %H:%M:%S]", gmtime()) 
    print("[INFO]{:22} Checking files".format(time))

    for path in checked_folders: 
        listfiles = [f for f in listdir(path) if isfile(join(path, f))]
        order_files(listfiles, path)
    
    with open(pathname+'/not_recognized.pkl', 'wb') as f:
        pickle.dump(not_recognized, f)

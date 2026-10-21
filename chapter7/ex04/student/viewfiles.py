"""
Program: viewFiles.py
Author: Michael Guillen

Print contents of file if input is a file, and print contents of all
files if input is a directory
"""

import os, os.path

def main():
    path = os.getcwd()
    displayFiles(path)


def displayFiles(pathName):
    if os.path.isfile(pathName):
        print("File name:", pathName)
        openFile = open(pathName)
        contents = openFile.read()
        print(contents)
        openFile.close()
    elif os.path.isdir(pathName):
        print("Directory name:", pathName) 
        _list = os.listdir(pathName)
        for element in _list:
            fullPath = pathName + os.sep + element  
            displayFiles(fullPath)  

if __name__ == "__main__":
    main()
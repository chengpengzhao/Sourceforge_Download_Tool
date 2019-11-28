# Sourceforge_Download_Tool
 This is a simple python script which is used to download files from [sourceforge](https://sourceforge.net/). 
## At the begining
 Oneday I suddenly want to download the [OpenFOAM_Workshops](https://sourceforge.net/projects/openfoam-extend/files/OpenFOAM_Workshops/) to study. However, I found it was a waste of time when I was clicking a file by another. So I made a simple python crawler to build folders and download files automatically.
## What I use
 - Python3
 - Requests lib for python
 - [you-get](https://you-get.org/)
## How to use it
 1. Run the `getlinks.py` to build folders and generate .txt files which include download urls.
 2. Run the `downloadfiles.py` to read the generated .txt files and use you-get to download them.
 3. If the size of what you want to download is to big, you may run the `downloadfiles.py` several times and the program will begin from the files you haven't got.

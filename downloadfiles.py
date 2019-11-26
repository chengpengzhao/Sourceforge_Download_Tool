import re
import os

def findlinks_and_download(item):
    current = os.getcwd()
    path = re.findall('(.*?)\\\\links.txt', item)[0]
    os.chdir(path)
    f = open('links.txt', 'r')
    for line in f.readlines():
        filename_with_suffix= re.findall('https://sourceforge.net/projects.*/(.*?)/download',line)[0]
        if not os.path.exists(filename_with_suffix):
            os.system("you-get " + "-O"+filename_with_suffix+"  "+ line )
    os.chdir(current)


if __name__ == '__main__':
    g = os.walk('.')
    files = []
    for path, dir_list, file_list in g:
        for file_name in file_list:
            files.append(os.path.join(path, file_name))
    for item in files:
        if re.findall('links.txt', item) == []:
            continue
        else:
            findlinks_and_download(item)

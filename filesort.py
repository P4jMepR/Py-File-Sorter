import os, re, shutil
numberoffiles = 0
#This solution is faster but path is absolute and both variables have to be adjusted in order for it to work!
#filesdir = "C:\\Users\\Boryshehe\\Desktop\\sort\\notsorted"
#homedir = "C:\\Users\\Boryshehe\\Desktop\\sort"
filesdir = os.getcwd() + "/" + "notsorted"
homedir = os.getcwd()
def createfolder():
	path = homedir + "\\" + ext
	path = str(path)
	if not os.path.exists(ext):
		os.makedirs(ext)
	return path
filestosort = os.listdir(filesdir)
for plik in filestosort:
	konkretnyplik = filestosort[numberoffiles]
	if "." in konkretnyplik:
		directorytofile = filesdir + "\\" + konkretnyplik
		ext = os.path.splitext(konkretnyplik)[1]
		ext = ext.lstrip(".")
		path = createfolder()
		shutil.move(directorytofile, path)
	numberoffiles += 1
print("Done")
import os, shutil
numberoffiles = 0

""""
This solution does not require moving script to desired directory, but used path is absolute and it has to be adjusted in order for it to work!

filesdir = "C:\\Users\\[windows-username]\\Desktop\\"
homedir = "C:\\Users\\[windows-username]\\Desktop\\"
"""

filesdir = os.getcwd()
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
	if "." in konkretnyplik and konkretnyplik != "filesort.py":
		directorytofile = filesdir + "\\" + konkretnyplik
		ext = os.path.splitext(konkretnyplik)[1]
		ext = ext.lstrip(".")
		path = createfolder()
		shutil.move(directorytofile, path)
	numberoffiles += 1
print("Done")

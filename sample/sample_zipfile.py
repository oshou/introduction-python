import zipfile

files = zipfile.ZipFile("test.zip")
print(files.namelist())

files.extractall()

files.close()

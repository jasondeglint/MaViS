import os



folder = '/home/bll/output5/'


files = os.listdir(folder)
print(type(files))
files.sort()
print(files)
print(len(files))
print(files[int(len(files)/2)])
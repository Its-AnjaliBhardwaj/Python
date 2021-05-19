files = ['demo.exe', 'help.txt', 'asleeep.py', 'dox.doc']

#lambda expression

remove_extensions = lambda filename: filename.split('.')[0]
clean_names = list(map(remove_extensions, files))
print(clean_names)
'''Delete files by name, extension, size, or a combination of the three

    cli flags:

    file name (optional)
    file extension (optional)
    files size (optional)
'''
import os

my_path = 'C:/Users/J/Documents/python/book1-exercises/chp09/practice_files/little pics'

for current_folder, subfolders, file_names in os.walk(my_path):
	for f in file_names:
		possible_deletions = os.path.join(current_folder, f)
		if f[-3:].lower() == 'jpg':
			size = os.path.getsize(possible_deletions)
			if size < 2000:
				print(os.remove(possible_deletions))
				print('{} has been removed.'.format(possible_deletions))
				print('\n')


'''
flag for file extension

flag for file size in bytes

flag for file name

path to folder containing files to be deleted

help section

'''

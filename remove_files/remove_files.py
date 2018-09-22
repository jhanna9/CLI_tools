'''Delete files by name, extension, size, or a combination of the three

    cli flags:

    path to file
    file name (optional)
    file extension (optional)
    files size (optional)
'''
import argparse
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Path to the files.')
    parser.add_argument('-nm', '--name', help='The name of the file to be deleted.', action='store_true')
    parser.add_argument('-ext', '--extension', help='The type of extension to be deleted', action='store_true')
    parser.add_argument('-s', '--size', help='The minimum size of the file to be deleted', action='store_true')
    args = parser.parse_args()

    if args.private:
        print('ig account is private')
    else:
        get_content(get_links(args.username))


if __name__ == '__main__':
    main()

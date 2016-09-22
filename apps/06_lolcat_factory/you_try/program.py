import os
import platform

import cat_service
import subprocess


def main():
    # print the header
    print_header()

    # get or create output folder
    folder = get_or_create_output_folder()
    print('Found or created folder: ' + folder)

    # download cats
    download_cats(folder)

    # display cats
    display_cats(folder)


def print_header():
    print('---------------------------------')
    print('          CAT FACTORY')
    print('---------------------------------')


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)
    # print(full_path)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print('Contacting server to download cats...')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat {}'.format(i)
        print('Downloading cat {}'.format(name))
        cat_service.get_cat(folder, name)
    print('done.')


def display_cats(folder):
    # open folder
    print('Displaying cats in OS window.')
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['start', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print('We do not support your OS.')


if __name__ == '__main__':
    main()

import os
import cat_service


def main():
    print_header()
    folder = get_or_create_output_folder()
    print('Found or created folder: {}'.format(folder))

    download_cats(folder)
    # display cats
    print('Hello from Main')


def print_header():
    print('-----------------------------')
    print('-------- CAT FACTORY --------')
    print('-----------------------------')


def get_or_create_output_folder():
    # print(__name__)
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    # full_path = os.path.abspath(os.path.join('.', folder))
    full_path = os.path.abspath(os.path.join(base_folder, folder))
    # print(full_path)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):  # Para chequear si el directoorio existe
        print('Creando nuevo directorio en: {}.'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print('Contacting server to download cats...')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat {}'.format(i)
        print('Downloading cat {}'.format(name))
        # print(i, end=', ') # con "end" se puede definir el caracter final de cada print
        cat_service.get_cat(folder, name)

    print('Done! ')


if __name__ == '__main__':
    main()

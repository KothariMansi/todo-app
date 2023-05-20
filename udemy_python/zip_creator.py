import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, 'compressed.zip')
    with zipfile.ZipFile(dest_path, 'w') as archive:
        try:
            for filepath in filepaths:
                filepath = pathlib.Path(filepath)
                archive.write(filepath, arcname=filepath.name)
        except:
            archive.write(filepaths, arcname=filepath.name)


if __name__ == "__main__":
    make_archive('C:/Users/PC/Desktop/python/udemy_python/new/c.txt',
                 'C:/Users/PC/Desktop/python/udemy_python/new')

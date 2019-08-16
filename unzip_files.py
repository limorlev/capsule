import sys
import os
from zipfile import ZipFile

# source_path = r'H:\CapsulaArchive_TEMP\BatchProcess\Output'
# dest_path = r'H:\CapsulaArchive_TEMP\BatchProcess\Output\test'

source_path = r'\\clalit\dfs$\CapsulaArchive_TEMP\BatchProcess\Output\ASAF_Archive'
dest_path = r'\\clalit\dfs$\Integration\Capsula'
list_files = list()


def create_list_full_path_file(source_path):
    for path, dir_list, file_list in os.walk(source_path):
        for file_name in file_list:
            list_files.append(os.path.join(path, file_name))
    return list_files


def unzip_file(file, dest_path):
    with ZipFile(file, 'r') as zipObj:
        zipObj.extractall(dest_path)

#
# def unzip_files(file):
#     with ZipFile(file, 'r') as zipObj:
#         listOfFileNames = zipObj.namelist()
#         for fileName in listOfFileNames:
#             if fileName.endswith('.xml'):
#                 zipObj.extract(fileName, r'H:\CapsulaArchive_TEMP\BatchProcess\Output\xml')
#             else:
#                 zipObj.extract(fileName, r'H:\CapsulaArchive_TEMP\BatchProcess\Output\others')


if __name__ == '__main__':
    # source_path = sys.argv[1]
    # dest_path = sys.argv[2]

    list_files = create_list_full_path_file(source_path)
    for file_full_path in list_files:
        try:
            unzip_file(file_full_path, dest_path)
        except Exception as ex:
            print("ther is a problame to unzip file: {} Error:{}".format(file_full_path, ex))
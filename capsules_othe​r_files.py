import os
import shutil


def create_list_full_path_file(list_files, source_path):
    '''

    :param source_path: source path with files after unzip
    :return: list with files full path
    '''
    for path, dir_list, file_list in os.walk(source_path):
        for file_name in file_list:
            list_files.append(os.path.join(path, file_name))
    return list_files


def parse_file_name(split_file_name):
    '''

    :param split_file_name: list with data from file name
    :return: tuple (kod_moh_alfa, file_name_year, file_name_month, file_name_day)
    '''
    kod_moh_alfa = split_file_name[3]
    if kod_moh_alfa == '11108':
        kod_moh_alfa = '11109'
    file_name_date = split_file_name[4][:8]
    file_name_year = file_name_date[:4]
    file_name_month = file_name_date[4:6]
    file_name_day = file_name_date[6:8]
    return kod_moh_alfa, file_name_year, file_name_month, file_name_day


def split_name_file(file_name):
    '''

    :param file_name: string file name
    :return: list after split
    '''
    list_file_name = file_name.split('_')
    return list_file_name

# def move_file(source, dest, message):
#     try:
#         shutil.move(source, dest)
#     except OSError as ex:
#         print(message.format(ex))


def main(source_path, dest_path, archive_duplicates_path, archive_error_path):
    list_files = list()
    list_files = create_list_full_path_file(list_files, source_path)

    for file_full_path in list_files:
        file_name = os.path.basename(file_full_path)
        split_file_name = split_name_file(file_name)
        if len(split_file_name) == 7:
            kod_moh_alfa, file_name_year, file_name_month, file_name_day = parse_file_name(split_file_name)

            dest_location = os.path.join(dest_path, kod_moh_alfa, file_name_year, file_name_month, file_name_day)

            '''create folders if not exsist'''
            if not os.path.exists(dest_location):
                try:
                    os.makedirs(dest_location)
                except OSError as ex:
                    print("There is a problem creating folders. Error! {}".format(ex))
                    raise Exception("There is a problem creating folders. Error! {}".format(ex))

            if os.path.isfile(os.path.join(dest_location, file_name)):
                try:
                    print("The file_name {} olready exsist in the path {}. the file going move to {}".format(file_name, dest_location, archive_duplicates_path))
                    shutil.move(file_full_path, archive_duplicates_path)
                except shutil.Error:
                    print("There is a problem moving the file to the destination. {} status code 30.".format(file_full_path))
            else:
                try:
                    shutil.move(file_full_path, dest_location)
                except shutil.Error:
                    print("There is a problem moving the file to the destination. {} status code 30.".format(file_full_path))
        else:
            print("Invalid file name: {} status code 40.".format(file_name))
            try:
                shutil.move(file_full_path, archive_error_path)
            except shutil.Error:
                print("There is a problem moving the file {} to the archive error path. {}.".format(file_full_path, archive_error_path))
            continue


if __name__ == '__main__':
    '''prod'''
    # source_path = r'\\clalit\dfs$\Integration\Capsula'
    # dest_path = r'\\clalit\dfs$\OfekDocs\Capsula'
    # archive_duplicates_path = r'\\clalit\dfs$\OfekDocs\Capsula\Archive_Duplicates'
    # archive_error_path = r'\\clalit\dfs$\OfekDocs\Capsula\Archive_Error'

    '''test'''
    # source_path = r'H:\CapsulaArchive_TEMP\BatchProcess\Output\others'
    # dest_path = 'C:\capsula'
    # archive_duplicates_path = r'C:\capsula\Archive_Duplicates'
    # archive_error_path = r'C:\capsula\Archive_Error'

    '''home'''
    source_path = r'T:\Users\yaniv\Dropbox\Dropbox\Limor_Laptop\capsula'
    dest_path = r'T:\Users\yaniv\Dropbox\Dropbox\Limor_Laptop\capsula\dest'
    archive_duplicates_path = r'T:\Users\yaniv\Dropbox\Dropbox\Limor_Laptop\capsula\Archive_Duplicates'
    archive_error_path = r'T:\Users\yaniv\Dropbox\Dropbox\Limor_Laptop\capsula\Archive_Error'

    main(source_path, dest_path, archive_duplicates_path, archive_error_path)

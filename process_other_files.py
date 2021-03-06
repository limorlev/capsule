import os
import shutil
import settings
from AppContext import AppContext
import os


def create_list_full_path_file(list_files, source_path):
    for path, dir_list, file_list in os.walk(source_path):
        for file_name in file_list:
            list_files.append(os.path.join(path, file_name))
    return list_files


def file_name_exceptions(kod_moh_alfa, file_name_year, file_name_month, file_name_day):
    if kod_moh_alfa == '11108':
        kod_moh_alfa = '11109'

    return kod_moh_alfa, file_name_year, file_name_month, file_name_day


def parse_file_name(file_name_parts):
    kod_moh_alfa = file_name_parts[3]
    file_name_date = file_name_parts[4][:8]
    file_name_year = file_name_date[:4]
    file_name_month = file_name_date[4:6]
    file_name_day = file_name_date[6:8]
    kod_moh_alfa, file_name_year, file_name_month, file_name_day = file_name_exceptions(kod_moh_alfa,
                                                                                        file_name_year,
                                                                                        file_name_month,
                                                                                        file_name_day)
    return kod_moh_alfa, file_name_year, file_name_month, file_name_day


# def move_file(source, dest, message):
#     try:
#         shutil.move(source, dest)
#     except OSError as ex:
#         print(message.format(ex))


def main(source_path, dest_path, archive_duplicates_path, archive_error_path):
    files_to_process = list()
    files_to_process = create_list_full_path_file(files_to_process, source_path)

    for file_full_path in files_to_process:
        file_name = os.path.basename(file_full_path)
        file_name_parts = file_name.split('_')
        if len(file_name_parts) == settings.FILE_NAME_PARTS:
            kod_moh_alfa, file_name_year, file_name_month, file_name_day = parse_file_name(file_name_parts)
            dest_location = os.path.join(dest_path, kod_moh_alfa, file_name_year, file_name_month, file_name_day)

            # create folders if not exist
            if not os.path.exists(dest_location):
                try:
                    os.makedirs(dest_location)
                except OSError as ex:
                    print(settings.error_messages['folder_creation_error'].format(ex))
                    raise Exception(settings.error_messages['folder_creation_error'].format(ex))

            if os.path.isfile(os.path.join(dest_location, file_name)):
                try:
                    print(settings.error_messages['existing_file'].format(file_name,
                                                                     dest_location,
                                                                     archive_duplicates_path))
                    shutil.move(file_full_path, archive_duplicates_path)
                except shutil.Error:
                    print("There is a problem moving the file to the destination. {} status code 30.".format(
                                                                                                        file_full_path))
            else:
                try:
                    shutil.move(file_full_path, dest_location)
                except shutil.Error:
                    print("There is a problem moving the file to the destination. {} status code 30.".format(
                                                                                                        file_full_path))
        else:
            print(settings.error_messages['error_files'].format(file_name))
            try:
                shutil.move(file_full_path, archive_error_path)
            except shutil.Error:
                print("There is a problem moving the file {} to the archive error path. {}.".format(file_full_path,
                                                                                                    archive_error_path))
            # continue


if __name__ == '__main__':
    app_context = AppContext()
    env = app_context.get_environment()
    main(settings.capsules_paths[env]['source_path'],
         settings.capsules_paths[env]['dest_path'],
         settings.capsules_paths[env]['archive_duplicates_path'],
         settings.capsules_paths[env]['archive_error_path'])



capsules_paths = {
    'prod': {
        'source_path': r'\\clalit\dfs$\Integration\Capsula',
        'dest_path': r'\\clalit\dfs$\OfekDocs\Capsula',
        'archive_duplicates_path': r'\\clalit\dfs$\OfekDocs\Capsula\Archive_Duplicates',
        'archive_error_path': r'\\clalit\dfs$\OfekDocs\Capsula\Archive_Error',
    },
    'test': {
        'source_path': r'H:\CapsulaArchive_TEMP\BatchProcess\Output\others',
        'dest_path': r'C:\capsula',
        'archive_duplicates_path': r'C:\capsula\Archive_Duplicates',
        'archive_error_path': r'C:\capsula\Archive_Error',
    },
    'home': {
        'source_path': r'T:\Users\yaniv\Dropbox\Dropbox\Limor_Laptop\capsula',
        'dest_path': r'T:\Users\yaniv\Dropbox\Dropbox\Limor_Laptop\capsula\dest',
        'archive_duplicates_path': r'T:\Users\yaniv\Dropbox\Dropbox\Limor_Laptop\capsula\Archive_Duplicates',
        'archive_error_path': r'T:\Users\yaniv\Dropbox\Dropbox\Limor_Laptop\capsula\Archive_Error',
    },
}

FILE_NAME_PARTS = 7
CONFIGURATION_FILE = r'c:\user\conf.json'
DEFAULT_ENVIRONMENT = 'home'
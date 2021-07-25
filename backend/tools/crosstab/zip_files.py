import os
from zipfile import ZipFile

def get_all_file_paths(directory):
    
    file_paths = []

    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths

def zip_files(directory):

    file_paths = get_all_file_paths(directory)
    print('Following files will be zipped:')
    
    for file_name in file_paths:
        print(file_name)

    with ZipFile('./static/files/results.zip','w') as zip:
        for file in file_paths:
            zip.write(file)

    print('All files zipped successfully!')
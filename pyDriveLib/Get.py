from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import shutil
import os


def get_file_by_title(drive:GoogleDrive, parent_id:str, file_title:str, dst="", move=False):
    file_list = drive.ListFile({'q': f"'{parent_id}' in parents and trashed=false"}).GetList()
    for file in file_list:
        if file['title'] == file_title:
            file.GetContentFile(file['title'])
    if move and os.path.isdir(dst):
        shutil.move(file_title, dst)


def get_file_by_list(drive:GoogleDrive, file_list:list, dst="", move=False):
    for file in file_list:
        file.GetContentFile(file['title'])
        if move and os.path.isdir(dst):
            filename = rename_if_file_exists(dst, file['title'])
            os.rename(file['title'], filename)
            shutil.move(filename, dst)


def get_id_by_title(drive:GoogleDrive, parent_id:str, file_title:str, all_folder=False):
    file_list = drive.ListFile({'q': f"'{parent_id}' in parents and trashed=false"}).GetList()
    result = []
    for file in file_list:
        if file_title in file['title']:
            result.append(file)
        elif all_folder and file['mimeType'] == 'application/vnd.google-apps.folder':
            result = result + get_id_by_title(drive, file['id'], file_title, all_folder=True)
    return result


def rename_if_file_exists(path:str, filename:str):
    new_filename = filename
    count = 1
    while os.path.exists(f'{path}/{new_filename}'):
        sep_point = filename.rfind('.')
        new_filename = filename[:sep_point] + f'({count})' + filename[sep_point:]
        count = count+1
    return new_filename


from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os


def build_opt_path(drive:GoogleDrive, parent_id:str, opt_path_name:str, max_generation:int, population:int):
    # Create opt path
    file_metadata = {
        'title': opt_path_name,
        'parents': [{'id': parent_id}],
        'mimeType': 'application/vnd.google-apps.folder'
    }
    opt_path = drive.CreateFile(file_metadata)
    opt_path.Upload()

    # create gen path under opt path
    for generation in range(1, max_generation+1):
        file_metadata = {
            'title': f'Gen{generation}',
            'parents': [{'id': opt_path['id']}],
            'mimeType': 'application/vnd.google-apps.folder'
        }
        gen_path = drive.CreateFile(file_metadata)
        gen_path.Upload()

        # create gbest folder under gen path
        file_metadata = {
            'title': 'gbest',
            'parents': [{'id': gen_path['id']}],
            'mimeType': 'application/vnd.google-apps.folder'
        }
        gbest_path = drive.CreateFile(file_metadata)
        gbest_path.Upload()

        # create p path under gen path
        for p in range(1, population+1):
            file_metadata = {
                'title': f'p{p}',
                'parents': [{'id': gen_path['id']}],
                'mimeType': 'application/vnd.google-apps.folder'
            }
            p_path = drive.CreateFile(file_metadata)
            p_path.Upload()

            # create pbest folder under p path
            file_metadata = {
                'title': 'pbest',
                'parents': [{'id': p_path['id']}],
                'mimeType': 'application/vnd.google-apps.folder'
            }
            pbest_path = drive.CreateFile(file_metadata)
            pbest_path.Upload()

    return opt_path


# this function will create a mode.txt in drive,
# we can update/check content of it to tell
# all computers, what is the phase in entire workflow
def create_mode_file(drive:GoogleDrive, parent_id:str, local_mode_file:str):
    if not os.path.exists(local_mode_file):
        return
    file_metadata = {
        'title': 'mode.txt',
        'parents': [{'id': parent_id}]
    }
    file = drive.CreateFile(file_metadata)
    file.SetContentFile(local_mode_file)
    # this will override existed mode.txt, at most one mode.txt in parent_id
    # if there is a mode.txt under parent_id, but in trashed, it will replace the file in trashed...
    file['title'] = 'mode.txt'
    file.Upload()
    return file

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pyDriveLib import Build
from pyDriveLib import Get
from pyDriveLib import Put
import os


gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

workspace_id = '1Wmy48lI4owzLI6SM82tkgx0UzayABvTN'
#Build.build_opt_path(drive, workspace_id, 'testing', 2, 3)

#Get.get_file(drive, workspace_id, 'tt123.txt', move=True, dst='./to here')

#files = Get.get_id_by_title(drive, workspace_id, '.txt', all_folder=True)
#Get.get_file_by_list(drive, files, dst='./to here', move=True)

#Put.put_entire_dir_to_id(drive, workspace_id, './from here', change_name=True, put_folder_name='new from here')

#Put.put_all_files_to_id(drive, workspace_id, './from here', layer=3)

os.popen('echo mode_zz > mode.txt')

Build.create_mode_file(drive, workspace_id, './mode.txt')

os.popen('echo mode_y > mode.txt')


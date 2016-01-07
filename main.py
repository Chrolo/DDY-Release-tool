import configLoader
import subprocess
import shutil
import sys
torrent_files_folder = sys.argv[1]
torrent_save_path = sys.argv[2]
config_file_path = sys.argv[3]

print()     # extra line
print('adding files from "' + torrent_files_folder + '" to torrent file')
print('file will be saved to: ' + torrent_save_path)
print('config file path: ' + config_file_path)

config = configLoader.get_config(config_file_path)
file_name = torrent_save_path.split('\\')[-1]   # last element is the file name

subprocess.call([config['mktorrent_location'],
                 '-a', config['announce'],
                 '-c', '"' + config['comment'] + '"',
                 '-o', file_name,
                 torrent_files_folder])

# 2. COPY files/folder to another folder (???)

print(file_name)
shutil.move(file_name, torrent_save_path)

# upload to mega.nz (not implemented)

# upload to Nyaa

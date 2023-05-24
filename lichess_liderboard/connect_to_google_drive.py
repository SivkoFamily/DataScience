import logging
import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

logging.basicConfig(
    filename='test_logs.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(funcName)s || %(message)s', force=True)

def upload_file_in_google_drive(dir_path=''):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    logging.info('Start function upload_dir')
    try:
        fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
        for file in fileList:
            print('Title: %s, ID: %s' % (file['title'], file['id']))
            if(file['title'] == "data_for_tableau"):
                fileID = file['id']
        for file_name in os.listdir(dir_path):
            print(file_name)
            my_file = drive.CreateFile({'title': f'{file_name}', "mimeType": "text/csv", "parents": [{"kind": "drive#fileLink", "id": fileID}]})
            my_file.SetContentFile(os.path.join(dir_path, file_name))
            my_file.Upload()
        logging.info('Finish function upload_dir')
    except:
        logging.info('Function upload_dirupload_dir does not work !')

def main():
    print(upload_file_in_google_drive(dir_path='D:/dev/DataScience/lichess_liderboard/data_for_visualization'))

if __name__ =='__main__':
    main()

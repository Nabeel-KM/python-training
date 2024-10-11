import os
import datetime
import shutil

def backup_files(source,destination):
    today = datetime.datetime.today()
    backup_file_name  = os.path.join(destination,f"backup_{today}")
    shutil.make_archive(backup_file_name,"gztar",source)


source = "/home/nabeel-sarfraz/python-training"
destination = "/home/nabeel-sarfraz/python-training/backups"

backup_files(source, destination)
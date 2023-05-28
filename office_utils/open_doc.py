import os
import subprocess


def open_doc(file_path):
    args = [
        'C:\Program Files\LibreOffice\program\soffice.exe',
        '-o',
        file_path
    ]
    subprocess.call(args)


def get_absolute_path(path):
    return os.path.abspath(path)

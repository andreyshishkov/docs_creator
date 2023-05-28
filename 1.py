import os
import subprocess

path = r"C:\Users\Андрей\PycharmProjects\docs_creator\documents\acts\2023-05-28 15_41_00.odt"

args = [
    'C:\Program Files\LibreOffice\program\soffice.exe',
    '-o',
    path
]

subprocess.call(args)
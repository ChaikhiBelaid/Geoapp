import cx_Freeze
import sys
import xlrd
import datetime
import time


base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("Geoapp.py", base=base, icon="logo.ico")]

cx_Freeze.setup(
    name = "Geoapp",
    options = {"build_exe": {"packages":["tkinter","xlrd","time","datetime"], "include_files":["logo.ico","entre1.txt","sortie1.txt","entre2.txt","sortie2.txt","stock_entre.txt","stock_sortie.txt","base de données.xlsx"]}},
    version = "0.1",
    description = "Application de gestion de stock de déchets",
    executables = executables
    )
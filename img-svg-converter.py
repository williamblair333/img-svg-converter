import PySimpleGUI as sg
#from pathlib import Path
import pathlib
import os
import subprocess

sg.ChangeLookAndFeel('Reddit')

layout = [#[sg.Text('Click Rename files or folders')],
          #[sg.Text('Source for Folders', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
          [sg.Text('Image Source ', size=(15, 1)), sg.InputText(), sg.FileBrowse()],
          #[sg.InputText('This is my text', size=(15, 1))],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('Image to SVG Converter - Wayne Township IT Department', layout)

event, values = window.read()
window.close()

ext_svg = '.svg'

src_filename = values[0]

getpath = pathlib.Path(src_filename)
src_pathname = getpath.parent

dest_filename = str(src_pathname) + "\\" + (os.path.splitext(os.path.basename(src_filename))[0]) + ext_svg

src_filename = src_filename.replace("/", "\\")

print(src_filename)
#print (src_pathname)
print(dest_filename)

conversion = "C:\\util\\ImageMagick-7.0.10-30-portable-Q16-HDRI-x64\\magick.exe" + " " + src_filename + " " + dest_filename

print(conversion)
subprocess.call(conversion)

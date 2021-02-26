# Program name: ivy-svg-converter.py                                            #
# Author: William Blair                                                         #
# Date: 9/21/2020                                                               #
# Purpose:                                                                      #
# PySimpleGUI program that will more easily allow the user to                   #   
# 1. Convert image files to svg format                                          #
#                                                                               #

import PySimpleGUI as sg
import pathlib
import os
import subprocess

sg.ChangeLookAndFeel('Reddit')

layout =  [sg.Text('Image Source ', size=(15, 1)), sg.InputText(), \
           sg.FileBrowse()], [sg.Submit(), sg.Cancel()]

window = sg.Window('Image to SVG Converter - Insert IT Dept Name Here', layout)

event, values = window.read()
window.close()

ext_svg = '.svg'

src_filename = values[0]

getpath = pathlib.Path(src_filename)
src_pathname = getpath.parent

dest_filename = str(src_pathname) + "\\" + \
                (os.path.splitext(os.path.basename(src_filename))[0]) + ext_svg

src_filename = src_filename.replace("/", "\\")

print(src_filename)
print(dest_filename)

# You will need to install ImageMagick in order to do the actual conversion. 
# Change path as appropriate for location and OS
conversion = "C:\\util\\ImageMagick-7.0.10-30-portable-Q16-HDRI-x64\\magick.exe" + \
             " " + src_filename + " " + dest_filename

print(conversion)
subprocess.call(conversion)

#################################################################################

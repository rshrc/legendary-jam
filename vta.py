#!/usr/bin/env python3

import os
import re
import subprocess as sp

inputMediaFormat = "." + input("Enter input media format : ")
outputMediaFormat = "." + input("Enter output media format : ")

# Taking all the current files of specified format inside dir
for (dirname, dirs, files) in os.walk('.'):
    for inputFileName in files:
        # ex : if filename ends with ".mp4"
        if inputFileName.endswith(inputMediaFormat):
            # giving a new name to the file, for easy use
            newInputFileName = inputFileName.replace(" ", "_")
            newInputFileName = re.sub(
                "[^a-zA-Z0-9 \n\._]", "", newInputFileName)
            os.rename(inputFileName, newInputFileName)
            print("Renamed : "+inputFileName+" with " + newInputFileName)
            print("Converting " + inputFileName +
                  "to " + outputMediaFormat + "format")
            outputFileName = newInputFileName[:-4] + outputMediaFormat
            print(inputFileName)
            print(outputFileName)
            command = "ffmpeg -i " + newInputFileName + " "+outputFileName
            print(command)
            # converted to new file
            os.system(command)


# check if ffmpeg is installed in given system or not
# try:
#     checkffmpeg = sp.check_output(
#         "dpkg -l | grep \"ffmpeg\"", shell=True)
#     if checkffmpeg is not None:
# Taking the input and output media format

# except:
#     print("Need to install ffmpeg linux package")
#     os.system("sudo apt-get install ffmpeg")

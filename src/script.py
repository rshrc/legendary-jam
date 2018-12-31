#!/usr/bin/env python3

import os
import re

input_media_format = "." + input("Enter input media format : ")
output_media_format = "." + input("Enter output media format : ")

# Taking all the current files of specified format inside dir
for (dir_name, dirs, files) in os.walk('.'):
    for input_file_name in files:
        # ex : if filename ends with ".mp4"
        if input_file_name.endswith(input_media_format):
            # giving a new name to the file, for easy use
            new_input_file_name = input_file_name.replace(" ", "_")
            new_input_file_name = re.sub(
                "[^a-zA-Z0-9 \n\._]", "", new_input_file_name)
            os.rename(input_file_name, new_input_file_name)
            print("Renamed : " + input_file_name + " with " + new_input_file_name)
            print("Converting " + input_file_name +
                  "to " + output_media_format + "format")
            output_file_name = new_input_file_name[:-4] + output_media_format
            print(input_file_name)
            print(output_file_name)
            command = "ffmpeg -i " + new_input_file_name + " " + output_file_name
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

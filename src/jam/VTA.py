#!/usr/bin/env python3

import os
import re


class VTA:

    def __init__(self, input_media_format, output_media_format):
        """
        Takes two parameters during object creation (input -> output)
        :param input_media_format:
        :param output_media_format:
        """
        self.input_media_format = "." + input_media_format
        self.output_media_format = "." + output_media_format

    def convert_playlist(self):
        """
        Searches the entire directory for specified input files, and
        uses ffmpeg to convert the files into the specified output file
        :return: None
        """
        # Taking all the current files of specified format inside dir
        for (dir_name, dirs, files) in os.walk('.'):
            for input_file_name in files:
                # ex : if filename ends with ".mp4"
                if input_file_name.endswith(self.input_media_format):
                    # giving a new name to the file, for easy use
                    new_input_file_name = input_file_name.replace(" ", "_")
                    new_input_file_name = re.sub(
                        "[^a-zA-Z0-9 \n\._]", "", new_input_file_name)
                    os.rename(input_file_name, new_input_file_name)
                    print("Renamed : " + input_file_name + " with " + new_input_file_name)
                    print("Converting " + input_file_name +
                          "to " + self.output_media_format + "format")
                    output_file_name = new_input_file_name[:-4] + self.output_media_format
                    print(input_file_name)
                    print(output_file_name)
                    command = "ffmpeg -i " + new_input_file_name + " " + output_file_name
                    print(command)
                    # converted to new file
                    os.system(command)

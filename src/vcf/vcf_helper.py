#! /usr/bin/env python
#  -*- coding: utf-8 -*-
import os.path
import re
from datetime import datetime
from typing import List

from visitor import Visitor

vcard_regex_pattern = """.*VCARD\d*BEGIN\:VCARDVERSION\:\d\.\dN\:(\w+);*(.+)ORG\:(.+)TITLE\:(.*?)TEL;.*EMAIL\:(.+)NOTE\:"""


def receive_and_save(data: str, destination_directory: str) -> List[Visitor]:
    save_file(data, destination_directory)

    # Match Data
    found_visitors = match_data(data)

    # Print label
    if found_visitors:
        for found in found_visitors:
            found.print()

    return found_visitors


def match_data(data) -> List[Visitor]:
    """

    :param data: Scanned data
    :return: List[Visitor] Visitor list of matchs
    """

    result = re.match(vcard_regex_pattern, data)
    return_data = []

    print(data)
    if result:
        print("Search successful.")

        visitor = Visitor(
            result[1].strip(),
            result[2].strip(),
            result[3].strip(),
            result[4].strip(),
            result[5].strip()
        )
        return_data = [visitor]

    else:
        print("Search unsuccessful.")

    return return_data;


def save_file(data: str, destination_directory: str) -> str:
    print("Saving file")

    _create_dir(destination_directory)
    now = datetime.now()  # current date and time
    filename = now.strftime("%Y%m%d%H%M%S.%f.txt")
    file_location = os.path.join(destination_directory, filename)
    with open(file_location, 'w') as file:
        file.writelines("%s\n" % data)
    return file_location


def _create_dir(directory: str) -> None:
    try:
        if not os.path.exists(directory):
            os.mkdir(directory)
    except FileExistsError as e:
        print(e)

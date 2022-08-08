#! /usr/bin/env python
#  -*- coding: utf-8 -*-
import os.path
import re
from datetime import datetime
import sys



from src.vcf.visitor import Visitor


def load_template(printer_language: str = 'ipl', template_id: int = 0) -> str:
    data = ''
    template_filename = '%s_%02d.txt' % (printer_language, template_id)
    template_file_location = os.path.join('data', 'template', template_filename)

    with open(template_file_location, "r", encoding="utf8") as f:
        data = f.read()

    return data


def replace_visitor_fields(template: str, visitor: Visitor) -> str:
    data = template.replace('first_name', visitor.first_name)
    data = data.replace('last_name', visitor.last_name)

    return data


def print_label(label_str: str, printer_name: str) -> None:
    file_location = save_print_file(label_str)
    print("Printing %s ON %s" % (file_location, printer_name))

    if sys.platform == "win32":
        _print_windows(file_location, printer_name)

    if sys.platform != "win32":
        _print_linux(file_location, printer_name)


def _print_linux(file_location: str, printer_name: str) -> None:

    command = "lpr -P %s %s" % (printer_name, file_location)
    print(command)
    os.system(command)


def _print_windows(file_location: str, printer_name: str) -> None:

    command = 'PRINT %s /D:"%s"' % (file_location, printer_name)
    print(command)
    os.system(command)


def save_print_file(data) -> str:
    """

    :rtype: str Location of the saved file
    """
    # save
    filename = 'print_label.txt'
    file_location = os.path.join('data', filename)
    with open(file_location, 'w') as file:
        file.write(data)

    return file_location

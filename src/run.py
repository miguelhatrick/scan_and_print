#! /usr/bin/env python
#  -*- coding: utf-8 -*-
from typing import List

from vcf.visitor import Visitor
from vcf import vcf_helper
from vcf import print_helper
import configparser


def read_file():
    with open("data/vcard.txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            if not len(line.strip()):
                continue

            visitors = vcf_helper.receive_and_save(line, './collected')

            process(visitors)


def run_nonstop():
    while True:
        data = str(input())
        visitors = vcf_helper.receive_and_save(data, './collected')

        process(visitors)


def process(visitors: List[Visitor]):
    if not len(visitors):
        visitors = [Visitor('Visitante Stand 3355', '', 'Estimado', '', '')]

    for visitor in visitors:
        label_str = print_helper.replace_visitor_fields(template, visitor)

        print_helper.print_network(label_str, network_printer)


# Read local file `config.ini`.
config = configparser.ConfigParser()
config.read('config.ini')

printer = config.get('PRINT', 'LOCAL_PRINTER')
network_printer = config.get('PRINT', 'NETWORK_PRINTER_1')
template = print_helper.load_template_by_filename(config.get('PRINT', 'TEMPLATE_NAME'))
template_no_data = print_helper.load_template_by_filename(config.get('PRINT', 'NO_DATA_TEMPLATE_NAME'))

run_nonstop()

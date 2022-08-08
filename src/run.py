#! /usr/bin/env python
#  -*- coding: utf-8 -*-
from typing import List

from src.vcf.visitor import Visitor
from vcf import vcf_helper
from vcf import print_helper


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
        print_helper.print_label(template_no_data, printer)

    for visitor in visitors:
        label_str = print_helper.replace_visitor_fields(template, visitor)
        print_helper.print_label(label_str, printer)


printer = """\\\\DESKTOP-6DMSB1J\\pc43t"""
template = print_helper.load_template('ipl', 0)
template_no_data = print_helper.load_template_by_filename('ipl_no_data.txt')

run_nonstop()

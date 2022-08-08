#! /usr/bin/env python
#  -*- coding: utf-8 -*-
from typing import List

from src.vcf.visitor import Visitor
from vcf import vcf_helper
from vcf import print_helper


def read_file():
    with open("data/vcard.txt", "r") as f:
        data = f.read()
        visitors = vcf_helper.receive_and_save(data, './collected')

        process(visitors)


def run_nonstop():
    while True:
        data = str(input())
        visitors = vcf_helper.receive_and_save(data, './collected')

        process(visitors)


def process(visitors: List[Visitor]):
    for visitor in visitors:
        label_str = print_helper.replace_visitor_fields(template, visitor)
        print_helper.print_label(label_str, printer)


printer = """\\\\DESKTOP-6DMSB1J\\pc43t"""
template = print_helper.load_template('ipl', 0)
read_file()

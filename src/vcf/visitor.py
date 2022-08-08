#! /usr/bin/env python
#  -*- coding: utf-8 -*-

class Visitor:
    first_name: str
    last_name: str
    company: str
    title: str
    email: str

    def __init__(self, first_name: str,
                 last_name: str,
                 company: str,
                 title: str,
                 email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.title = title
        self.email = email

    def print(self) -> None:
        """
        Prints the current user data
        :rtype: object
        """
        print("-" * 120)
        print("First name : %s" % self.first_name)
        print("Last name : %s" % self.last_name)
        print("Company name : %s" % self.company)
        print("Title name : %s" % self.title)
        print("email : %s" % self.email)
        print("-" * 120)

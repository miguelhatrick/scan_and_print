#! /usr/bin/env python
#  -*- coding: utf-8 -*-

class Visitor:
    email: str
    last_name: str
    first_name: str

    def __init__(self, first_name: str, last_name: str, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def print(self) -> None:
        """
        Prints the current user data
        :rtype: object
        """
        print("-" * 120)
        print("First name : %s" % self.first_name)
        print("Last name : %s" % self.last_name)
        print("email : %s" % self.email)
        print("-" * 120)

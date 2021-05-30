#!python
# encoding: utf-8

# Created by Preload at 2020-07-13


class Verbose():
    def __init__(self):
        self.be_loud = False
        pass

    def print_info(self, *args):
        if self.be_loud:
            print(*args)

    def set_verbose_on(self):
        self.be_loud = True

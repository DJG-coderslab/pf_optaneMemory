#!python
# encoding: utf-8

# Created by Preload at 2020-07-14

import subprocess
import sys

from configparser import ConfigParser
from pathlib import Path

from frontend import FrontEnd


class Rstcli:
    def __init__(self, verb):
        self.frontend = FrontEnd()
        self.verb = verb
        if getattr(sys, 'frozen', False):
            self.app_path = Path(sys.executable).parent
        elif __file__:
            self.app_path = Path(__file__).parent
        self.rstcli = Path(self.app_path / 'rstcli64.exe')
        self.ini_file = self.app_path / 'optane.ini'
        self.set_up()
        self.parameters = [str(self.rstcli)]
        self.choosing_cli()

    def set_up(self):
        if self.ini_file.is_file():
            parser = ConfigParser()
            try:
                parser.read(self.ini_file)
                self.app_path = Path(parser.get('rstcli', 'path'))
                self.rstcli = Path(self.app_path /
                                   parser.get('rstcli', 'file_name'))
            except Exception:
                self.frontend.rstcli_error('Error reading .ini file')
        else:
            self.frontend.rstcli_error(self.rstcli)
            sys.exit(8)

    def cmd(self, *args):
        self.verb.print_info("cmd function:")
        params = self.parameters + args[0]
        optane = subprocess.Popen(params,
                                  stdout=subprocess.PIPE, shell=True)
        (output, err) = optane.communicate()
        output = output.decode("utf-8")
        return output

    def choosing_cli(self):
        parameters = ['-I']
        output = self.cmd(parameters)
        if 'cannot be used' in output:
            lines = (output.split('\r\n'))
            for i, line in enumerate(lines):
                if 'of the driver' in line:
                    self.rstcli = Path(
                        self.app_path /
                        ('rstcli64_' + line.split()[2][:4] + '.exe'))
        self.parameters = [str(self.rstcli)]

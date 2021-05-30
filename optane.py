import argparse
import sys


from verbose import Verbose
from frontend import FrontEnd
from rstcli_command import Rstcli


VERSION = '1.5.2'
DATE = '11.12.2020'


def size2int(value):
    """
    Function to convert size from rstcli to int number
    :param value:  size of disk, in string
    :return: size of disk in int
    """
    value = value
    if isinstance(value, int):
        return value
    return int(value.split()[0])


def enable_optane():
    clear_metadata()
    params = ['--OptaneMemory', '--enable']
    rstcli.cmd(params)


def clear_metadata():
    params = ['-M', '-Z']
    rstcli.cmd(params)


def check_optane():
    verb.print_info("check_optane")
    output_optane = rstcli.cmd(['--OptaneMemory', '--info'])
    output_i = rstcli.cmd(['-I'])
    verb.print_info(output_i)

    if 'Array_Intel_Optane' in output_i:
        frontend.optane_is_ok_info()
        return

    if 'Platform is Intel Optane ready.' in output_optane:
        frontend.optane_can_enable_info()
        return

    if 'PCH: Not supported' in output_optane and \
            'Optane feature: Not supported' in output_optane:
        """AHCI instead RAID in BIOS"""
        frontend.print_error(
            'Check setup Sata mode in BIOS (should be RTS with Optane)')
        return

    if 'Intel Optane memory module not detected: not present or ' \
       'remapping disabled' in output_optane:
        clear_metadata()
        check_optane()
        return

    if '--disable to continue' in output_optane:
        disable_optane()
        check_optane()
        return

    frontend.print_error('Unexpected error...')
    return


def disable_optane():
    params = ['--OptaneMemory', '--disable']
    rstcli.cmd(params)
    frontend.disable_optane_info()


def print_version():
    print('Version: {}'.format(VERSION))
    sys.exit()


# ========================================================================
#
#                          MAIN PROGRAM
#
# ========================================================================

do_enable = False
app_path = None
frontend = FrontEnd()
verb = Verbose()
parser = argparse.ArgumentParser()

parser.add_argument('-c', '--check', action='store_true')
parser.add_argument('-e', '--enable', action='store_true')
parser.add_argument('-d', '--disable', action='store_true')
parser.add_argument('-v', '--version', action='store_true')
parser.add_argument('-V', '--verbose', action='store_true')

args = parser.parse_args()
check = args.check
enable = args.enable
disable = args.disable
version = args.version

if args.verbose:
    verb.set_verbose_on()

rstcli = Rstcli(verb)

if version:
    print_version()
if check:
    check_optane()
if enable:
    enable_optane()
    check_optane()
if disable:
    disable_optane()

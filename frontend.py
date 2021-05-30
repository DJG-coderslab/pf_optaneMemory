#!python
# encoding: utf-8

# Created by Preload at 2020-07-14


import color_console as cons


class FrontEnd:
    def __init__(self):
        self.default_colors = cons.get_text_attr()
        self.default_fg = self.default_colors & 0x0007
        self.default_bg = self.default_colors & 0x0070

    def optane_is_ok_info(self):
        note = r"""


       ____  _____ _______       _   _ ______   _        ____  _  __
      / __ \|  __ \__   __|/\   | \ | |  ____| (_)      / __ \| |/ /
     | |  | | |__) | | |  /  \  |  \| | |__     _ ___  | |  | | ' / 
     | |  | |  ___/  | | / /\ \ | . ` |  __|   | / __| | |  | |  <  
     | |__| | |      | |/ ____ \| |\  | |____  | \__ \ | |__| | . \  _
      \____/|_|      |_/_/    \_\_| \_|______| |_|___/  \____/|_|\_\(_) 



            """
        cons.set_text_attr(self.default_colors)
        cons.set_text_attr(
            cons.FOREGROUND_GREEN | self.default_bg | cons.FOREGROUND_INTENSITY)
        print(note)
        cons.set_text_attr(
            cons.FOREGROUND_YELLOW | self.default_bg | cons.FOREGROUND_INTENSITY)
        print('     Please reboot the device before install OS')
        cons.set_text_attr(self.default_colors)

    def optane_can_enable_info(self):
        note = r''' 
                  ____  _____ _______       _   _ ______                            
                 / __ \|  __ \__   __|/\   | \ | |  ____|                           
                | |  | | |__) | | |  /  \  |  \| | |__                              
                | |  | |  ___/  | | / /\ \ | . ` |  __|                             
                | |__| | |      | |/ ____ \| |\  | |____                            
                 \____/|_|      |_/_/    \_\_| \_|______|   _         
                       | |                           | |   | |        
       ___ __ _ _ __   | |__   ___    ___ _ __   __ _| |__ | | ___  
      / __/ _` | '_ \  | '_ \ / _ \  / _ \ '_ \ / _` | '_ \| |/ _ \ 
     | (_| (_| | | | | | |_) |  __/ |  __/ | | | (_| | |_) | |  __/ 
      \___\__,_|_| |_| |_.__/ \___|  \___|_| |_|\__,_|_.__/|_|\___| 


            '''
        cons.set_text_attr(self.default_colors)
        cons.set_text_attr(
            cons.FOREGROUND_YELLOW | self.default_bg | cons.FOREGROUND_INTENSITY)
        print(note)
        cons.set_text_attr(self.default_colors)

    def print_error(self, err):
        err = err
        cons.set_text_attr(self.default_colors)
        cons.set_text_attr(
            cons.FOREGROUND_RED | self.default_bg | cons.FOREGROUND_INTENSITY)
        note = r"""

                 ______ _____  _____   ____  _____        
                |  ____|  __ \|  __ \ / __ \|  __ \       
                | |__  | |__) | |__) | |  | | |__) |      
                |  __| |  _  /|  _  /| |  | |  _  /       
                | |____| | \ \| | \ \| |__| | | \ \ _ _ _ 
                |______|_|  \_\_|  \_\\\____/|_|  \_(_|_|_)


            """
        cons.set_text_attr(self.default_colors)
        cons.set_text_attr(
            cons.FOREGROUND_RED | self.default_bg | cons.FOREGROUND_INTENSITY)
        print(note)
        print(err)
        cons.set_text_attr(self.default_colors)
        return

    def disable_optane_info(self):
        note = r"""


       ____  _____ _______       _   _ ______                           _ _           _     _          _ 
      / __ \|  __ \__   __|/\   | \ | |  ____|                         | (_)         | |   | |        | |
     | |  | | |__) | | |  /  \  |  \| | |__    __      ____ _ ___    __| |_ ___  __ _| |__ | | ___  __| |
     | |  | |  ___/  | | / /\ \ | . ` |  __|   \ \ /\ / / _` / __|  / _` | / __|/ _` | '_ \| |/ _ \/ _` |
     | |__| | |      | |/ ____ \| |\  | |____   \ V  V / (_| \__ \ | (_| | \__ \ (_| | |_) | |  __/ (_| |
      \____/|_|      |_/_/    \_\_| \_|______|   \_/\_/ \__,_|___/  \__,_|_|___/\__,_|_.__/|_|\___|\__,_|


        """
        cons.set_text_attr(self.default_colors)
        cons.set_text_attr(
            cons.FOREGROUND_YELLOW | self.default_bg | cons.FOREGROUND_INTENSITY)
        print(note)
        cons.set_text_attr(self.default_colors)

    def rstcli_error(self, path):
        cons.set_text_attr(
            cons.FOREGROUND_RED | self.default_bg | cons.FOREGROUND_INTENSITY)
        print('\nNot found the rstcli, expected here: {}'.format(path))
        cons.set_text_attr(self.default_colors)

"""  
ASCII generator:
http://patorjk.com/software/taag/#p=testall&f=Alpha&t=OPTANE%20was%20disabled
Font Name: Big
"""

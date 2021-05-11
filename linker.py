#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# LinKer v1.0 (GNU/Linux x86_64).
# Copyright (C) 2021 egrullon <Amix>.
# License GPLv3+: GNU GPL version 3 or later <https://www.gnu.org/licenses/gpl-3.0.html>.
# This program comes with ABSOLUTELY NO WARRANTY.
# This is free software and you are free to change and redistribute it.

# Author: egrullon <Amix>
# Date: 2021-05-10
# egrullon@cystrong.com
# www.cystrong.com
# Description: Find internal links potentially related to a given domain. This tool is very important as part of the Bug Bounties techniques.


import sys
import re
import socket
import urllib.request
from urllib.error import URLError
from bs4 import BeautifulSoup

def banner():
    print("""

       █████        ███             █████
      ░░███        ░░░             ░░███
       ░███        ████  ████████   ░███ █████  ██████  ████████
       ░███       ░░███ ░░███░░███  ░███░░███  ███░░███░░███░░███
       ░███        ░███  ░███ ░███  ░██████░  ░███████  ░███ ░░░
       ░███      █ ░███  ░███ ░███  ░███░░███ ░███░░░   ░███
       ███████████ █████ ████ █████ ████ █████░░██████  █████
      ░░░░░░░░░░░ ░░░░░ ░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░░  ░░░░░
                                                                v1.0
    """)
    
    return ''

try:
    def find_links(target):
        if not re.match('(?:http|https)://', target):
            return 'http://{}'.format(target)
        return target

    if len(sys.argv) != 2:
        print(banner())
        print('[*] Invalid amount of arguments.')
        print('[*] Usage: sudo python3 linker.py cystrong.com\n')
        sys.exit()

    else:
        target = (sys.argv[1])
        content = urllib.request.urlopen(find_links(target)).read()
        get_html_code = BeautifulSoup(content, 'html.parser')
        for links in get_html_code.find_all('a'):
            print(links.get('href'))

except KeyboardInterrupt:
    print("\nExiting Program")
    sys.exit()

except socket.gaierror:
    print("Connection Error")
    sys.exit()

except URLError:
    print("Unable to Open")
    sys.exit()


if __name__ == '__main__':
    print(find_links(target))

#!e:\projects\python\poc\webdemo-master\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'flex==6.14.1','console_scripts','swagger-flex'
__requires__ = 'flex==6.14.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('flex==6.14.1', 'console_scripts', 'swagger-flex')()
    )

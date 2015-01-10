import os
from datetime import datetime

hooking_time = datetime.now().strftime('%d-%m-%Y-%H-%M')

##ATTRIBUTS
ATTRIBUT_KEY= 'com.apple.FinderInfo'

SETTINGS_DIR = '.lokingfixers/logs' 

##LOG SETTINGS
LOG_FOLDER = SETTINGS_DIR
LOG_FILE_SIZE = 1 * 1024 * 1024
LOG_FILENAME = os.path.join(LOG_FOLDER, datetime.now().strftime('log-%d-%m-%Y-%H-%M.log'))
LOG_REPORT = os.path.join(LOG_FOLDER, datetime.now().strftime('report-%d-%m-%Y-%H-%M.log'))
LOG_ERROR = os.path.join(LOG_FOLDER, datetime.now().strftime('error-%d-%m-%Y-%H-%M.log'))

##HOME CONFIG FILES SETTINGS

SRC = os.path.expanduser('~')

# Where to put the archive
DEST_FOLDER = ''
DEST = os.path.join(SRC,DEST_FOLDER)

# Name of the archive
ARCHIVE = 'HomeDirectoryConfig.tar.gz'

# files to backup
FILES_LIST = [
        '.profile',
        '.pythonenv.py',
        '.emacs',
        '.vimrc',
        '.inputrc',
        '.gitconfig',
        '.pdbrc',
    ]

HOME_CONFIG = {
    'src' : SRC,
    'dest' : DEST,
    'files' : FILES_LIST,
    'archive' : 'HomeDirectoryConfig.tar.gz'
}

#DATABASE

dbname = 'lokingfixers.db'

DB = {
    'default': 'sqlite:///'+os.path.realpath(dbname),
    'test': 'sqlite:///'+os.path.realpath('test.db')
}
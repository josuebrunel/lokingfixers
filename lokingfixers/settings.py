import os
from datetime import datetime

##ATTRIBUTS
ATTRIBUT_KEY= 'com.apple.FinderInfo'

##LOG SETTINGS
LOG_FOLDER = 'lokingfixers/logs'
LOG_FILE_SIZE = 1 * 1024 * 1024
LOG_FILENAME = os.path.join(LOG_FOLDER, datetime.now().strftime('log-%d-%m-%Y-%H-%M.log'))
LOG_REPORT = os.path.join(LOG_FOLDER, datetime.now().strftime('report-%d-%m-%Y-%H-%M.log'))
LOG_ERROR = os.path.join(LOG_FOLDER, datetime.now().strftime('error-%d-%m-%Y-%H-%M.log'))

##HOME CONFIG FILES SETTINGS

HOME_CONFIG = {
    'src' : os.environ['HOME'],
    'dest' : os.path.join(os.environ['HOME'],'workspace/system/'),
    'files' : [
        '.profile',
        '.pythonenv.py',
        '.emacs',
        '.vimrc',
        '.inputrc',
        '.gitconfig'
    ],
    'archive' : 'HomeDirectoryConfig.tar.gz'
}

#DATABASE 
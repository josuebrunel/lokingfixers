import os
from datetime import datetime

#ATTRIBUTS
ATTRIBUT_KEY= 'com.apple.FinderInfo'

#LOG SETTINGS
LOG_FOLDER = 'logs'
LOG_FILE_SIZE = 1 * 1024 * 1024
LOG_FILENAME = os.path.join(LOG_FOLDER, datetime.now().strftime('log-%d-%m-%Y-%H-%M.log'))
LOG_REPORT = os.path.join(LOG_FOLDER, datetime.now().strftime('report-%d-%m-%Y-%H-%M.log'))
LOG_ERROR = os.path.join(LOG_FOLDER, datetime.now().strftime('error-%d-%m-%Y-%H-%M.log'))

#HOME CONFIG FILES SETTINGS
CONFIG_FILES_FOLDER_SRC=os.environ['HOME']
CONFIG_FILES_FOLDER_DEST = os.envrion['HOME']+'workspace/system/'
CONFIG_FILES = ['.profile', '.pythonenv', '.emacs', '.vimrc', '.inputrc', '.gitconfig']
CONFIG_ARCHIVES = 'HomeDirectoryConfig'

#DATABASE 
import os
from datetime import datetime

#LOG SETTINGS
LOG_FOLDER = 'logs'
LOG_FILE_SIZE = 1 * 1024 * 1024
LOG_FILENAME = os.path.join(LOG_FOLDER, datetime.now().strftime('log-%d-%m-%Y-%H-%M.log'))
LOG_REPORT = os.path.join(LOG_FOLDER, datetime.now().strftime('report-%d-%m-%Y-%H-%M.log'))
LOG_ERROR = os.path.join(LOG_FOLDER, datetime.now().strftime('error-%d-%m-%Y-%H-%M.log'))

#DATABASE 
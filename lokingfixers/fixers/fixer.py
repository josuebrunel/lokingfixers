import os, imp
from lokingfixers.tools import FLogger

# Loading from source file
settings = imp.load_source('', os.path.join(os.path.expanduser('~'), '.lokingfixers/settings.py'))
LOG_FILENAME, LOG_REPORT, LOG_ERROR = settings.LOG_FILENAME, settings.LOG_REPORT, settings.LOG_ERROR

class Fixer(object):
    """
    """

    def __init__(self, logger_name='fixer'):
        """
        """
        self.logger_name = logger_name
        
        self.logger = FLogger(self.logger_name, logfilename=LOG_FILENAME)
        self.reporter = FLogger(self.logger_name, logfilename=LOG_REPORT)
        self.log_error = FLogger(self.logger_name, logfilename=LOG_ERROR)

   
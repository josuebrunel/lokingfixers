from tools import FLogger
from cfg import LOG_FILENAME, LOG_REPORT, LOG_ERROR

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
    
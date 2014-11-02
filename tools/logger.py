import logging
from logging import Logger, handlers

from cfg import LOG_FILE_SIZE

class FLogger(Logger):
    """Custom Logger
    """

    def __init__(self, logname, loglevel=logging.DEBUG, logfilename=None):
        """
        """
        super(FLogger, self).__init__(logname)

        self.logname = logname
        self.loglevel = loglevel
        self.logfilename = logfilename

        self.setLevel(loglevel)

        if self.logfilename:
            file_handler = handlers.RotatingFileHandler(logfilename, 'w', LOG_FILE_SIZE, 10)
            file_handler.setFormatter(logging.Formatter('[%(name)s %(asctime)s %(levelname)s]: %(message)s'))

            self.addHandler(file_handler)
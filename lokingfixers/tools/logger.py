import logging
from logging import Logger, handlers

from lokingfixers.settings import LOG_FILE_SIZE

from lokingfixers.models import LogModel, DBSession

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

class SqlAlchemyHandler(handlers):
    """Custom handlers to allow logging to SqlAlchemy Database
    """

    def emit(self, record):
        """
        """

        trace = None
        exc = record.__dict__['exc_info']

        if exc:
            trace = traceback.format_exc(exc)

        log = LogModel (
            logger=record.__dict__['name'],
            level=record.__dict__['levelname'],
            trace=trace,
            msg=record.__dict__['msg'],
        )

                
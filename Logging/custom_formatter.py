import logging

class CustomFormatter(logging.Formatter):

    def format(self, record):
        record.message = record.getMessage()
        if self.usesTime():
            asctime = self.formatTime(record, self.datefmt)
        return "[{}] [{}] [{}] {}".format(asctime, record.levelname, record.name, record.message)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = CustomFormatter()

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")

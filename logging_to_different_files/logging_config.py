import logging
from logging.handlers import TimedRotatingFileHandler

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

class MyFilter(logging.Filter):

    def filter(self, record: logging.LogRecord) -> bool:
        return is_ascii(record.getMessage())

# def filter_asci(record: logging.LogRecord) -> bool:
#     return is_ascii(record.getMessage())


class SpecialFileHandler(TimedRotatingFileHandler):

    def emit(self, record):
        if not record.levelno == self.level:
            return
        super().emit(record)


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s"
        }
    },
    "filters": {
        "myfilter": {
            "()": MyFilter,
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base",
            'filters': ['myfilter']
        },
        "file_info": {
            "()": SpecialFileHandler,
            "level": "INFO",
            "formatter": "base",
            "filename": "info.log",
            "when": "h",
            "interval": 10,
            "backupCount": 1,
            'filters': ['myfilter']
        },
        "file_debug": {
            "()": SpecialFileHandler,
            "level": "DEBUG",
            "formatter": "base",
            "filename": "debug.log",
            "when": "h",
            "interval": 10,
            "backupCount": 1,
            'filters': ['myfilter']
        },
        "file_exception": {
            "()": SpecialFileHandler,
            "level": "ERROR",
            "formatter": "base",
            "filename": "exception.log",
            "when": "h",
            "interval": 10,
            "backupCount": 1,
            'filters': ['myfilter']
        }
    },
    "loggers": {
        "module_logger": {
            "lvl": "DEBUG",
            "handlers": ["file_info", "file_exception", "file_debug", "console"],
            # "propagate": False,
        }
    },
    # "filters": ["filter_asci"]
    # "root": {} # == "": {}
}

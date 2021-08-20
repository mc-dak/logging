import logging


def is_ascii(s):
    return all(ord(c) < 128 for c in s)

class MyFilter(logging.Filter):

    def filter(self, record: logging.LogRecord) -> bool:
        return is_ascii(record.getMessage())


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
        "sendto": {
            "class": "logging.handlers.HTTPHandler",
            "level": "DEBUG",
            "host": "127.0.0.1:5000",
            "url": "/logs",
            "method": "POST",
        },

    },
    "loggers": {
        "module_logger": {
            "lvl": "DEBUG",
            "handlers": ["sendto", "console"],
            # "propagate": False,
        }
    },

    # "root": {} # == "": {}
}


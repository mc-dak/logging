from typing import Union, Callable
from operator import sub, mul, truediv, add
import logging.config
import logging


OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}

Numeric = Union[int, float]

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def filter_asci(record: logging.LogRecord) -> bool:
    return is_ascii(record.getMessage())

def set_logger(name, level):
    logging.config.fileConfig('logging_conf.ini')
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addFilter(filter_asci)
    return logger


utils_logger = set_logger('module_logger.utils', logging.INFO)


def string_to_operator(value: str) -> Callable[[Numeric, Numeric], Numeric]:
    """
    Convert string to arithmetic function
    :param value: basic arithmetic function
    """
    if not isinstance(value, str):
        utils_logger.error(f'value {value} is not str', exc_info=True)

    if value not in OPERATORS:
        utils_logger.error(f'value {value} not in operators', exc_info=True)

    return OPERATORS[value]

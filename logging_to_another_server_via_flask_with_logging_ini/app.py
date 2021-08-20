import sys
from utils import string_to_operator, set_logger
import logging

def calc(args, logger):
    logger.debug(f'Arguments: {args}')
    num_1 = args[0]
    operator = args[1]
    num_2 = args[2]
    try:
        num_1 = float(num_1)
    except ValueError as e:
        logger.exception(f'Error while converting number 1 {e}')

    try:
        num_2 = float(num_2)
    except ValueError as e:
        logger.exception(f'Error while converting number 1 {e}')

    try:
        operator_func = string_to_operator(operator)
        result = operator_func(num_1, num_2)
        logger.info(f'Result: {result}')
        logger.debug(f'{num_1} {operator} {num_2} = {result}')
    except KeyError as e:
        logger.exception(f'Key error {e}')


if __name__ == '__main__':
    app_logger = set_logger('module_logger.app', logging.DEBUG)
    # calc(sys.argv[1:], app_logger)
    calc('2+7', app_logger)

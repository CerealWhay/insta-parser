
import logging


def set_logger_config():
    file_log = logging.FileHandler('Log.log')
    console_out = logging.StreamHandler()

    logging.basicConfig(
        handlers=(file_log, console_out),
        format='[%(asctime)s | %(levelname)s]: %(message)s',
        datefmt='%d-%b-%y %H:%M:%S',
        level=logging.INFO,
    )


def divider():
    print("------------------------------------------------------------------------------------------------------")
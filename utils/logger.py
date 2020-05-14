import logging


def get_logger():
    logger = logging.getLogger("MyLogger")
    logger.setLevel("DEBUG")
    time_format = "%Y-%m-%d %H:%M:%S"
    log_format = logging.Formatter('%(asctime)s: %(name)s - %(levelname)s - %(message)s', time_format)
    baby_handler = logging.FileHandler("my_log.log")
    baby_handler.setFormatter(log_format)
    logger.addHandler(baby_handler)
    return logger

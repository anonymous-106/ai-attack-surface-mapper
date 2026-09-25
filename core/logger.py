import logging

from config import Config

def setup_logger():
    logging.basicConfig(
        level = getattr(logging, Config.LOG_LEVEL),
        format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    )

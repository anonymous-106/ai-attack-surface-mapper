import logging

from core.logger import setup_logger

def test_info_logging(caplog):
    setup_logger()

    with caplog.at_level(logging.INFO):
        logging.getLogger(__name__).info("Test info message")

    assert "Test info message" in caplog.text


def test_warning_logging(caplog):
    setup_logger()

    with caplog.at_level(logging.WARNING):
        logging.getLogger(__name__).warning("Test warning message")

    assert "Test warning message" in caplog.text


def test_error_logging(caplog):
    setup_logger()

    with caplog.at_level(logging.ERROR):
        logging.getLogger(__name__).error("Test error message")

    assert "Test error message" in caplog.text
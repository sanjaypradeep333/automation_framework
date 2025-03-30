import os
import logging

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)  # Create 'logs' folder if it doesn't exist


def get_logger(test_case_name):
    """Returns a logger that writes logs to a separate file for each test case."""

    log_file = os.path.join(LOG_DIR, f"{test_case_name}.log")

    logger = logging.getLogger(test_case_name)
    logger.setLevel(logging.INFO)

    # Check if handler already exists to prevent duplicate logs
    if not logger.hasHandlers():
        file_handler = logging.FileHandler(log_file, mode='w')  # 'w' to overwrite previous logs
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

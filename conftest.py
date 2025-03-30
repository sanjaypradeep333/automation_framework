# conftest.py (now in C:\Users\sanja\automation_framework\)
import pytest
import logging
import os
from datetime import datetime
from selenium import webdriver

# BASE_DIR is now the project root
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(BASE_DIR, "logs"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "reports"), exist_ok=True)

@pytest.fixture(autouse=True)
def logger(request):
    test_name = request.node.name
    logger = logging.getLogger(test_name)
    logger.setLevel(logging.DEBUG)
    logger.handlers = []
    log_file = os.path.join(BASE_DIR, "logs", f"{test_name}.log")
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    yield logger
    logger.removeHandler(file_handler)
    logger.removeHandler(console_handler)

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def pytest_sessionfinish(session, exitstatus):
    """Generate basic test report"""
    report_file = os.path.join(BASE_DIR, "reports", f"report_{datetime.now().strftime('%Y%m%d_%H%M')}.txt")
    with open(report_file, 'w') as f:
        f.write(f"Tests run: {session.testscollected}\n")
        f.write(f"Passed: {session.testscollected - session.testsfailed}\n")
        f.write(f"Failed: {session.testsfailed}\n")
    print(f"\nReport generated: {report_file}")
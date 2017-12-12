import sys
import os


def pytest_sessionstart(session):
    sys.path.insert(0, os.path.abspath('solutions'))

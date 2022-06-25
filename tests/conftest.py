import logging

import pytest


@pytest.fixture
def mock_logger():
    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    return log

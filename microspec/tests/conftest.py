import pytest
import microspec as usp

@pytest.fixture(scope="session")
def devkit_connection():
    """Open communication with the dev-kit once for all tests.
    """
    return usp.Devkit()

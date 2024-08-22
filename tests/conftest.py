import pytest
import os

def pytest_addoption(parser):
    """
    Add a command-line option to pytest to pass the API key.
    """
    parser.addoption(
        "--apikey", 
        action="store", 
        default=None, 
        help="API Key for IP2Location.io Python tests"
    )

@pytest.fixture(scope="session")
def global_data(request):
    """
    Fixture to provide global test data, including the API key.

    The API key can be passed as a command-line argument or through an
    environment variable. Command-line argument takes precedence.
    """
    # First, try to get the API key from the command-line argument
    api_key = request.config.getoption("--apikey")
    
    # If no API key is provided via command line, fallback to environment variable
    if not api_key:
        api_key = os.getenv("IP2LOCATION_API_KEY")

    # If neither command-line argument nor environment variable is set, raise an error
    if not api_key:
        pytest.fail("API key is not set. Pass it via the --apikey argument or set the IP2LOCATION_API_KEY environment variable.")

    # Return the global data containing the API key
    return {
        "apikey": api_key,
        # Add any other global data as needed
    }

import pytest

@pytest.fixture(scope = 'module')
def global_data():
    return {'apikey': "YOUR_API_KEY"}
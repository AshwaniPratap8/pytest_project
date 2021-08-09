def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="chrome", help="Type in browser type (chrome / IE) ")
    parser.addoption("--username", action="store", default="username", help="username")
    parser.addoption("--password", action="store", default="password", help="password")



@pytest.fixture(scope="module")

def params(request):
    params = {'password': request.config.getoption('--password'), 'username': request.config.getoption('--username')}
    if params['username'] is None or params['password'] is None:
        pytest.skip()
    return params
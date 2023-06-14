import pytest
from faker import Faker

from models import Account, Client

fake_gen = Faker(locale='uk_UA')


@pytest.fixture(scope='session')  # default = function, class, module, session
def new_client():
    client = Client(
        name=fake_gen.name(),
        address=fake_gen.address()
    )
    yield client
    del client

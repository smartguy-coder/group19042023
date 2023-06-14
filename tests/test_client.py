from models import AccountType


def test_client(new_client):
    print(new_client.__dict__)
    assert new_client.accounts == []


def test_client_open_new_deposit_account(new_client):
    print(new_client.__dict__)
    new_client.open_new_account(AccountType.DEPOSIT)
    assert new_client.accounts
    assert len(new_client.accounts) == 1
    assert new_client.accounts[0].account_type is AccountType.DEPOSIT


def test_client_open_add_money_deposit_account(new_client):
    print(new_client.__dict__)
    account = new_client.accounts[0]
    assert account.account_type is AccountType.DEPOSIT
    account.deposit_money(1000)
    assert account.balance == 1000

from models import AccountType


class TestClientCreation:
    def test_client(self, new_client):
        print(new_client.__dict__)
        assert new_client.accounts

    def test_client_open_new_deposit_account(self, new_client):
        print(new_client.__dict__)
        new_client.open_new_account(AccountType.DEPOSIT)
        assert new_client.accounts
        assert new_client.accounts[-1].account_type is AccountType.DEPOSIT


class TestClientAddMoney:
    def test_client_open_add_money_deposit_account(self, new_client):
        print(new_client.__dict__)
        account = new_client.accounts[-1]
        assert account.account_type is AccountType.DEPOSIT
        account.deposit_money(1000)
        assert account.balance == 1000

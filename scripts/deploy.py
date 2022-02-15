from brownie import accounts, config, SimpleStorage


def deploy_simple_storage():
    # Accounts from automatically created accounts of brownie
    account = accounts[0]
    # Custom account created using 'brownie accounts new <account-name>'
    # account = accounts.load("farzam-account")
    # Custom account imported from .env file
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # Improted from brownie config file ---Better practice
    # account = accounts.add(config["wallets"]["from_key"])

    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    # The value in wait() is the required confirmations before the TransactionReceipt is processed
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def main():
    deploy_simple_storage()

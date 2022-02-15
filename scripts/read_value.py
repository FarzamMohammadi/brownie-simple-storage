from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[-1]
    value = simple_storage.retrieve()
    print(value)


def main():
    read_contract()

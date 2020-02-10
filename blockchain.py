# initializing you blockchain list
blockchain = []


def get_last_blockchain_value():
    """
    :return: returns the last value of the current blockchain
    """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """
    :param transaction_amount: current amount for the transaction
    :param last_transaction: last previous transaction chain
    :return: prinst the result at every step
    """
    blockchain.append([last_transaction, transaction_amount])
    print(blockchain)


def get_user_input():
    return float(input("Your transaction amount please: "))


# testing it up

tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(),
          transaction_amount=tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)

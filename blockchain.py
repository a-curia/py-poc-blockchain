# initializing you blockchain list
MINING_REWARD = 10 # given to the person who creates a new block
genesis_block = {
    "previous_hash": '',
    "index": 0,
    "transactions": []
}
blockchain = [genesis_block]
open_transactions = []
owner = "Adrian"
participants = {"Max"}  # set()


def get_last_blockchain_value():
    """
    :return: returns the last value of the current blockchain
    """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def verify_transaction(transaction):

    # print(transaction)
    # print(get_balance(transaction["sender"]))

    sender_balance = get_balance(transaction["sender"])

    return sender_balance >= transaction["amount"]



def add_transaction(sender, recipient, amount=1.0):
    """
    :param sender:
    :param recipient:
    :param amount:
    :return: append a new value as well as the last blockchain value to the blockchain
    """
    transaction = {"sender": sender, "recipient": recipient, "amount": amount}
    if verify_transaction(transaction): # use not to check the tansactions validity
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    # create a new block to our blockchain
    # when called all open transactions are added to a block which is then added to the blockchain

    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    print("hashed_block = "+hashed_block+"\n")

    reward_transaction = {"sender": "MINING","recipient": owner, "amount": MINING_REWARD}
    copied_transacions = open_transactions[:]
    copied_transacions.append(reward_transaction)
    block = {"previous_hash": hashed_block, "index": len(blockchain), "transactions": copied_transacions}
    blockchain.append(block)
    return True  # so set the opne_transactions to []


def get_balance(participant):
    tx_sender = [[tx["amount"] for tx in block['transactions'] if tx["sender"] == participant] for block in blockchain]
    open_tx_sender = [tx["amount"] for tx in open_transactions if tx["sender"] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]

    tx_recipient = [[tx["amount"] for tx in block['transactions'] if tx["recipient"] == participant] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]

    return amount_received - amount_sent

# reward for miners


def get_transaction_value():
    """
    :return: get the user input, transform it from a string to a float and store it
    """
    tx_sender = owner
    tx_recipient = input("Recipient: ")
    tx_amount = float(input("Amount: "))
    return (tx_sender, tx_recipient, tx_amount)


def get_user_choice():
    user_input = input("Your choice: ")
    return user_input


def print_blockchain_emelents():
    # Output the blockchain list to the console
    for block in blockchain:
        print("Outputting Block >> ")
        print(block)


def hash_block(block):
    """
    :param block:
    :return: hash version of that block
    """
    return "-".join([str(block[key]) for key in block])


def verify_chain():
    """
    :return: compare stored hash in a given block with the  precalculated hash of the previous block
    """
    for (index, block) in enumerate(blockchain):
        if index == 0:
            # this is the genesis block so we don't do anything
            continue

        if block["previous_hash"] != hash_block(blockchain[index - 1]):
            return False

    return True

def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])
    # is_valid = True
    # for tx in open_transactions:
    #     if verify_transaction(tx):
    #         is_valid = True
    #     else:
    #         is_valid = False
    # return is_valid



waiting_for_input = True
# Get user input as many times as user wants
while waiting_for_input:
    print("Please chose:")
    print("1. Add a new transaction value")
    print("2. Mine a new block")
    print("3. Output the blockchain blocks")
    print("4. Output participants")
    print("5. Check transaction validity")
    print("h. Manipulate  the chain")
    print("q. Quit")
    user_choice = get_user_choice()

    if user_choice == '1':
        tx_data = get_transaction_value()
        print(tx_data)
        (sender, recipient, amount) = tx_data
        if add_transaction(sender,recipient,amount):
            print("\nTransaction added!")
        else:
            print("\nTransaction FAILED!")
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_emelents()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        if verify_transactions():
            print("All transactions are valid!")
        else:
            print("There are INVALID transactions!")
    elif user_choice == 'h':
        # manipulate the blockchain
        if len(blockchain) >= 1:
            blockchain[0] = {
                "previous_hash": '',
                "index": 0,
                "transactions": [{"sender": "Hack", "recipient": "HackRec", "amount": 100.10}]
            }
    elif user_choice == 'q':
        # break
        waiting_for_input = False
    else:
        print("Invalid input option")

    if not verify_chain():
        print_blockchain_emelents()
        print("Invalid blockchain")
        break
    print(get_balance("Adrian"))
else:
    print("While loop is done. Same for for loop!")

print("Done!")

# initializing you blockchain list
genesis_block = {
    "previous_hash": '',
    "index": 0,
    "transactions": []
}
blockchain = [genesis_block]
open_transactions = []
owner = "Adrian"
participants = {"Max"} # set()


def get_last_blockchain_value():
    """
    :return: returns the last value of the current blockchain
    """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(sender, recipient, amount=1.0):
    """
    :param sender:
    :param recipient:
    :param amount:
    :return: append a new value as well as the last blockchain value to the blockchain
    """
    transaction = {"sender": sender, "recipient": recipient, "amount": amount}
    open_transactions.append(transaction)

    participants.add(sender)
    participants.add(recipient)


def mine_block():
    # create a new block to our blockchain
    # when called all open transactions are added to a block which is then added to the blockchain

    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)

    # for key in last_block:
    #     value = last_block[key]
    #     hashed_block = hashed_block + str(value)

    print(hashed_block)
    print("\n")

    block = {"previous_hash": hashed_block, "index": len(blockchain), "transactions": open_transactions}
    blockchain.append(block)


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

    # block_index = 0
    # is_valid = True
    #
    # # for block_index in range(len(blockchain)):
    # #     if block_index == 0:
    # #         continue
    # #     elif blockchain[block_index][0] == blockchain[block_index - 1]:
    # #         is_valid = True
    # #     else:
    # #         is_valid = False
    #
    # for block in blockchain:
    #     print(block)
    #     print(blockchain[block_index -1])
    #
    #     if block_index == 0:
    #         block_index = block_index + 1
    #         continue
    #
    #     if block[0] == blockchain[block_index - 1]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    #     block_index += 1
    #
    # return  is_valid


# # testing it up
# tx_amount = get_transaction_value()
# add_transaction(tx_amount)


waiting_for_input = True
# Get user input as many times as user wants
while waiting_for_input:
    print("Please chose:")
    print("1. Add a new transaction value")
    print("2. Mine a new block")
    print("3. Output the blockchain blocks")
    print("4. Output participants")
    print("h. Manipulate  the chain")
    print("q. Quit")
    user_choice = get_user_choice()

    if user_choice == '1':
        tx_data = get_transaction_value()
        sender, recipient, amount = tx_data
        add_transaction(sender, recipient, amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_emelents()
    elif user_choice == '4':
        print(participants)
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
        print("Invalid blockchain")
        break
    print("choice register with continue instead of break")
else:
    print("While loop is done. Same for for loop!")

    # get_transaction_value()
    # add_value(tx_amount, get_last_blockchain_value())

    # # Output the blockchain list to the console
    # for block in blockchain:
    #     print("Outputting Block >> ")
    #     print(block)

print("Done!")

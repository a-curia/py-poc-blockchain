# initializing you blockchain list
blockchain = []


def get_last_blockchain_value():
    """
    :return: returns the last value of the current blockchain
    """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    """
    :param transaction_amount: current amount for the transaction
    :param last_transaction: last previous transaction chain
    :return: prinst the result at every step
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """
    :return: get the user input, transform it from a string to a float and store it
    """
    user_input = float(input("Your transaction amount please: "))
    return user_input


def get_user_choice():
    user_input = input("Your choice: ")
    return user_input


def print_blockchain_emelents():
    # Output the blockchain list to the console
    for block in blockchain:
        print("Outputting Block >> ")
        print(block)

def verify_chain():

    block_index = 0
    is_valid = True

    # for block_index in range(len(blockchain)):
    #     if block_index == 0:
    #         continue
    #     elif blockchain[block_index][0] == blockchain[block_index - 1]:
    #         is_valid = True
    #     else:
    #         is_valid = False

    for block in blockchain:
        print(block)
        print(blockchain[block_index -1])

        if block_index == 0:
            block_index = block_index + 1
            continue

        if block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1

    return  is_valid


# # testing it up
# tx_amount = get_transaction_value()
# add_transaction(tx_amount)


waiting_for_input = True
# Get user input as many times as user wants
while waiting_for_input:
    print("Please chose:")
    print("1. Add a new transaction value")
    print("2. Output the blockchain blocks")
    print("h. Manipulate  the chain")
    print("q. Quit")
    user_choice = get_user_choice()

    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_emelents()
    elif user_choice == 'h':
        # manipulate the blockchain
        if len(blockchain) >= 1:
            blockchain[0] = [2]
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

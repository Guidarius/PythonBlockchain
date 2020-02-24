blockchain = []

def get_last_block_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def get_user_choice():
    user_input = input("Enter your choice: ")
    return user_input

def get_transaction():
    user_input = float(input('Your transaction amount please: '))
    return user_input

def add_value(block_amount, last_block=[1]):
    if last_block == None:
        last_block = [1]
    blockchain.append([last_block, block_amount])

def print_each_block():
    for block in blockchain:
        print('Outputting Block')
        print(block)

def verify_chain():
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    return is_valid


                
transaction_amount = get_transaction()
add_value(transaction_amount)

waiting_for_input = True

while waiting_for_input:
    print("1: Add a new transaction value")
    print("2: Output the blockchain blocks")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice =='1':
        transaction_amount = get_transaction()
        add_value(transaction_amount, get_last_block_value())
    elif user_choice == '2':
        print_each_block()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2 ]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Please pick something')
    if not verify_chain():
        print_each_block
        print('Invalid blockchain!')
        break

print('Done!')

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
                
transaction_amount = get_transaction()
add_value(transaction_amount)

while True:
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
        break
    else:
        print('Please pick something')

print('Done!')

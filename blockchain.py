blockchain = [1]

def get_last_block_value():
    return blockchain[-1]

def add_value(block_amount, last_block=[1]):
    blockchain.append([blockchain[-1], block_amount])

transaction_amount = float(input('Your transaction amount please: '))
add_value(transaction_amount)
add_value(4, get_last_block_value())
add_value(12, get_last_block_value())

print(blockchain)

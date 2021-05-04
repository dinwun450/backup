from hashlib import sha256

MAX_NONCE = 10000000000
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Successfully mined bitcoins with value of nonce of: {nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct hash. Attempted mining bitcoin {MAX_NONCE} times")

if __name__ == '__main__':
    transactions = '''
    Mirai->Yuuki->20,
    Buur->Kreek->51
    '''
    difficulty = 4
    import time
    start = time.time()
    print("Mining start!")
    new_hash = mine(6,transactions,'0000x15n8WBS3nCXAMXcgNZrD2WxjBvTzonyKgD', difficulty)
    total_time = str((time.time() - start))
    print(f"Mining end. Total time for mining is: {total_time} seconds")
    print(new_hash)
from Cryptodome.Hash import keccak
import sys


def keccak256(data):
    k = keccak.new(digest_bits=256)
    k.update(data)
    return k.hexdigest()


def find_next_valid_blocks(start_block, count=10):
    valid_blocks = []
    block_number = start_block
    while len(valid_blocks) < count:
        encoded_block_number = block_number.to_bytes(32, byteorder='big')
        hash_value = keccak256(encoded_block_number)
        hash_int = int(hash_value, 16)

        if hash_int % 5 == 0:
            valid_blocks.append(block_number)
            print(block_number)
            print(hash_int)

        block_number += 1

    return valid_blocks



next_valid_blocks = find_next_valid_blocks(243798)
print("The next 10 valid block numbers are:")
for block in next_valid_blocks:
    print(block)

def calculate_storage(filesize):
    block_size = 4096
    full_blocks = filesize // block_size
    partial_block_remainder = block_size % filesize

    if partial_block_remainder > 0:
        return 8192
    return 4096

print(calculate_storage(4097))
def swap_bits(x, i, j):
#Extract the i-th and j-th bits, and see if they differ
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) (1 << j)
        x ^= bit_mask
return x
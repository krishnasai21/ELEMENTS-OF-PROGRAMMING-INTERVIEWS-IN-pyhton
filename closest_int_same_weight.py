def closest_int_same_bit_count(x: int) 
num_unsigned_bits = 64
for i in range(num_unsigned_bits -1):
if (x >> i) & 1 != (x >> (i+1))&1:
x ^ =(1 << i) | (1 <<(i+1))
# Swaps bit-i and bit-(i+1)
return x
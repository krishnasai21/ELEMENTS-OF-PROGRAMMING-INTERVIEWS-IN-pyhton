#using lookup table approach for the solution
#Brute_force algorithm iterate through the 32 least significant bits of the input and swap each with the corresponding most--
#significant bit.
#Illustating the approach with 8-bit integers and 2-bit lookup table keys. The table is rev =((00),(10),(01),(11))
#If the input is(10010011),its reverse is rev(11),rev(00),rev(01),rev(10) i.e, (11001001)

def reverse_bits int:
    mask_size = 16
    bit_mask = 0xFFFF
    return (PRECOMPUTED_REVERSE[x & bit_mask]) << (3* mask_size)| 
    PRECOMPUTED_REVERSE [(x >> mask_size) & bit_mask] << (2* mask_size)|
    PRECOMPUTED_REVERSE[(x >> (2* mask_size)) & bit_mask] << mask_size |
    PRECOMPUTED_REVERSE[(x >>(3* mask_size)) & bit_mask]
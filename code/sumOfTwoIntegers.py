def getSum(a: int, b: int) -> int:
    MASK = 0xFFFFFFFF  # 32-bit mask
    MAX = 0x7FFFFFFF  # max positive 32-bit int

    while b & MASK:
        carry = ((a & b) << 1) & MASK  # mask carry to 32 bits
        a = (a ^ b) & MASK  # mask a to 32 bits
        b = carry

    return a if a <= MAX else ~(a ^ MASK)

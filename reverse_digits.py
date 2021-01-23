def reverse(x: int) -> int:
    result, x-remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining // = 10
    return - result if x < 0 else result
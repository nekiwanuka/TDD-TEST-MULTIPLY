#  This file hold functions of multiply to use


# Define multiply function logic
def multiply(a, b):
    return 1


# Modifying the multiply logic
def multiply(a, b):
    return a * b


# ==================================================

# Modifying the multiply logic to use a different approach


# Another way to do multiply mannually
def multiply(var_a, var_b):
    result = var_a
    for x in range(1, var_b):
        result = result + var_a
    return result


# Another way of doing multiply using this approach
def multiply(a, b):
    ans = 0
    x = 0
    while x < a:
        ans = ans + b
        x = x + 1
    return ans

import random
import string
from  product.models import Products

# def generate_random_code(length):
#     # define the characters to use
#     chars = string.digits + string.ascii_letters

#     # keep generating codes until we find one that hasn't been used before
#     while True:
#         code = ''.join(random.choice(chars) for _ in range(length))
#         if not Products.objects.filter(product_code=code).exists():
#             break

#     return code
import random

def generate_random_code(length):
    # define the characters to use
    chars = "0123456789"

    # keep generating codes until we find one that hasn't been used before
    while True:
        code = ''.join(random.choice(chars) for _ in range(length))
        if not Products.objects.filter(product_code=code).exists():
            break

    return code
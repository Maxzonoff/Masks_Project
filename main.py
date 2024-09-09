from src import masks, utils

path_fake = "data/qwerty"
print(utils.get_operations_info(path_fake))

path_fake = "data/fake.json"
print(utils.get_operations_info(path_fake))

try:
    print(masks.get_mask_card_number("12345"))
except ValueError:
    pass
try:
    print(masks.get_mask_account("1234"))
except ValueError:
    pass

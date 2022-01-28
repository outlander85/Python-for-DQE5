def create_random_str(str_len: int = 20, upper_case: bool = False, lower_case: bool = True, digits: bool = False):
    condition = ''
    if upper_case:
        condition = condition + string.ascii_uppercase
    if lower_case:
        condition = condition + string.ascii_lowercase
    if digits:
        condition = condition + string.digits
    return ''.join(random.choices(condition, k=str_len))
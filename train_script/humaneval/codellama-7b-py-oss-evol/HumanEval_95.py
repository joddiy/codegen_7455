def check_dict_case(d):
    if not d:
        return False
    keys = list(d.keys())
    if all(isinstance(key, str) and key.islower() for key in keys):
        return True
    elif all(isinstance(key, str) and key.isupper() for key in keys):
        return True
    else:
        return False
def get_val(coll, key, default='git'):
    if key in coll:
        return coll[key]
    else:
        return default

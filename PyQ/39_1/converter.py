def list_to_dict(data, key='id'):
    ret = {}
    for row in data:
        ret[row[key]] = row
    return ret

def parse_ltsv(row):
    return dict(d.split(':', 1) for d in row.split('\t'))


def agg_ltsv_file(filepath, count_key):
    agged = {}
    with open(filepath, encoding='utf-8') as f:
        for row in f:
            data = parse_ltsv(row.strip())
            key = data[count_key]
            if key in agged:
                agged[key] += 1
            else:
                agged[key] = 1
    return agged

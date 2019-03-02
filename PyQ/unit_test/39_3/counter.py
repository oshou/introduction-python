def count_file_lines(filepath):
    with open(filepath, encoding="utf-8") as read_f:
        num_lines = len(read_f.readlines())
        return num_lines

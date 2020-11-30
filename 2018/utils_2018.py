def open_file(input_file):
    """Open TXT input and returns data"""
    f = open(input_file, "r")

    data = f.read()

    f.close()

    return data

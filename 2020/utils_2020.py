def open_file(input_file):
    """
    Open input and returns data
    :param input_file: A file with input data
    :return:
    """
    f = open(input_file, "r")

    data = f.read()

    f.close()

    return data

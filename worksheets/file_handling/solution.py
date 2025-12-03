def read_announcement(path):
    """Reads the announcement from the given file path.

    Args:
        path (str): The file path to read the announcement from.

    Returns:
        str: The content of the announcement.
    """
    with open(path, 'r') as file:
        announcement = file.read()
    return announcement
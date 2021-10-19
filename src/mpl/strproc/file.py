def read_file(filename: str) -> str:
    with open(filename, "r") as fh:
        text_content = fh.read()
        fh.close()

    return text_content

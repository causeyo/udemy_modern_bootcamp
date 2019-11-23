import re


def parse_bytes(input):
    byte_regex = re.compile(r'\b[01]{8}\b')
    return byte_regex.findall(input)

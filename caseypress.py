NO_SERIES = "none"
KEY_TEMPLATE = "TEMPLATE"
KEY_TITLE = "TITLE"
KEY_SUBTITLE = "SUBTITLE"
KEY_DATE = "DATE"
KEY_SERIES = "SERIES"
SEPARATOR = ": "


def read_file(file):
    with open(file, 'r') as f:
        return f.read()

def write_file(file, string):
    with open(file, 'w+') as f:
        f.write(string)


def parse_metadata(string):
    string = string.split("\n")
    metadata = dict()
    for line in string:
        line = line.split(SEPARATOR)
        metadata[line[0]] = line[1]
    return metadata


print(parse_metadata(read_file("test.meta")))

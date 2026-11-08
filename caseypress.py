NO_SERIES = "none"
KEY_TEMPLATE = "TEMPLATE"
KEY_TITLE = "TITLE"
KEY_SUBTITLE = "SUBTITLE"
KEY_DATE = "DATE"
KEY_SERIES = "SERIES"
SEPARATOR = ": "


def parse_metadata(string):
    string = string.split("\n")
    metadata = dict()
    for line in string:
        line = line.split(SEPARATOR)
        metadata[line[0]] = line[1]
    return metadata


with open("test.meta", 'r') as f:
    print(parse_metadata(f.read()))

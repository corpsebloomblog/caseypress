# METADATA PARSING
META_KEY_TEMPLATE = "TEMPLATE"
META_KEY_TITLE = "TITLE"
META_KEY_SUBTITLE = "SUBTITLE"
META_KEY_DATE = "DATE"
META_KEY_SERIES = "SERIES"
SEPARATOR = ": "

# PAGE TEMPLATING
TEMPLATE_KEY_TITLE = "[TITLE]"
TEMPLATE_KEY_SUBTITLE = "[SUBTITLE]"
TEMPLATE_KEY_DATE = "[DATE]"
TEMPLATE_KEY_TEXT = "[TEXT]"
TEMPLATE_KEY_POSTS = "[BLOGPOSTS]"

NO_SERIES = "none"


#--

def read_file(file):
    with open(file, 'r') as f:
        return f.read()

def write_file(file, string):
    with open(file, 'w+') as f:
        f.write(string)

#--

def parse_metadata(string):
    string = string.split("\n")
    metadata = dict()
    for line in string:
        line = line.split(SEPARATOR)
        metadata[line[0]] = line[1]
    return metadata


def fill_template(text, keypairs):
    for keypair in keypairs:
        text = text.replace(keypair[0], keypair[1])
    return text




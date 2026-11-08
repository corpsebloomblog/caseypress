CONFIG = "config"

# PAGE METADATA PARSING
META_TEMPLATE = "TEMPLATE"
META_TITLE = "TITLE"
META_SUBTITLE = "SUBTITLE"
META_DATE = "DATE"
META_SERIES = "SERIES"
# INDEX METADATA / CONFIG
META_TARGET_FOLDER = "TARGET"
META_POST_TEMPLATE = "POST TEMPLATE"
META_INDEX_TEMPLATE = "INDEX TEMPLATE"
# INDEX OTHER
SEPARATOR = ": "

# PAGE TEMPLATING
TEMPLATE_TITLE = "[TITLE]"
TEMPLATE_SUBTITLE = "[SUBTITLE]"
TEMPLATE_DATE = "[DATE]"
TEMPLATE_TEXT = "[TEXT]"
# INDEX TEMPLATING
TEMPLATE_KEY_POSTS = "[BLOGPOSTS]"
# TEMPLATING OTHER
NO_SERIES = "none"

#--
# HELPER FUNCTIONS
#--

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


def fill_template(text, keypairs):
    for keypair in keypairs:
        text = text.replace(keypair[0], keypair[1])
    return text

#--
# SCRIPT
#--

config = parse_metadata(read_file(CONFIG))
print(config)
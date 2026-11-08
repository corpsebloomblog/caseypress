import glob


CONFIG = "config"

# PAGE METADATA PARSING
META_TEMPLATE = "TEMPLATE"
META_TITLE = "TITLE"
META_SUBTITLE = "SUBTITLE"
META_DATE = "DATE"
META_SERIES = "SERIES"
# INDEX METADATA / CONFIG
META_TARGET_FOLDER = "TARGET"
META_POSTS_FOLDER = "POSTS"
META_POST_TEMPLATE = "LINK TEMPLATE"
META_INDEX_TEMPLATE = "INDEX TEMPLATE"
# METADATA OTHER
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

POST_EXTENSION = "html"
META_EXTENSION = "meta"

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

posts = glob.glob(f"{config[META_POSTS_FOLDER]}/**/*.{POST_EXTENSION}", recursive = True)
metadata = glob.glob(f"{config[META_POSTS_FOLDER]}/**/*.{META_EXTENSION}", recursive = True)

post_metadata_pairs = []
for post in posts:
	meta = (post[:-len(POST_EXTENSION)]+META_EXTENSION)
	if meta in metadata:
		post_metadata_pairs.append((post, meta))
	else:
		print(f"WARNING: .meta FILE FOR {post} MISSING")

for pair in post_metadata_pairs:
	post = read_file(pair[0])
	meta = parse_metadata(read_file(pair[1]))
	template = read_file(meta[META_TEMPLATE])
	keypairs = [
		[TEMPLATE_TITLE, meta[META_TITLE]], 
		[TEMPLATE_SUBTITLE, meta[META_SUBTITLE]],
		[TEMPLATE_DATE, meta[META_DATE]],
		[TEMPLATE_TEXT, post]
	]
	filled_post = fill_template(template, keypairs)
	
	filename = pair[0].split("/")[-1]

	write_file(f"{config[META_TARGET_FOLDER]}/{filename}", filled_post)
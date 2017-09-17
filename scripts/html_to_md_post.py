import os
import sys
import requests

URL = "http://fuckyeahmarkdown.com/go/"
OUTPUT = os.path.join(os.path.abspath(os.pardir), "_posts")


# Parse command line arguments
page_url = sys.argv[1] # Url of the page you want to convert in markdown
title = sys.argv[2] # Title of the post
name = sys.argv[3] # Name of the output file: format should be YYYY-MM-DD-short-name-of-the-page.md

# Construct query
params = {
    "u": page_url, # url encoded URI to parse
    "read": 1, # whether to run Readability or not, 0 turns off
    "md": 1, # whether to run Markdownify or not, 0 turns off
    "output": "markdown", # type of text to return: json, url (encoded), or markdown
}

# Convert documentation
response = requests.get(URL, params=params)

# Clean content
content = response.text

# Append FrontMatters snippet
front_matters = "---\ntitle: '" + title + "'\n---\n"
content = front_matters + content

# Save md post
with open(os.path.join(OUTPUT, name), 'w') as f:
    f.write(content)

print("++++File successfully saved in the posts_ folder!++++")

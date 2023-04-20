from bs4 import BeautifulSoup

# Conf (Read from arguments eventually)
get_tag = True
get_class = True
get_id = True

# Format HTML

html = ''
with open('test/test.html') as file:
    while line := file.readline():
        line = line.rstrip()
        if len(line) > 0:
            for c in line:
                if c == '<':
                    html += '\n' + c
                elif c == '>':
                    html += c + '\n'
                else:
                    html += c

# Only HTML Tags
tags = [
    l for l in '\n'.join([
        line for line in html.splitlines() if line
    ]).splitlines() if l[0] == '<'
]

# Change closing tags for END tags
for i in range(len(tags)):
    tag = tags[i]
    if len(tag) > 1 and tag[1] == '/':
        tag = tag.replace('/', '')
        tag = tag[:-1] + 'end' + tag[-1:]
        tags[i] = tag

# Parse HTML
parsed_tags = [BeautifulSoup(tag, 'html.parser') for tag in tags]

words = []
for tag in parsed_tags:
    word = ''
    all = tag.find_all()
    if get_tag:
        word += all[0].name
    if get_class:
        for e in all:
            if e.has_attr('class'):
                classes = e['class']
                word += ''.join(sorted(classes))
    if get_id:
        for e in all:
            if e.has_attr('id'):
                word += e['id']

    if len(word) > 0: words.append(word)

# Generate the corpus
corpus = ' '.join(words)
print(corpus)

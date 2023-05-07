from bs4 import BeautifulSoup

def read_html_file(filename):
    html = ''
    with open(filename) as file:
        while line := file.readline():
            # Remove railing spaces
            line = line.rstrip()
            # Ignore empty lines
            if len(line) > 0:
                # One HTML Tag per line
                for c in line:
                    if c == '<':
                        html += '\n' + c
                    elif c == '>':
                        html += c + '\n'
                    else:
                        html += c
    return html

def remove_content(html):
    return [l for l in '\n'.join([line for line in html.splitlines() if line]).splitlines() if l[0] == '<']

def rename_end_tags(tags):
    for i in range(len(tags)):
        tag = tags[i]
        if len(tag) > 1 and tag[1] == '/':
            tag = tag.replace('/', '')
            tag = tag[:-1] + 'end' + tag[-1:]
            tags[i] = tag
    return tags

def parse_tags(tags):
    return [BeautifulSoup(tag, 'html.parser') for tag in tags]

def generate_parsed_tags(html):
    return parse_tags(rename_end_tags(remove_content(html)))

def generate_words(parsed_tags, get_tag, get_class, get_id):
    words = []
    for tag in parsed_tags:
        word = ''
        all = tag.find_all()
        # Add element tag
        if get_tag:
            word += all[0].name
        # Add element Classes
        if get_class:
            for e in all:
                if e.has_attr('class'):
                    classes = e['class']
                    word += ''.join(sorted(classes))
        # Add element ID
        if get_id:
            for e in all:
                if e.has_attr('id'):
                    word += e['id']
        if len(word) > 0: words.append(word)
    return words

def generate_corpus(parsed_tags, get_tag=True, get_class=True, get_id=True):
    return ' '.join(generate_words(parsed_tags, get_tag, get_class, get_id))

import data_extract

def main():
    filename = 'test/test.html'
    # Read html file
    html = data_extract.read_html_file(filename)
    #  Parsed Tags
    parsed_tags = data_extract.generate_parsed_tags(html)
    # Generated corpus
    corpus = data_extract.generate_corpus(parsed_tags)
    print(corpus)

if __name__ == '__main__':
    main()

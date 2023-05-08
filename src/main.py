import data_extract
from gensim import corpora, models, similarities, downloader

def main():
    filename = '/home/fignewton/Documents/Projects/Python/Investigacion_en_CC/test/ecci.html'
    # Read html file
    html = data_extract.read_html_file(filename)
    #  Parsed Tags
    parsed_tags = data_extract.generate_parsed_tags(html)
    # Generated corpus
    corpus = data_extract.generate_corpus(parsed_tags)
    corpus = corpus.replace('-', '').replace('_', '')
    f = open(filename+'.corpus', 'w+')
    f.write(corpus)
    f.close()

if __name__ == '__main__':
    main()

import string

file = r'F:\DataSource\Text_Files\easy.txt'
stop_words_file = r'F:\DataSource\Text_Files\english_stop.txt'
STOP_WORDS = [word.strip().lower() for word in open(stop_words_file)]
# print(stop_words)


def stream_counter(stream, stop_words=STOP_WORDS):
    """Takes an inputstream and stop words as  input and returns word counter"""
    word_count = {}
    if not stop_words:
        stop_words = []
    for line in stream:
        for word in line.split():
            update_word_count(word,word_count,stop_words)
    return word_count

def document_counter(document, stop_words=STOP_WORDS):
    """Takes an inputstream and stop words as  input and returns word counter"""
    word_count = {}
    if not stop_words:
        stop_words = []
    for word in document.split():
        update_word_count(word,word_count,stop_words)
      
    return word_count

def update_word_count(word,word_count,stop_words):
    if word.lower() not in stop_words:
        word = ''.join(c for c in word if c not in string.punctuation)
        word_count[word] = word_count.get(word, 0) + 1
    
def main():
    with open(file, "r") as f:
        word_count = stream_counter(f, STOP_WORDS)
        print(word_count)


if __name__ == '__main__':
    main()

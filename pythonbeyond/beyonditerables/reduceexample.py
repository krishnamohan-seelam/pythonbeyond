from mapnreduce import document_counter, STOP_WORDS
from functools import reduce
from pprint import pprint
documents = [
    'It was the best of times, it was the worst of time',
    'I went to the woods because I wished to live deliberately, to front only the essential facts of life...',
    'Friends, Romans, countrymen, lend me your ears; I come to bury Caesar, not to praise him.',
    'I do not like green eggs and ham. I do not like them, Sam-I-Am.What is the time now?'
]


def merge_counts(d1, d2):
    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word, 0) + count
    return d


def main():
    counts = map(document_counter, documents)
    total_counts = reduce(merge_counts, counts)
    pprint(total_counts)


if __name__ == '__main__':
    main()

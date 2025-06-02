import time
from collections import defaultdict
from functools import wraps
import re
import sys


def calculate_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' took {elapsed_time:.6f} seconds to execute.")
        return result
    return wrapper


@calculate_time
def dict_init(do_print=False) -> dict:
    """Init Lemmatized Word Hashtable For the Count Function

    Key: every individual word
    Value: lemmatized word
    """
    last_lemmatized = ''
    words_for_count = dict()
    with open('2+2+3lem.txt') as f:
        for line in f:
            if not line.startswith(' '):
                last_lemmatized = line.strip()
                words_for_count[last_lemmatized] = last_lemmatized
            else:
                words = line.strip().split(',')
                for w in words:
                    words_for_count[w.strip()] = last_lemmatized

    if do_print:
        print('Initializing...\n' + '=' * 50)
        print('Hashtable Key Size:', len(words_for_count.keys()))
        print('Lemmatized Word Size:', len(set(words_for_count.values())))
        print('='*50)

    return words_for_count


@calculate_time
def count_words_print_topK(words_for_count: dict, text_path: str, top_k=50, do_print=False) -> dict:
    stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself',
                 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself',
                 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that',
                 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
                 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as',
                 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through',
                 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off',
                 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how',
                 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not',
                 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should',
                 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn',
                 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']

    word_count = defaultdict(int)
    with open(text_path) as f:
        # `[^\w\s]` matches any character that is neither an alphanumeric character nor a whitespace character.
        clean_text = re.sub(r'[^\w\s]', '', f.read())
        words = clean_text.lower().split()
        # words = [word for word in words if word not in stopwords]
        # do counting
        for w in words:
            if w in words_for_count:
                lemmatized_word = words_for_count[w]
                word_count[lemmatized_word] += 1

    if do_print:
        print('\nCounting...\n' + '=' * 50)
        print('Word Count:', sum(word_count.values()))
        print('Different Word Count:', len(word_count.keys()))
        print(f'Top {top_k} Freq is: ', dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True)[:top_k]))
        print('=' * 50)

    return word_count


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
        counts = count_words_print_topK(dict_init(do_print=True), input_file_path, top_k=50, do_print=True)
        print('Different Word Count:', len(counts.keys()))


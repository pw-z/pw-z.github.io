from collections import defaultdict
from datetime import datetime
import re
import sys

file_path = sys.argv[1]

last_lemmatized = ''
words_for_count = dict()
with open('2+2+3lem.txt') as f:
    # 34337 lemma in 2+2+3lem.txt
    for line in f:
        if not line.startswith(' '):
            last_lemmatized = line.strip()
            words_for_count[last_lemmatized] = last_lemmatized
        else:
            words = line.strip().split(',')
            for w in words:
                words_for_count[w.strip()] = last_lemmatized

word_count = defaultdict(int)
with open(file_path) as f:
    words = re.sub(r'[^\w\s]', '', f.read()).lower().split()
    for w in words:
        if w in words_for_count:
            word_count[words_for_count[w]] += 1

top_k = 50
print(f'*The vocabulary size up to now, as of {datetime.now().strftime("%Y.%m.%d")}, is **{len(word_count.keys())}**.*')
print(f'Top {top_k} freq. is: ', dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True)[:top_k]))


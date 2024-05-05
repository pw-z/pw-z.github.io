# Vocabulary 20k

## Intro

Here's a simple idea for predicting my vocabulary size. I'm going to put my favorite content here and then count them. A simple script for counting is as follows, the `2+2+3lem` from the [12Dicts Package](http://wordlist.aspell.net/12dicts/) is used for lemmatization.

```python
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
```

The intro stop here.

*The vocabulary size up to now, as of 2024.05.05, is **41**.*


## Tom's Diner

>"Tom's Diner" is a song written in 1982 by American singer and songwriter Suzanne Vega. It was first released as a track on the January 1984 issue of Fast Folk Musical Magazine. When first featured on one of her own studio albums, it appeared as the first track of her 1987 album Solitude Standing. It was later used as the basis for a remix by the British group DNA in 1990, which reached number 1 in Austria, Germany, Greece and Switzerland. The 1991 compilation Tom's Album includes the DNA version as well as cover versions by such artists as After One, Nikki D and Bingo Hand Job (R. E. M. and Billy Bragg). It was also used as the background soundtrack for the opening scene of the 1993 film Untamed Heart.


I am sitting In the morning
At the diner On the corner

I am waiting At the counter
For the man To pour the coffee

And he fills it Only halfway
And before I even argue

He is looking Out the window
At somebody Coming in

"It is always Nice to see you"
Says the man Behind the counter

To the woman Who has come in
She is shaking Her umbrella

And I look The other way
As they are kissing Their hellos

I'm pretending Not to see them
And Instead I pour the milk

I open Up the paper
There's a story Of an actor

Who had died While he was drinking
He was no one I had heard of

And I'm turning To the horoscope
And looking For the funnies

When I'm feeling Someone watching me
And so I raise my head

There's a woman On the outside
Looking inside Does she see me?

No she does not Really see me
Cause she sees Her own reflection

And I'm trying Not to notice
That she's hitching Up her skirt

And while she's Straightening her stockings
Her hair Is getting wet

Oh, this rain It will continue
Through the morning As I'm listening

To the bells Of the cathedral
I am thinking Of your voice

And of the midnight picnic Once upon a time
Before the rain began

I finish up my coffee
It's time to catch the train

*The vocabulary size up to now, as of 2024.05.05, is **183**.*

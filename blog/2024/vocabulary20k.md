# Vocabulary 20k

[TOC]

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


## [Song] Tom's Diner

> "Tom's Diner" is a song written in 1982 by American singer and songwriter Suzanne Vega. It was first released as a track on the January 1984 issue of Fast Folk Musical Magazine. When first featured on one of her own studio albums, it appeared as the first track of her 1987 album Solitude Standing. It was later used as the basis for a remix by the British group DNA in 1990, which reached number 1 in Austria, Germany, Greece and Switzerland. The 1991 compilation Tom's Album includes the DNA version as well as cover versions by such artists as After One, Nikki D and Bingo Hand Job (R. E. M. and Billy Bragg). It was also used as the background soundtrack for the opening scene of the 1993 film Untamed Heart.


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

And I'm turning To the ***horoscope***
And looking For the funnies

When I'm feeling Someone watching me
And so I raise my head

There's a woman On the outside
Looking inside Does she see me?

No she does not Really see me
Cause she sees Her own reflection

And I'm trying Not to notice
That she's hitching Up her skirt

And while she's ***Straightening*** her stockings
Her hair Is getting wet

Oh, this rain It will continue
Through the morning As I'm listening

To the bells Of the ***cathedral***
I am thinking Of your voice

And of the midnight picnic Once upon a time
Before the rain began

I finish up my coffee
It's time to catch the train

*The vocabulary size up to now, as of 2024.05.05, is **183**.*


## [Song] Freedom

(with Elayna Boynton)
(from "Django Unchained" soundtrack)
(Writer(s): Anthony Cornelius Hamilton, Kelvin L. Wooten, Elayna Lajean Boynton)

Ooh

Ooh

Felt like the weight of the world was on my shoulders…
Pressure to break or retreat at every turn;
Facing the fear that the truth I discovered;
No telling how all this will work out;
But I've come too far to go back now.

~I am looking for freedom,
Looking for freedom…
And to find it cost me everything I have.
Well I am looking for freedom,
Looking for freedom...
And to find it may take everything I have!

I know all too well it don’t come easy;
The chains of the world they seem to move in tight;
I try to walk around it,
But stumbling’s so familiar;
Try to get up but the doubt is so strong;
There’s gotta be a wind in my bones...

I'm looking for freedom,
Looking for freedom;
And to find it, cost me everything I have.
Well I’m looking for freedom,
I’m looking for freedom...
And to find it may take everything I have!

Oh
Not giving up has always been hard,
So hard...
But if I do the things the easy way I won’t get far.
Hmm, life hasn't been very kind to me lately,
Well,
But I suppose it’s a push for moving on,
Oh yeah;
In time the sun’s gonna shine on me nicely,
One day yeah,
Something tells me good things are coming and I ain't gonna not believe.

I'm looking for freedom,
Looking for freedom;
And to find it, cost me everything I have.
Well I’m looking for freedom,
I’m looking for freedom...
And to find it may take everything I have! 


## [Song] Love of My Life

> Queen - Track 9 on A Night at the Opera
> 
> This song is written about Mary Austin, with whom Freddie had a long-term relationship. They met in 1970, and Freddie referred to her once as the ‘love of his life’, ***despite*** engaging in relationships with men later on.
> 
> Austin and Mercury lived together for seven years and remained best friends until his death. In Mercury’s later life, she became his personal assistant, and after his death was the inheritor of the bulk of his estate.
> 
> https://genius.com/Queen-love-of-my-life-lyrics

[Intro]

[Verse 1]
Love of my life, you've hurt me
You've broken my heart
And now you leave me
Love of my life, can't you see?

[Chorus]
Bring it back, bring it back
Don't take it away from me
Because you don't know
What it means to me

[Verse 2]
Love of my life, don't leave me
You've taken my love (all my love)
And now desert me
Love of my life, can't you see?

[Chorus]
(Please bring it back, back) Bring it back, bring it back
Don't take it away from me
Because you don't know
What it means to me (means to me)

[Bridge]
You will remember when this is blown over
And everything's all by the way
When I grow older
I will be there at your side
To remind you
How I still love you (I still love you)

[Instrumental break]

[Chorus]
Back, hurry back
Please bring it back home to me
Because you don't know
What it means to me (means to me)

[Outro]
Love of my life
Love of my life
Ooh, ooh

*The vocabulary size up to now, as of 2024.05.12, is **299**.*



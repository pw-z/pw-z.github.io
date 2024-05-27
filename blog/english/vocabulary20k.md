# Vocabulary 20k

[TOC]

## Intro *41

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


## [Song] Tom's Diner *183

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


## [Song] Freedom *250

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
But ***stumbling***’s so familiar;
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

*The vocabulary size up to now, as of 2024.05.12, is **250**.*


## [Song] Love of My Life *299

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


## [Song] When I'm Sixty-Four *376

> "When I'm Sixty-Four" is a song by the English rock band The Beatles, written by Paul McCartney (credited to Lennon–McCartney) and released on their 1967 album Sgt. Pepper's Lonely Hearts Club Band. It was one of the first songs McCartney wrote; he was about 14, probably in April or May 1956. The song was recorded in a key different from the final recording; it was sped up at the request of McCartney to make his voice sound younger. It prominently features a trio of clarinets (two B♭ clarinets and one bass clarinet) throughout. 
>
> https://en.wikipedia.org/wiki/When_I%27m_Sixty-Four


When I get older losing my hair
Many years from now
Will you still be sending me a ***Valentine***
Birthday greetings bottle of wine

If I'd been out till quarter to three
Would you lock the door
Will you still need me, will you still feed me
When I'm sixty-four

You'll be older too
And if you say the word
I could stay with you

I could be handy, ***mending*** a ***fuse***
When your lights have gone
You can knit a sweater by the ***fireside***
Sunday mornings go for a ride
Doing the garden, digging the weeds
Who could ask for more

Will you still need me, will you still feed me
When I'm sixty-four

Every summer we can rent a cottage
In the Isle of Wight, if it's not too ***dear***
We shall scrimp and save
Grandchildren on your knee
Vera, Chuck and Dave

Send me a postcard, drop me a line
Stating point of view
Indicate precisely what you mean to say
Yours sincerely, wasting away

Give me your answer, fill in a form
Mine for ***evermore***
Will you still need me, will you still feed me
When I'm sixty-four

*The vocabulary size up to now, as of 2024.05.14, is **376**.*


## [Song] Parachute *412

> Track 3 on Friendly Fire (Sean Lennon album)
> 
> Friendly Fire is the second studio album by Sean Lennon, released on 2 October 2006 by Capitol Records in the US, and Parlophone in the UK. It reached #152 on the US Billboard 200 chart and #5 in the Top Heatseekers chart. It stayed on the French album chart for 43 weeks and was certified silver. 
> 

Love is like an aeroplane
Jump and then you pray
Lucky ones remain
In the clouds for days
Life is just a stage
Let's put on the best show
And let everyone know

'Cause if I have to die tonight
I'd rather be with you
Cut the ***parachute*** before you die
Baby don't you cry
You had to bring me down
We had some fun before we hit the ground

Love is like a ***hurricane***
You know it's on the way
You think you can be brave
Underneath the waves
Life is just a dream
Which of us is dreaming?
And who will wake up screaming?

'Cause if I have to die tonight
I'd rather be with you
Cut the parachute before you die
Baby don't you cry
You had to bring me down
We had some fun before we hit the ground

'Cause if I have to die tonight
I'd rather be with you
Cut the parachute before you die
Baby don't you cry
You had to bring me down
We had some fun before we hit the ground

'Cause if I have to die tonight
I'd rather be with you
Cut the parachute before you die
Baby don't you cry
You had to bring me down
We had some fun before we hit the ground

*The vocabulary size up to now, as of 2024.05.14, is **412**.*


## [Song] Like I'm Gonna Lose You *451

[Verse 1: Meghan Trainor]
I found myself dreaming in silver and gold
Like a scene from a movie that every broken heart knows
We were walking on moonlight, and you pulled me close
Split second and you disappeared and then I was all alone

[Pre-Chorus: Meghan Trainor]
I woke up in tears, with you by my side
A breath of relief, and I've realised
No, we're not promised tomorrow

[Chorus: Meghan Trainor]
So I'm gonna love you like I'm gonna lose you
I'm gonna hold you like I'm saying goodbye
Wherever we're standin', I won't take you for ***granted***
'Cause we'll never know when, when we'll run out of time
So I'm gonna love you like I'm gonna lose you (Lose you)
I'm gonna love you like I'm gonna lose you

[Verse 2: John Legend, Meghan Trainor]
In the blink of an eye, just a ***whisper*** of smoke
You could lose everything, the truth is you never know
So I'll kiss you longer, babe (Hey), any chance that I get
I'll make the most of the minutes and love with no regret

[Pre-Chorus: John Legend, Meghan Trainor, Both]
Let's take our time to say what we want (Say what we want)
Use what we got before it's all gone (All gone)
'Cause no (No), we're not promised tomorrow

[Chorus: Meghan Trainor, John Legend, Both]
So I'm gonna love you like I'm gonna lose you (Lose you)
I'm gonna hold you (Hey), like I'm saying goodbye
Wherever we're standin' (Yeah), I won't take you for granted
'Cause we'll never know when, when we'll run out of time
So I'm gonna love you (I'm gonna love you), like I'm gonna lose you (Like I'm gonna lose you)
I'm gonna love you (Love you), like I'm gonna lose you (Hey)

[Instrumental Bridge]

[Chorus: Meghan Trainor, John Legend, Both]
I'm gonna love you (Oh) like I'm gonna lose you (Like I'm gonna lose you)
I'm gonna hold you like I'm saying goodbye
Wherever we're standin', I won't take you for granted
'Cause we'll never know when, when we'll run out of time
So I'm gonna love you (I'm gonna love you, baby) like I'm gonna lose you (Like I'm gonna lose you)
I'm gonna love you (Oh) like I'm gonna lose you

*The vocabulary size up to now, as of 2024.05.15, is **451**.*


## [Book] Content by ChatGPT3.5 *574

Give me some wonderful ***excerpts*** from classic English books.

Certainly! Here are some wonderful excerpts from classic English books:

1. **"Pride and Prejudice" by Jane Austen:**
   "It is a truth universally acknowledged, that a single man ***in possession of*** a good fortune, must be ***in want of*** a wife."

2. **"Jane Eyre" by Charlotte Brontë:**
   "I am no bird; and no net ***ensnares*** me: I am a free human being with an independent will."

3. **"Great Expectations" by Charles Dickens:**
   "I loved her against reason, against promise, against peace, against hope, against happiness, against all discouragement that could be."

4. **"Wuthering Heights" by Emily Brontë:**
   "Whatever our souls are made of, his and mine are the same."

5. **"To Kill a Mockingbird" by Harper Lee:**
   "You never really understand a person until you consider things from his point of view... Until you climb inside of his skin and walk around in it."

6. **"1984" by George Orwell:**
   "War is peace. Freedom is ***slavery***. Ignorance is strength."

7. **"The Picture of Dorian Gray" by Oscar Wilde:**
   "The only way to get rid of a temptation is to yield to it. Resist it, and your soul grows sick with ***longing*** for the things it has forbidden to itself."

8. **"Moby-Dick" by Herman Melville:**
   "Call me Ishmael."

9. **"The Catcher in the Rye" by J.D. Salinger:**
   "All ***morons*** hate it when you call them a moron."

10. **"The Great Gatsby" by F. Scott Fitzgerald:**
    "So we beat on, boats against the current, ***borne*** back ***ceaselessly*** into the past."

These excerpts capture the essence and brilliance of some of the ***finest*** works in English literature.


I need more.

Of course! Here are more wonderful excerpts from classic English books:

11. **"Alice's Adventures in Wonderland" by Lewis Carroll:**
    "Why, sometimes I've believed as many as six impossible things before breakfast."

12. **"Frankenstein" by Mary Shelley:**
    "Life, although it may only be an accumulation of anguish, is dear to me, and I will defend it."

13. **"The Hobbit" by J.R.R. Tolkien:**
    "In a hole in the ground there lived a hobbit."

14. **"Sense and Sensibility" by Jane Austen:**
    "Know your own happiness. You want nothing but patience- or give it a more fascinating name, call it hope."

15. **"Dracula" by Bram Stoker:**
    "Listen to them, the children of the night. What music they make!"

16. **"The Adventures of Sherlock Holmes" by Arthur Conan Doyle:**
    "When you have eliminated all which is impossible, then whatever remains, however ***improbable***, must be the truth."

17. **"A Tale of Two Cities" by Charles Dickens:**
    "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness..."

18. **"Emma" by Jane Austen:**
    "Silly things do cease to be silly if they are done by sensible people in an ***impudent*** way."

19. **"The War of the Worlds" by H.G. Wells:**
    "No one would have believed in the last years of the nineteenth century that this world was being watched ***keenly*** and closely by intelligences greater than man's and yet as mortal as his own."

20. **"Robinson Crusoe" by Daniel Defoe:**
    "Thus fear of danger is ten thousand times more terrifying than danger itself when apparent to the eyes."

These timeless excerpts continue to ***resonate*** with readers across generations, showcasing the enduring power of classic English literature.

*The vocabulary size up to now, as of 2024.05.17, is **574**.*


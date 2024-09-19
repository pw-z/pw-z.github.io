# Vocabulary 20k


- [Intro](#intro)
- [Tom's Diner](#toms-diner)
- [Freedom](#freedom)
- [Love of My Life](#love-of-my-life)
- [When I'm Sixty-Four](#when-im-sixty-four)
- [Parachute](#parachute)
- [Like I'm Gonna Lose You](#like-im-gonna-lose-you)
- [BARREN SPRING](#barren-spring)
- [THE BEAST OF BURDEN](#the-beast-of-burden)


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

> "Tom's Diner" is a song written in 1982 by American singer and songwriter Suzanne Vega. It was first released as a track on the January 1984 issue of Fast Folk Musical Magazine. When first featured on one of her own studio albums, it appeared as the first track of her 1987 album Solitude Standing. It was later used as the basis for a remix by the British group DNA in 1990, which reached number 1 in Austria, Germany, Greece and Switzerland. The 1991 compilation Tom's Album includes the DNA version as well as cover versions by such artists as After One, Nikki D and Bingo Hand Job (R. E. M. and Billy Bragg). It was also used as the background soundtrack for the opening scene of the 1993 film Untamed Heart.

```
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
```

*The vocabulary size up to now, as of 2024.05.05, is **183**.*


## Freedom
```

from "Django Unchained" soundtrack

Writer(s): Anthony Cornelius Hamilton, Kelvin L. Wooten, Elayna Lajean Boynton

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
```

*The vocabulary size up to now, as of 2024.05.12, is **250**.*


## Love of My Life

> Queen - Track 9 on A Night at the Opera
> 
> This song is written about Mary Austin, with whom Freddie had a long-term relationship. They met in 1970, and Freddie referred to her once as the ‘love of his life’, ***despite*** engaging in relationships with men later on.
> 
> Austin and Mercury lived together for seven years and remained best friends until his death. In Mercury’s later life, she became his personal assistant, and after his death was the inheritor of the bulk of his estate.
> 
> https://genius.com/Queen-love-of-my-life-lyrics


```
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
```

*The vocabulary size up to now, as of 2024.05.12, is **299**.*


## When I'm Sixty-Four

> "When I'm Sixty-Four" is a song by the English rock band The Beatles, written by Paul McCartney (credited to Lennon–McCartney) and released on their 1967 album Sgt. Pepper's Lonely Hearts Club Band. It was one of the first songs McCartney wrote; he was about 14, probably in April or May 1956. The song was recorded in a key different from the final recording; it was sped up at the request of McCartney to make his voice sound younger. It prominently features a trio of clarinets (two B♭ clarinets and one bass clarinet) throughout. 
>
> https://en.wikipedia.org/wiki/When_I%27m_Sixty-Four


```
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
```

*The vocabulary size up to now, as of 2024.05.14, is **376**.*


## Parachute

> Track 3 on Friendly Fire (Sean Lennon album)
> 
> Friendly Fire is the second studio album by Sean Lennon, released on 2 October 2006 by Capitol Records in the US, and Parlophone in the UK. It reached #152 on the US Billboard 200 chart and #5 in the Top Heatseekers chart. It stayed on the French album chart for 43 weeks and was certified silver. 
> 

```
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
```

*The vocabulary size up to now, as of 2024.05.14, is **412**.*


## Like I'm Gonna Lose You

```
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
```

*The vocabulary size up to now, as of 2024.05.15, is **451**.*


## BARREN SPRING

> Pearl Sydenstricken Buck (1892-1973), American novelist. Her parents were ***missionaries*** in China, so she was brought up in our country. She was married, first, to John Lossing Buck, at one time professor of Rural Economics at the University of Nanking. This early part of her life she included in her ***biography*** of her mother, in her novel The Exile, published in 1935. In the same year she divorced her husband to marry her present husband Richard J. Walsh, owner of the John Day Publishing House. She still writes under the name of Mrs. Pearl S. Buck. The Good Earth, generally considered as her best novel on China, was awarded the Pulitzer Prize in 1931 for being the best novel published for that year in America.

Liu, the farmer, sat at the door of his one-room house. It was a warm evening in late February, and in his thin body he felt the coming of spring. How he knew that the time had now come when ***sap*** should stir in trees and life begin to move in the soil he could not have told himself. In other years it would have been easy enough. He could have pointed to the ***willow*** trees about the house, and shown the swelling buds. But there were no more trees now. He had cut them off during the bitter winter when they were starving for food and he had sold them one by one. Or he might have pointed to the pink-tipped buds of his three peach trees and his six ***apricot*** trees that his father had planted in his day so that now, being at the height of their time, they bore a load of fruit every year. But these trees were also gone. Most of all, in any other year than this he might have pointed to his wheat fields, where he planted wheat in the winter when the land was not needed for rice, and where, when spring was moving into summer, he planted the good rice, for rice was his chief crop. But the land told nothing, this year. There was no wheat on it, for the flood had covered it long after wheat should have been planted, and it lay there ***cracked*** and like ***clay*** but newly dried.

Well, on such a day as this, if he had his buffalo and his ***plow*** as he had always had in other years, he would have gone out and plowed up that cracked soil. He ***ached to*** plow it up and make it look like a field again, yes, even though he had not so much as one seed to put in it. But he had no buffalo. If anyone had told him that he would eat his own water buffalo that plowed the good land for him, and year after year pulled the stone roller over the grain and ***threshed*** it at harvest he would have called that man idiot. Yet it was what he had done. He had eaten his own water buffalo, he and his wife and his parents and his four children, they had all eaten the buffalo together.

But what else could they do on that dark winter's day when the last of their store of grain was gone, when the trees were cut and sold, when he had sold everything, even the little they had saved from the flood, and there was nothing left except the ***rafters*** of the house they had and the ***garments*** they wore? Was there sense in stripping the coat off one's back to feed one's belly? Besides, the beast was starving also, since the water had covered even the grass lands, and they had had to go far afield to gather even enough to cook its bones and flesh. On that day when he had seen the faces of his old parents set as though dead, on that day when he had heard the crying of his children and seen his little daughter dying, such a despair had ***seized*** him as made him like a man without his reason, so that he had gathered together his feeble strength and he had done what he said he never would; he had taken the kitchen knife and gone out and killed his own beast. When he did it, even in his despair, he groaned, for it was as though he killed his own brother. To him it was the last sacrifice.

Yet it was not enough. No, they grew hungry again and there was nothing left to kill. Many of the villagers went south to other places, or they went down the river to beg in the great cities. But he, Liu the farmer, had never begged. Moreover, it seemed to him then that they must all die and the only comfort left was to die on their own land. His neighbor had come and begged him to set forth with them; yes, he had even said he would carry one of the old parents on his back so that Liu might carry the other, seeing that his own old father was already dead. But Liu had refused, and it was well, for in the next two days the old mother was dead, and if she had died on the way he could only have cast her by the roadside lest the others be delayed and more of them die. As it was he could put her safely into their own ground, although he had been so weak that it had taken him three days to dig a hole deep enough for her little old ***withered*** body. And then before he could get her buried he and his wife had ***quarreled*** over the poor few clothes on the old body. His wife was a hard woman and she would have buried the old mother naked, if he had let her, so as to have the clothes for the children. But he made her leave on the inner coat and trousers; although they were only rags after all, and when he saw the cold earth against his old mother's flesh—well, that was sorrow for a man, but it could not be helped. Three more he had buried somehow, his old father and his baby daughter and the little boy who had never been strong.

That was what the winter's famine had taken from them. It would have taken them all except that in the great pools lying everywhere, which were left from the flood, there were shrimps, and these they had eaten raw and were still eating, although they were all sick with a ***dysentery*** that would not get well. In the last day or so his wife had crawled out and dug a few sprouting ***dandelions***. But there was no fuel and so they also were eaten raw. But the bitterness was good after the tasteless flesh of the raw shrimps. Yes, spring was coming.

He sat on heavily, looking out over his land. If he had his buffalo back, if he had his plow that they had burned for fuel, he could plow the land. But when he thought of this as he did many times every day, he felt helpless as a leaf tossed upon the flood. The buffalo was gone; gone also his plow and every implement of wood and bamboo, and what other had he? Sometimes in the winter he had felt grateful that at least the flood had not taken all the house as it had so many other houses. But now suddenly it came to him that he could be grateful for nothing, no, not even that he had his life left him and the life of his wife and the two older children. He felt tears come into his eyes slowly as they had not even come when he buried his old mother and saw the earth fall against her flesh, bared by the rags which had comforted him that day. But now he was comforted by nothing. He muttered to himself.

“I have no seed to plant in the land. There the land lies! I could go and claw it up with my hands if I had the seed and the land would bear. I know my good land. But I have no seed and the land is empty. Yes, even though spring comes, we must still starve!”

And he looked, hopeless, into the barren spring.

*The vocabulary size up to now, as of 2024.06.17, is **659**.*


## THE BEAST OF BURDEN

> “THE BEAST OF BURDEN, from On a Chinese Screen, by William Somerset Maugham, New York, George H. Doran Company, 1922, pp. 77-79.
> William Somerset Maugham （1874-1965）, English dramatist and novelist. In 1921, Mr. Maugham traveled through China. His impressions of places and persons he recorded in his book of delightful sketches On a Chinese Screen, from which book THE BEAST OF BURDEN and THE SONG OF THE RIVER were taken.

At first when you see the coolie on the road, bearing his load, it is as a pleasing object that he strikes the eye. In his blue rags, a blue of all colors from indigo to turquoise and then to the paleness of a milky sky, he fits the landscape. He seems exactly right as he trudges along the narrow causeway between the rice fields or climbs a green hill. His clothing consists of no more than a short coat and a pair of trousers; and if he had a suit which was at the beginning all of a piece, he never thinks when it comes to patching to choose a bit of stuff of the same color. He takes anything that comes handy. From sun and rain he protects his head with a straw hat shaped like an extinguisher with a preposterously wide, flat brim.

You see a string of coolies come along, one after the other, each with a pole on his shoulders from the ends of which hang two great bales, and they make an agreeable pattern. It is amusing to watch their hurrying reflections in the padi water. You watch their faces as they pass you. They are good-natured faces and frank, you would have said, if it had not been drilled into you that the oriental is inscrutable; and when you see them lying down with their loads under a banyan tree by a wayside shrine, smoking and chatting gaily, if you have tried to lift the bales they carry for thirty miles or more a day, it seems natural to feel admiration for their endurance and their spirit. But you will be thought somewhat absurd if you mention your admiration to the old residents of China. You will be told with a tolerant shrug of the shoulders that the coolies are animals and for two thousand years from father to son have carried burdens, so it is no wonder if they do it cheerfully. And indeed you can see for yourself that they begin early, for you will encounter little children with a yoke on their shoulders staggering under the weight of vegetable baskets.

The day wears on and it grows warmer. The coolies take off their coats and walk stripped to the waist. Then sometimes in a man resting for an instant, his load on the ground but the pole still on his shoulders so that he has to rest slightly crouched, you see the poor tired heart beating against the ribs: you see it as plainly as in some cases of heart disease in the out-patients' room of a hospital. It is strangely distressing to watch. Then also you see the coolies' backs. The pressure of the pole for long years, day after day, has made hard red scars, and sometimes even there are open sores, great sores without bandages or dressing that rub against the wood; but the strangest thing of all is that sometimes, as though nature sought to adapt man for these cruel uses to which he is put, an odd malformation seems to have arisen so that there is a sort of hump, like a camel's, against which the pole rests. But beating heart or angry sore, bitter rain or burning sun notwithstanding, they go on eternally, from dawn till dusk, year in year out, from childhood to the extreme of age. You see old men without an ounce of fat on their bodies, their skin loose on their bones, wizened, their little faces wrinkled and apelike, with hair thin and grey; and they totter under their burdens to the edge of the grave in which at last they shall have rest. And still the coolies go, not exactly running, but not walking either, sidling quickly, with their eyes on the ground to choose the spot to place their feet, and on their faces a strained, anxious expression. You can make no longer a pattern of them as they wend their way. Their effort oppresses you. You are filled with a useless compassion.

In China it is man that is the beast of burden.

“To be harassed by the wear and tear of life, and to pass rapidly through it without the possibility of arresting one's course, —is not this pitiful indeed? To labor without ceasing, and then, without living to enjoy the fruit, worn out, to depart, suddenly, one knows not whither, —is not that a just cause for grief?”

So wrote the Chinese mystic.

*The vocabulary size up to now, as of 2024.06.24, is **828**.*
# 乐理基础～搞清楚一些最基本的重要乐理

目标：理解音程、音阶、和弦概念，支撑下一步在吉他指板上实践练习。  
参考书：The Musician's Guide to Theory and Analysis (Third Edition) 

[TOC]

## 术语

* 音名 Pitch: A B C D E F G
* 音高 Pitch-CLass
* 八度 Octave
* 升降音 Flats and Sharps
* 同音异名 Enharmonic Pitches
* 半音级 Half Step (or Semitone) 
* 全音级 Whole Step (or Whole Tone)
* 音程 Interval
* 自然音组 Diatonic Collection
* 变化音组 Chromatic Collection
* 音阶 Scales: Ordered Pitch-Class Collections
* 大调音阶;自然大调 Major Scale
* 半音音阶 Chromatic Scale
* 主音 Tonic

## 音程

### 大小调音阶上的纯音程与大小音程

音程描述音之间的距离单位为度，几个音`pitch`即几度，可依据包含的半音数`half-step`进一步细分音程质量`quality` ～如大二度`major`小二度`minor`
* 大小调音阶中1、4、5、8四个位置的音一致，称纯音程
* 大调音阶位置3、6、7比小调音阶对应多半音，分别称大、小音程
* 大小调位置2皆为大二度

```
F大调：F  G  A ♭B  C  D  E  F
F小调：F  G ♭A ♭B  C ♭D ♭E  F

C大调：C  D  E  F  G  A  B  C
C小调：C  D ♭E  F  G ♭A ♭B  C
```

|  度数  | 半音数量 | 音程名称                   |                                                           举例                                                            |
| :----: | :------: | -------------------------- | :-----------------------------------------------------------------------------------------------------------------------: |
|   1    |    0     | 纯一度 perfect unison (PU) |                                                           `C-C`                                                           |
|   2    |    1     | 小二度 minor seconds (m2)  |                  C大调：C  D  **<a style='color:red'>E  F</a>**  G  A  **<a style='color:red'>B  C</a>**                  |
|   2    |    2     | 大二度 major seconds (M2)  | F大调：**<a style='color:red'>F  G</a>**  A ♭B  C  D  E  F</br>F小调：**<a style='color:red'>F  G</a>** ♭A ♭B  C ♭D ♭E  F |
|   3    |    3     | 小三度 minor thirds (m3)   |               F大调：F  G  A ♭B  C  D  E  F</br>F小调：**<a style='color:red'>F  G ♭A</a>** ♭B  C ♭D ♭E  F                |
|   3    |    4     | 大三度 major thirds (M3)   |               F大调：**<a style='color:red'>F  G  A</a>** ♭B  C  D  E  F</br>F小调：F  G ♭A ♭B  C ♭D ♭E  F                |
|   4    |    5     | 纯四度 perfect fourth (P4) |                                                           `C-F`                                                           |
| 4 or 5 |    6     | 增四度 A4 or 减五度 d5     |
|   5    |    7     | 纯五度 perfect fifth (P5)  |                                                           `C-G`                                                           |
|   6    |  8whwwh  | 小六度 minor sixth (m6)    |               F大调：F  G  A ♭B  C  D  E  F</br>F小调：**<a style='color:red'>F  G ♭A ♭B  C ♭D</a>** ♭E  F                |
|   6    |  9wwhww  | 大六度 major sixth (M6)    |               F大调：**<a style='color:red'>F  G  A ♭B  C  D</a>**  E  F</br>F小调：F  G ♭A ♭B  C ♭D ♭E  F                |
|   7    | 10whwwhw | 小七度 minor seventh (m7)  |               F大调：F  G  A ♭B  C  D  E  F</br>F小调：**<a style='color:red'>F  G ♭A ♭B  C ♭D ♭E</a>**  F                |
|   7    | 11wwhwww | 大七度 major seventh (M7)  |               F大调：**<a style='color:red'>F  G  A ♭B  C  D  E</a>**  F</br>F小调：F  G ♭A ♭B  C ♭D ♭E  F                |
|   8    |    12    | 纯八度 perfect octave (P8) |                                                           `C-C`                                                           |


音程命名规律：**一四五八无大小，二三六七没有纯**
音程反转规律：**大小互换纯不变，两两相加等于九**
>When intervals are inverted,
• perfect intervals remain perfect;
• major intervals invert to minor;
• minor intervals invert to major;
• and the two interval sizes always sum to 9 (e.g., 1 inverts to 8, 3 inverts to 6, 4 inverts to 5).

### 增减音程以及如何推算音程名称

减 <- 纯 -> 增 ：比纯小半音则为减，比纯大半音则为增，小两个半音为倍减，同理推倍增，实践中基本不使用倍增倍减

减 <- 小 <--> 大 -> 增 ：同上如纯大变化，大小音程也可按照半音过度到增减音程

任意取一个音程例如`♭B-E`，横跨了BCDE四个音所以是四度（回忆B大调音阶，从B开始按照全全半全全全半推出：`B、C♯、D♯、E、F♯、G♯、A♯`，B到E是纯四度、5个半音），又因为B降低半音（整体音程跨度增加半音），所以`♭B-E`为增四度。🤔️或者这样想：在♭B大调音阶中，`B♭、C、D、E♭、F、G、A、B♭`，`B♭-E♭`为纯四度，所以`♭B-E`为增四度。

5个半音可以是纯四度也可以是增三度。度数、半音数与音程之间的关系不能简单映射，要综合来看。

拓展链接：
* [音程查找索引 - musicca.com](https://www.musicca.com/zh/interval-finder)
* [半音可以描述所有的音程关系吗？如果能，那度存在的意义是什么？ - 知乎](https://www.zhihu.com/question/39434850/answer/84746214)

### 吉他指板上的音程关系

吉他标准调弦从6弦到1弦空弦音分别是：`E2、A2、D3、G3、B3、E4`，可推算2弦3弦之间是大三度，其余相邻两弦均为纯四度。
```
空吉他指板模版
E--|--|--|--|--|--|--|--|--|--|--|--|--|-|-|-|-|-|-|-|
B--|--|--|--|--|--|--|--|--|--|--|--|--|-|-|-|-|-|-|-|
G--|--|--|--|--|--|--|--|--|--|--|--|--|-|-|-|-|-|-|-|
D--|--|--|--|--|--|--|--|--|--|--|--|--|-|-|-|-|-|-|-|
A--|--|--|--|--|--|--|--|--|--|--|--|--|-|-|-|-|-|-|-|
E--|--|--|--|--|--|--|--|--|--|--|--|--|-|-|-|-|-|-|-|
  0     3     5     7     9       12
```

6弦1弦相差2个八度同品同音，再通过音程关系，可从任意品格出发，找到对应音的所有八度音，记住这些相对位置，便于后续熟练掌握整个指板。
```
从任意位置比如6弦3品出发，找到所有8度音
E-|--|--|-X|--|--|--|--|--|--|--|--|--|--|-|X|-|-|-|-|-|
B-|--|--|--|--|--|--|--|-X|--|--|--|--|--|-|-|-|-|-|-|X|
G-|--|--|--|--|--|--|--|--|--|--|--|-X|--|-|-|-|-|-|-|-|
D-|--|--|--|--|-X|--|--|--|--|--|--|--|--|-|-|-|X|-|-|-|
A-|--|--|--|--|--|--|--|--|--|-X|--|--|--|-|-|-|-|-|-|-|
E-|--|--|-X|--|--|--|--|--|--|--|--|--|--|-|X|-|-|-|-|-|
    1     3     5     7     9       12
```


## 音阶

大调音阶：全全半全全全半 w-w-h-w-w-w-h
小调音阶：全半全全半全全 w-h-w-w-h-w-w

| 大调                  | 音阶                   |
| --------------------- | ---------------------- |
| C大调 `C Major Scale` | `C D E F G A B C`      |
| D大调 `D Major Scale` | `D E F♯ G A B C♯ D`    |
| E大调 `E Major Scale` | `E F♯ G♯ A B C♯ D♯ E`  |
| F大调 `F Major Scale` | `F G A B♭ C D E F`     |
| G大调 `G Major Scale` | `G A B C D E F♯ G`     |
| A大调 `A Major Scale` | `A B C♯ D E F♯ G♯ A`   |
| B大调 `B Major Scale` | `B C♯ D♯ E F♯ G♯ A♯ B` |


## 和弦



# 何为博士（译The illustrated guide to a Ph.D.）
*Posted on 2020.03.29 by [pwz](http://pwz.wiki) under [**CC BY-NC 2.5**](http://creativecommons.org/licenses/by-nc/2.5/)*  
*本文译自 [Matt Might](http://matt.might.net/) - [The illustrated guide to a Ph.D.](http://matt.might.net/articles/phd-school-in-pictures/)*  

* [译文](#%E8%AF%91%E6%96%87)
* [绘图说明](#%E7%BB%98%E5%9B%BE%E8%AF%B4%E6%98%8E)
* [版权声明](#%E7%89%88%E6%9D%83%E5%A3%B0%E6%98%8E)


## 译文

>每年秋天我都要向新一批博士生解释，到底什么是博士，那很难用言语来表述，于是我画了一组图来解释这个事情。  
> *Every fall, I explain to a fresh batch of Ph.D. students what a Ph.D. is.
> It's hard to describe it in words.
> So, I use pictures.
> Read below for the illustrated guide to a Ph.D.*

>请想象一个圆，它包含了人类所有的知识：  
>*Imagine a circle that contains all of human knowledge:*

<br>
<div class="black"></div>
<br>

>完成小学的学业之后，你获得了一点基础知识：  
>*By the time you finish elementary school, you know a little:*

<br>
<div class="black">
    <div class="blue"></div>
</div>
<br>

>完成中学的学业之后，你的基础知识又增加了一些：  
>*By the time you finish high school, you know a bit more:*

<br>
<div class="black">
    <div class="blue"></div>
    <div class="green"></div>
</div>
<br>

>攻读学士学位可以让你获得一些专业知识：  
> *With a bachelor's degree, you gain a specialty:*

<br>
<div class="black">
    <div class="blue"></div>
    <div class="green"></div>
    <div class="pink"></div>
    <div class="pink2"></div>
</div>
<br>

>攻读硕士学位让你的专业知识继续加深：  
> *A master's degree deepens that specialty:*

<br>
<div class="black">
    <div class="blue"></div>
    <div class="green"></div>
    <div class="pink"></div>
    <div class="pink2"></div>
    <div class="pinkred"></div>
</div>
<br>

>继续研读专业论文，你将接近人类知识的边缘：  
> *Reading research papers takes you to the edge of human knowledge:*

<br>
<div class="black">
    <div class="blue"></div>
    <div class="green"></div>
    <div class="pink"></div>
    <div class="pink2"></div>
    <div class="pinkred"></div>
    <div class="red"></div>
</div>
<br>

>等到达了边界，你全神贯注：  
> *Once you're at the boundary, you focus:*

<br>
<div class="black">
    <div class="blue"></div>
    <div class="green"></div>
    <div class="pink"></div>
    <div class="pink2"></div>
    <div class="pinkred"></div>
    <div class="red"></div>
    <div class="block"></div>
</div>
<br>

>年复一年地往外推：  
> *You push at the boundary for a few years:*

<div class="part2">
    <div class="part2-1"></div>
    <div class="part2-2"></div>
</div>
<br>

>终于有一天，边界被你推出去了一块：  
> *Until one day, the boundary gives way:*

<div class="part2">
    <div class="part2-1"></div>
    <div class="part2-2-2"></div>
    <div class="part2-dot"></div>
    <div class="part2-dot2"></div>
</div>
<br>

>如此，被你推出去的这一小块凹槽，便是博士：  
> *And, that dent you've made is called a Ph.D.*

<div class="part2">
    <div class="part2-1"></div>
    <div class="part2-2-2"></div>
    <div class="part2-dot"></div>
    <div class="part2-dot2"></div>
    <div class="phdtag1">◀▬ Ph.D.</div>
</div>
<br>

>当然，此时你眼中的世界或许已是这般模样：  
> *Of course, the world looks different to you now:*

<div class="part2">
    <div class="part2-1-2"></div>
    <div class="phdRed"></div>
</div>
<br>

>那是因为你太过全神贯注了，请别忘了整张图的景色：  
> *So, don't forget the bigger picture:*

<div class="black">
    <div class="dot"></div>
    <div class="dot2"></div>
    <div class="phdtag2">◀▬ Ph.D.</div>
</div>
<br>

>学海无涯，继续探索吧。  
> *Keep pushing.*

<br>


其实这篇短文还没结束，作者后面还有一幅图：

<div class="sonborder">
    <div class="part2-1"></div>
    <div class="son"></div>
    <div class="sontag">◀▬Knowledge to save my son's life</div>
</div>
<br>

这最后一张图，一言难尽。作者的孩子患有罕见病，当时写这篇文章的时候他家孩子的病还没有着落，所以说【Knowledge to save my son's life】属于尚不存在的知识，被画到外面去。

最近貌似已经定位到了大概病因，有些进展了，详情、近况可以翻翻他的博客。

<br>


## 绘图说明

用CSS绘图的基本思路在于，先利用边框的各种属性来形成基本图形（矩形、圆形、椭圆、三角形等），再利用基本图形的定位、旋转等操作进行组合，最终形成想要的（复杂）图形。

本文中图形的比例大致是按照原文中原图真实像素的1/3进行处理的，原文为网页中的jpg图片（存在缩放等），本文是实打实的像素，虽然像素比例只有原文中的1/3，但实际显示效果没有小那么多。另外，颜色是用PS的吸管工具从原图中提取出来的，部分形状的定位参数是通过实时显示试出来的，均略有偏差。

直接看代码吧，以这张图为例：

<div class="black">
    <div class="blue"></div>
    <div class="green"></div>
    <div class="pink"></div>
    <div class="pink2"></div>
    <div class="pinkred"></div>
    <div class="red"></div>
    <div class="block"></div>
</div>
<br>

HTML代码如下：
```html
<div class="black">
    <div class="blue"></div>
    <div class="green"></div>
    <div class="pink"></div>
    <div class="pink2"></div>
    <div class="pinkred"></div>
    <div class="red"></div>
    <div class="block"></div>
</div>
```
每一个div都是一个基本图形，单独进行修饰从而方便组合复用：
```css
.black {/*人类知识的边界*/
    width: 240px;
    height: 240px;           /*定义一个200*200的正方形区域*/
    border-radius: 120px;    /*圆角参数大于长宽一半便成了圆形*/
    /*background: white; */  /*背景白色*/ /*此处不设置背景色，采用默认背景色*/
    margin:0 auto;           /*外边距=0，居中显示*/
    position: relative;      /*采用相对定位*/
    border:1px black solid;  /*边框样式*/
    z-index: 0;              /*设置图层优先级*/
}
.green {/*中学*/
    width: 46px;
    height: 46px;            /*定义一个46*46的正方形区域*/
    border-radius: 100px;    /*圆角参数大于长宽一半便成了圆形*/
    background: #84dc4a;     /*背景色 通过PS吸管工具提取自原文图片*/ 
    position: absolute;      /*采用绝对定位 方便叠加显示*/
    top:50%;
    left:50%;
    transform: translate(-50%, -50%);   /*居中处理*/
    z-index: 6;              /*设置图层优先级*/
}
.blue {/*小学*/
    width: 27px;
    height: 27px;            /*定义一个27*27的正方形区域*/
    border-radius: 100px;    /*圆角参数大于长宽一半便成了圆形*/
    background: #2043dd;     /*背景色 通过PS吸管工具提取自原文图片*/ 
    position: absolute;      /*采用绝对定位 方便叠加显示*/
    top:50%;
    left:50%;
    transform: translate(-50%, -50%);/*居中处理*/
    z-index: 7;
}
.pink {/*本科*/
    width: 64px;
    height: 64px;            /*定义一个64*64的正方形区域*/
    border-radius: 100px;    /*圆角参数大于长宽一半便成了圆形*/
    background: #ff7e7f;     /*背景色 通过PS吸管工具提取自原文图片*/ 
    position: absolute;      /*采用绝对定位 方便叠加显示*/
    top:50%;
    left:50%;
    transform: translate(-50%, -50%); /*居中处理*/
    z-index: 5;
}
.pink2 {/*本科-凸出去的粉色椭圆*/
    width: 25px;
    height: 45px;            /*定义椭圆长宽范围*/
    border-radius: 90% / 100% 100% 0 0;    /*椭圆的圆角参数*/
    background: #ff7e7f;     /*背景色 通过PS吸管工具提取自原文图片*/ 
    position: absolute;      /*采用绝对定位 方便叠加显示*/
    top:50%;
    left:50%;
    transform-origin: center bottom;/*以底部中心为旋转中心*/
    transform: translate(-50%, -100%) rotate(45deg);/*先平移，再顺时针旋转45度*/
    z-index: 4;
}
.pinkred {/*硕士-粉红椭圆*/
    width: 24px;
    height: 80px;            /*定义椭圆长宽范围*/
    border-radius: 90% / 100% 100% 0 0;    /*椭圆的圆角参数*/
    background: #ff4948;     /*背景色 通过PS吸管工具提取自原文图片*/ 
    position: absolute;
    top:50%;
    left:50%;
    transform-origin: center bottom;
    transform: translate(-50%, -100%) rotate(45deg);/*先平移后旋转*/
    z-index: 3;
}
.red {/*博士-红椭圆*/
    width: 25px;
    height: 119px;            /*定义椭圆长宽范围*/
    border-radius: 80% / 100% 100% 0 0;    /*椭圆的圆角参数*/
    background: #fe0000;      /*背景色 通过PS吸管工具提取自原文图片*/ 
    position: absolute;
    top:50%;
    left:50%;
    transform-origin: center bottom;
    transform: translate(-50%, -100%) rotate(45deg);
    z-index: 2;
}
.block {/*点状线方块*/
    width: 40px;
    height: 40px;
    border:1px black dotted;  /*边框样式*/
    position: absolute;
    top: 6.5%;
    left: 77%;
    z-index: 10;
}
```

再看看这张：

<div class="part2">
    <div class="part2-1"></div>
    <div class="part2-2-2"></div>
    <div class="part2-dot"></div>
    <div class="part2-dot2"></div>
    <div class="phdtag1">◀▬ Ph.D.</div>
</div>
<br>

HTML代码（请忽略毫无辨识度的变量名）：
```html
<div class="part2">
    <div class="part2-1"></div>
    <div class="part2-2-2"></div>
    <div class="part2-dot"></div>
    <div class="part2-dot2"></div>
    <div class="phdtag1">◀▬ Ph.D.</div>
</div>
```
CSS代码：
```css
.part2 { /*边界*/
    width: 240px;
    height: 240px;      /*与前文黑色圆形区域大小一致*/
    overflow:hidden;    /*超出部分隐藏*/
    position: relative; /*相对定位*/
    margin: 0 auto;     /*水平居中*/
}
.part2-1{ /*四分之一圆弧*/
    width: 240px;
    height: 240px;
    border-radius: 0 240px 0 0;
    margin:0 auto;           /*外边距=0，居中显示*/
    position: relative;
    border:4px black solid;  /*边框样式*/
    border-left: 0;          /*不显示左侧边框*/
    border-bottom: 0;        /*不显示底部边框*/
    transform: translate(0,30px); /*将圆弧稍微往下移动一点*/
}

.part2-2 { /*圆弧内的红色椭圆*/
    width: 50px;
    height: 232px;            
    border-radius: 80% / 100% 100% 0 0;   /*定义一个半椭圆*/
    background: #ff0000;                  /*背景色*/ 
    position: absolute;
    top:110%;                             /*将椭圆挪下来*/
    transform-origin: center bottom;      /*以底部中间为旋转中心*/
    transform: translate(-50%, -100%) rotate(45deg);/*先平移后旋转*/
}
.part2-2-2 { /*圆弧内的红色椭圆 稍加长版*/
    width: 50px;
    height: 237px;            
    border-radius: 80% / 100% 100% 0 0;  
    background: #ff0000;       
    position: absolute;
    top:110%;
    transform-origin: center bottom;
    transform: translate(-50%, -100%) rotate(45deg);
}
.part2-dot {/*小凹槽*/
    width: 16px;
    height: 12px;            /*此处大小是根据视觉效果调整出来的*/
    border:4px black solid;  /*边框样式*/
    border-radius: 120px 120px 0 0;
    position: absolute;
    top: 36.8%;
    left: 65.2%;
    transform-origin: center bottom;
    transform: rotate(45deg);
}
.part2-dot2 {/*用于遮挡四分之一圆弧上的线，使小凹槽并入圆弧中*/
    width: 10px;
    height: 10px;            /*此处大小是根据视觉效果调整出来的*/
    background: red;
    border-radius: 120px;
    position: absolute;
    top: 38.5%;
    left: 67.2%;             /*此处位置是根据视觉效果调整出来的*/
}
.phdtag1 {/*Ph.D.文字标签*/
    font-size: 12px;
    font-weight: bold;
    position: absolute;
    top: 35%;
    left: 77%;
}
```

大概就是这么多。


## 版权声明

> License: Creative Commons
> 
> I receive numerous requests to reproduce this work, and I'm happy to grant them all, subject to three small conditions:
> 
>     Please attribute the original work to me (Matt Might) and link back to this page in your reproduction:
> 
>      http://matt.might.net/articles/phd-school-in-pictures/
> 
>     as The Illustrated Guide to a Ph.D.
>     When you attribute, please also link my name, Matt Might, to:
> 
>      http://matt.might.net/
> 
>     And, don't forget the "Keep pushing," at the bottom!
> 
> This work is licensed under the [Creative Commons Attribution-NonCommercial 2.5 License](http://creativecommons.org/licenses/by-nc/2.5/).
> 
> That means you can share, copy, modify and reproduce this work as long as you attribute the original work to me and link back to it as outlined above.
> 
> However, you may not sell this work, or use it for commercial purposes. You may only distribute it free of charge. If you're not sure whether your use is a "commercial purpose," please send me an email.
> 
> If possible, please host the images on your own server instead of linking back to mine. 

<style type="text/css">
 /*part1*/
.black { /*人类知识的边界*/
    width: 240px;
    height: 240px;           /*定义一个200*200的正方形区域*/
    border-radius: 120px;    /*圆角参数大于长宽一半便成了圆形*/
    /*background: white; */  /*背景白色*/ /*此处不设置背景色，采用默认背景色*/
    margin:0 auto;           /*外边距=0，居中显示*/
    position: relative;      /*采用相对定位*/
    border:1px black solid;  /*边框样式*/
    z-index: 0;              /*设置图层优先级*/
}
.green {/*中学*/
    width: 46px;
    height: 46px;            /*定义一个46*46的正方形区域*/
    border-radius: 100px;    /*圆角参数大于长宽一半便成了圆形*/
    background: #84dc4a;     /*背景色 通过PS吸管工具提取自原文图片*/ 
    position: absolute;      /*采用绝对定位 方便叠加显示*/
    top:50%;
    left:50%;
    transform: translate(-50%, -50%);   /*居中处理*/
    z-index: 6;              /*设置图层优先级*/
}
.blue {/*小学*/
    width: 27px;
    height: 27px;            /*定义一个27*27的正方形区域*/
    border-radius: 100px;    /*圆角参数大于长宽一半便成了圆形*/
    background: #2043dd;     /*背景色 通过PS吸管工具提取自原文图片*/ 
    position: absolute;      /*采用绝对定位 方便叠加显示*/
    top:50%;
    left:50%;
    transform: translate(-50%, -50%);/*居中处理*/
    z-index: 7;
}
.pink {/*本科*/
    width: 64px;
    height: 64px;            /*定义一个64*64的正方形区域*/
    border-radius: 100px;    /*圆角参数大于长宽一半便成了圆形*/
    background: #ff7e7f;     /*背景色 通过PS吸管工具提取自原文图片*/ 
    position: absolute;      /*采用绝对定位 方便叠加显示*/
    top:50%;
    left:50%;
    transform: translate(-50%, -50%); /*居中处理*/
    z-index: 5;
}
.pink2 {/*本科-凸出去的粉色椭圆*/
    width: 25px;
    height: 45px;            /*定义椭圆长宽范围*/
    border-radius: 90% / 100% 100% 0 0;    /*椭圆的圆角参数*/
    background: #ff7e7f;     /*背景色 通过PS吸管工具提取自原文图片*/ 
    position: absolute;      /*采用绝对定位 方便叠加显示*/
    top:50%;
    left:50%;
    transform-origin: center bottom;/*以底部中心为旋转中心*/
    transform: translate(-50%, -100%) rotate(45deg);/*先平移，再顺时针旋转45度*/
    z-index: 4;
}
.pinkred {/*硕士-粉红椭圆*/
    width: 24px;
    height: 80px;            /*定义椭圆长宽范围*/
    border-radius: 90% / 100% 100% 0 0;    /*椭圆的圆角参数*/
    background: #ff4948;     /*背景色 通过PS吸管工具提取自原文图片*/ 
    position: absolute;
    top:50%;
    left:50%;
    transform-origin: center bottom;
    transform: translate(-50%, -100%) rotate(45deg);/*先平移后旋转*/ 
    z-index: 3;
}
.red {/*博士-红椭圆*/
    width: 25px;
    height: 119px;            /*定义椭圆长宽范围*/
    border-radius: 80% / 100% 100% 0 0;    /*椭圆的圆角参数*/
    background: #fe0000;      /*背景色 通过PS吸管工具提取自原文图片*/ 
    position: absolute;
    top:50%;
    left:50%;
    transform-origin: center bottom;
    transform: translate(-50%, -100%) rotate(45deg);  
    z-index: 2;
}
.block {/*点状线方块*/
    width: 40px;
    height: 40px;
    border:1px black dotted;  /*边框样式*/
    position: absolute;
    top: 6.5%;
    left: 77%;   
    z-index: 10; 
}
.dot {
    width: 8px;
    height: 4px;           /*定义一个200*200的正方形区域*/
    border:1px black solid;  /*边框样式*/
    border-radius: 120px 120px 0 0;
    position: absolute;
    top: 6.5%;
    left: 77%;
    transform: translate(16px,18px) rotate(45deg) translate(0px,-2.5px);
}
.dot2 {/*用于遮挡dot下边界*/
    width: 6px;
    height: 6px;           /*定义一个200*200的正方形区域*/
    background: white;
    /*border:1px black solid;*/  /*边框样式*/
    border-radius: 120px;
    position: absolute;
    z-index: 1;
    top: 13.6%;
    left: 84.1%;
}
/*part2*/
.part2 { /*边界*/
    width: 240px;
    height: 240px;      /*与前文黑色圆形区域大小一致*/
    overflow:hidden;    /*超出部分隐藏*/
    position: relative; /*相对定位*/
    margin: 0 auto;     /*水平居中*/
}
.part2-1{ /*四分之一圆弧*/
    width: 240px;
    height: 240px;
    border-radius: 0 240px 0 0;
    margin:0 auto;           /*外边距=0，居中显示*/
    position: relative;
    border:4px black solid;  /*边框样式*/
    border-left: 0;          /*不显示左侧边框*/
    border-bottom: 0;        /*不显示底部边框*/
    transform: translate(0,30px); /*将圆弧稍微往下移动一点*/
}

.part2-2 { /*圆弧内的红色椭圆*/
    width: 50px;
    height: 232px;            
    border-radius: 80% / 100% 100% 0 0;   /*定义一个半椭圆*/
    background: #ff0000;                  /*背景色*/ 
    position: absolute;
    top:110%;                             /*将椭圆挪下来*/
    transform-origin: center bottom;      /*以底部中间为旋转中心*/
    transform: translate(-50%, -100%) rotate(45deg);/*先平移后旋转*/
}
.part2-2-2 { /*圆弧内的红色椭圆 稍加长版*/
    width: 50px;
    height: 237px;            
    border-radius: 80% / 100% 100% 0 0;  
    background: #ff0000;       
    position: absolute;
    top:110%;
    transform-origin: center bottom;
    transform: translate(-50%, -100%) rotate(45deg);
}
.part2-dot {/*小凹槽*/
    width: 16px;
    height: 12px;            /*此处大小是根据视觉效果调整出来的*/
    border:4px black solid;  /*边框样式*/
    border-radius: 120px 120px 0 0;
    position: absolute;
    top: 36.8%;
    left: 65.2%;
    transform-origin: center bottom;
    transform: rotate(45deg);
}
.part2-dot2 {/*用于遮挡四分之一圆弧上的线，使小凹槽并入圆弧中*/
    width: 10px;
    height: 10px;            /*此处大小是根据视觉效果调整出来的*/
    background: red;
    border-radius: 120px;
    position: absolute;
    top: 38.5%;
    left: 67.2%;             /*此处位置是根据视觉效果调整出来的*/
}

.part2-1-2{ /*四分之一圆弧 超级加粗*/
    width: 240px;
    height: 240px;
    border-radius: 0 240px 0 0;
    margin:0 auto;           /*外边距=0，居中显示*/
    position: absolute;
    border:90px black solid;  /*边框样式*/
    border-left: 0;
    border-bottom: 0;
    transform: translate(0,30px);
    z-index: -9;
}
.phdRed { /*大红色区域*/
    width: 300px;
    height: 300px;         
    border-radius: 240px;    
    background: #ff0000;      
    position: absolute;
    top: 40%;
    left: -50%;
    z-index: -10;
}
.phdtag1 {/*Ph.D.文字标签*/
    font-size: 12px;
    font-weight: bold;
    position: absolute;
    top: 35%;
    left: 77%;
}
.phdtag2 {
    font-size: 5px;
    font-weight: bold;
    position: absolute;
    top: 13%;
    left: 90%;
}

.sonborder {
    width: 400px;
    height: 240px;      /*与前文黑色圆形区域大小一致*/
    overflow:hidden;    /*超出部分隐藏*/
    position: relative; /*相对定位*/
    margin: 0 auto;     /*水平居中*/
}
.son {
    width: 16px;
    height: 16px;            /*此处大小是根据视觉效果调整出来的*/
    border:4px black solid;  /*边框样式*/
    border-radius: 120px;
    position: absolute;
    top: 30%;
    left: 65%;
    transform-origin: center bottom;
    transform: rotate(45deg);
}
.sontag {
    font-size: 10px;
    font-weight: bold;
    position: absolute;
    top: 30%;
    left: 75%; 
}
</style>
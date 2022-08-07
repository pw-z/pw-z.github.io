# JavaWeb技术栈概览与小结


## Maven

<head>
<title>Maven</title>
<style type="text/css">
    body {color: #000000; font-size: 10pt; font-family: "SansSerif", sans-serif; }
li { list-style: none;  margin: 0; }
p { margin: 0; }

span.l { color: red; font-weight: bold; }

a.mapnode:link,
a.mapnode:visited,
a.mapnode:active,
a.mapnode:hover {
    text-decoration: none; color: black;
}
a.mapnode:hover { background: #eeeee0; }
span.foldopened, span.foldclosed  {
    font-size: xx-small;
    border-width: 1;
    font-family: monospace;
    padding: 0em 0.25em 0em 0.25em;
    background: #e0e0e0;
    cursor:pointer;
}
span.foldopened  {
    color: white;
    VISIBILITY: visible;
}
span.foldclosed {
    color: #666666;
    VISIBILITY: hidden;
}
span.foldspecial {
    color: #666666;
    font-size: xx-small;
    border-style: none solid solid none;
    border-color: #CCCCCC;
    border-width: 1;
    font-family: sans-serif;
    padding: 0em 0.1em 0em 0.1em;
    background: #e0e0e0;
    cursor:pointer;
}

</style>
</head>
<body style="background-color:#e9e5dc;">
<script type="text/javascript">
// Here we implement folding. It works fine with MSIE5.5, MSIE6.0 and
// Mozilla 0.9.6.

if (document.layers) {
    //Netscape 4 specific code
    pre = 'document.';
    post = ''; }
if (document.getElementById) {
    //Netscape 6 specific code
    pre = 'document.getElementById("';
    post = '").style'; }
if (document.all) {
    //IE4+ specific code
    pre = 'document.all.';
    post = '.style'; }

function layer_exists(layer) {
    try {
	eval(pre + layer + post);
	return true; }
    catch (error) {
	return false; }}

function show_layer(layer) {
    eval(pre + layer + post).position = 'relative';
    eval(pre + layer + post).visibility = 'visible'; }

function hide_layer(layer) {
    eval(pre + layer + post).visibility = 'hidden';
    eval(pre + layer + post).position = 'absolute'; }

function hide_folder(folder) {
    hide_folding_layer(folder);
    show_layer('show'+folder);

    scrollBy(0,0); // This is a work around to make it work in Browsers (Explorer, Mozilla)
}

function show_folder(folder) {
    // Precondition: all subfolders are folded

    show_layer('hide'+folder);
    hide_layer('show'+folder);
    show_layer('fold'+folder);

    scrollBy(0,0); // This is a work around to make it work in Browsers (Explorer, Mozilla)

    var i;
    for (i=1; layer_exists('fold'+folder+'_'+i); ++i) {
	show_layer('show'+folder+'_'+i); }
}
function show_folder_completely(folder) {
    // Precondition: all subfolders are folded

    show_layer('hide'+folder);
    hide_layer('show'+folder);
    show_layer('fold'+folder);

    scrollBy(0,0); // This is a work around to make it work in Browsers (Explorer, Mozilla)

    var i;
    for (i=1; layer_exists('fold'+folder+'_'+i); ++i) {
	show_folder_completely(folder+'_'+i); }
}



function hide_folding_layer(folder) {
    var i;
    for (i=1; layer_exists('fold'+folder+'_'+i); ++i) {
	hide_folding_layer(folder+'_'+i); }

    hide_layer('hide'+folder);
    hide_layer('show'+folder);
    hide_layer('fold'+folder);

    scrollBy(0,0); // This is a work around to make it work in Browsers (Explorer, Mozilla)
}

function fold_document() {
    var i;
    var folder = '1';
    for (i=1; layer_exists('fold'+folder+'_'+i); ++i) {
	hide_folder(folder+'_'+i); }
}

function unfold_document() {
    var i;
    var folder = '1';
    for (i=1; layer_exists('fold'+folder+'_'+i); ++i) {
	show_folder_completely(folder+'_'+i); }
}

</script>
<SPAN class="foldspecial" onclick="unfold_document()">All +</SPAN>
<SPAN class="foldspecial" onclick="fold_document()">All -</SPAN>
<p>Maven<ul>
<li><span id="show1_1" class="foldclosed" onClick="show_folder('1_1')" style="POSITION: absolute">+</span> <span id="hide1_1" class="foldopened" onClick="hide_folder('1_1')">-</span>
简介<ul id="fold1_1" style="POSITION: relative; VISIBILITY: visible;">
<li><span id="show1_1_1" class="foldclosed" onClick="show_folder('1_1_1')" style="POSITION: absolute">+</span> <span id="hide1_1_1" class="foldopened" onClick="hide_folder('1_1_1')">-</span>
maven作用<ul id="fold1_1_1" style="POSITION: relative; VISIBILITY: visible;">
<li><span id="show1_1_1_1" class="foldclosed" onClick="show_folder('1_1_1_1')" style="POSITION: absolute">+</span> <span id="hide1_1_1_1" class="foldopened" onClick="hide_folder('1_1_1_1')">-</span>
标准化的项目结构<ul id="fold1_1_1_1" style="POSITION: relative; VISIBILITY: visible;">
<li>src/<ul>
<li>main/<ul>
<li>java/</li><li>resources/</li><li><span style="color: #999999; font-size: 8pt; font-style: italic; ">webapp/</span></li></ul>
</li><li>test/<ul>
<li>java/</li></ul>
</li></ul>
</li><li>pom.xml</li></ul>
</li><li><span id="show1_1_1_2" class="foldclosed" onClick="show_folder('1_1_1_2')" style="POSITION: absolute">+</span> <span id="hide1_1_1_2" class="foldopened" onClick="hide_folder('1_1_1_2')">-</span>
标准化的构建流程<ul id="fold1_1_1_2" style="POSITION: relative; VISIBILITY: visible;">
<li>编译</li><li>测试</li><li>打包</li><li>发布</li></ul>
</li><li>方便的依赖管理</li></ul>
</li><li><span id="show1_1_2" class="foldclosed" onClick="show_folder('1_1_2')" style="POSITION: absolute">+</span> <span id="hide1_1_2" class="foldopened" onClick="hide_folder('1_1_2')">-</span>
maven模型<ul id="fold1_1_2" style="POSITION: relative; VISIBILITY: visible;">
<li>项目对象模型（POM）（Project Object Model）</li><li>依赖管理模型（Denpendency）</li><li>插件（Plugin）</li></ul>
</li><li><span id="show1_1_3" class="foldclosed" onClick="show_folder('1_1_3')" style="POSITION: absolute">+</span> <span id="hide1_1_3" class="foldopened" onClick="hide_folder('1_1_3')">-</span>
maven仓库<ul id="fold1_1_3" style="POSITION: relative; VISIBILITY: visible;">
<li>本地仓库（Local Repository）</li><li>中央仓库（Central Repository）</li><li>远程仓库（私服）（Remote Repository）</li></ul>
</li></ul>
</li><li><span id="show1_2" class="foldclosed" onClick="show_folder('1_2')" style="POSITION: absolute">+</span> <span id="hide1_2" class="foldopened" onClick="hide_folder('1_2')">-</span>
安装配置、基本命令<ul id="fold1_2" style="POSITION: relative; VISIBILITY: visible;">
<li><span id="show1_2_1" class="foldclosed" onClick="show_folder('1_2_1')" style="POSITION: absolute">+</span> <span id="hide1_2_1" class="foldopened" onClick="hide_folder('1_2_1')">-</span>
安装配置<ul id="fold1_2_1" style="POSITION: relative; VISIBILITY: visible;">
<li>1、下载解压安装</li><li>2、配置系统环境变量</li><li>3、配置本地&远程仓库<ul>
<li><mirror></li></ul>
</li></ul>
</li><li><span id="show1_2_2" class="foldclosed" onClick="show_folder('1_2_2')" style="POSITION: absolute">+</span> <span id="hide1_2_2" class="foldopened" onClick="hide_folder('1_2_2')">-</span>
基本命令<ul id="fold1_2_2" style="POSITION: relative; VISIBILITY: visible;">
<li>mvn compile<ul>
<li>产出target目录</li></ul>
</li><li>mvn clean<ul>
<li>清除target目录</li></ul>
</li><li>mvn package<ul>
<li>打jar包</li></ul>
</li><li>mvn test<ul>
<li>自动执行Test目录下的测试方法</li></ul>
</li><li>mvn install<ul>
<li>将打包好的jar包注册到本地maven仓库</li></ul>
</li></ul>
</li></ul>
</li><li><span id="show1_3" class="foldclosed" onClick="show_folder('1_3')" style="POSITION: absolute">+</span> <span id="hide1_3" class="foldopened" onClick="hide_folder('1_3')">-</span>
生命周期<ul id="fold1_3" style="POSITION: relative; VISIBILITY: visible;">
<li><span style="color: #999999; font-size: 8pt; font-style: italic; ">maven生命周期分为3套，执行后面命令会自动触发前面命令</span></li><li>clean：清理
    <p>
      pre-clean&nbsp;&nbsp;--&gt;&nbsp;&nbsp;clean&nbsp;&nbsp;--&gt;&nbsp;&nbsp;post-clean
    </p>
  </li><li>default：核心操作（编译、测试、打包、安装）
    <p>
      complie --&gt;&nbsp;&nbsp;test&nbsp;&nbsp;--&gt;&nbsp;&nbsp;package&nbsp;&nbsp;--&gt;&nbsp;&nbsp;install
    </p>
  </li><li>site：产生报告，发布站点等
    <p>
      pre-site&nbsp;&nbsp;--&gt;&nbsp;&nbsp;site&nbsp;&nbsp;--&gt;&nbsp;&nbsp;post-site
    </p>
  </li></ul>
</li><li><span id="show1_4" class="foldclosed" onClick="show_folder('1_4')" style="POSITION: absolute">+</span> <span id="hide1_4" class="foldopened" onClick="hide_folder('1_4')">-</span>
坐标<ul id="fold1_4" style="POSITION: relative; VISIBILITY: visible;">
<li><span style="color: #999999; font-size: 8pt; font-style: italic; ">maven坐标是【资源的唯一标识】，用来定义项目或引入依赖</span></li><li>groupid：项目隶属组织名称，通常是域名反写</li><li>artifactid：项目名称（通常是模块名称）</li><li>version：版本号</li><li><span id="show1_4_1" class="foldclosed" onClick="show_folder('1_4_1')" style="POSITION: absolute">+</span> <span id="hide1_4_1" class="foldopened" onClick="hide_folder('1_4_1')">-</span>
scope：jar包作用范围<ul id="fold1_4_1" style="POSITION: relative; VISIBILITY: visible;">
<li>complie：编译环境有效（默认就用这个就行）</li><li>test</li><li>provided</li><li>runtime</li><li>system</li><li>import</li></ul>
</li></ul>
</li><li><span id="show1_5" class="foldclosed" onClick="show_folder('1_5')" style="POSITION: absolute">+</span> <span id="hide1_5" class="foldopened" onClick="hide_folder('1_5')">-</span>
依赖管理<ul id="fold1_5" style="POSITION: relative; VISIBILITY: visible;">
<li><dependency></li></ul>
</li></ul>
<SCRIPT type="text/javascript">
fold_document();
</SCRIPT>


# 使用Perl正则替换优化tail-f命令查看日志的显示效果
Tail -f logs with syntax highlighting through perl regex replace  
*Posted on 2021.05.10 by [Pengwei Zhang](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*  

日常运维频繁使用`tail -f`看日志，可以通过能控制显示效果的转义序列及Perl-pe模式下的正则替换实现tail命令的自定义语法高亮支持。

## 相关知识



## 脚本

日志格式如下：

```log
[2021-03-21 16:19:01][QOfY4eI3][SQL][0:3]select * from IRS_CHECK where f_id = 'GET_MSGID'
[2021-03-21 16:19:01][ydyHfeuy][REQ]{"code":"67a5298c8cf6a78e91f9c7cc461a5695d467b0f7da956e84c1013cde4d3b427da58430ccad744628","u":"FRONT","f":"GET_MSGID","l":"34C3B3B3D3B343B324C3C334D3344616165615ea6125913f266c157bf69549b6f991b0"}
[2021-03-21 16:19:01][ydyHfeuy][SQL][0:3]SELECT FUNCTION_NO F, OUTPUTPARAM, INPUTPARAM, SERVICES_INFO,FUNC_TYPE,DATASOURCE,SCRIPT_INFO from P_FUNCTION_NO  WHERE FUNCTION_NO = 'GET_MSGID'
[2021-03-21 16:19:01][ydyHfeuy][SQL][0:1]SELECT FUNCTION_NO F, OUTPUTPARAM, INPUTPARAM, SERVICES_INFO,FUNC_TYPE,DATASOURCE,SCRIPT_INFO from P_FUNCTION_NO  WHERE FUNCTION_NO = 'FRAM_SYSTEM'
[2021-03-21 16:19:02][ydyHfeuy][SQL][10:3]SELECT (SERIAL_MID + 1) AS SERIAL_MID,SERIAL_PRE, SERIAL_SUF, TO_FIELD,SERIAL_MID_LENGTH FROM P_SERIAL_NO_STRATEGY WHERE DEAL_NAME='MSG_ID' AND UNIT_CODE='kingstar' FOR UPDATE UPDATE P_SERIAL_NO_STRATEGY SET SERIAL_MID=?, UPDATE_TIME=? WHERE DEAL_NAME='MSG_ID' AND UNIT_CODE='kingstar'
[2021-03-21 16:19:02][ydyHfeuy][RES][20]{"CODE":"200","code":"200","header":{"code":"0","errMessage":""},"tradeDate":{"tradeDate":"00000208"},"SYS_REAL_DATETIME":"2021-03-21 16:19:01"}
[2021-03-21 16:19:02][v3WRMNqB][SQL][0:3]select * from IRS_CHECK where f_id = 'RT02'
[2021-03-21 16:19:02][JNpPjltQ][REQ]{"code":"a568f91844bde8b434d5daab5e02e55444cb0655a15c5e7c6de30d915ef14846bed3a45893272960","ENTITYID":"1234001","RECORDNUM":"1","f":"RT02","STATUS1":"0","MSGTYPE":null,"l":"34C3B3B3D3B343B324C3C334D3344616165615ea6125913f266c157bf69549b6f991b0","MEMID":null,"DEALCODE":"IRS201404160000001","CONTRACTCODE":"CF201404160000033","u":"FRONT","STATUS3":"4","STATUS2":"3","DEALTYPE":"N","SENDTIME":null,"ID":"1","MSGID":null}
[2021-03-21 16:19:02][JNpPjltQ][SQL][0:1]SELECT FUNCTION_NO F, OUTPUTPARAM, INPUTPARAM, SERVICES_INFO,FUNC_TYPE,DATASOURCE,SCRIPT_INFO from P_FUNCTION_NO  WHERE FUNCTION_NO = 'RT02'
[2021-03-21 16:19:02][JNpPjltQ][SQL][0:1]SELECT FUNCTION_NO F, OUTPUTPARAM, INPUTPARAM, SERVICES_INFO,FUNC_TYPE,DATASOURCE,SCRIPT_INFO from P_FUNCTION_NO  WHERE FUNCTION_NO = 'FRAM_SYSTEM'
[2021-03-21 16:19:02][JNpPjltQ][SQL][0:1]SELECT PARAMVALUE FROM P_PARAMS where PARAMNAME = 'SYS_SYSDATE_FLAG'
[2021-03-21 16:19:02][JNpPjltQ][SQL][0:3]SELECT * FROM ( SELECT A.*, ROWNUM RN FROM ( select   COLUMN_NAME AS COLUMN_NAME   from   user_cons_columns  where   constraint_name   =   (select   constraint_name   from   user_constraints where   table_name ='BASE_TRADE_INFO'  and   constraint_type   ='P') ) A WHERE ROWNUM <= 10) WHERE RN > 0
[2021-03-21 16:19:02][JNpPjltQ][SQL][29]UPDATE BASE_TRADE_INFO SET TRADE_STATUS='4',MODIFY_TIME=TO_DATE('2021-03-21 16:19:02','YYYY-MM-DD HH24:MI:SS') WHERE  CUST_TRADECODE='1234001' AND DEAL_CODE='IRS201404160000001' effect:0
[2021-03-21 16:20:01][xjR155pI][SQL][0:1]SELECT FUNCTION_NO F, OUTPUTPARAM, INPUTPARAM, SERVICES_INFO,FUNC_TYPE,DATASOURCE,SCRIPT_INFO from P_FUNCTION_NO  WHERE FUNCTION_NO = 'RT02'
[2021-03-21 16:20:01][xjR155pI][SQL][0:2]SELECT FUNCTION_NO F, OUTPUTPARAM, INPUTPARAM, SERVICES_INFO,FUNC_TYPE,DATASOURCE,SCRIPT_INFO from P_FUNCTION_NO  WHERE FUNCTION_NO = 'FRAM_SYSTEM'
[2021-03-21 16:20:01][xjR155pI][SQL][1:3]SELECT PARAMVALUE FROM P_PARAMS where PARAMNAME = 'SYS_SYSDATE_FLAG'
[2021-03-21 16:20:02][xjR155pI][SQL][0:6]SELECT * FROM ( SELECT A.*, ROWNUM RN FROM ( select   COLUMN_NAME AS COLUMN_NAME   from   user_cons_columns  where   constraint_name   =   (select   constraint_name   from   user_constraints where   table_name ='BASE_TRADE_INFO'  and   constraint_type   ='P') ) A WHERE ROWNUM <= 10) WHERE RN > 0
[2021-03-21 16:20:02][xjR155pI][SQL][28]UPDATE BASE_TRADE_INFO SET TRADE_STATUS='4',MODIFY_TIME=TO_DATE('2021-03-21 16:20:01','YYYY-MM-DD HH24:MI:SS') WHERE  CUST_TRADECODE='1234001' AND DEAL_CODE='IRS201404160000001' effect:0
[2021-03-21 16:20:02][xjR155pI][Debug]service return null:SCHInterfaceService
[2021-03-21 16:20:02][xjR155pI][RES][45]{"CODE":"200","code":"200","SYS_REAL_DATETIME":"2021-03-21 16:20:01"}
[2021-03-21 16:21:01][mtSFjbvS][SQL][0:3]select * from IRS_CHECK where f_id = 'GET_MSGID'
[2021-03-21 16:21:01][wEfsfuoO][REQ]{"code":"3ecb49142fcbc530a555ba53891884e9e896b08b52a38228d3b4ef8de4a54364bcfdf47876371970","u":"FRONT","f":"GET_MSGID","l":"34C3B3B3D3B343B324C3C334D3344616165615ea6125913f266c157bf69549b6f991b0"}
```


## 补充笔记

### tail -f

*tail命令属于[GNU core utilities](https://www.gnu.org/software/coreutils/)，官网可以下载到源码*

//TODO 源码阅读

`-f`参数开启follow模式，文件有改动时候追加文件尾到标准输出流中。


### perl -pe

通过`perl -h`检索各参数的意义，参数组合`-pe`可以实现在命令行中执行perl代码，并且自动输入输出。

```
Usage: perl [switches] [--] [programfile] [arguments]
  -0[octal]         specify record separator (\0, if no argument)
  -a                autosplit mode with -n or -p (splits $_ into @F)
  -C[number/list]   enables the listed Unicode features
  -c                check syntax only (runs BEGIN and CHECK blocks)
  -d[:debugger]     run program under debugger
  -D[number/list]   set debugging flags (argument is a bit mask or alphabets)
  -e program        one line of program (several -e's allowed, omit programfile)
  -E program        like -e, but enables all optional features
  -f                don't do $sitelib/sitecustomize.pl at startup
  -F/pattern/       split() pattern for -a switch (//'s are optional)
  -i[extension]     edit <> files in place (makes backup if extension supplied)
  -Idirectory       specify @INC/#include directory (several -I's allowed)
  -l[octal]         enable line ending processing, specifies line terminator
  -[mM][-]module    execute "use/no module..." before executing program
  -n                assume "while (<>) { ... }" loop around program
  -p                assume loop like -n but print line also, like sed
  -s                enable rudimentary parsing for switches after programfile
  -S                look for programfile using PATH environment variable
  -t                enable tainting warnings
  -T                enable tainting checks
  -u                dump core after parsing program
  -U                allow unsafe operations
  -v                print version, patchlevel and license
  -V[:variable]     print configuration summary (or a single Config.pm variable)
  -w                enable many useful warnings
  -W                enable all warnings
  -x[directory]     ignore text before #!perl line (optionally cd to directory)
  -X                disable all warnings
  
Run 'perldoc perl' for more help with Perl.
```

`perl -e`命令行模式直接执行之后的代码，类比`python -c`：

```vb
┌──(fine㉿10)-[/bin]
└─$ perl -e 'print "hello"'
hello

┌──(fine㉿10)-[/bin]
└─$ python -c 'print "hello"'
hello
```

### perl 正则表达式



### perl 特殊变量

perl语言中定义了很多特殊变量，与正则表达式相关的如下：

|name|full name|describe|
|:---:|:--:|:---|
|$n  |-  |包含上次模式匹配的第n个子串（括号中的子表达式）|
|$&  |$MATCH  |前一次成功模式匹配的字符串|
|$`  |$PREMATCH  |前次匹配成功的子串之前的内容|
|$'  |$POSTMATCH  |前次匹配成功的子串之后的内容|
|$+  |$LAST_PAREN_MATCH  |与上个正则表达式搜索格式匹配的最后一个括号|

例子：
```perl
#!/bin/perl

$str="abcd1234qwer";
$str=~ m/1234/;
print "\$& = $&\n";
print "\$` = $`\n";
print "\$' = $'\n";
print "\$1 = $1\n";
print "---\n";

$str=~ m/(1234)(qwer)/;
print "\$1 = $1\n";
print "\$2 = $2\n";
print "\$+ = $+\n";

# ┌──(fine㉿10)-[~/Desktop]
# └─$ ./perl.pl 
# $& = 1234
# $` = abcd
# $' = qwer
# $1 = 
# ---
# $1 = 1234
# $2 = qwer
# $+ = qwer
```

### stdin、stdout与管道

标准输入输出流一般情况下直接连接到键盘与屏幕，管道的作用在于将上一个程序的标准输出流**重定向**到下一个程序的标准输入中去。






## 代码及效果概览



```shell

tail -f xxx.log | perl -pe 's/(ERROR)/\e[1;31m$1\e[0m/g'

时间：[0-9]*-[0-9]*-[0-9]* [0-9]*:[0-9]*:[0-9]*
批次：\[[a-zA-Z0-9]{8}]


tail -f xxx.log | perl -pe 's/([0-9]*-[0-9]*-[0-9]* [0-9]*:[0-9]*:[0-9]*)/\e[1;31m$1\e[0m/g'
```
#!/bin/perl

$PID_PATTERN = "(\[[a-zA-Z0-9]{8}])";
$TIME_PATTERN = "([0-9]*-[0-9]*-[0-9]* [0-9]*:[0-9]*:[0-9]*)";
$ERROR_KEYWORDS = "(ErrorMsgException|NullPointerException|FileNotFoundException|JSONException|NumberFormatException|Error|Exception|失败)";
$MOCK_KEYWORDS = "()";  # 挡板接口

$PID = "";
$OLD_PID = "";

# 30  黑色
# 31  红色
# 32  绿色
# 33  黄色
# 34  蓝色
# 35  紫色
# 36  青色
# 37  白色

$PID_COLOR = 36;
$TIME_COLOR = 32;
$SQL_COLOR = 32;
$REQ_COLOR = 35;
$RES_COLOR = 35;
$ERROR_COLOR = 31;
$MOCK_COLOR = 33;

while(<STDIN>){
  # 日期着色
  $_ =~ s/$TIME_PATTERN/\e[1;32m$1\e[0m/g;  # g=全局匹配
  # 线程号着色（同线程同颜色）
  if($_ =~ m/(\[[a-zA-Z0-9]{8}])/){
    $PID = substr($&,1,8);
    # print "Got PID : $PID\n";
    # print "Old PID : $OLD_PID\n";
    if($PID eq $OLD_PID){
      # print "++++++++++++++++++++++++++++++\n";
      # $PID_COLOR = ($PID_COLOR == 35) ? 35 : 36;  # 
      $_ =~ s/\[$PID]/[\e[1;\Q$PID_COLOR\Em$PID\e[0m]/g;
    }else{
      # print "------------------------------\n";
      $OLD_PID = $PID;
      $PID_COLOR = ($PID_COLOR == 35) ? 36 : 35;
      $_ =~ s/\[$PID]/[\e[1;\Q$PID_COLOR\Em$PID\e[0m]/g;
    }
  }
  # REQ着色（但不污染详细日志）
  $_ =~ s/(\[REQ])/[\e[1;\Q$REQ_COLOR\EmREQ\e[0m]/g;
  # RES着色（但不污染详细日志）
  $_ =~ s/(\[RES])/[\e[1;\Q$RES_COLOR\EmRES\e[0m]/g;
  # SQL着色（但不污染详细日志）
  $_ =~ s/(\[SQL])/[\e[1;\Q$SQL_COLOR\EmSQL\e[0m]/g;

  # 报错关键字着色
  $_ =~ s/($ERROR_KEYWORDS)/\e[1;\Q$ERROR_COLOR\Em$1\e[0m/ig;  # i=忽略大小写
  # 挡板接口着色
  # $_ =~ s/$MOCK_KEYWORDS/\e[1;\Q$MOCK_COLOR\Em$1\e[0m/ig;

  print "$_";
}

#-------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------
# $PID_PATTERN = "(\[[a-zA-Z0-9]{8}])";$TIME_PATTERN = "([0-9]*-[0-9]*-[0-9]* [0-9]*:[0-9]*:[0-9]*)";$ERROR_KEYWORDS = "(ErrorMsgException|NullPointerException|FileNotFoundException|JSONException|NumberFormatException|Error|Exception|失败)";$MOCK_KEYWORDS = "()";$PID = "";$OLD_PID = "";$PID_COLOR = 36;$TIME_COLOR = 32;$SQL_COLOR = 32;$REQ_COLOR = 35;$RES_COLOR = 35;$ERROR_COLOR = 31;$MOCK_COLOR = 33;  $_ =~ s/$TIME_PATTERN/\e[1;32m$1\e[0m/g;  if($_ =~ m/(\[[a-zA-Z0-9]{8}])/){    $PID = substr($&,1,8);    print "Got PID : $PID\n";    print "Old PID : $OLD_PID\n";    if($PID eq $OLD_PID){      print "++++++++++++++++++++++++++++++\n";      $_ =~ s/\[$PID]/[\e[1;\Q$PID_COLOR\Em$PID\e[0m]/g;    }else{      print "------------------------------\n";      $OLD_PID = $PID;      $PID_COLOR = ($PID_COLOR == 35) ? 36 : 35;      $_ =~ s/\[$PID]/[\e[1;\Q$PID_COLOR\Em$PID\e[0m]/g;    }  }  $_ =~ s/(\[REQ])/[\e[1;\Q$REQ_COLOR\EmREQ\e[0m]/g;  $_ =~ s/(\[RES])/[\e[1;\Q$RES_COLOR\EmRES\e[0m]/g;  $_ =~ s/(\[SQL])/[\e[1;\Q$SQL_COLOR\EmSQL\e[0m]/g;  $_ =~ s/($ERROR_KEYWORDS)/\e[1;\Q$ERROR_COLOR\Em$1\e[0m/ig;


# 

# tail -10000f 2021-03-21.log | perl -pe '$PID_PATTERN = "(\[[a-zA-Z0-9]{8}])";$TIME_PATTERN = "([0-9]*-[0-9]*-[0-9]* [0-9]*:[0-9]*:[0-9]*)";$ERROR_KEYWORDS = "(ErrorMsgException|NullPointerException|FileNotFoundException|JSONException|NumberFormatException|Error|Exception|失败)";$MOCK_KEYWORDS = "()";$PID = "";$TIME_COLOR = 32;$SQL_COLOR = 32;$REQ_COLOR = 35;$RES_COLOR = 35;$ERROR_COLOR = 31;$MOCK_COLOR = 33;  $_ =~ s/$TIME_PATTERN/\e[1;32m$1\e[0m/g;  if($_ =~ m/(\[[a-zA-Z0-9]{8}])/){    $PID = substr($&,1,8);    print "Got PID : $PID\n";    print "Old PID : $OLD_PID\n";    if($PID eq $OLD_PID){      print "++++++++++++++++++++++++++++++\n"; $PID_COLOR = ($PID_COLOR == 35) ? 35 : 36;     $_ =~ s/\[$PID]/[\e[1;\Q$PID_COLOR\Em$PID\e[0m]/g;    }else{      print "------------------------------\n";      $OLD_PID = $PID;      $PID_COLOR = ($PID_COLOR == 35) ? 36 : 35;      $_ =~ s/\[$PID]/[\e[1;\Q$PID_COLOR\Em$PID\e[0m]/g;    }  }  $_ =~ s/(\[REQ])/[\e[1;\Q$REQ_COLOR\EmREQ\e[0m]/g;  $_ =~ s/(\[RES])/[\e[1;\Q$RES_COLOR\EmRES\e[0m]/g;  $_ =~ s/(\[SQL])/[\e[1;\Q$SQL_COLOR\EmSQL\e[0m]/g;  $_ =~ s/($ERROR_KEYWORDS)/\e[1;\Q$ERROR_COLOR\Em$1\e[0m/ig;'


#-------------------------------------------------------------------------------------------------
# 显示方式：

# 0（默认）
# 1（高亮(好像就是加粗)）
# 22（非粗体）
# 4（下划线）
# 24（非下划线）
# 5（闪烁）
# 25（非闪烁）
# 7（反显）
# 27（非反显）


# 颜色：

# 字体色	背景色	颜色
# 30	40	黑色
# 31	41	红色
# 32	42	绿色
# 33	43	黄色
# 34	44	蓝色
# 35	45	紫色
# 36	46	青色
# 37	47	白色

# ------------------------------
# $vocal = <STDIN>;
# print "what you said : $vocal";
# for($i = 1;$i <= 9; $i++){
#   if($i == 1){print "the $i st echo : ";}
#   elsif($i == 2){print "the $i nd echo : ";}
#   elsif($i == 3){print "the $i rd echo : " ;}
#   else{print "the $i th echo : ";}
#   print "$vocal";
# }
# ------------------------------

# ------------------------------
# while(1){
#   # $_ = <STDIN>;
#   if(m/[5]/){
#     print "Hit!\n";
#   }else{
#     print "Oops.\n";
#   }
# }

# # [test@localhost ~]$ ./perl.pl
# # 123
# # Oops.
# # 789
# # Oops.
# # 456
# # Hit!
# # 12345678
# # Hit!
# ------------------------------

# ------------------------------

# perl -pe 'print"1. $_";s/hello/olleh/;print"2. $_";s/olleh/hi/;print"3. "'
# 等价于：

# while(<STDIN>){  # 标准输入流默认存到了$_中
#   {
#     print"1. $_";
#     $_ =~ s/hello/olleh/;
#     print"2. $_";
#     $_ =~ s/olleh/hi/;
#     print"3. ";
#   }
#   print "$_";
# }
# ------------------------------

# ------------------------------

# while(1){
#   print "Input a +86 phone number:\n";
#   $phone = <STDIN>;
#   if($phone =~ /^(13[0-9]|14[5|7]|15[0|1|2|3|4|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}/){
#     print "Oh, that's a truly number.\n"
#   }else{
#     print "Fake number!\n"
#   }
# }


# [test@localhost ~]$ ./perl.pl
# Input a +86 phone number:
# 14412340000
# Fake number!
# Input a +86 phone number:
# 18810325061
# Oh, that's a truly number.
# Input a +86 phone number:
# 18446441009
# Fake number!
# Input a +86 phone number:
# ^C

# ------------------------------

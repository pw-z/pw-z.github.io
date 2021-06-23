#!/bin/bash
# show logs of today and many days after 
# log file of today should exist already
# the others may not, so >> first before tail -f
# note that only changed file will be updated in tail -f mode

LOG_PATH="tomcat9/cmbirs/LOG/"
date1=$(date +%Y-%m-%d)
date2=$(date +%Y-%m-%d --date="+1 day")
date3=$(date +%Y-%m-%d --date="+2 day")
date4=$(date +%Y-%m-%d --date="+3 day")
date5=$(date +%Y-%m-%d --date="+4 day")
date6=$(date +%Y-%m-%d --date="+5 day")
date7=$(date +%Y-%m-%d --date="+6 day")
date8=$(date +%Y-%m-%d --date="+7 day")
date9=$(date +%Y-%m-%d --date="+8 day")
date10=$(date +%Y-%m-%d --date="+9 day")
date11=$(date +%Y-%m-%d --date="+10 day")
date12=$(date +%Y-%m-%d --date="+11 day")
date13=$(date +%Y-%m-%d --date="+12 day")
date14=$(date +%Y-%m-%d --date="+13 day")
>> $LOG_PATH${date1}.log
>> $LOG_PATH${date2}.log
>> $LOG_PATH${date3}.log
>> $LOG_PATH${date4}.log
>> $LOG_PATH${date5}.log
>> $LOG_PATH${date6}.log
>> $LOG_PATH${date7}.log
>> $LOG_PATH${date8}.log
>> $LOG_PATH${date9}.log
>> $LOG_PATH${date10}.log
>> $LOG_PATH${date11}.log
>> $LOG_PATH${date12}.log
>> $LOG_PATH${date13}.log
>> $LOG_PATH${date14}.log
tail -f $LOG_PATH${date1}.log  $LOG_PATH${date2}.log $LOG_PATH${date3}.log $LOG_PATH${date4}.log $LOG_PATH${date5}.log $LOG_PATH${date6}.log $LOG_PATH${date7}.log $LOG_PATH${date8}.log  $LOG_PATH${date9}.log $LOG_PATH${date10}.log $LOG_PATH${date11}.log  $LOG_PATH${date12}.log  $LOG_PATH${date13}.log   $LOG_PATH${date13}.log  $LOG_PATH${date14}.log | perl -pe '$PID_PATTERN = "(\[[a-zA-Z0-9]{8}])";$TIME_PATTERN = "([0-9]*-[0-9]*-[0-9]* [0-9]*:[0-9]*:[0-9]*)";$ERROR_KEYWORDS = "(ErrorMsgException|NullPointerException|FileNotFoundException|JSONException|NumberFormatException|Error|Exception|null|失败)";$TIME_COLOR = 32;$SQL_COLOR = 32;$REQ_COLOR = 35;$RES_COLOR = 35;$ERROR_COLOR = 31;$MOCK_COLOR = 33;  $_ =~ s/$TIME_PATTERN/\e[1;32m$1\e[0m/g;  if($_ =~ m/(\[[a-zA-Z0-9]{8}])/){    $PID = substr($&,1,8);    if($PID eq $OLD_PID){      $PID_COLOR = ($PID_COLOR == 35) ? 35 : 36;      $_ =~ s/\[$PID]/[\e[1;\Q$PID_COLOR\Em$PID\e[0m]/g;    }else{      $OLD_PID = $PID;      $PID_COLOR = ($PID_COLOR == 35) ? 36 : 35;      $_ =~ s/\[$PID]/[\e[1;\Q$PID_COLOR\Em$PID\e[0m]/g;    }  }  $_ =~ s/(\[REQ])/[\e[1;\Q$REQ_COLOR\EmREQ\e[0m]/g;  $_ =~ s/(\[RES])/[\e[1;\Q$RES_COLOR\EmRES\e[0m]/g;  $_ =~ s/(\[SQL])/[\e[1;\Q$SQL_COLOR\EmSQL\e[0m]/g;  $_ =~ s/($ERROR_KEYWORDS)/\e[1;\Q$ERROR_COLOR\Em$1\e[0m/ig;'


# different between '>' and '>>' order:
# ---------------------------------------------------------------------------------------------
# echo "hello" > a.txt        clear a.txt (or create it if not exist) then put "hello" into it 
# echo "hello" >> a.txt       create a.txt(if not exist) then append "hello" at the end of it
# ---------------------------------------------------------------------------------------------


# this script is the command-line version (with a little diff) of the code here:
# ---------------------------------------------------------------------------------------------
# $PID_PATTERN = "(\[[a-zA-Z0-9]{8}])";
# $TIME_PATTERN = "([0-9]*-[0-9]*-[0-9]* [0-9]*:[0-9]*:[0-9]*)";
# $ERROR_KEYWORDS = "(ErrorMsgException|NullPointerException|FileNotFoundException|JSONException|NumberFormatException|Error|Exception|null|失败)";


# 30  黑色
# 31  红色
# 32  绿色
# 33  黄色
# 34  蓝色
# 35  紫色
# 36  青色
# 37  白色

# $TIME_COLOR = 32;
# $SQL_COLOR = 32;
# $REQ_COLOR = 35;
# $RES_COLOR = 35;
# $ERROR_COLOR = 31;
# $MOCK_COLOR = 33;

# while(<STDIN>){
#   $_ =~ s/$TIME_PATTERN/\e[1;32m$1\e[0m/g;
#   if($_ =~ m/(\[[a-zA-Z0-9]{8}])/){
#     $PID = substr($&,1,8);
#     if($PID eq $OLD_PID){
#       $PID_COLOR = ($PID_COLOR == 35) ? 35 : 36;
#       $_ =~ s/\[$PID]/[\e[1;\Q$PID_COLOR\Em$PID\e[0m]/g;
#     }else{
#       $OLD_PID = $PID;
#       $PID_COLOR = ($PID_COLOR == 35) ? 36 : 35;
#       $_ =~ s/\[$PID]/[\e[1;\Q$PID_COLOR\Em$PID\e[0m]/g;
#     }
#   }
#   $_ =~ s/(\[REQ])/[\e[1;\Q$REQ_COLOR\EmREQ\e[0m]/g;
#   $_ =~ s/(\[RES])/[\e[1;\Q$RES_COLOR\EmRES\e[0m]/g;
#   $_ =~ s/(\[SQL])/[\e[1;\Q$SQL_COLOR\EmSQL\e[0m]/g;
#   $_ =~ s/($ERROR_KEYWORDS)/\e[1;\Q$ERROR_COLOR\Em$1\e[0m/ig;

#   print "$_";
# }

# ---------------------------------------------------------------------------------------------

# An API Autotest Tool Part1: Basic Functions Implementation

- [An API Autotest Tool Part1: Basic Functions Implementation](#an-api-autotest-tool-part1-basic-functions-implementation)
  - [1 Introduction](#1-introduction)
  - [2 Code Review](#2-code-review)
    - [2.1 Handle Test Cases with Excel](#21-handle-test-cases-with-excel)
      - [2.1.1 Case Template](#211-case-template)
      - [2.1.2 Read Cases from Excel](#212-read-cases-from-excel)
<<<<<<< HEAD
    - [2.2 Handle Log with Logging](#22-handle-log-with-logging)
    - [2.3 Handle Basic Parameters with Configparser](#23-handle-basic-parameters-with-configparser)
      - [2.3.1 Config File Template](#231-config-file-template)
      - [2.3.2 Read Conifg File](#232-read-conifg-file)
    - [2.4 Handle Shell Commands with Paramiko](#24-handle-shell-commands-with-paramiko)
    - [2.5 Handle Post Request with Requests](#25-handle-post-request-with-requests)
    - [2.6 Handle SQL with cx_Oracle](#26-handle-sql-with-cx_oracle)
    - [2.7 The Main Script](#27-the-main-script)
=======
    - [2.2 Handle Basic Parameters with Configparser](#22-handle-basic-parameters-with-configparser)
      - [2.2.1 Config File Template](#221-config-file-template)
      - [2.2.2 Read Conifg File](#222-read-conifg-file)
    - [2.3 Handle Shell Commands with Paramiko](#23-handle-shell-commands-with-paramiko)
    - [2.4 Handle Post Request with Requests](#24-handle-post-request-with-requests)
    - [2.5 Handle DQL with cx_Oracle](#25-handle-dql-with-cx_oracle)
    - [2.6 Handle Log with Logging](#26-handle-log-with-logging)
    - [2.7 The Main Method Script](#27-the-main-method-script)
>>>>>>> e20548277862dca650faf9ceb690b242803ace77
    - [2.8 *Generate Test Report](#28-generate-test-report)
  - [3 Todo List](#3-todo-list)

## 1 Introduction

This is a simlpe data-driven api autotest tool(or so-called testing framework), implemented **WITHOUT** using `unittest` or `pytest`. The main procedure for a complete api test using this tool is:

1. write test cases in a `.xlsx` file, every case mainly includes the following contents: 
   * api address like `http://127.0.0.1:8089/test`
   * request body for the `post` method of http protocol and expected results (`key:value`) in response
   * shell commands you want to run before sending request
   * SQL you want to run after getting response and expected SQL results (`key:value`)
2. set the default config info in `config.ini` such as path_to_excel or default_content_type.
3. run the test by running `run_test.py`, which will handle every case in the excel:
   * execute shell commands and print the result
   * post the request and verify the response
   * execute the SQL and verify the result
   * generate an all-in-one(html, js, css) test report

Every function is implemented for specific requirements, it can not handle the `get` method because it's unnecessary for now, as I said, this is a simple tool, there is a long-todo-list.

All code in this blog will be archived in `./my_site_root/code/some_sub_path/api-autotest-tool`, the code may have changed a lot if I am still working on it, that won't be updated here.

## 2 Code Review

```powershell
PS C:\pw-z.github.io\code\api-autotest-tool> tree /F
Folder PATH listing for volume Pomelo
Volume serial number is 96AE-B4C9
C:.
│  readme.md
│
└─src
    │  config.ini
    │  run_test.py
    │
    ├─case
    │    case.xlsx
    │
    ├─handler
    │    case_handler.py
    │    parameter_handler.py
    │    shell_handler.py
    │    sql_handler.py
    │  
    │
    ├─helper
    │    case_helper.py
    │    log_helper.py
    │    report_helper.py
    │  
    │
    ├─report
    │  ├─archived
    │  │      TestReport-20210705-190943.html
    │  │      TestReport-20210715-180623.html
    │  │
    │  └─template
    │        template.css
    │        template.html
    │  
    └─test
```

### 2.1 Handle Test Cases with Excel

#### 2.1.1 Case Template

|CaseName|CaseStep|Run?|Method|URI|Port|Address|ContentType|ShellScript|Body|ExpectedData|ResponseParameter|DQL|ExpectedDQLData|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|case1|step1|y|post||||||
||step2|n|post||||||
||step3|y|post||||||
|case2|step1|y|post||||||
||step2|y|post||||||

The Excel template has a certain header in ft row, from the second row, each line will be treated as a step in a case, each case should contain one step at least. You can also consider cases as test suites and steps as cases, no difference.

Only those steps whose `Run?` flag is 'y' will be run. If all steps in a case are skipped, this case will be marked as a skiped one and will not be displayed in the test report.

The `Method` should always be 'post', in fact this can be removed from the template, whatever its value is, every step will be send through the `post` method, as I said, this is just what I need for now. The meaning of this column, just in case, some day we need a `get`.

The `URI`, `Port` and `ContentType` can be config in `config.ini` and the value in config file will be used when these are empty.

The `ShellScript` will be executed before sending the `Body`, which help us getting the test environment ready, for example:

```shell
cd ~/test_project/input

echo '
test data1
test data2
test data3
' > test_data.txt

cat test_data.txt

date -s 20210101
```
This script will put our test data in the proper location and set the system date to what we want. Note that if the command has no output such as `echo 'something' > somewhere`, we don't know the result in test_log of the test tool, write a `cat` after that is fine.

The `Address` is necessary, it will be attached to the `URI` and the `Port`, if you set the `URI='http://yourhost.com', Port=8089, Address='/login'`, then the final api address will be `http://yourhost.com/8089/login`. 

The `Body`, `ExpectedData` and `ResponseParameter` are a group. Ft the `Body` will be sent, after we got a response, the `parameter_handler` will check every `key:value` in `ExpectedData`, return a pass flag if it's indeed in the response or a fail if not, in the meantime, the `parameter_handler` will collect the value of the key in `ResponseParameter`, so you can use it with `${key}` after then(only in `Body`). By the way, in `ResponseParameter`, you can rename a parameter using `key:renamed_key`, this is helpful in the situation that we want to store many parameters with the same name.

Here is an instance:

Ft step:
```
Body:
  data={
      "userId":"user1",
      "PASSWORD":"pw1",
      "f":"Login"
  }

ResponseParameter:
  token:token1
```

After the ft step, we got a parameter `token1` that can be used in the next step, just assume that `token1=ALSKDJFLASKDJFLKLSKDJFlkjdlskafjLKDHLGKASHD`, write next step `Body` like this:

```
data={
  "f":"some function",
  "token":"${token1}"
}
```
then the request body will be flushed before being sent:
```
data={
  "f":"some function",
  "token":"ALSKDJFLASKDJFLKLSKDJFlkjdlskafjLKDHLGKASHD"
}
```

The last two column `DQL` and `ExpectedDQLData` work in the same way as the `Body` and `ExpectedData`.


#### 2.1.2 Read Cases from Excel

This code is developed from [Import Testcases From Excel to Testlink](https://www.pwz.wiki/blog/2021/06/20210623-import-testcases-from-excel-to-testlink), it read the excel file and init a list contains all the cases(in dict format).

`xlrd` is a tool which can handle `.xlsx` file, for some reason, the latest version of `xlrd` supports `.xls` format only, here you need to `pip install xlrd==1.2.0`, then it works. This is a little ..., I am considering replace it with `pandas`.

```python
# ./helper/case_helper.py

import xlrd
from helper.log_helper import *

logger = init_logger(__name__)


def get_column_index(sheet, column_name):
    column_index = None
    for i in range(sheet.ncols):
        if sheet.cell_value(0, i) == column_name:
            column_index = i
            break
    return column_index


def get_case_step(sheet_object, row_number):
    case_step = {
        'CaseStep': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'CaseStep')],
        'Method': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'Method')],
        'URI': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'URI')],
        'Port': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'Port')],  # 8089.0
        'Address': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'Address')],
        'Body': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'Body')],
        'ContentType': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'ContentType')],
        'ResponseParameter': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'ResponseParameter')],
        'ExpectedData': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'ExpectedData')],
        'ShellScript': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'ShellScript')],
        # 'Run?': str(sheet_object.row_values(row_number)[get_column_index(sheet_object, 'Run?')])[:-2],   # 111.0
        'Run?': str(sheet_object.row_values(row_number)[get_column_index(sheet_object, 'Run?')]),  # '111
        'DQL': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'DQL')],
        'ExpectedDQLData': str(
            sheet_object.row_values(row_number)[get_column_index(sheet_object, 'ExpectedDQLData')]).upper().splitlines()
    }
    case_step['ResponseParameter'] = str(case_step['ResponseParameter']).splitlines()

    wanted_paras = {}
    lines = str(case_step['ExpectedData']).splitlines()
    for line in lines:
        i = line.find(':')
        wanted_paras[line[:i]] = line[i + 1:]
    case_step['ExpectedData'] = wanted_paras

    return case_step


def read_excel(file_path, sheet_name):
    case_list_dic = []
    case_step_list = []
    try:
        book = xlrd.open_workbook(file_path)
    except Exception as error:
        logger.error(r'can not open the excel file  ' + str(error))
        return error
    else:
        sheet = book.sheet_by_name(sheet_name)
        rows = sheet.nrows
        case_name = sheet.row_values(1)[get_column_index(sheet, 'CaseName')]  # when i==1, case name must exists
        case_step = get_case_step(sheet, 1)
        case_step_list.append(case_step)
        last_case_name = case_name
        for i in range(2, rows):  # ignore table header
            case_name = sheet.row_values(i)[get_column_index(sheet, 'CaseName')]
            if case_name == '':  # the same case
                case_step = get_case_step(sheet, i)
                case_step_list.append(case_step)
            else:  # new case
                case_dict = {
                    'CaseName': last_case_name,
                    'CaseSteps': case_step_list
                }
                case_list_dic.append(case_dict)

                case_step_list = []
                last_case_name = case_name

                case_step = get_case_step(sheet, i)
                case_step_list.append(case_step)
            if i == rows - 1:
                case_dict = {
                    'CaseName': last_case_name,
                    'CaseSteps': case_step_list
                }
                case_list_dic.append(case_dict)
    return case_list_dic
```

A `case_list_dic` sample:

```python
case_list_dic = [
  case1,
  case2,
  case3 = {
    'CaseName':case_name,
    'CaseSteps':[
      step1,
      step2,
      step3 = {
        'CaseStep':step_name,
        'Method':'post',
        'Body':...,
        'Run?':'y',
        'Key':'Value',
        ...and so on
      }
    ]
  }
]
```

### 2.2 Handle Log with [Logging][Logging]

The `log_helper.py` creates three handlers:
* fh = logging.FileHandler(log_path)
* ch = logging.StreamHandler()
* sh = logging.StreamHandler(__sio)

`fh` and `ch` are easy to understand, one prints logs to the log file and the other to the console.

<<<<<<< HEAD
`sh` is a `StreamHandler` initialized with an `io.StringIO`, it's used to record step running logs. The logs in `sh` will be cleared before running a new step and stored in `step_run_log` after the step is completed.
=======
#### 2.2.1 Config File Template
>>>>>>> e20548277862dca650faf9ceb690b242803ace77

```python
# helper/log_helper.py
import logging
import time
import io

__sio = io.StringIO()


def init_sio():
    __sio.truncate(0)
    __sio.seek(0)


def get_sio():
    return __sio


def init_logger(__name__):

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    today = time.strftime('%Y-%m-%d')
    log_name = today + '.log'
    log_path = 'log/' + log_name
    # log_path = log_name

    formatter = logging.Formatter('%(levelname)s [%(asctime)s] %(message)s')

    fh = logging.FileHandler(log_path, encoding='utf-8')
    ch = logging.StreamHandler()

    sh = logging.StreamHandler(__sio)

    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    sh.setFormatter(formatter)

    fh.setLevel(logging.DEBUG)
    ch.setLevel(logging.INFO)
    sh.setLevel(logging.INFO)

    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.addHandler(sh)
    return logger
```

A log sample:

```log
DEBUG [2021-07-15 08:45:52,192] parameter handler initialize success # {'uri': 'http://127.0.0.1', 'port': '8089', 'content_type': 'application/x-www-form-urlencoded;charset=UTF-8', 'ssh_hostname': '127.0.0.1', 'ssh_username': 'testfx', 'ssh_password': 'testfx', 'excel_path': './case/case.xlsx', 'sheet_list': ['test'], 'db_uri': '127.0.0.1:1517/test2', 'db_username': 'test', 'db_password': 'test', 'db_oracle_lib_dir': 'C:\\oracle\\instantclient_19_11', 'test_report_title': 'TEST API AUTOTEST'}
DEBUG [2021-07-15 08:45:53,641] connect to Oracle success: 15.3.0.0.0
INFO [2021-07-15 08:45:53,674] 
====================================================================================================
 Run Case # 参数获取1
====================================================================================================
INFO [2021-07-15 08:45:53,676] 
**********************************************************************
 Run Step # 登录获取token1
**********************************************************************
INFO [2021-07-15 08:45:53,705] Request url: http://127.0.0.1:8089/login
INFO [2021-07-15 08:45:53,706] Content type: application/x-www-form-urlencoded;charset=UTF-8
INFO [2021-07-15 08:45:53,706] Request body:
data={
    "userId":"userid1",
    "PASSWORD":"pw1234",
    "f":"Login"
}
INFO [2021-07-15 08:45:56,781] Response:
{
    "CODE":"200",
    "code":"200",
    "u":{
        "PHONENUM":"",
        "STATUS":"1",
        "USERNOTE":"",
        "ENTITY_ID":"999",
        "PASSWORD":"143434C378479718",
        "ACCTION":"0",
        "PWD_EXPIRY":"",
        "USERID":"userid",
        "USERNAME":"管理员",
        "CREATE_TIME":"",
        "EMAIL":"",
        "CREATE_ID":"auto"
    },
    "permission":[
        {
            "MID":"PublicModule",
            "MPARENTCODE":"",
            "TEXT":"公共模块",
            "LV_ORDER":"7",
            "MLEVEL":"1",
            "MURL":"",
            "ICON":"",
            "VISIBLE":"",
            "children":[
                {
                    "MID":"UserManagement",
                    "MPARENTCODE":"PublicModule",
                    "TEXT":"用户管理",
                    "LV_ORDER":"7-1",
                    "MLEVEL":"2",
                    "MURL":"",
                    "ICON":"",
                    "VISIBLE":""
                }
            ]
        }
    ],
    "token":"43C353C334C334D314D3B3B3C3B31463243414C3b01596bf03b15298ead03dc23515c1fc"
}
INFO [2021-07-15 08:45:56,781] Flush parameter: token
INFO [2021-07-15 08:45:56,782]   token-->43C353C334C334D314D3B3B3C3B31463243414C3b01596bf03b15298ead03dc23515c1fc
INFO [2021-07-15 08:45:56,782] Verify parameters in response...
INFO [2021-07-15 08:45:56,782]  does "TYPE_DESC" == "机构类型" ?
DEBUG [2021-07-15 08:45:56,782] find "TYPE_DESC":"机构类型", in response
INFO [2021-07-15 08:45:56,782] Correct! Expected value of "TYPE_DESC" is "机构类型", found "机构类型".
INFO [2021-07-15 08:45:56,782]  does "TEXT" == "公共模块" ?
DEBUG [2021-07-15 08:45:56,783] find "TEXT":"用户管理", in response
ERROR [2021-07-15 08:45:56,783] Bad Value! Expected value of "TEXT" is "公共模块" but found "用户管理"
INFO [2021-07-15 08:45:56,904] Execute SQL: SELECT * FROM BASE_PARAM
INFO [2021-07-15 08:45:56,905] SQL results: 
INFO [2021-07-15 08:45:56,905] [('CNY_INTEREST_RATE', '利率', '0.1', '0', '', '垫款利率', None, None, None, None),('TRADE_DATE', '交易日期', '20210401', '1', '', '交易日期', None, None, None, datetime.datetime(2021, 7, 14, 21, 24, 38, 769081))]
INFO [2021-07-15 08:45:56,912] Verify parameters in sql result... 
ERROR [2021-07-15 08:45:56,912] Bad Parameter! No column named --> COUNT(*)
INFO [2021-07-15 08:45:56,912] 
**********************************************************************
 Run Step # 登录获取token2
**********************************************************************
INFO [2021-07-15 08:45:56,912] Execute command:
ls
INFO [2021-07-15 08:45:56,943] Command result:
checklog.sh
k_show-many-logs.sh
LOG
mock_path
share
showlog.sh
timerlog.sh
tomcat9

INFO [2021-07-15 08:45:56,944] Request url: http://127.0.0.1:8089/login
INFO [2021-07-15 08:45:56,944] Content type: application/x-www-form-urlencoded;charset=UTF-8
INFO [2021-07-15 08:45:56,944] Request body:
data={
    "userId":"userid2",
    "PASSWORD":"pw1234",
    "f":"Login"
}
INFO [2021-07-15 08:45:56,984] Response:
{"code":"200","token":"43C353C334C334D314D3B3B3C3B31463243414C3b01596bf03b15298ead03dc23515c1fc"}
INFO [2021-07-15 08:45:56,984] Flush parameter: token
INFO [2021-07-15 08:45:56,985]   token-->43C353C334C334D314D3B3B3C3B31463243414C3b01596bf03b15298ead03dc23515c1fc
INFO [2021-07-15 08:45:57,010] Execute SQL: SELECT count(*) FROM BASE_PARAM
INFO [2021-07-15 08:45:57,010] SQL results: 
INFO [2021-07-15 08:45:57,010] [(32,)]
INFO [2021-07-15 08:45:57,010] Verify parameters in sql result... 
INFO [2021-07-15 08:45:57,010] Correct! Expected value of COUNT(*) is 32, found 32.
```


### 2.3 Handle Basic Parameters with [Configparser][Configparser]

With the help of `configparser`, it's easy to handle a `config.ini` out of the code. Pay attention to the comments in `[database]` section, about 'oracle instant client'.

#### 2.3.1 Config File Template

```
[http]
# Default interface URI, if `URI` in case.xlsx was empty, this will be used
URI = http://
# Port information, if `Port` in case.xlsx was empty, this will be used
Port = 
#Content-Type information
content_type = application/x-www-form-urlencoded;charset=UTF-8

[shell]
#ssh info
ssh_hostname=
ssh_username=
ssh_password=

[case]
#TestCase file path
excel_path=./case/case.xlsx
#TestCase sheet names
sheet_list=import_customer
;sheet_list=test

[database]
#SUPPORT ORACLE ONLY
#read https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html#wininstall
#if you don't know what is 'oracle instant client'
db_oracle_lib_dir=C:\oracle\instantclient_19_11
db_uri=
db_username=
db_password=

[other]
test_report_title= TEST API AUTOTEST
```

<<<<<<< HEAD
#### 2.3.2 Read Conifg File
=======
#### 2.2.2 Read Conifg File
>>>>>>> e20548277862dca650faf9ceb690b242803ace77

Basically there is no differences between common parameters and the configs in `config.ini`, so all config info will be set into a parameter pool in class `Parameter` at the init time.

```python
# handler/parameter_handler.py
import configparser
from helper.log_helper import *

logger = init_logger(__name__)


class Parameter:
    __global_configs = {}
    __parameter_pool = {}

    def __init__(self, configpath):
        cnf = configparser.ConfigParser()
        cnf.read(configpath)

        uri = cnf.get('http', 'URI')
        port = cnf.get('http', 'Port')
        content_type = cnf.get('http', 'content_type')

        ssh_hostname = cnf.get('shell', 'ssh_hostname')
        ssh_username = cnf.get('shell', 'ssh_username')
        ssh_password = cnf.get('shell', 'ssh_password')

        excel_path = cnf.get('case', 'excel_path')
        sheet_list = cnf.get('case', 'sheet_list')

        db_uri = cnf.get('database', 'db_uri')
        db_username = cnf.get('database', 'db_username')
        db_password = cnf.get('database', 'db_password')
        db_oracle_lib_dir = cnf.get('database', 'db_oracle_lib_dir')

        self.__global_configs['uri'] = uri
        self.__global_configs['port'] = port
        self.__global_configs['content_type'] = content_type

        self.__global_configs['ssh_hostname'] = ssh_hostname
        self.__global_configs['ssh_username'] = ssh_username
        self.__global_configs['ssh_password'] = ssh_password

        self.__global_configs['excel_path'] = excel_path
        self.__global_configs['sheet_list'] = sheet_list.split(',')

        self.__global_configs['db_uri'] = db_uri
        self.__global_configs['db_username'] = db_username
        self.__global_configs['db_password'] = db_password
        self.__global_configs['db_oracle_lib_dir'] = db_oracle_lib_dir

        test_report_title = cnf.get('other', 'test_report_title')
        self.__global_configs['test_report_title'] = test_report_title

        logger.debug("parameter handler initialize success # " + str(self.__global_configs))

```

Of couse, there will be a setter and a getter in `Parameter`:

```python
# handler/parameter_handler.py
class Parameter:
    def get_parameter(self, p_name):
        if p_name in self.__global_configs:
            return self.__global_configs[p_name]
        elif p_name in self.__parameter_pool:
            return self.__parameter_pool[p_name]
        else:
            return False

    def add_parameter(self, p_name, p_value):
        self.__parameter_pool[p_name] = p_value
        return True
```

There are four more methods in `Parameter` class:

```python

def flush_parameter_pool(self, parameters, response):
  pass

def flush_body_parameter(self, body):
  pass

def verify_parameter_in_response(self, paras_dict, response):
  pass

def verify_parameter_in_sql_result(self, paras, results, db_col):
  pass
```

The method name is clear enough, let's review it in detail later.


### 2.4 Handle Shell Commands with [Paramiko][Paramiko]

```python
# handler/shell_handler.py
import paramiko  # ShellHandler
from helper.log_helper import *
logger = init_logger(__name__)


class ShellHandler:

    def __init__(self, parameter_handler):
        self.ssh_hostname = parameter_handler.get_parameter('ssh_hostname')
        self.ssh_username = parameter_handler.get_parameter('ssh_username')
        self.ssh_password = parameter_handler.get_parameter('ssh_password')
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=self.ssh_hostname, port=22, username=self.ssh_username, password=self.ssh_password)

    def run(self, case):

        sh = case['ShellScript']
        logger.info("Execute command:\n" + sh)
        stdin, stdout, stderr = self.ssh.exec_command(sh)
        res, err = stdout.read(), stderr.read()
        result = res if res else err
        logger.info("Command result:\n " + result.decode())

        return True

    def close(self):
        self.ssh.close()
```

### 2.5 Handle Post Request with [Requests][Requests]

```python
# handler/case_handler.py
import requests
from helper.log_helper import *
logger = init_logger(__name__)


class CaseHandler:

    def __init__(self, parameter_handler):
        self.para = parameter_handler

    def __before_run(self, body):
        new_body = self.para.flush_body_parameter(body)
        return new_body

    def __after_run(self, case, response):
        # 1. flush the parameter pool
        self.para.flush_parameter_pool(case['ResponseParameter'], response.text)
        # 2. verify the expected response values
        flag = self.para.verify_parameter_in_response(case['ExpectedData'], response.text)
        return flag

    def run(self, case):
        # __uri = (case['URI']!='') ? case['URI'] : para.get_parameter('uri')
        __uri = case['URI'] if case['URI'] != '' else self.para.get_parameter('uri')
        __port = str(case['Port'])[:4] if str(case['Port'])[:4] != '' else self.para.get_parameter('port')
        __header = case['ContentType'] if case['ContentType'] != '' else self.para.get_parameter('content_type')

        if __uri != '' and __port != '' and case['Address'] != '' and __header != '':
            url = __uri + ":" + __port + case['Address']
            header = {'content-type': __header}
            logger.info('Request url: ' + url)
            logger.info('Content type: ' + __header)
        else:
            return False

        # TODO: PARAMETER REPLACE ..done.
        body = case['Body']
        body = self.__before_run(body)
        logger.info('Request body:\n' + body)

        try:
            res = requests.post(url, headers=header, data=body.encode('utf-8'))
            # print(res.json())
            logger.info('Response:\n' + res.text)
        except Exception as e:
            logger.error(e)
            return False
        else:
            return self.__after_run(case, res)
```

<<<<<<< HEAD
Here we meet `para.flush_body_parameter(body)`, `para.flush_parameter_pool(case['ResponseParameter'], response.text)` and `para.verify_parameter_in_response(case['ExpectedData'], response.text)`.
=======
Here we meet `para.flush_body_parameter(body)`, `para.flush_parameter_pool(case['ResponseParameter'], response.text)` and `para.verify_parameter_in_response(case['ExpectedData'], response.text)`
>>>>>>> e20548277862dca650faf9ceb690b242803ace77

See the code first.

```python
# handler/parameter_handler.py
import re
from helper.log_helper import *

logger = init_logger(__name__)


class Parameter:
    def flush_parameter_pool(self, parameters, response):
        fail_count = 0
        # print(parameters)
        # print(response)
        if len(parameters) == 0:
            return True
        else:
            for p in parameters:
                if ':' not in p:
                    logger.info('Flush parameter: ' + p)
                    if p in response:
                        re_string = r'("{0}" *: *.*?)'.format(p) + '[,|)|}]'
                        finds = re.finditer(re_string, response)
                        for find in finds:
                            s = find.group(1).split(':')
                            find_value = s[1]
                            if '"' in find_value:
                                # self.__parameter_pool[p] = find_value[1:-1]
                                logger.info('  ' + p + '-->' + find_value[1:-1])
                                self.add_parameter(p, find_value[1:-1])  # deal with "key":"value"
                            else:
                                # self.__parameter_pool[p] = find_value  # deal with "key":value
                                logger.info('  ' + p + '-->' + find_value)
                                self.add_parameter(p, find_value)
                    else:
                        fail_count += 1
                        logger.warning("No parameter in response -> {0}".format(p))
                else:
                    # rename parameter with string after ':'
                    p_origin = p[:p.find(':')]
                    p_rename = p[p.find(':') + 1:]
                    logger.info('Flush parameter: ' + p_origin)
                    if p_origin in response:
                        re_string = r'("{0}" *: *.*?)'.format(p_origin) + '[,|)|}]'
                        finds = re.finditer(re_string, response)
                        for _p in finds:
                            s = _p.group(1).split(':')
                            find_value = s[1]
                            if '"' in find_value:
                                # self.__parameter_pool[p_rename] = find_value[1:-1]  # deal with "key":"value"
                                logger.info('  ' + p + '-->' + find_value[1:-1])
                                self.add_parameter(p_rename, find_value[1:-1])  # deal with "key":"value"
                            else:
                                # self.__parameter_pool[p_rename] = find_value  # deal with "key":value
                                logger.info('  ' + p + '-->' + find_value)
                                self.add_parameter(p_rename, find_value)
                    else:
                        fail_count += 1
                        logger.error("No parameter in response -> {0}".format(p_origin))
            return True if fail_count == 0 else False

<<<<<<< HEAD
=======

>>>>>>> e20548277862dca650faf9ceb690b242803ace77
    def flush_body_parameter(self, body):
        """
        replace '${A}' with 'A' in __parameter_pool
        :param body:
        :return: 
        """
        paras = re.finditer(r'\$\{\w*\}', body)
        fail_count = 0
        for p in paras:
            # re.sub(r'\$\{\w*\}', self.get_parameter(p.group()[2:-1]), request_body)
            # print(p.group())
            _p = self.get_parameter(p.group()[2:-1])
            if _p:
                body = body.replace(p.group(), _p)
                logger.info('Replace parameter: {0} --> {1}'.format(p.group(), _p))
            else:
                fail_count += 1
                logger.error("Fail to replace parameter -> {0}".format(p.group()[2:-1]))
                pass

        # if fail_count:
        #     self.logger.error("fail to replace parameter * {0}".format(fail_count))
        return body

    def verify_parameter_in_response(self, paras_dict, response):
        # paras_dict = { 'expected_name1': 'expected_value1', 'expected_name2': 'expected_value2', ... }
        flag = True
        if len(paras_dict) == 0:
            pass
        else:
            logger.info('Verify parameters in response...')
            for key in paras_dict:
                logger.info(" does " + key + " == " + paras_dict[key] + " ?")
                if key in response:
                    # re_string = r'{0} *: *\".*?\"'.format(key)  # outdated
                    re_string = '({0} *: *.*?)'.format(key) + '[,|)|}]'
                    finds = re.finditer(re_string, response)
                    for _p in finds:
                        logger.debug("find {} in response".format(_p.group()))
                        s = _p.group(1).split(':')
                        _p_name = s[0]
                        _p_value = s[1]
                        # print(s)
                        # print(s[1:-1])
                        if paras_dict[key] == _p_value:
                            logger.info("Correct! Expected value of {0} is {1}, found {2}.".format(key, paras_dict[key], _p_value))
                        else:
                            logger.error(
                                "Bad Value! Expected value of {0} is {1} but found {2}".format(key, paras_dict[key], _p_value))
                            flag = False
                else:
                    logger.error("Bad Parameter! No parameter named --> {0}".format(key))
                    flag = False
        return flag
```

<<<<<<< HEAD
As a digression, I'd like to talk about why this is a tool **WITHOUT** using `pytest` or `utittest`? That's because, I didn't know them when I was writing this tool! I am still learning, knowing not enough about those python's powerful libraries :). The code like `re_string = '({0} *: *.*?)'.format(key) + '[,|)|}]'` or `paras = re.finditer(r'\$\{\w*\}', body)` is awful, can not deal with all the situations. Notice that the `response` is in `json` format! All re stuff can be replace with `import json` and some more clean code. Nevermind, I'll put that in the long-todo-list.
=======
As a digression, I would like to talk about why this is a tool **WITHOUT** using `pytest` or `utittest`, that's because, I didn't know anything about them at all when I was writing this tool! I am learning! Knowing very little about python's powerful libraries.

Considering the requirements about handling the parameters, first thing coming up in my mind is `regular expression`, so I go search for the re lib in python then the code like `re_string = '({0} *: *.*?)'.format(key) + '[,|)|}]'` or `paras = re.finditer(r'\$\{\w*\}', body)` is written down, that's awful code with many bugs, can not deal with all the situations. Notice that the `response` is in `json` format! All re stuff can be replace with `import json` and some more clean code. However, I didn't konw the `json` lib at that time.

>>>>>>> e20548277862dca650faf9ceb690b242803ace77


### 2.6 Handle SQL with [cx_Oracle][cx_Oracle]

Basically the same as `CaseHandler`. 

```python
# handler/sql_handler.py
import cx_Oracle as oracle  # SQLHandler
from helper.log_helper import *
logger = init_logger(__name__)


class SQLHandler:

    def __init__(self, parameter_handler):
        self.para = parameter_handler
        oracle.init_oracle_client(parameter_handler.get_parameter('db_oracle_lib_dir'))
        self.db_uri = parameter_handler.get_parameter('db_uri')
        self.db_username = parameter_handler.get_parameter('db_username')
        self.db_password = parameter_handler.get_parameter('db_password')
        self.db_conn = oracle.connect(self.db_username, self.db_password, self.db_uri)
        self.db_cur = self.db_conn.cursor()
        logger.debug("connect to Oracle success: " + self.db_conn.version)

    def __after_run(self, case, results, db_col):
        flag = self.para.verify_parameter_in_sql_result(case['ExpectedDQLData'], results, db_col)
        return flag

    def run(self, case):
        db_cur = self.db_cur
        sql = case['DQL']
        # sql = "SELECT PARAM_VALUE FROM BASE_PARAM WHERE ID='TRADE_DATE'"
        db_cur.execute(sql)
        db_col = db_cur.description
        results = db_cur.fetchall()
        logger.info("Execute SQL: " + case['DQL'])
        logger.info("SQL results: ")  # here may return too much stuff, take care of your SQL conditions
        logger.info(results)
        # TODO handle multiple SQL results  ...done.
        return self.__after_run(case, results, db_col)

    def close(self):
        self.db_cur.close()
        self.db_conn.close()
```

This handler can only handle the query statements, `DML` or even `DDL` is not required for now.

As far as all SQL statements are executed by the `db_cur.execute(sql)`, a `delete from ...` statement may be executed successfully, but the `__after_run()` method will definitely fail.

```python
# handler/parameter_handler.py
import configparser
from helper.log_helper import *

logger = init_logger(__name__)


class Parameter:
    def verify_parameter_in_sql_result(self, paras, results, db_col):
        logger.info("Verify parameters in sql result... ")

        def verify_method1():
            if para == str(results):
                # TODO maybe we should consider more when para=='32' but result==32,
                # TODO not just str(result) then conclude that para==result
                logger.info("Correct! Expected SQL result is {1}".format(paras, results))
                return True
            else:
                logger.warning("Bad Value! Expected SQL result is {0} but found {1}".format(paras, results))
                return False

        def verify_method2():
            colon_index = para.index(':')
            para_name = para[:colon_index]
            para_value = para[colon_index + 1:]
            para_col_number = -1
            for col in db_col:
                col_description = list(col)
                if para_name in col_description:
                    # print(db_col.index(col))
                    para_col_number = db_col.index(col)
                    break
            if para_col_number != -1:
                for row in results:
                    # if results contains more then one row, every row needs to meet the para_name:para_value
                    row_list = list(row)
                    _found_value = str(row_list[para_col_number])
                    if para_value == _found_value:
                        # TODO maybe we should consider more when para=='32' but result==32,
                        # TODO not just str(result) then conclude that para==result
                        logger.info('Correct! Expected value of {0} is {1}, found {2}.'.format(para_name, para_value, _found_value))
                        return True
                    else:
                        logger.warning('Bad Value! Expected value of {0} is {1} BUT found {2}!'.format(para_name, para_value, _found_value))
                        return False
            else:
                logger.error('Bad Parameter! No column named --> {0}'.format(para_name))
                return False

        flag = True
        for para in paras:  # paras = ['only_one_string_without_colon'] or ['expected_name:expected_value', 'n2:v2',...]
            if ':' in para:
                r = verify_method2()
            else:
                r = verify_method1()
            if not r:
                flag = False
        return flag
```

### 2.7 The Main Script

The `run_test.py` script offers a main method, handles the whole test (cases, steps) and collects some useful information for generating test report.

```python
# ./run_test.py

from handler.parameter_handler import Parameter
from handler.case_handler import CaseHandler
from handler.shell_handler import ShellHandler
from handler.sql_handler import SQLHandler
from helper.case_helper import *
from helper.log_helper import *
import datetime
import helper.report_helper as r

if __name__ == '__main__':

    configpath = './config.ini'
    para = Parameter(configpath)

    # print(para.get_parameter('excel_path'))
    # print(para.get_parameter('sheet_list'))
    excel_path = para.get_parameter('excel_path')
    # print(excel_path)
    sheets = para.get_parameter('sheet_list')

    logger = init_logger(__name__)
    # print(logger.level)

    casehandler = CaseHandler(para)
    shellhandler = ShellHandler(para)
    sqlhandler = SQLHandler(para)

    test_result_detail = []
    test_result_summary = dict(
        count_all_cases=0,
        count_success_cases=0,
        count_fail_cases=0,
        test_start_time=datetime.datetime.now(),
        test_end_time='',
        test_report_title=para.get_parameter('test_report_title')
    )

    count_all_cases = 0
    count_success_cases = 0
    count_fail_cases = 0

    for sheet in sheets:
        cases = read_excel(excel_path, sheet)
        # print(cases)

        for case in cases:
            case_start_time = datetime.datetime.now()
            logger.info('\n' + '='*100 + '\n Run Case # ' + case['CaseName'] + '\n' + '='*100)

            case_run_result = True
            steps_run_detail = []
            count_all_steps = 0
            count_success_steps = 0
            count_fail_steps = 0
            for step in case['CaseSteps']:
                if step['Run?'] != 'y':
                    # logger.info('SKIP CASE')
                    continue
                else:
                    init_sio()  # clear the string io cache, start recording step run info
                    step_start_time = datetime.datetime.now()
                    logger.info('\n' + '-' * 70 + '\n Run Step # ' + step['CaseStep'] + '\n' + '-' * 70)
                    r1 = True
                    r2 = True
                    r3 = True

                    if step['ShellScript'] != '':
                        r1 = shellhandler.run(step)
                    if step['Body'] != '':
                        r2 = casehandler.run(step)
                    if step['DQL'] != '':
                        r3 = sqlhandler.run(step)
                    step_run_result = r1 and r2 and r3
                    if step_run_result is False:
                        case_run_result = False

                    step_run_log = get_sio().getvalue()
                    step_end_time = datetime.datetime.now()
                    step_duration = step_end_time - step_start_time
                    temp_dict = {'step_name': step['CaseStep'],
                                 'start_time': step_start_time,
                                 'end_time': step_end_time,
                                 'duration': step_duration,
                                 'run_result': step_run_result,
                                 'run_log': step_run_log}
                    steps_run_detail.append(temp_dict)
                    if step_run_result:
                        count_success_steps += 1
                    else:
                        count_fail_steps += 1
                    count_all_steps += 1

            if count_all_steps == 0:  # no step run in this case
                logger.info('SKIP\n')
                continue

            case_end_time = datetime.datetime.now()
            case_duration = case_start_time - case_end_time
            case_temp_dict = {
                'case_name': case['CaseName'],
                'start_time': case_start_time,
                'end_time': case_end_time,
                'duration': case_duration,
                'run_result': case_run_result,
                'count_all_steps': count_all_steps,
                'count_success_steps': count_success_steps,
                'count_fail_steps': count_fail_steps,
                'step_detail': steps_run_detail
            }
            test_result_detail.append(case_temp_dict)

            if case_run_result:
                count_success_cases += 1
            else:
                count_fail_cases += 1
            count_all_cases += 1

    test_result_summary['test_end_time'] = datetime.datetime.now()
    test_result_summary['test_duration'] = test_result_summary['test_end_time'] - test_result_summary['test_start_time']
    test_result_summary['count_all_cases'] = count_all_cases
    test_result_summary['count_success_cases'] = count_success_cases
    test_result_summary['count_fail_cases'] = count_fail_cases

    shellhandler.close()
    sqlhandler.close()

    r.generate_report(test_result_summary, test_result_detail)
```

### 2.8 *Generate Test Report

Generate test report from scratch is not that easy, took almost half of my time on this project. See here --> [][]

## 3 Todo List

* [x] add readme file
* [ ] replace `re` with `json`
* [ ] support `get` method
* [ ] support `DML`
* [ ] add more code annotation
* [ ] format testing log
* [ ] replace `xlrd` with `pandas`
* [ ] refactor the code in `case_helper.py`
* [ ] ! try `pytest` or `unittest`
* [ ] ! generate test report with [Allure][Allure]
* [ ] ! another mode: manage cases in `.py` or `.yaml`


[Configparser]:https://docs.python.org/3.8/library/configparser.html "https://docs.python.org/3.8/library/configparser.html"
[Paramiko]:http://www.paramiko.org/ "http://www.paramiko.org/"
[Requests]:https://docs.python-requests.org/en/master/ "https://docs.python-requests.org/en/master/"
[cx_Oracle]:https://oracle.github.io/python-cx_Oracle/ "https://oracle.github.io/python-cx_Oracle/"
[Logging]:https://docs.python.org/3.8/library/logging.html "https://docs.python.org/3.8/library/logging.html"
[Allure]:http://allure.qatools.ru/ "http://allure.qatools.ru/"
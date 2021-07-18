# A Data-driven API Autotest Tool Written in Python

- [A Data-driven API Autotest Tool Written in Python](#a-data-driven-api-autotest-tool-written-in-python)
  - [1 Introduction](#1-introduction)
  - [2 Code Review](#2-code-review)
    - [2.1 Handle Test Cases with Excel](#21-handle-test-cases-with-excel)
      - [2.1.1 Case Template](#211-case-template)
      - [2.1.2 Read Cases from Excel](#212-read-cases-from-excel)
    - [2.2 Handle Basic Parameters with Configparser](#22-handle-basic-parameters-with-configparser)
    - [2.3 Handle Shell Commands with Paramiko](#23-handle-shell-commands-with-paramiko)
    - [2.4 Handle Post Request with Requests](#24-handle-post-request-with-requests)
    - [2.5 Handle DQL with cx_Oracle](#25-handle-dql-with-cx_oracle)
    - [2.6 The Main Method Script](#26-the-main-method-script)
    - [2.7 Handle Log with Logging](#27-handle-log-with-logging)
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

Every function is implemented for specific requirements, it can not handle the `get` method because I don't need it for now, as I said, this is a simple tool, there is a long todo list.

All code here in this blog will be archived in `./my_site_root/code/some_sub_path/api-autotest-tool`, the code may have changed a lot if I am still working on it, that won't be updated here.

## 2 Code Review

### 2.1 Handle Test Cases with Excel

#### 2.1.1 Case Template

|CaseName|CaseStep|Run?|Method|URI|Port|Address|ContentType|ShellScript|Body|ExpectedData|ResponseParameter|DQL|ExpectedDQLData|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|case1|step1|y|post||||||
||step2|n|post||||||
||step3|y|post||||||
|case2|step1|y|post||||||
||step2|y|post||||||

The Excel template has a certain header in first row, from the second row, each line will be treated as a step in a case, each case should contain one step at least. You can also consider cases as test suites and steps as cases, no difference.

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

The `Body`, `ExpectedData` and `ResponseParameter` are a group. First the `Body` will be sent, after we got a response, the `parameter_handler` will check every `key:value` in `ExpectedData`, return a pass flag if it's indeed in the response or a fail if not, in the meantime, the `parameter_handler` will collect the value of the key in `ResponseParameter`, so you can use it with `${key}` after then(only in `Body`). By the way, in `ResponseParameter`, you can rename a parameter using `key:renamed_key`, this is helpful in the situation that we want to store many parameters with the same name.

Here is an instance:

First step:
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

After the first step, we got a parameter `token1` that can be used in the next step, just assume that `token1=ALSKDJFLASKDJFLKLSKDJFlkjdlskafjLKDHLGKASHD`, write next step `Body` like this:

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
        'Port': sheet_object.row_values(row_number)[get_column_index(sheet_object, 'Port')],  # 9192.0
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
# case_list_dic = [
#   case1,
#   case2,
#   case3 = {
#     'CaseName':case_name,
#     'CaseSteps':[
#       step1,
#       step2,
#       step3 = {
#         'CaseStep':step_name,
#         'Method':'post',
#         'Body':...,
#         'Run?':'y',
#         'Key':'Value',
#         ...and so on
#       }
#     ]
#   }
# ]
```

### 2.2 Handle Basic Parameters with [Configparser][Configparser]

With the help of `configparser`, it's easy to handle a `config.ini` out of the code. Pay attention to the comments in `[database]` section, about 'oracle instant client'.

### 2.2.1 Config File Template

```python
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

### 2.2.2 Read Conifg

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


### 2.3 Handle Shell Commands with [Paramiko][Paramiko]

```python
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

### 2.4 Handle Post Request with [Requests][Requests]

```python
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

Here we meet the `` and ``,

### 2.5 Handle DQL with [cx_Oracle][cx_Oracle]

### 2.6 Handle Log with [Logging][Logging]

### 2.7 The Main Method Script


### 2.8 *Generate Test Report


[Configparser]:https://docs.python.org/3.8/library/configparser.html "https://docs.python.org/3.8/library/configparser.html"
[Paramiko]:http://www.paramiko.org/ "http://www.paramiko.org/"
[Requests]:https://docs.python-requests.org/en/master/ "https://docs.python-requests.org/en/master/"
[cx_Oracle]:https://oracle.github.io/python-cx_Oracle/ "https://oracle.github.io/python-cx_Oracle/"
[Logging]:https://docs.python.org/3.8/library/logging.html "https://docs.python.org/3.8/library/logging.html"

## 3 Todo List
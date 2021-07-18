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
   1. execute shell commands and print the result
   2. post the request and verify the response
   3. execute the SQL and verify the result
   4. generate an all-in-one(html, js, css) test report



## 2 Code Review

### 2.1 Handle Test Cases with Excel

#### 2.1.1 Case Template
#### 2.1.2 Read Cases from Excel

### 2.2 Handle Basic Parameters with [Configparser][Configparser]

### 2.3 Handle Shell Commands with [Paramiko][Paramiko]

### 2.4 Handle Post Request with [Requests][Requests]

### 2.5 Handle DQL with [cx_Oracle][cx_Oracle]

### 2.6 The Main Method Script

### 2.7 Handle Log with [Logging][Logging]

### 2.8 *Generate Test Report


[Configparser]:https://docs.python.org/3.8/library/configparser.html "https://docs.python.org/3.8/library/configparser.html"
[Paramiko]:http://www.paramiko.org/ "http://www.paramiko.org/"
[Requests]:https://docs.python-requests.org/en/master/ "https://docs.python-requests.org/en/master/"
[cx_Oracle]:https://oracle.github.io/python-cx_Oracle/ "https://oracle.github.io/python-cx_Oracle/"
[Logging]:https://docs.python.org/3.8/library/logging.html "https://docs.python.org/3.8/library/logging.html"

## 3 Todo List
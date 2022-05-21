# Import Testcases From Excel to Testlink
*Posted on 2021.06.23 by [Pengwei Zhang](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)* 

<!-- TOC -->

* [Main Procedure](#main-procedure)
* [Testcase Template](#testcase-template)
* [Dependencies & Config](#dependencies--config)
* [Code Review](#code-review)
    * [Handle Test Cases](#handle-test-cases)
    * [Init Test Porject](#init-test-porject)
    * [Handle Test Suite](#handle-test-suite)
    * [Import Test Cases](#import-test-cases)
* [reference](#reference)

<!-- /TOC -->

Write test cases in Excel then import them to Testlink using this script. That is an acceptable way to manage test case at present. Code in this blog will be archived in `../code` subfolder, the code may have been updated since this blog was posted.

## Main Procedure

1. Connect to testlink using the dev-Key
2. Get the project or create it if not exist
3. Get test cases from excel
4. Get suite path from test case
5. Create test suite (if the suite not exist) and import test case


## Testcase Template

|suite_path|casename|summary|precondition|step|excepted|execution_type|priority|author|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|suite1|case1|summary1|precondition1|step1|excepted1|manual|high|zhangpw|
|suite2/suite2-1|case2|summary2|precondition2|step1|excepted1|manual|high|zhangpw|
|suite2/suite2-2|case3|summary3|precondition3|step1|excepted1|manual|medium|zhangpw|
|suite3/suite3-1|case4|summary4|precondition4|step1|excepted1|automated|medium|zhangpw|
|suite3/suite3-1|case5|summary5|precondition5|step1|excepted1|automated|low|zhangpw|
|suite3/suite3-2/3-2-1|case6|summary6|precondition6|step1|excepted1|automated|high|zhangpw|


## Dependencies & Config

```python
# this script runs well under python3.8
import testlink as tl
import xlrd  # 1.2.0 version

filepath = r"../input/testcase_template_2.xlsx"
sheets = ['suitename1']

TESTLINK_SERVER_URL = "http://xxxx:xxx/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
TESTLINK_API_KEY = "xxxxxxxxxxxxxxxxxxxx"
PROJECT_NAME = "TEST-PROJECT"
TESTCASE_PREFIX = "pwz-auto-"
```

Note that the latest version of xlrd can't deal with `xlsx` format, here we need 1.2.0 version (can be installed with command `pip install xlrd==1.2.0` and `pip uninstall xlrd` should be run if the latest version had been install), what's more, xlrd is incompatible with python3.9 (cause `AttributeError: 'ElementTree' object has no attribute 'getiterator'`), 3.8 is fine.

You can change the `filepath`, but the template file is specific, as shown [here](#testcase-template).

The `sheets` points to all sheets you want to run in your excel, set `sheets` at `['sheet1', 'sheet2']` if sheet2's steps need the result of sheet1 as its input.

`/testlink/lib/api/xmlrpc/v1/xmlrpc.php` in `TESTLINK_SERVER_URL` is a fixed value, just replace `xxxx:xxx` with your `ip_address:port_number`.

`TESTLINK_API_KEY` can be generate in `testlink_homepage/my_setting/API_interface`.


## Code Review

### Handle Test Cases

```python
import xlrd

def read_excel(file_path, sheet_name):
    """
    get test cases of specific sheet
    :param file_path: Excel path
    :param sheet_name: sheet name which you want to run
    :return: case_list_dic
    """

    def get_column_index(sheet, column_name):
        """
        get the index of specific column in specific sheet
        :param sheet: sheet to deal with
        :param column_name: column name
        :return: int
        """
        column_index = None
        for i in range(sheet.ncols):
            if sheet.cell_value(0, i) == column_name:
                column_index = i
                break
        return column_index

    case_list_dic = []
    try:
        book = xlrd.open_workbook(file_path)
    except Exception as error:
        logger.error('Open excel error: ' + str(error))
        return error
    else:
        sheet = book.sheet_by_name(sheet_name)
        rows = sheet.nrows
        for i in range(1, rows):  # ignore the first row
            case_dic = {
                'suite_path': sheet.row_values(i)[get_column_index(sheet, 'suite_path')],
                'casename': sheet.row_values(i)[get_column_index(sheet, 'casename')],
                'precondition': sheet.row_values(i)[get_column_index(sheet, 'precondition')],
                'step': sheet.row_values(i)[get_column_index(sheet, 'step')],
                'excepted': sheet.row_values(i)[get_column_index(sheet, 'excepted')],
                'execution_type': sheet.row_values(i)[get_column_index(sheet, 'execution_type')],
                'author': sheet.row_values(i)[get_column_index(sheet, 'author')],
                'priority': sheet.row_values(i)[get_column_index(sheet, 'priority')],
                'summary': sheet.row_values(i)[get_column_index(sheet, 'summary')]
            }
            case_list_dic.append(case_dic)
    return case_list_dic
```


### Init Test Porject

```python

def init_test_project(testlink_api):
    # def get_projectid_by_name(tlapi, name):
    #     projects = tlapi.getProjects()
    #     for project in projects:
    #         if project["name"] == name:
    #             return project["id"]
    #     return -1

    def get_project_by_name(tlapi, name):
        try:
            project = tlapi.getTestProjectByName(name)
        except Exception as e:
            print(e)
            return -1
        else:
            return project

    project = get_project_by_name(testlink_api, PROJECT_NAME)
    if project == -1:  # project not exist, create one
        print("no project found, creating...")
        try:
            testlink_api.createTestProject(PROJECT_NAME, TESTCASE_PREFIX)
        except Exception as e:
            print("create fail : ")
            print(e)
        else:
            project = get_project_by_name(testlink_api, PROJECT_NAME)
            print("create project {0} (ID = {1}) successful.".format(PROJECT_NAME, project['id']))
            return project
    else:
        print(project)
        return project

```


### Handle Test Suite

```python

def get_or_create_suite_by_name_and_parentid(suite_name, project_id, parent_suite_id, TESTCASE_PREFIX):
    def find_suite_in_all_suites():
        all_suites = tlapi.getTestSuite(suite_name, TESTCASE_PREFIX)
        # print(all_top_suites)
        for suite in all_suites:
            if suite['name'] == suite_name and suite['parent_id'] == parent_suite_id:
                return suite
        return -1

    if parent_suite_id == '':  # meet a top suite
        all_top_suites = tlapi.getFirstLevelTestSuitesForTestProject(project_id)
        print(all_top_suites)
        for suite in all_top_suites:
            if suite['name'] == suite_name:
                return suite
        # find none, create one
        try:
            print("creating top suite ({0}) ...".format(suite_name))
            suite_add_info = tlapi.createTestSuite(project_id, suite_name, "test_detail")[0]
        except Exception as e:
            print(e)
        else:
            print("create suite successful, suite = {0}".format(suite_add_info))
            all_top_suites = tlapi.getFirstLevelTestSuitesForTestProject(project_id)
            print(all_top_suites)
            for suite in all_top_suites:
                if suite['name'] == suite_name:
                    return suite
    else:  # not a top suite
        try:
            all_suites_with_the_name = tlapi.getTestSuite(suite_name, TESTCASE_PREFIX)
        except Exception as e:  # nothing found, just create it
            print("no suite found")
            print(e)
            try:
                print("creating suite...")
                tlapi.createTestSuite(project_id, suite_name, "test_detail", parentid=parent_suite_id)
            except Exception as e:
                print(e)
            else:
                suite = find_suite_in_all_suites()
                if suite != -1:
                    print("create suite successful, suite = {0}".format(suite))
                    return suite
                else:
                    raise Exception("fail to create the suite!!")
        else:  # found something, but may not what we want
            for suite in all_suites_with_the_name:
                if suite["parent_id"] == parent_suite_id:
                    print("got {0} = {1}".format(suite_name, suite))
                    return suite  # suite found
            # oops
            try:
                print("creating suite {0} with parent id {1} ...".format(suite_name, parent_suite_id))
                tlapi.createTestSuite(project_id, suite_name, "test_detail", parentid=parent_suite_id)
            except Exception as e:
                print(e)
            else:
                suite = find_suite_in_all_suites()
                if suite != -1:
                    print("create suite successful, suite = {0}".format(suite))
                    return suite
                else:
                    raise Exception("fail to create the suite!!")
```


### Import Test Cases

```python
def import_test_cases(tlapi, project_id, cases):
    count = {'succeed': 0, 'failed': 0}
    for case in cases:
        # print("-----------------" + case["suite_path"])
        suite_path = case["suite_path"]
        parent_suite = {}
        for i in range(0, suite_path.count("/") + 1):
            _index = suite_path.find("/")

            if _index != -1:
                _suite_name = suite_path[:_index]
                suite_path = suite_path[_index + 1:]
            else:
                _suite_name = suite_path
            # print(_suite_name)

            if i == 0:
                parent_suite["id"] = ""
            if parent_suite["id"] == "":
                print(_suite_name + " is the top level suite")
                # TODO : GET SUITE OR CREATE ON IF NOT EXIST WITH SUITE NAME
                try:
                    suite = get_or_create_suite_by_name_and_parentid(_suite_name, project_id, "", TESTCASE_PREFIX)
                    print(suite)
                except Exception as e:
                    print("*" * 50)
                    print(e)
            else:
                print(_suite_name + " is the subsuite under parent " + parent_suite["name"])
                # TODO : GET SUITE OR CREATE ON IF NOT EXIST WITH SUITE NAME AND PARENT SUITE(ID)
                try:
                    suite = get_or_create_suite_by_name_and_parentid(_suite_name, project_id, parent_suite["id"], TESTCASE_PREFIX)
                    print(suite)
                except Exception as e:
                    print("#" * 80)
                    print(e)
            parent_suite = suite

        # create suite done, now create test case
        print('under the path {}'.format(case["suite_path"]))
        print('!!!!! create test case under {}'.format(parent_suite['name']))

        """        
        createTestCase: Create a test case
        positional args: testcasename, testsuiteid, testprojectid, authorlogin,
                         summary
        optional args : steps, preconditions, importance, executiontype, order,
                        internalid, checkduplicatedname, actiononduplicatedname,
                        status, estimatedexecduration
                        
        argument 'steps' will be set with values from .stepsList, 
        - when argsOptional does not include a 'steps' item
        - .stepsList can be filled before call via .initStep() and .appendStep()
        
        otherwise, optional arg 'steps' must be defined as a list with 
        dictionaries , example
            [{'step_number' : 1, 'actions' : "action A" , 
                'expected_results' : "result A", 'execution_type' : 0},
                 {'step_number' : 2, 'actions' : "action B" , 
                'expected_results' : "result B", 'execution_type' : 1},
                 {'step_number' : 3, 'actions' : "action C" , 
                'expected_results' : "result C", 'execution_type' : 0}]
            
        possible values for optional arguments testlink/cfg/const.inc.php
        importance:    1 (low)    2 (medium) 3 (high)   
        status:        1 (draft)             2 (readyForReview)
                       3 (reviewInProgress)  4 (rework) 
                       5 (obsolete)          6 (future)
                       7 (final)
        executiontype: 1 (Manual)            2 (Automated)
        """
        switcher = {
            "low": 1,
            "medium": 2,
            "high": 3,
            "manual": 1,
            "automated": 2
        }
        c_name = case['casename']
        c_precondition = case['precondition']
        c_step = case['step']
        c_excepted = case['excepted']
        c_author = case['author']
        c_summary = case['summary']
        # c_steps = list(zip(case['step'].split('\n'), case['excepted'].split('\n')))
        c_steps = [{'step_number': 1, 'actions': c_step.replace("\n", "<br>"),
                    'expected_results': c_excepted.replace("\n", "<br>"), 'execution_type': 0}]  # ONLY ONE STEP
        c_importance = switcher.get(case['priority'])
        c_execution_type = switcher.get(case['execution_type'])
        try:
            tlapi.createTestCase(c_name, parent_suite['id'], project_id, c_author, c_summary, c_steps,
                                 preconditions=c_precondition, importance=c_importance, executiontype=c_execution_type)
        except Exception as e:
            print(e)
            count['failed'] += 1
        else:
            count['succeed'] += 1
    return count
```

## reference

[https://github.com/orenault/TestLink-API-Python-client/blob/master/example/TestLinkExampleGenericApi.pyj](https://github.com/orenault/TestLink-API-Python-client/blob/master/example/TestLinkExampleGenericApi.py)  
[https://blog.csdn.net/weixin_41576586/article/details/89551395](https://blog.csdn.net/weixin_41576586/article/details/89551395)
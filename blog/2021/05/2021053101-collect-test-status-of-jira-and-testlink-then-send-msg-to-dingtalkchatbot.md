# 获取Jira与Testlink测试概况并推送消息到钉钉机器人
*2021053101-collect-test-status-of-jira-and-testlink-then-send-msg-to-dingtalkchatbot*  
*Posted on 2021.05.31 by [Pengwei Zhang](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*  


## JIRA数据获取

JQL是JIRA官方提供的高级搜索工具，与SQL语法没差别，熟悉一下相关字段的定义即可上手。

```python
from jira import JIRA

def login_jira_and_get_bug_status(export_file):
    """
    通过JIRA官方API登录获取缺陷数据，写入到指定文件中
    
    :param export_file: 数据导出文件
    :return:
    """
    # JIRA_URL = "http://XXX.XXX.XXX.XXX:XXXX"  # 内网
    JIRA_URL = "http://XXX.XXX.XXX.XXX:XXXX"  # 外网
    JIRA_USERNAME = "USERNAME"
    JIRA_PASSWORD = "PASSWORD"

    def print_all_project_info(_jira):
        for _project in _jira.projects():
            print(_project.key, _project.name, _project.id)

    jira = JIRA(JIRA_URL, basic_auth=(JIRA_USERNAME, JIRA_PASSWORD))
    # print_all_project_info(jira)
    project = jira.project('CMBIRS')
    count_new_today = jira.search_issues(
        'project = "{0}" and created > "-12h"'.format(project.name), maxResults=-1)
    count_all = jira.search_issues('project = "{0}"'.format(project.name), maxResults=-1)
    count_not_handle = jira.search_issues(
        'project = "{0}" AND status in ("In Progress", Reopened, New, REJECTED)'.format(project.name), maxResults=-1)
    count_not_verify = jira.search_issues(
        'project = "{0}" AND status in ("In Progress", Reopened, Resolved, New, REJECTED) AND resolution = 已解决'.format(
            project.name), maxResults=-1)

    print("今日新增 = " + str(len(count_new_today)))
    print("缺陷总数 = " + str(len(count_all)))
    print("尚未处理 = " + str(len(count_not_handle)))
    print("尚未回归 = " + str(len(count_not_verify)))
    export_file.write("今日新增 = " + str(len(count_new_today)) + "\n")
    export_file.write("缺陷总数 = " + str(len(count_all)) + "\n")
    export_file.write("尚未处理 = " + str(len(count_not_handle)) + "\n")
    export_file.write("尚未回归 = " + str(len(count_not_verify)) + "\n")

```


## TESTLINK数据获取

Testlink的python包封装的功能与本次的需求不是很相符（也可能是我没仔细读文档漏掉了），下面的方法里绕了个圈子才获取到当前测试计划中用例的执行情况。计算进度是临时加的函数，图方便直接到excel中复制了计划进度过来与当前进度做差。

`TESTLINK_SERVER_URL`为访问Testlink接口的固定地址，此地址可访问的前提是服务器配置了允许通过API访问，默认情况下应该是开着的。`TESTLINK_API_KEY`为访问TESTLINK需要的token，在个人设置中心可以生成。项目当前测试计划下面只有一个测试版本，所以代码里涉及到测试版本的地方直接调用了`builds[0]`，多个测试版本的情况下对`build_id`处理需要调整。`SUITES_NAME`定义了需要进行数据统计的一级模块名称，这里如此处理是由于测试计划中仅包含该项目下的部分测试用例，不需要也不应该循环把所有SUITE的数据输出。

```python
import testlink

def login_testlink_and_get_case_status(export_file):
    """
    通过TESTLINK官方API登录并获取数据，写入到指定文件中

    :param export_file: 数据导出文件
    :return:
    """
    # TESTLINK_SERVER_URL = "http://XXX.XXX.XXX.XXX:XXXX/testlink/lib/api/xmlrpc/v1/xmlrpc.php"  # 内网
    TESTLINK_SERVER_URL = "http://XXX.XXX.XXX.XXX:XXXX/testlink/lib/api/xmlrpc/v1/xmlrpc.php"  # 外网
    TESTLINK_API_KEY = "bdfabc369495f0cbb93a2be883bd3ab0"
    PROJECT_NAME = "XXXXXX"
    TESTPLAN_NAME = "自动化测试"
    SUITES_NAME = ("客户管理", "客户资金管理", "大额操作管理", "操作管理", "交易管理", "费率管理", "抵押品管理", "对账", "报表管理")

    def print_all_project_info(tlapi):
        projects = tlapi.getProjects()
        for project in projects:
            # print(project)
            print(project["id"], project["name"])

    def get_projectid_by_name(tlapi, name):
        projects = tlapi.getProjects()
        for project in projects:
            if project["name"] == name:
                return project["id"]
        return -1

    def get_testplanid_by_project_id_and_planname(tlapi, project_id, planname):
        testplans = tlapi.getProjectTestPlans(project_id)
        for testplan in testplans:
            if testplan["name"] == planname:
                return testplan["id"]
        return -1

    def calculate_progress(_progress):
        """计算当前进度与预期进度的差值"""
        _current_date = time.strftime("%Y%m%d", time.localtime())
        progress_goal = {"20210527": 0.484,
                         "20210528": 0.5007,
                         "20210529": 0.5007,
                         "20210530": 0.5007,
                         "20210531": 0.5173,
                         "20210601": 0.534,
                         "20210602": 0.5506,
                         "20210603": 0.5673,
                         "20210604": 0.5839,
                         "20210605": 0.5839,
                         "20210606": 0.5839,
                         "20210607": 0.6005,
                         "20210608": 0.6172,
                         "20210609": 0.6338,
                         "20210610": 0.6505,
                         "20210611": 0.6671,
                         "20210612": 0.6671,
                         "20210613": 0.6671,
                         "20210614": 0.6671,
                         "20210615": 0.6838,
                         "20210616": 0.7004,
                         "20210617": 0.7171,
                         "20210618": 0.7337,
                         "20210619": 0.7337,
                         "20210620": 0.7337,
                         "20210621": 0.7503,
                         "20210622": 0.767,
                         "20210623": 0.7836,
                         "20210624": 0.8003,
                         "20210625": 0.8169,
                         "20210626": 0.8169,
                         "20210627": 0.8169,
                         "20210628": 0.8336,
                         "20210629": 0.8502,
                         "20210630": 0.8668,
                         "20210701": 0.8835,
                         "20210702": 0.9001,
                         "20210703": 0.9001,
                         "20210704": 0.9001,
                         "20210705": 0.9168,
                         "20210706": 0.9334,
                         "20210707": 0.9501,
                         "20210708": 0.9667,
                         "20210709": 0.9834,
                         "20210710": 0.9834,
                         "20210711": 0.9834,
                         "20210712": 1}
        return _progress - progress_goal[_current_date]

    # 登录并根据前面参数依次定位到项目->测试计划->测试版本
    tlapi = testlink.TestlinkAPIGeneric(TESTLINK_SERVER_URL, TESTLINK_API_KEY)
    project_id = get_projectid_by_name(tlapi, PROJECT_NAME)
    print("PROJECT: " + PROJECT_NAME + " Project id = " + project_id)
    testplan_id = get_testplanid_by_project_id_and_planname(tlapi, project_id, TESTPLAN_NAME)
    print("TESTPLAN:" + TESTPLAN_NAME + " Testplan id = " + testplan_id)
    builds = tlapi.getBuildsForTestPlan(testplan_id)
    # print_all_top_testsuites_by_projectid(tlapi, project_id)
    # print_all_testsuites_by_planid(tlapi, testplan_id)
    # print(builds[0]['name'] + " build id = " + builds[0]['id'])

    """
    NOTE:TestLink用例执行情况枚举值
    # IN FILE custom_config.inc.php
    # $tlCfg->results['status_code'] = array (
    # "failed" => 'f',
    # "blocked" => 'b',
    # "passed" => 'p',
    # "not_run" => 'n',
    # "not_available" => 'x',
    # "unknown" => 'u',
    # "all" => 'all'
    # );
    """
    # 按执行情况获取测试计划（版本）下的所有测试用例
    cases_all = tlapi.getTestCasesForTestPlan(testplan_id)
    cases_passed = tlapi.getTestCasesForTestPlan(testplan_id, buildid=builds[0]['id'], executestatus='p')
    cases_failed = tlapi.getTestCasesForTestPlan(testplan_id, buildid=builds[0]['id'], executestatus='f')
    cases_blocked = tlapi.getTestCasesForTestPlan(testplan_id, buildid=builds[0]['id'], executestatus='b')
    count_executed = len(cases_blocked) + len(cases_passed) + len(cases_failed)
    count_not_run = len(cases_all) - count_executed
    progress = count_executed / (count_executed + count_not_run)
    print("测试版本：" + builds[0]['name'] + " 已执行：" + str(count_executed) + " 待执行：" + str(count_not_run))
    export_file.write("测试版本：" + builds[0]['name'] + " 已执行：" + str(count_executed) + " 待执行：" + str(count_not_run) + "\n")

    # 按模块获取测试用例并对用例执行情况进行计数
    print("各个模块执行情况：")
    export_file.write("各个模块执行情况：" + "\n")
    suites = tlapi.getTestSuitesForTestPlan(testplan_id)
    for suite in suites:
        count_passed = 0
        count_blocked = 0
        count_failed = 0
        count_not_run = 0
        if suite["name"] in SUITES_NAME:
            cases = tlapi.getTestCasesForTestSuite(suite["id"])
            # print(cases)
            for case in cases:
                case_id = case["id"]
                try:
                    case_info = cases_all[case_id]
                    case_exec_status = case_info[0]["exec_status"]
                    if case_exec_status == "n":
                        count_not_run += 1
                    elif case_exec_status == "p":
                        count_passed += 1
                    elif case_exec_status == "b":
                        count_blocked += 1
                    elif case_exec_status == "f":
                        count_failed += 1
                except:
                    # print("测试计划中无 id={0} 对应用例".format(case_id))
                    pass
            
            _count_executed = count_passed + count_blocked + count_failed
            _count_not_run = count_not_run
            print("> " + suite["name"] + " id=" + suite["id"] + "\t" + "已执行：" + str(_count_executed) + "  待执行：" + str(_count_not_run))
            export_file.write("> " + suite["name"] + "\t" + "已执行：" + str(_count_executed) + "  待执行：" + str(_count_not_run) + "\n")

    # 计算并输入当前测试用例的执行进度
    delta = calculate_progress(progress)
    sign = ''
    if delta > 0:sign = '+'
    print("当前进度 = %2.2f%%" % (progress * 100) + "  较预期：" + sign + " %2.2f%%" % (delta * 100))
    export_file.write("当前进度：%2.2f%%" % (progress * 100) + "  较预期：" + sign + "%2.2f%%" % (delta * 100) + "\n")

```


## 推送消息到钉钉机器人

到钉钉群中新建一个自定义机器人后拿到webhook，也就是下面的`ROBOT_URL`，然后即可通过官方的python包傻瓜式发消息。`chatbot`这个包似乎很久没有维护了，Python2环境下会有小问题。这篇博客是脚本写完后好几天才整理的，这里第一个参数为啥要传文件路径而不是直接传要发送的消息，第二个参数为什么写上去了后面又把它晾那里没有用起来，不记得了，就这样吧。

```python
import dingtalkchatbot.chatbot as cb

def send_to_dingtalk_robot(msg, url=''):
    """
    根据日期获取当日数据，推送到钉钉机器人

    :param msg: 存储待发送信息的文件路径
    :param url: 钉钉机器人webhook
    :return:
    """
    ROBOT_URL = "https://oapi.dingtalk.com/robot/send?access_token=XXX"  # 测试群
    # ROBOT_URL = "https://oapi.dingtalk.com/robot/send?access_token=XXX"  # 工作群
    with open(msg, 'r') as f:
        datas = f.read()
        # print("当日测试情况：\n" + datas)
        if len(datas) != 0:
            bot = cb.DingtalkChatbot(ROBOT_URL)
            bot.send_text(msg=datas)
        else:
            print("empty msg file")

```

## 定时获取数据并推送消息

服务器由于测试需要，会频繁变更系统时间，所以此处又添加了一个方法`getBeijinTime()`获取网络时间（直接在网上找来的），再通过网络时间来实现定时发送。

*如果服务器也不联网，那这里如何实现每天的定时任务？在初始某个时刻开始累加CPU时间？可以开一开脑洞。*

```python
import time
import requests

def getBeijinTime():
    """
    获取北京时间
    这个方法来自这里：https://www.cnblogs.com/xiexiaokui/p/14217254.html
    """
    # HTTP客户端运行的浏览器类型的详细信息。通过该头部信息，web服务器可以判断到当前HTTP请求的客户端浏览器类别。
    hea = {'User-Agent': 'Mozilla/5.0'}  # 站点服务器认为自己（浏览器）兼容Moailla的一些标准
    # 设置访问地址，我们分析到的；
    url = r'http://time1909.beijing-time.org/time.asp'
    # 用requests get这个地址，带头信息的；
    r = requests.get(url=url, headers=hea)
    # 检查返回的通讯代码，200是正确返回；
    if r.status_code == 200:
        # 定义result变量存放返回的信息源码；
        result = r.text
        # 通过;分割文本；
        data = result.split(";")
        # 以下是数据文本处理：切割、取长度
        year = data[1][len("nyear") + 3: len(data[1])]
        month = data[2][len("nmonth") + 3: len(data[2])]
        day = data[3][len("nday") + 3: len(data[3])]
        # wday = data[4][len("nwday")+1 : len(data[4])-1]
        hrs = data[5][len("nhrs") + 3: len(data[5])]
        # hrs = data[5][len("nhrs") + 3: len(data[5]) - 1] #不需要减1
        minute = data[6][len("nmin") + 3: len(data[6])]
        sec = data[7][len("nsec") + 3: len(data[7])]
        # 这个也简单把切割好的变量拼到beijinTimeStr变量里；
        beijinTimeStr = "%s-%s-%s %s:%s:%s" % (year, month, day, hrs, minute, sec)
        ltime = time.strptime(beijinTimeStr, "%Y-%m-%d %H:%M:%S")  # 返回结果是一个结构体
        # ltime：time.struct_time(tm_year=2020, tm_mon=10, tm_mday=9, tm_hour=9, tm_min=32, tm_sec=39, tm_wday=4, tm_yday=283, tm_isdst=-1)
        return ltime

def is_18_clock():
    current_time = time.strftime('%H:%M:%S', getBeijinTime())
    print("current time is " + current_time)
    if current_time[:2] == "18":
        return True
    else:
        return False


def main():
    # current_date = time.strftime("%Y-%m-%d", time.localtime())  # 本地时间
    current_date = time.strftime('%Y-%m-%d', getBeijinTime())  # 网络时间
    filepath = "data/" + current_date + ".txt"

    with open(filepath, 'w') as f:
        f.write("=" * 15 + "缺陷概况" + "=" * 15 + "\n")
        login_jira_and_get_bug_status(f)
        f.write("=" * 36 + "\n\n")
        print()
        f.write("=" * 15 + "用例概况" + "=" * 15 + "\n")
        login_testlink_and_get_case_status(f)
        f.write("=" * 36 + "\n\n")
        # f.write("Timestamp # " + time.strftime("%Y.%m.%d %H:%M:%S", time.localtime()))  # 本地时间
        f.write("Timestamp # " + time.strftime('%Y-%m-%d %H:%M:%S', getBeijinTime()))  # 网络时间

    send_to_dingtalk_robot(filepath)


if __name__ == '__main__':
    while True:
        if is_18_clock():
            print("now run >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            main()
            print("run over >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
            time.sleep(3600)
        else:
            print("not the time --------------------------\n")
            time.sleep(3600)
```

## 潦草收尾

这个脚本已经超出预期的长度，之前没想让它放到服务器上一直跑，日志、错误处理都被省掉，实测一个网络超时整个脚本就会崩，不过秉着能用就行的原则暂时就写成这样不再多花费时间，以后有需要再完善。

代码里用了很多Print，像如下这样重写一下Print函数，也算是有日志了。

```python
import os

rewrite_print = print
def print(*arg):
    """
    重写print函数，向日志文件中输出
    这个重写copy自：https://blog.csdn.net/weixin_43046726/article/details/108999846
    """
    rewrite_print(*arg)
    output_dir = "log"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        # print('新建log文件夹')
    log_name = 'log.txt'  # 日志文件名称
    filename = os.path.join(output_dir, log_name)
    rewrite_print(*arg, file=open(filename, "a"))  # 写入文件
```

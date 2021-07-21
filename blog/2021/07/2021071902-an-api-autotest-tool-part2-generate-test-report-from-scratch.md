<!-- no toc -->
# An API Autotest Tool Part2: Generate Test Report from Scratch

*Posted on 2021.07.19 by [Pengwei Zhang](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)* 

*Inspired by the [HTMLTestRunner](http://tungwaiyip.info/software/HTMLTestRunner.html)*

- [An API Autotest Tool Part2: Generate Test Report from Scratch](#an-api-autotest-tool-part2-generate-test-report-from-scratch)
  - [How it looks](#how-it-looks)
  - [Code Summary](#code-summary)
  - [Html Templates](#html-templates)
    - [Report Template](#report-template)
    - [Summary Template](#summary-template)
    - [Case Template](#case-template)
    - [Step Template](#step-template)
    - [CSS Template](#css-template)
  - [The JS Function](#the-js-function)


## How it looks

Here is an example page --> [test-report-template.html](./2021071902-test-report-template.html)

![](./2021071902-report-screenshot.png)

## Code Summary

The basic idea of ​​generating a test report is：
1. Make some templates and set variables what we need in the templates
2. Collect relevant information during the test
3. Replace variables with relevant information
4. Join all the templates together to get the final test report

Additional works includes:
1. css code
2. js code to control the view
3. draw a pie chat in summary part of the report

```python
REPORT_TEMPLATE = """
    template
"""
SUMMARY_TEMPLATE = """
    template
"""
CASE_TEMPLATE = """
    template
"""
STEP_TEMPLATE = """
    template
"""
CSS_TEMPLATE = """
    template
"""

def generate_html_style():
    return CSS_TEMPLATE

def generate_html_summary(test_summary_dict):
    summary = SUMMARY_TEMPLATE % test_summary_dict
    return summary

def generate_html_body(test_summary_dict, case_detail_list):
    def get_step_list(steps):
        pass_step_list += STEP_TEMPLATE.format(...)
    # get test summary --> generate_html_summary(test_summary_dict)
    # get test detail --> for every case: get_step_list(steps)
    return body_summary, body_detail

def generate_report(test_summary_dict, case_detail_list):
    # get title
    # get css --> generate_html_style()
    # get html body --> generate_html_body(test_summary_dict, case_detail_list)
    html_dict = dict(
        title=title,
        style=css,
        body_summary=body_summary,
        body_detail=body_detail
    )
    report_html = REPORT_TEMPLATE % html_dict
    print report_html

```

## Html Templates

### Report Template

```html
<!DOCTYPE html>
<html>

<head>
<meta charset="utf-8"> 
<title>%(title)s</title>
<style>
    %(style)s
</style>
</head>

<body>
    <div class="report_body">
        <h1 class="report_title">%(title)s</h1>
        %(body_summary)s
        <div class="report_detail">
            <h2>Detail</h2>
            %(body_detail)s
        </div>
    </div>

    <!--script----------------------------------------------------------------------->
    <script>

    </script>
    <!--script---------------------------------------------------------------end----->

</body>
</html>
```

### Summary Template

```html
<div class="report_summary">
        <h2>Summary</h2>
        <div class="summary_text">
            <p>
                <span>Start: %(test_start_time)s</span><br/>
                <span>End:  %(test_end_time)s</span><br/>
                <span>Duration: %(test_duration)s</span><br/>
            </p>
            
            <div class="summary_chart">
                <img id="pie_chart" alt="" src="data:image/png;base64,%(pie_chart)s"/>
            </div>
            
            <p>
                <span>Total: %(count_all_cases)s</span>
                <span>Success: %(count_success_cases)s</span>
                <span>Fail: %(count_fail_cases)s</span>
            </p>
        </div>
</div>
```

### Case Template

```html
<!-- 
{0} = run_result (pass_case, fail_case)
{1} = case_name
{2} = count_all_steps
{3} = count_success_steps
{4} = count_fail_steps
{5} = step_detail 
-->
<div class="{0}">
    <div class="case_info" onclick="show_or_close_case_detail(this)">
        <span class="name">{1}</span>
        <span class="status">{2}/{3}/{4}</span>
    </div>
    <div class="step_list" style="display: none;">
    {5}
    </div>
</div>
```

### Step Template

```html
<!-- 
{0} = run_result
{1} = %(name)s
{2} = %(start)s
{3} = %(end)s
{4} = %(duration)s
{5} = step run log
-->
<div class="{0}">
    <div class="step_info" onclick="show_or_close_step_detail(this)">
        <span class="step_name">{1}</span>
        <span class="step_duration">Dur: {4}</span>
        <span class="step_end_time">End: {3}</span>
        <span class="step_start_time">Start: {2}</span>
    </div>
    <div class="step_detail">
    {5}
    </div>
</div>
```

### CSS Template

```css
/* --------------------------- basic setting --------------------------- */
.report_body {
    max-width: 900px;
    margin-right: auto;
    margin-left: auto;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
    font-size: 16px;
    line-height: 1.2;
}
h1 {
    padding-bottom: 2px;
    border-bottom: 3px solid #eaecef;
    background-color: #ffffff;
}
h2 {
    padding-bottom: 3px;
    border-bottom: 1px solid #f5f3f3;
    background-color: #ffffff;
}
/* --------------------------- basic setting --------------------------- */

/* --------------------------- report summary -------------------------- */
.report_summary {
    width: 98%;
    margin: 20px auto;
    height: 400px;
}

.summary_text {
    width: 98%;
    text-align: center;
    height: 100%;
}

.summary_chart {
    height: 60%;
}

#pie_chart {
    max-width: 100%;
    max-height: 100%;
    display: block;
    margin: auto;
}
/* --------------------------- report summary -------------------------- */


/* --------------------------- report detail --------------------------- */
.report_detail {
    width: 98%;
    margin: 40px auto;
}

.case_info,
.step_info{
    padding: 3px;
    border: 2px solid #ffffff;
}
.case_info:hover,
.step_info:hover{
    border-bottom: 1px solid #6d6d6d;
    cursor: pointer;
}
.case_info .status {
    float: right;
}

.pass_case,
.fail_case,
.error_case {
    border: 2px;
    padding: 3px;
    margin: 8px;
}

.pass_case .case_info { background-color: #f7f7f7; }
.fail_case .case_info { background-color: #f7f7f7; color: red;}
.error_case .case_info { background-color: #d55858; }

.step_list {
    display: none;
    width: 95%;
    margin: auto;
}

.pass_step,
.fail_step,
.error_step {
    padding: 3px;
    margin: 8px;
    font-size: 16px;
}

.fail_step .step_info {
     color: #ff0032;
}

.error_step .step_info {
    color: #cc0000;
}

.step_start_time,
.step_end_time,
.step_duration{
    float: right;
    margin:auto;
    font-size: 14px;
}

.step_detail {
    font-size: 14px;
    line-height: 1.2;
    width: 98%;
    margin: 4px auto;
    padding: 4px;
    border: 1px solid rgba(138, 176, 187, 0.25);
    white-space: pre-line;
    word-wrap: break-word;
    word-break: break-all;
}
/* --------------------------- report detail --------------------------- */
```

## The JS Function



```javascript
function show_or_close_case_detail(that) {
    var current_display_mode = that.parentNode.lastElementChild.style.display;
    var div_step_detail = that.parentNode.lastElementChild.getElementsByClassName('step_detail');
    if (current_display_mode != 'none') {
        that.parentNode.lastElementChild.style.display = 'none';
        for (let index = 0; index < div_step_detail.length; index++) {
            div_step_detail[index].style.display = 'none';
        }
    } else {
        that.parentNode.lastElementChild.style.display = 'block';
        for (let index = 0; index < div_step_detail.length; index++) {
            div_step_detail[index].style.display = 'none';
        }
    }
}
function show_or_close_step_detail(that) {
    var current_display_mode = that.parentNode.lastElementChild.style.display;
    if (current_display_mode != 'none') {
        that.parentNode.lastElementChild.style.display = 'None';
    } else {
        that.parentNode.lastElementChild.style.display = 'block';
    }
}
```
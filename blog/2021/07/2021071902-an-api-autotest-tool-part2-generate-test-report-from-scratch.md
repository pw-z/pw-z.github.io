# An API Autotest Tool Part2: Generate Test Report from Scratch

*Posted on 2021.07.19 by [Pengwei Zhang](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)* 

*Strongly inspired by the [HTMLTestRunner](http://tungwaiyip.info/software/HTMLTestRunner.html)*


The basic idea of ​​generating a test report is：
1. Make some templates and set variables what we need in the templates
2. Collect relevant information during the test
3. Replace variables with relevant information
4. Join all the templates together to get the final test report

Additional works includes:
1. Some CSS code 
2. Some JS code 

## Code Summary

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

## Html Template



### Report Template
### Summary Template
### Case Template
### Step Template
### CSS Template
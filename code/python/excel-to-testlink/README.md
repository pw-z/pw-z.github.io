# Testlink Cases Import Tool

说明  
* excel2xml.py
  * Testlink导入需要xml格式，此脚本将指定模板的excel转换为能够导入到testlink中的xml文件
  * 使用./imput/testcase_template_1.xlsx作为模板
* excel2testlink.py
  * 将Excel中的用例直接远程导入到testlink的指定项目中，项目及TestSuite不存在则直接创建，目前导入不会覆盖旧用例，同名用例也会被导进去
  * 使用./imput/testcase_template_2.xlsx作为模板
  * TODO:
    1. 将所有print语句换成logger
    2. 增加多步骤模式
    3. 注释补全
    4. 删除无用代码及注释
    
依赖  
* TestLink-API-Python-client
* xlrd 1.2.0
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def test1():
    response = """{"CODE":"200","code":"200","u":{"PHONENUM":"","STATUS":"1","USERNOTE":"","ENTITY_ID":"999",
    "PASSWORD":"143434C378479718","ACCTION":"0","PWD_EXPIRY":"","USERID":"143374","USERNAME":"管理员","CREATE_TIME":"",
    "EMAIL":"","CREATE_ID":"auto"},"permission":[{"MID":"PublicModule","MPARENTCODE":"","TEXT":"公共模块","LV_ORDER":"7",
    "MLEVEL":"1","MURL":"","ICON":"","VISIBLE":"","children":[{"MID":"UserManagement","MPARENTCODE":"PublicModule",
    "TEXT":"用户管理","LV_ORDER":"7-1","MLEVEL":"2","MURL":"","ICON":"","VISIBLE":"","children":[{
    "MID":"UserManagement_query","MPARENTCODE":"UserManagement","TEXT":"查询","LV_ORDER":"7-1-1","MLEVEL":"3",
    "MURL":"","ICON":"","VISIBLE":""},{"MID":"UserManagement_reset","MPARENTCODE":"UserManagement","TEXT":"重置",
    "LV_ORDER":"7-1-2","MLEVEL":"3","MURL":"","ICON":"","VISIBLE":""},{"MID":"UserManagement_add",
    "MPARENTCODE":"UserManagement","TEXT":"新增","LV_ORDER":"7-1-3","MLEVEL":"3","MURL":"","ICON":"","VISIBLE":""},
    {"MID":"UserManagement_update","MPARENTCODE":"UserManagement","TEXT":"修改","LV_ORDER":"7-1-4","MLEVEL":"3",
    "MURL":"","ICON":"","VISIBLE":""},{"MID":"UserManagement_del","MPARENTCODE":"UserManagement","TEXT":"用户注销",
    "LV_ORDER":"7-1-5","MLEVEL":"3","MURL":"","ICON":"","VISIBLE":""},{"MID":"UserManagement_pm",
    "MPARENTCODE":"UserManagement","TEXT":"分配岗位","LV_ORDER":"7-1-6","MLEVEL":"3","MURL":"","ICON":"","VISIBLE":""}]},
    {"MID":"InstitutionManagement","MPARENTCODE":"PublicModule","TEXT":"机构管理","LV_ORDER":"7-3","MLEVEL":"2",
    "MURL":"","ICON":"","VISIBLE":"","children":[{"MID":"InstitutionManagement_query",
    "MPARENTCODE":"InstitutionManagement","TEXT":"查询","LV_ORDER":"7-3-1","MLEVEL":"3","MURL":"","ICON":"",
    "VISIBLE":""},{"MID":"InstitutionManagement_reset","MPARENTCODE":"InstitutionManagement","TEXT":"重置",
    "LV_ORDER":"7-3-2","MLEVEL":"3","MURL":"","ICON":"","VISIBLE":""},{"MID":"InstitutionManagement_synch",
    "MPARENTCODE":"InstitutionManagement","TEXT":"同步","LV_ORDER":"7-3-3","MLEVEL":"3","MURL":"","ICON":"",
    "VISIBLE":""}]}]}],"SYS_REAL_DATETIME":"2021-03-20 23:08:06","enum":{"ENTITY_TYPE":[{"DESCRIBE":"全部","VALUE":"*",
    "DISPLAY_ORDER":"1","TYPE":"ENTITY_TYPE","DESC_OTHER":"ENTITY_TYPE","TYPE_DESC":"机构类型","MODULE":"",
    "UPDATE_TIME":"","SYS_STATUS":""},{"DESCRIBE":"总行","VALUE":"1","DISPLAY_ORDER":"2","TYPE":"ENTITY_TYPE",
    "DESC_OTHER":"ENTITY_TYPE","TYPE_DESC":"机构类型","MODULE":"","UPDATE_TIME":"","SYS_STATUS":""},{"DESCRIBE":"分行",
    "VALUE":"2","DISPLAY_ORDER":"3","TYPE":"ENTITY_TYPE","DESC_OTHER":"ENTITY_TYPE","TYPE_DESC":"机构类型","MODULE":"",
    "UPDATE_TIME":"","SYS_STATUS":""}]},
    "token":"63D343D324B3C3B324D3B3B3C3B31463243414C355a72792a9155eefe6c9de2675c3bc87",
     "TEXT":""}
     """

    re_s1 = r'{0} *: *\".*?\"'.format('"TEXT"')
    re_s2 = '("TEXT" *: *.*?)[,|)|}]'
    re_s3 = '({0} *: *.*?)'.format('"TEXT"') + '[,|)|}]'
    finds = re.finditer(re_s3, response)
    for p in finds:
        print(p.group(1))

def test2():
    res = """{"result":[{"ACC_ID":"000501","PRODUCT":"IRS","CUSTOMER_ID":"1120870002","LOCALSYS_ID":"00000284",
    "CUSTOMER_NAME_CH":"小小测试002","CUST_TRADECODE":"2087002","ACCOUNT_NO":"112220870002","ACCOUNT_NAME":"小小测试002",
    "MARGIN_NO":"220088770002","MARGIN_NAME":"小小测试002","CUSTOMER_TYPE":"legal","CERTIFICATE_TYPE":"C35",
    "CERTIFICATE_NO":"11230000-9","PROTOCOL_ID":"10101","PROTOCOL_NAME":"协议编号01","CONTACTS1":"cjh",
    "CONTACTS_PHONE1":"18800208064","CONTACTS2":"","CONTACTS_PHONE2":"","CONTACTS3":"","CONTACTS_PHONE3":"",
    "MANAGER1":"","MANAGER_PHONE1":"","MANAGER2":"","MANAGER_PHONE2":"","MANAGER3":"","MANAGER_PHONE3":"",
    "SIGN_STATUS":"0","MARGIN_STATUS":"1","RATE_STATUS":"1","CUSTOMER_STATUS":"0","CREATE_TIME":"2021-03-20 
    16:30:37","MODIFY_TIME":"2021-03-20 16:30:37","RN":"1"}],"total":1,"pageCount":1,"CODE":"200","code":"200",
    "SYS_REAL_DATETIME":"2021-03-22 15:14:39"} """

    p_origin = 'ACCOUNT_NO'
    r = r'("{0}" *: *.*?)'.format(p_origin) + '[,|)|}]'
    finds = re.finditer(r, res)
    for p in finds:
        print(p.group(1))
        s = p.group(1).split(':')
        find_value = s[1]
        print(find_value)
        if '"' in find_value:
            final_value = find_value[1:-1]  # deal with "key":"value"
        else:
            final_value = find_value  # deal with "key":value
        print(final_value)


if __name__ == '__main__':
    # test1()
    test2()

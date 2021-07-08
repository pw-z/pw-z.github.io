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


if __name__ == '__main__':
    test1()


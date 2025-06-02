#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser
from handler.ParameterHandler import Parameter


def test_configparser():
    cnf = configparser.ConfigParser()
    cnf.read('../config.ini')
    print(cnf.sections())
    for section in cnf.sections():
        print("options in " + section + ": ")
        print(cnf.options(section))

    for section in cnf.sections():
        print(cnf.items(section))

    uri = cnf.get('http', 'URI')
    port = cnf.get('http', 'Port')
    content_type = cnf.get('http', 'content_type')
    print(uri + '/' + port)
    print('content type: ' + content_type)

    excel_path = cnf.get('case', 'filepath')
    print('file path: ' + excel_path)

    ssh_hostname = cnf.get('shell', 'ssh_hostname')
    ssh_username = cnf.get('shell', 'ssh_username')
    ssh_password = cnf.get('shell', 'ssh_password')
    print('ssh ' + ssh_username + '@' + ssh_hostname + ' with pwd = ' + ssh_password)


if __name__ == '__main__':
    configpath = '../config.ini'
    para = Parameter(configpath)
    # print(para.get_parameter('uri'))
    # print(para.get_parameter('ur'))
    para.add_parameter('token', ' #TEST# ')
    # token = para.get_parameter('token')
    # print(token)

    # s = 'hello-${token}-7894654'
    # print(s.replace('${token}', para.get_parameter('token')))

    # s = para.flush_body_parameter('hello-${token}-7894${X}65${Y}4')
    # print(s)
    title = para.get_parameter('test_report_title')
    print(title)


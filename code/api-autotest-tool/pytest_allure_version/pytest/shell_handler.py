#!/usr/bin/env python
# -*- coding: utf-8 -*-


import paramiko  # ShellHandler
from log_helper import *
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
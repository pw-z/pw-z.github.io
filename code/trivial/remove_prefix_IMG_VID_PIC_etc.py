#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022
import os
import random
import sys
from PIL import Image
from PIL.ExifTags import TAGS



def traverse_and_process(path='.'):
    """
    遍历指定路径下所有文件，执行相关处理逻辑
    :param out_path:
    :param path:
    :return:
    """
    print("start traverse " + path)
    process_count = process_failed_count = count = 0
    path_queue = [path, ]
    fail_list = []
    while len(path_queue) > 0:
        current_path = path_queue.pop(0)
        print(f'\ncurrent path: {current_path}')

        dir_list = os.listdir(current_path)
        print(f'listdir: {dir_list}\n' + '-'*100)

        for d_or_f in dir_list:
            item = os.path.join(current_path, d_or_f)
            print(f'>>>>>>>>>>>>  {item}')
            if os.path.isdir(item):
                path_queue.append(item)
                print(f'---  new dir enqueue, queue length:{len(path_queue)}')
                continue

            # ============================================================
            # 编写处理逻辑
            # ============================================================
            try:
                # 特殊文件前缀重命名处理
                spec_prefix = ["VID_","B612咔叽_","Screenshot_"]
                for pre in spec_prefix:
                    if pre in d_or_f:
                        os.rename(item, os.path.join(current_path, f"{d_or_f[len(pre):]}"))
                        process_count += 1

            except Exception as e:
                process_failed_count += 1
                print(e)
                fail_list.append(item)

            count += 1
            # ============================================================
    print("="*50)
    print(f"total: {count} \nprocessed: {process_count}\nprocessed_failed: {process_failed_count}")

    if process_failed_count > 0:
        print("-"*50+"\nfail list:")
        for i in fail_list:
            print(i)


def get_field (img,field) :
    for (k,v) in img._getexif().items():
        if TAGS.get(k) == field:
            return v
    raise Exception("DateTimeOriginalNotFound")


if __name__ == '__main__':
    traverse_and_process()


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022
import os
import sys
from PIL import Image


def traverse_and_process(path='.'):
    """
    遍历指定路径下所有文件，执行相关处理逻辑
    :param out_path:
    :param path:
    :return:
    """
    print("start traverse " + path)
    process_count = count = 0
    path_queue = [path, ]
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
            if item.endswith('.png'):
                print(f'processing ... {item}')
                # img = Image.open(item)
                # img = img.convert("RGB")
                # img.save(item.replace('webp', 'jpg'), "JPEG", quality=100, progressive=True)

                process_count += 1
            count += 1
            # ============================================================
    print(f"total: {count} \n processed: {process_count}")


if __name__ == '__main__':
    traverse_and_process()


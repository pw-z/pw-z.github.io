#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022
import os
from PIL import Image


def convert_all_webp_to_jpg(path='.', out_path='./out'):
    """
    将指定路径下所有webp格式照片转换为jpg
    :param out_path:
    :param path:
    :return:
    """
    webp_count = count = 0
    os.makedirs(out_path) if not os.path.exists(out_path) else path
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

            if item.endswith('.webp'):
                print(f'!!!!!!!!!!!!!!!!!!!{item}')
                img = Image.open(item)
                img = img.convert("RGB")
                # 原路径保存
                # img.save(item.replace('webp', 'jpg'), "JPEG", quality=100, progressive=True)
                # 统一保存到out目录
                img.save(os.path.join(out_path, d_or_f.replace('webp', 'jpg')), "JPEG", quality=100, progressive=True)

                webp_count += 1
            count += 1
    print(f'[{count}] pics processed, convert [{webp_count}] webp to jpg.')


if __name__ == '__main__':
    convert_all_webp_to_jpg()


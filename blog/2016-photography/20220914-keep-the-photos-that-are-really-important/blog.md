# 保留真正重要的照片
*Posted on 2022.09.15 by [Pengwei](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*  

- [照片删减的依据](#照片删减的依据)
- [辅助工具与代码](#辅助工具与代码)
- [参考材料](#参考材料)

## 照片删减的依据

![](repo-statistic.png)

照片库规模最膨胀时逼近10万张，文件夹管理，用`年份/月份/日期及主题`三级目录的形式进行归档。近两年分批次精简库存，最近一轮清理两周前开始，当时规模有`24,356 Files, 684 Folders，435 GB`，现在两周过去数据变为`12,045 Files, 421 Folders, 179 GB`（上图），无论从照片数量还是整体体积上，都已经达到这轮清理开始时的目标——缩减一半。有些删上瘾了，这种清理工作没有个清晰的边界，2012~2022，11年跨度的照片算下来平均每年仍1000多张，我真的每年有1000多张值得保留的照片么？没有，还可以继续删下去。到什么时候为止呢？需要简单明确的观念与规则，从而保存或删除照片有依据。

作为摄影师或普通人有不同的核心诉求，列出可以检验对应诉求的问题，对问题的回答是否定的，那就不是一张值得保留的照片。结合近几天的清理工作，如下几个问题已经足够。诉求是最根本的，校验问题可以调整从而适配当时的想法。

* 作为摄影师，追求能打动人心的优秀摄影作品
  * 是否打动你自己乃至有分享的冲动？
  * 是否有信心将这张照片卖出去？
* 作为普通人，希望保留生活中值得纪念的场景
  * 你还记得这张照片拍摄时候的心情吗？
  * 将来你有一面墙贴满了各种照片，这会是其中一张吗？

这些问题作为照片管理时的依据，同样可以用在拍摄阶段。电子相机让拍摄成本大大降低，容易过度按快门，拍些有的没的最后还是都删掉了，制造了拍摄时与后期是双重的精力浪费。珍惜每一次快门，拿出一点摄影师的精神来。


## 辅助工具与代码

* 磁盘文件数据分析：[diskanalyzer](https://www.diskanalyzer.com/)
* RAW文件批量转换：[WidsMob ImageConvert](https://www.widsmob.com/imageconvert)(收费)

* 遍历所有文件执行自定义逻辑：

  ```python
  #!/usr/bin/env python
  # -*- coding: utf-8 -*-
  # created by pwz.wiki 2022
  import os
  import sys
  from PIL import Image


  def traverse_and_process(path='.'):
      """遍历指定路径下所有文件，执行相关处理逻辑"""
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
      print(f"total: {count} \nprocessed: {process_count}")


  if __name__ == '__main__':
      traverse_and_process()
  ```

## 参考材料

[My free-software photography workflow](https://blog.fidelramos.net/photography/photography-workflow#5-replication-with-syncthing)  

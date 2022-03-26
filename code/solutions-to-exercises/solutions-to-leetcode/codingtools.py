import os
import functools
import time


class CodingTool:
    @staticmethod
    def rename_files_in_python_style(path='.', no_upper=False):
        """
        重命名当前目录及所有子目录下的文件：
        1.字母大小写处理 2.小数点及空格转换为下划线 3.多个连续下划线合并为一个
        :param no_upper: 是否将所有大写字母转为小写
        :param path:
        :return:
        """
        dir_list = os.listdir(path)
        print(f'current listdir: {dir_list}')
        for d_or_f in dir_list:
            print(f'handling {d_or_f}')
            if d_or_f == 'codingtools.py':
                print('no need to rename')
                continue

            if os.path.isdir(os.path.join(path, d_or_f)):
                sub_path = os.path.join(path, d_or_f)
                print(f'deal with sub_path: {sub_path}')
                CodingTool.rename_files_in_python_style(sub_path, no_upper)
            elif os.path.isfile(os.path.join(path, d_or_f)):
                fname, ftype = os.path.splitext(d_or_f)
                if no_upper:
                    fname = fname.lower()
                    print('******' + fname)
                print(fname)
                fname = fname.replace('.', '_')
                fname = fname.replace(' ', '_')
                new_name = fname[0]
                for c in fname[1:]:
                    if c != '_' or new_name[-1] != '_':
                        new_name += c
                    print(new_name)

                new_name += ftype
                if new_name == d_or_f:
                    print('no need to rename')
                else:
                    os.rename(os.path.join(path, d_or_f), os.path.join(path, new_name))
                    print(f'rename <{d_or_f}> to <{new_name}>')
            else:
                return

        def performance_analyzer(func):
            """计算执行耗时
            :param func:
            :return:
            """
            @functools.wraps(func)  # 同步func原本的签名
            def wrapper(*args, **kw):
                print(f'exec {func.__name__}():')
                start = time.perf_counter()
                result = func(*args, **kw)
                end = time.perf_counter()
                print(f'cost: {(end - start) * 1000}ms')
                return result
            return wrapper


if __name__ == '__main__':
    CodingTool.rename_files_in_python_style(no_upper=True)

# Windows上配置运行bottom-up-attention
*Last updated on 2019.03.19 by [vilaseaka.github.io](https://vilaseaka.github.io) under CC BY-SA 4.0*  

论文地址：[Bottom-Up and Top-Down Attention for Image Captioning and Visual Question Answering](https://arxiv.org/pdf/1707.07998.pdf)
项目代码：[GitHub / bottom-up-attention
](https://github.com/peteanderson80/bottom-up-attention)

关于此项目：这个项目是从[py-R-FCN-multiGPU](https://github.com/bharatsingh430/py-R-FCN-multiGPU)修改而来的，而后者又从[py-fast-rcnn](https://github.com/rbgirshick/py-faster-rcnn)代码修改而来，RCNN全称为Region-CNN，是基于卷积神经网络(CNN)、线性回归和支持向量机(SVM)等算法，实现目标检测的技术。

项目理论背景：参考➡[重磅|基于深度学习的目标检测综述(一）](https://blog.csdn.net/l7H9JA4/article/details/79620247)

论文/项目内容：参考⬇  
* [视觉场景理解论文阅读笔记:Bottom-Up and Top-Down Attention for Image Captioning and Visual Question Answering](https://blog.csdn.net/u012991166/article/details/80659909)
* [论文笔记：Bottom-Up and Top-Down Attention for Image Captioning and Visual Question Answering](https://blog.csdn.net/sinat_26253653/article/details/78436112)

#### 配置此项目需要的环境
```
* Caffe框架
* Python2.7或3.5(由于caffe限制只能是这两个版本)
* 三个python包
    - cython
    - python-opencv
    - easydict
* VisualStudio2013或2015(由于caffe限制只能是这两个版本)
* CMake
* CUDA&&CuDNN
* MinGW(make工具)
* 各种可能用到的工具与中间件
```


--------
## 1 安装python依赖包
此项目的运行，需要cython, python-opencv, easydict这三个包，本机中没有，需要额外安装。*(安装Python的过程就不写了)*
```shell
#查看pip版本
pip --version
#如果pip没有安装，尝试从本地库中开启它 
#(使用--user解决权限不足的问题)
python -m ensurepip --default-pip --user
#如果还不能运行pip
#下载并安装[get-pip.py](https://bootstrap.pypa.io/get-pip.py)#(可以使用"--prefix="参数指定安装位置)
python get-pip.py
#确保pip，setuptools和wheel是最新的:
python -m pip install --upgrade pip setuptools wheel --user
#将pip添加到环境变量中，pip.exe位于python安装目录的Scripts文件夹下
#安装三个依赖包
pip install Cyphon --user
pip install easydict --user
pip install opencv-python --user
```
----

## 2 安装Caffe框架

### 2.1 Caffe简介
Caffe is a deep learning framework made with expression, speed, and modularity in mind. It is developed by Berkeley AI Research ([BAIR](http://bair.berkeley.edu/)) and by community contributors. [Yangqing Jia](http://daggerfs.com/) created the project during his PhD at UC Berkeley. Caffe is released under the [BSD 2-Clause license](https://github.com/BVLC/caffe/blob/master/LICENSE).<br>
[Caffe-官网](http://caffe.berkeleyvision.org/) /
[Caffe-GitHub](https://github.com/BVLC/caffe)

### 2.2 生产环境准备

**必要依赖：**

* Visual Studio *(目前仅支持VS2013或2015版本)*
* CMake 3.4以上版本

**可选依赖：**

* 开启GPU加速需安装(**在此项目中必选**)：
    - [CUDA](https://developer.nvidia.com/cuda-downloads) 7.5(*NVIDIA公司提供的GPU运算平台*)(*VS2015需要CUDA8.0*)
    - cuDNN(*用于加速深度网络训练*)
* 开启Python支持需安装(**在此项目中必选**)： 
    - **Python 2.7**或者**Python 3.5**
    - (*截至本文更新时间2019年3月18日Caffe只支持到Python3.5，使用3.6版本会编译出错*)
* 使用Git工具需安装：
    -  [Git for Windows](https://git-scm.com/downloads)
* 需要使用matcaffe接口则需安装**Matlab**。

*(确保安装之后将cmake.exe以及python.exe加入到系统环境变量中)*

### 2.3 配置安装Caffe

##### 2.3.1 下载Caffe源码
使用git命令下载或者直接到GitHub上下载window分支的压缩包
```shell
#git命令：
C:\Projects> git clone https://github.com/BVLC/caffe.git
C:\Projects> cd caffe
C:\Projects\caffe> git checkout windows
```
##### 2.3.2 修改build_win.cmd脚本配置
配置命令写在**"./scripts/build_win.cmd"**中，按需求更改配置，注意要修改的是else{ }中的参数而不是文件首APPVEYOR{ }中的内容,脚本中的注释很详细。这个脚本会下载相关的依赖，建立一个Visual Studio项目(或者ninja build files，具体看配置中的选择)并构建Release配置。

**问题1**
如果你安装了GCC（例如通过MinGW），那么Ninja会在检测到Visual Studio编译器之前检测到它，从而导致错误。在这种情况下有几个选择：

* 手动在配置文件中添加VS的编译器(cl.exe)路径(两个命令如下，放到cmake参数字段)
    - CMAKE_C_COMPILER=your/path/to/cl.exe
    - CMAKE_CXX_COMPILER=your/path/to/cl.exe
* 设置WITH_NINJA=0
* 卸载GCC

如果编译出错重新编译之前请删除build文件夹。

**问题2**
由于网络状况以及数据源的问题，在线下载依赖包迟迟下载不下来，于是在网上找了别人下载好的压缩包(压缩包在此提供→)。根据命令行中的提示将压缩包放到“C:\Users\Sauro\.caffe\dependencies”路径下(本文中是这个路径，Sauro为本机windows用户名，具体放在哪里看命令行里怎么写的)，不用解压。

##### 2.3.3 运行脚本
```shell
./build_win.cmd
```

--------

## 3 生成Cython模块
命令很简单，一条make即可，但是如何在winodws下使用make命令？

* 下载并安装[MinGW](http://www.mingw.org/)
* 将bin目录加入到系统路径中
* 在bin目录中将mingw32-make.exe复制一份，重命名为make(笑)

生成Cython模块:
```shell
cd $REPO_ROOT/lib
make
```

**报错**
```
error: Microsoft Visual C++ 9.0 is required. Get it from http://aka.ms/vcpython27
```
缺什么就下什么→[Microsoft Visual C++ Compiler for Python 2.7](http://www.microsoft.com/en-us/download/confirmation.aspx?id=44266)下载完之后安装即可，安装完后重新make。


## 4 安装
```shell
cd $REPO_ROOT/caffe
#配置好cafffe框架后(前文已经配置好)直接⬇
make -j8 && make pycaffe
```

参考：
[FAST RCNN安装配置精华](https://blog.csdn.net/dachao_xu/article/details/47321705)

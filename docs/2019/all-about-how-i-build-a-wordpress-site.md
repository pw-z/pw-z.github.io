# WordPress博客搭建详细过程  
*Last updated on 2019.03.17 by [Pengwei Zhang](http://pwz.wiki) under CC BY-SA 4.0*  

本文内容包括服务器生产环境的(手动)搭建、wordpress的安装与修改以及操作过程中一些问题的解决，所有操作基于Linux，是一份WordPress博客构建过程的完整记录，脱离脚本令人对整套系统有更清楚的认知，同时也使部分操作较为繁琐。

##### 目录
```shell
1 服务器生产环境的(手动)搭建
    1.1 Nginx的安装与配置
        1.1.1 准备编译环境
        1.1.2 安装PCRE库(源码编译)
        1.1.3 安装Zlib库(源码编译)
        1.1.4 安装OpenSSL库(源码编译)
        1.1.5 安装Nginx(源码编译)
        1.1.6 配置Nginx
    1.2 PHP的安装与配置
        1.2.1 PHP的安装
        1.2.2 PHP的配置
    1.3 MySQL的安装与配置
        1.3.1 MySQL的安装
        1.3.2 MySQL的配置
        1.3.3 MySQL数据库的一些常用操作
2 WordPress的安装与配置
    2.1 WordPress的安装
    2.2 解决错误：Call undefined function gzinflate()
    2.3 php不加载php.ini问题的解决：
3 对博客的个性化修改
    3.1 主题文件的修改
        3.1.1 配色调整
        3.1.2 页面布局调整
        3.1.3 页脚信息修改
        3.1.4 标题信息的修改
    3.2 上传限制的修改
    3.3 解决无法裁剪图片的问题
    3.4 设置文章永久固定链接
    3.5 网站备份方案
```

### 1 服务器生产环境的(手动)搭建
**网络服务器**、**数据库**以及**PHP语言环境**是运行WordPress所需要的最基本的组件，本文选用Nginx(latest stable version)+MySQL5.5+PHP7.3这套组合(加上Linux系统即LNMP)，此组合足够稳定且对系统资源占用较小。为了熟悉Linux系统操作以及摆脱使用脚本所产生的黑盒，本文使用纯手动的方式配置这套环境，若没有此需求可以使用[LNMP一键安装包](https://lnmp.org/install.html)快速搭建。以下为手动搭建LNMP生产环境的操作过程。
*默认服务器中已经安装好Linux操作系统，本文为CentOS6.5，其他版本的linux系统请自行判断是否需要调整指令*
#### 1.1 Nginx的安装与配置
Linux系统下可以使用源代码编译安装、二进制包安装以及yum在线安装等多种方式安装软件，使用源代码编译的方式安装软件可操作空间较大(可修改源码、自定义编译选项等等)。本文使用源码编译方式安装Nginx，主要流程分为:
* 编译环境的准备
* 几个重要扩展模块的安装(PCRE+Zlib+SSL)
* Nginx的安装与配置
##### 1.1.1 准备编译环境
```shell
yum -y install gcc gcc-c++ automake autoconf libtool make
```
##### 1.1.2 安装PCRE库
PCRE库包含一套正则匹配函数，可以使Nginx支持Rewrite功能。PCRE最新版本地址→[PCRE](https://ftp.pcre.org/pub/pcre/)
```shell
#选择安装路径:
cd /usr/local/src
#下载PCRE安装包:
wget https://ftp.pcre.org/pub/pcre/pcre-8.43.tar.gz
#查看下载的文件：
ls
#解压：
tar -zxvf pcre-8.43.tar.gz
#进入解压出来的文件夹：
cd pcre-8.43
#编译安装：
./configure
make && make install
#检查安装结果：
pcre-config --version
```
##### 1.1.3 安装Zlib库
Zlib库包含一套数据压缩算法，Nginx的数据压缩模块GZIP_MODULE的实现依赖于Zlib库。Zlib最新版本地址→[Zlib](http://www.zlib.net/)。
```shell
cd /usr/local/src
wget http://www.zlib.net/zlib-1.2.11.tar.gz
tar -zxvf zlib-1.2.11.tar.gz
cd zlib-1.2.11
./configure
make && make install
```
##### 1.1.4 安装OpenSSL库
用于支持https请求，进行安全通信。
```shell
cd /usr/local/src
wget http://artfiles.org/openssl.org/source/openssl-1.1.1b.tar.gz
tar -zxvf openssl-1.1.1b.tar.gz
#安装openssl到 /usr/local/src/openssl 目录:
./config shared zlib  --prefix=/usr/local/src/openssl && make && make install
```
##### 1.1.5 安装Nginx
Nginx的安装与上述拓展库的安装同理，不同之处在于安装配置选项较多，详细的配置选项说明见Nginx官网文档[Building nginx from Sources](http://nginx.org/en/docs/configure.html),此处介绍本文涉及的几个选项:
```shell
--with-pcre=path 设置PCRE库的路径
--with-zlib=path 设置Zlib库的路径
--with-http_ssl_module 开启SSL模块
--prefix=path 设置编译之后的文件存放的地方
--sbin-path=path 设置Nginx编译后的可执行文件路径，默认路径为prefix/sbin/nginx
--conf-path=path 设置conf文件路径，默认路径为prefix/conf/nginx.conf
--pid-path=path 设置nginx.pid文件存放的路径，默认路径为prefix/logs/nginx.pid
```
具体安装过程：
```shell
#路径选择：
cd /usr/local/src
#下载:
wget http://nginx.org/download/nginx-1.14.2.tar.gz
#解压：
tar -zxvf nginx-1.14.2.tar.gz
#进入：
cd nginx-1.14.2
#执行configure配置脚本:
./configure \
--prefix=/usr/local/webserver \
--sbin-path=/usr/local/webserver/nginx \
--conf-path=/usr/local/webserver/nginx.conf \
--pid-path=/usr/local/webserver/nginx.pid \
--with-http_ssl_module \
--with-pcre=/usr/local/src/pcre-8.43 \
--with-zlib=/usr/local/src/zlib-1.2.11
#安装：
make && make install
#查看Nginx安装结果：
/usr/local/webserver/nginx -v
```
##### 1.1.6 配置Nginx

添加用户与用户组，专门用于WEB服务
```shell
/usr/sbin/groupadd www
/usr/sbin/useradd -g www www
```
按照需求配置nginx.conf：
```shell
vim /usr/local/webserver/nginx.conf
```
本文涉及的配置文件修改与说明：
```shell
#运行用户或者组，默认为nobody，此处修改为刚刚创建的www
user www www;  
#允许生成的进程数，与CPU核心数一致即可
worker_processes 1;  
#nginx进程运行文件存放地址
pid /usr/local/webserver/logs/nginx.pid;

events {
    #最大连接数
    worker_connections  1024;
}

http {
    #文件扩展名与文件类型映射表
    include       mime.types;
    default_type  application/octet-stream;
    #允许以sendfile方式传输文件
    sendfile on;   
    #连接超时时间
    keepalive_timeout 60;

    #开启gzip压缩
    gzip on;
    #设定不压缩小于设置值的文件
    gzip_min_length 1k;
    #设置压缩级别(1-9)，越大压缩得越好但也越占用CPU资源
    gzip_comp_level 1;
    # 禁用IE6的gzip
    gzip_disable "MSIE [1-6]\.";

    #虚拟主机配置
    server {
        #单连接请求上限
        keepalive_requests 120; 
        #监听端口
        listen       8080;   
        #访问地址设置(www.example.com)
        server_name  localhost;

        #默认请求
        location / {
            #网站根目录(/usr/local/webserver/html)
            root   html;
            #首页索引文件
            index  index.html index.htm index.php;
        }

        #错误页面设置
        error_page  404              /404.html;
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }
}
```
运行Nginx：
```shell
#检查配置文件正确性
/usr/local/webserver/nginx -t
#启动nginx→nginx安装地址 -c nginx配置文件地址
/usr/local/webserver/nginx -c /usr/local/webserver/nginx.conf
#重载配置文件(重启 reopen 停止 stop)
/usr/local/webserver/nginx -s reload
```
验证Nginx是否运行： 
```shell
#查看进程：
ps -ef|grep nginx
#浏览器访问欢迎页：
在浏览器中输入在nginx.conf中配置的server_name地址，
本文设置的地址为XXX.XXX.XXX.XXX:8080
回车访问，看到Welcome to nginx!即Nginx配置完成。
```
设置Nginx开机自启：
```shell
#在/etc/init.d目录下创建nginx文件

vim /etc/init.d/nginx

#将下面的代码写入nginx中
#此脚本来自nginx官网
#注意将nginx="XXXX"修改成nginx执行程序的路径。
#将NGINX_CONF_FILE="XXXX"修改成nginx.conf文件的路径。

#!/bin/sh
#
# nginx - this script starts and stops the nginx daemon
#
# chkconfig:   - 85 15
# description:  NGINX is an HTTP(S) server, HTTP(S) reverse \
#               proxy and IMAP/POP3 proxy server
# processname: nginx
# config:      /etc/nginx/nginx.conf
# config:      /etc/sysconfig/nginx
# pidfile:     /var/run/nginx.pid
# Source function library.
. /etc/rc.d/init.d/functions
# Source networking configuration.
. /etc/sysconfig/network
# Check that networking is up.
[ "$NETWORKING" = "no" ] && exit 0
nginx="/usr/local/webserver/nginx"
prog=$(basename $nginx)
NGINX_CONF_FILE="/usr/local/webserver/nginx.conf"
[ -f /etc/sysconfig/nginx ] && . /etc/sysconfig/nginx
lockfile=/var/lock/subsys/nginx
make_dirs() {
   # make required directories
   user=`$nginx -V 2>&1 | grep "configure arguments:.*--user=" | sed 's/[^*]*--user=\([^ ]*\).*/\1/g' -`
   if [ -n "$user" ]; then
      if [ -z "`grep $user /etc/passwd`" ]; then
         useradd -M -s /bin/nologin $user
      fi
      options=`$nginx -V 2>&1 | grep 'configure arguments:'`
      for opt in $options; do
          if [ `echo $opt | grep '.*-temp-path'` ]; then
              value=`echo $opt | cut -d "=" -f 2`
              if [ ! -d "$value" ]; then
                  # echo "creating" $value
                  mkdir -p $value && chown -R $user $value
              fi
          fi
       done
    fi
}
start() {
    [ -x $nginx ] || exit 5
    [ -f $NGINX_CONF_FILE ] || exit 6
    make_dirs
    echo -n $"Starting $prog: "
    daemon $nginx -c $NGINX_CONF_FILE
    retval=$?
    echo
    [ $retval -eq 0 ] && touch $lockfile
    return $retval
}
stop() {
    echo -n $"Stopping $prog: "
    killproc $prog -QUIT
    retval=$?
    echo
    [ $retval -eq 0 ] && rm -f $lockfile
    return $retval
}
restart() {
    configtest || return $?
    stop
    sleep 1
    start
}
reload() {
    configtest || return $?
    echo -n $"Reloading $prog: "
    killproc $nginx -HUP
    RETVAL=$?
    echo
}
force_reload() {
    restart
}
configtest() {
  $nginx -t -c $NGINX_CONF_FILE
}
rh_status() {
    status $prog
}
rh_status_q() {
    rh_status >/dev/null 2>&1
}
case "$1" in
    start)
        rh_status_q && exit 0
        $1
        ;;
    stop)
        rh_status_q || exit 0
        $1
        ;;
    restart|configtest)
        $1
        ;;
    reload)
        rh_status_q || exit 7
        $1
        ;;
    force-reload)
        force_reload
        ;;
    status)
        rh_status
        ;;
    condrestart|try-restart)
        rh_status_q || exit 0
            ;;
    *)
        echo $"Usage: $0 {start|stop|status|restart|condrestart|try-restart|reload|force-reload|configtest}"
        exit 2
esac

#授予文件权限
chmod 755 /etc/init.d/nginx 
#加入启动项
chkconfig --add /etc/init.d/nginx
chkconfig nginx on
#测试
service nginx start
service nginx stop
service nginx status
```

#### 1.2 PHP的安装与配置

##### 1.2.1 PHP的安装
依旧使用源码编译的方式安装PHP，版本选择最新版→[PHP](http://php.net/get/php-7.3.3.tar.gz/from/a/mirror)
```shell
#选择路径
cd /usr/local
#下载PHP源码
wget http://am1.php.net/get/php-7.3.3.tar.gz/from/this/mirror
#解压
tar -zxvf mirror
#进入
cd php-7.3.3
#编译选项
./configure --enable-fpm --with-mysqli --with-openssl --with-curl
#报错：configure: error: libxml2 not found. Please check your libxml2 installation.
yum install libxml2-devel
#重新./configure
./configure --enable-fpm --with-mysqli --with-openssl --with-curl
#安装
make && make install
(失误……之前路径选择了/usr/local，现在local成了PHP的根目录，
没有创建子文件夹……local文件夹现在乱成一团了，应该在上一步中指定安装路径才好 --prefix=PATH)
```
##### 1.2.2 PHP的配置

PHP-FPM(PHP FastCGI Process Manager)即PHP FastCGI 进程管理器，用于管理PHP 进程池的程序，PHP5.3之后集成了PHP-FPM，无需单独安装。php配置文件有php.ini、php-fpm.cof以及在php-fpm.conf中引入的php-fpm.d/www.conf。php-fpm.conf是PHP-FPM的主配置文件，www.conf 是PHP-FPM进程池的默认配置文件，按需求自行配置，配置文件中的注解很详细。[PHP官方文档](http://php.net/docs.php)
```shell
    #将配置文件复制到相应位置(复制源为php-7.3.3文件夹，即一开始解压的地方)
    cp php.ini-development /usr/local/php/php.ini
    cp /usr/local/etc/php-fpm.conf.default /usr/local/etc/php-fpm.conf
    cp sapi/fpm/php-fpm /usr/local/bin

    #将 php.ini 文件中的配置项 cgi.fix_pathinfo 设置为 0 。 
    #这里的修改关于一个漏洞，此处不展开解释了，感兴趣自行搜索。
    vim /usr/local/php/php.ini
    cgi.fix_pathinfo=0

    #修改php-fpm.conf以引入php-fpm.d/www.conf这个配置文件
    vim  /usr/local/etc/php-fpm.conf
    #找到最底下一行，删掉NONE
    include=/etc/php-fpm.d/*.conf
    #尝试运行
    /usr/local/bin/php-fpm
    #报错
    ERROR: Unable to globalize '/etc/php-fpm.d/*.conf' (ret=2) from /usr/local/etc/php-fpm.conf at line 143.
    #尝试解决问题
        cd /usr/local/etc/php-fpm.d
        ls
        发现只有一个www.conf.default,没有www.conf
        回到php-fpm.conf
        vim  /usr/local/etc/php-fpm.conf
        include=/etc/php-fpm.d/*.conf.default
        :wq保存退出
    #尝试运行
    /usr/local/bin/php-fpm
    #报错，同样问题
    回去将include修改为
    include=/usr/local/etc/php-fpm.d/*.conf.default
    #尝试运行
    /usr/local/bin/php-fpm
    #查看进程
    ps -aux |grep php-fpm
    #运行成功

    #修改PHP-FPM的用户组与用户(使用上文中创建的www www)
    vim /usr/local/etc/php-fpm.d/www.conf.default
    user = www
    group = www

    #更改Nginx配置以支持PHP
    vim /usr/local/webserver/nginx.conf
    #找到下面这段，将注释打开。作用是将PHP请求转发到PHP-FPM处理，配置使用默认即可。
    location ~ \.php$ {
        root           html;
        fastcgi_pass   127.0.0.1:9000;
        fastcgi_index  index.php;
        #注意这里⬇，将scripts替换为网站根目录(本文为：/usr/local/webserver/html)
        #fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
        fastcgi_param  SCRIPT_FILENAME  /usr/local/webserver/html$fastcgi_script_name;
        include        fastcgi_params;
    }
    #重载配置文件(重启 reopen 停止 stop)
    /usr/local/webserver/nginx -s reload
    #运行php
    /usr/local/bin/php-fpm

    #验证php是否配置好
    #在网站根目录新建php文件，写一句
    <?php phpinfo(); ?>
    #浏览器输入：XXX.XXX.XXX.XXX:8080/XXX.php，回车访问
    #出现php信息页面，PHP配置完成。
```
设置PHP开机自启动：
```shell
#PHP的安装包中自带自启脚本，位置在sapi/fpm/init.d.php.fpm,将此文件复制到/etc/init.d目录
cp /usr/local/php-7.3.3/sapi/fpm/init.d.php-fpm /etc/init.d/php-fpm
#赋予php-fpm执行权限
chmod 755 /etc/init.d/php-fpm 
#加入启动项
chkconfig --add php-fpm
#检查
chkconfig --list php-fpm
#345为ON则设置成功
```


#### 1.3 MySQL的安装与配置

依旧选择源码编译的方式安装mysql。本文选择MySQL5.5版本。

##### 1.3.1 MySQL的安装

安装准备：
```shell
#选择路径,下载并解压MySQL5.5的源码包(Source Code)
cd /usr/local
wget https://dev.mysql.com/get/Downloads/MySQL-5.5/mysql-5.5.62.tar.gz
tar -zxvf mysql-5.5.62.tar.gz
#删除压缩包
rm mysql-5.5.62.tar.gz

#安装cmake(推荐的编译工具)
yum install cmake
#安装ncurses(ncurses是字符终端下屏幕控制的基本库)
yum install ncurses-devel
#其他相关依赖前文安装Nginx时已经安装好了⬇
(yum -y install gcc gcc-c++ automake autoconf libtool make)

#新建mysql服务的专用用户
groupadd mysql
useradd -r -g mysql mysql
#新建MySQL安装目录与数据库目录(mkdir dir_name 在当前目录下创建文件夹)
mkdir mysql
mkdir mysqldb

#进入mysql源码包文件夹
cd /usr/local/mysql-5.5.62
```
编译准备：
```shell
    cmake \
    -DCMAKE_INSTALL_PREFIX=/usr/local/mysql \
    -DMYSQL_DATADIR=/usr/local/mysqldb \
    -DSYSCONFDIR=/etc \
    -DMYSQL_TCP_PORT=3306 \
    -DMYSQL_USER=mysql \
    -DWITH_MYISAM_STORAGE_ENGINE=1 \
    -DWITH_INNOBASE_STORAGE_ENGINE=1 \
    -DWITH_MEMORY_STORAGE_ENGINE=1 \
    -DWITH_PARTITION_STORAGE_ENGINE=1 \
    -DWITH_READLINE=1 \
    -DMYSQL_UNIX_ADDR=/var/lib/mysql/mysql.sock \
    -DENABLED_LOCAL_INFILE=1 \
    -DEXTRA_CHARSETS=all \
    -DDEFAULT_CHARSET=utf8 \
    -DDEFAULT_COLLATION=utf8_general_ci
```
```shell
#以上参数的简要解释
-DCMAKE_INSTALL_PREFIX=     mysql安装目录(/usr/local/mysql)
-DMYSQL_DATADIR=            mysql数据文件目录(/usr/local/mysqldb)
-DSYSCONFDIR=               mysql配置文件目录
-DMYSQL_TCP_PORT=3306       mysql服务器监听端口(默认即3306) 
-DMYSQL_USER=               设置mysql用户
-DWITH_XXX_ENGINE=1         启用XXX引擎的支持
-DWITH_READLINE=1           使用readline功能
-DMYSQL_UNIX_ADDR=          UNIX套接字文件路径
-DENABLED_LOCAL_INFILE=1    允许从本地导入数据功能
-DEXTRA_CHARSETS=all        安装所有扩展字符集
-DDEFAULT_CHARSET=          设置服务器的字符集(utf8)
-DDEFAULT_COLLATION=        服务器排序规则(utf8_general_ci==快速)

#如果出错，按照错误信息进行相应处理之后删除之前的配置文件重新编译
rm -rf CMakeCache.txt
cmake XXXXXXXXXXXXXXX
#如果成功，会看到提示信息
(Build files have been written to：/usr/local/masql)
```
编译安装：
```shell
make
make install
```
##### 1.3.2 MySQL的配置
```shell
#修改mysql相关目录用户及权限
cd /usr/local/mysql
chown -R mysql:mysql .
cd /usr/local/mysqldb
chown -R mysql:mysql .

#初始化数据库
cd /usr/local/mysql    
/scripts/mysql_install_db --user=mysql --datadir=/usr/local/mysqldb

#得到如下提示信息(留存备用)
To start mysqld at boot time you have to copy
support-files/mysql.server to the right place for your system
PLEASE REMEMBER TO SET A PASSWORD FOR THE MySQL root USER !
To do so, start the server, then issue the following commands:
./bin/mysqladmin -u root password 'new-password'
./bin/mysqladmin -u root -h ecs-438c password 'new-password'
Alternatively you can run:
./bin/mysql_secure_installation
which will also give you the option of removing the test
databases and anonymous user created by default.  This is
strongly recommended for production servers.
See the manual for more instructions.
You can start the MySQL daemon with:
cd . ; ./bin/mysqld_safe &
You can test the MySQL daemon with mysql-test-run.pl
cd ./mysql-test ; perl mysql-test-run.pl

#复制mysql启动脚本
cp /usr/local/mysql/support-files/mysql.server /etc/init.d/mysqld
#将启动脚本加入系统环境变量(从而可以在任何路径下使用mysql命令)
vim /etc/profile
    在文件末加上
    PATH=/usr/local/mysql/bin:/usr/local/mysql/lib:$PATH
    export PATH
    :wq
source /etc/profile
```
启动MySQL服务以及一些报错的解决：
```shell
#尝试启动-1
service mysqld start
#报错-1
    #Directory '/var/lib/mysql' for UNIX socket file don't exists.
    #尝试解决
    #手动建立/var/lib/mysql/mysql.sock
#尝试启动-2
service mysqld start
#报错-2
    #Starting MySQL..The server quit without updating PID file (/var/lib/mysql/ecs-438c.pid).
    #搜索此问题，有文写道将/etc/mysql下的my.cnf文件删除即可，本文服务器my.cnf位于etc根目录，
    #打开此文件发现datadir参数不正确，修改使其指向正确的地址(前文中设置为/usr/local/mysqldb)  
#尝试启动-3
service mysqld start
#启动成功

#查看MySQL运行状态
service mysqld status
#关闭mysql
service mysqld stop
#报错
    #MySQL server PID file could not be found!                  [FAILED]
    #解决办法：
    vim /etc/my.cnf
    #删除关于pid文件的路径指定，让系统使用默认路径
#再次尝试关闭，关闭成功
```
设置MySQL服务开机自启：
```shell
#添加启动项
service mysqld start 
chkconfig --level 345 mysqld on
#显示服务列表
chkconfig --list
#看到mysql的服务且3、4、5皆为on则设置成功
```
##### 1.3.3 MySQL数据库的一些常用操作

修改mysql的root密码(忘记已有root密码的前提下)：
```shell
#先停止当前mysql服务
service mysqld stop
#以跳过权限认证的方式开启mysql服务
mysqld --skip-grant-tables
#另开一个ss连接(如果是本地服务器就另开一个命令窗口)
#转入mysql安装目录下的bin子目录
cd /usr/local/mysql/bin
#输入mysql回车将出现MySQL提示符"mysql>"(顺利的话)
mysql> use mysql;
mysql> update user set password=password("XXXX") where user="root";
mysql> flush privileges;
mysql> quit;
```
开启远程连接服务：
```shell
1)确保服务器33.6端口对外开放
2)将用户数据表中的host字段改成'%':
    mysql -u root -p
    mysql>use mysql;
    mysql>update user set host = '%' where user = 'root';
    查看修改结果：
    mysql>select host, user from user;  
    mysql>quit;G1jiangxingnvzi
```
**基础环境的搭建到此全部完成。**

-------


### 2 WordPress的安装与配置

#### 2.1 WordPress的安装

WordPress的安装比较简单，在配置好生产环境之后，下载WordPress的安装包，解压到WEB服务器的网站根目录或者二级目录中,使用浏览器访问服务器地址,然后按照WordPress的提示进行操作即可。

> Run the WordPress installation script by accessing the URL in a web browser. This should be the URL where you uploaded the WordPress files.
> If you installed WordPress in the root directory, you should visit: http://example.com/ 
> If you installed WordPress in its own subdirectory called blog, for example, you should visit: http://example.com/blog/

首先准备wordpress要用的数据库：
```shell
#创建wordpress专用的数据库(库名自定，此处为wordpress_zpw)
mysql -u root -p
mysql> create database wordpress_zpw;
#设置新建数据库的用户以及密码(此处用户名:username 密码:password)
mysql> create user 'username'@'localhost' identified by "password";
mysql> grant all privileges on wordpress_zpw.* to username@'localhost';
#刷新权限
mysql> flush privileges;
mysql> quit
```
下载并解压wordpress安装文件到相应目录(本文为网站根目录，此服务器只跑这一个博客)：
```shell
#进入Nginx网站根目录
cd /usr/local/webserver/html
#下载WordPress最新版安装包
wget https://wordpress.org/latest.tar.gz
#解压
tar -zxvf latest.tar.gz
#解压后的文件都在wordpress子目录下，全部移出来("."代表当前目录)
mv wordpress/* .
#删掉空文件夹wordpress以及压缩包latest.tar.gz
rm -r wordpress
rm latest.tar.gz
```
浏览器访问站点安装wordpress：
```shell
#服务器还没有绑定域名，所以直接访问：
XXX.XXX.XXX.XXX:8080/index.php
#(index.php为wordpress的安装引导页)
#按照提示填写信息安装

#信息填写完毕后安装完成并登陆系统后报错：
Fatal error: Uncaught Error: Call to undefined function gzinflate()
```
#### 2.2 解决Fatal error: Uncaught Error: Call to undefined function gzinflate()

原因在于源码编译php时没有配置zlib模块。
在不重新编译PHP的情况下为其添加拓展模块(zlib模块):
```shell
#找到php的源码文件夹
cd usr/local/php-7.3.3/ext/zlib
cp config0.m4 config.m4

#执行phpize生成配置文件
phpize
#报错：
configure.ac:3: error: Autoconf version 2.68 or higher is required
configure.ac:3: the top level
autom4te: /usr/bin/m4 failed with exit status: 63

#使用yum升级autoconf
yum update autoconf
#提示已经是最新版本
#查看当前autoconf版本：
rpm -qf /usr/bin/autoconf 

autoconf-2.63-5.1.el6.noarch

#不满足要求，使用手动升级：
#先卸载当前autoconf：
rpm -e --nodeps autoconf-2.63

#下载安装autoconf 2.68:
cd /usr/local/src
wget ftp://ftp.gnu.org/gnu/autoconf/autoconf-2.68.tar.gz 
tar zxvf  autoconf-2.68.tar.gz
cd autoconf-2.68
./configure
make && make install

#重新尝试phpize命令
cd /usr/local/php-7.3.3/ext/zlib
phpize

#获得php-config脚本的位置
which php-config

/usr/local/bin/php-config

#编译安装
./configure --with-php-config=/usr/local/bin/php-config --with-zlib
make && make install

#安装完成，提示如下信息
#Build complete.
#Don't forget to run 'make test'.
#Installing shared extensions:     /usr/local/lib/php/extensions/no-debug-non-zts-20180731/
#在上述信息中的文件夹中可以看到
opcache.a  opcache.so  zlib.so
#编辑php.ini,添加zlib.so扩展
vim /usr/local/php/php.ini
extension=zlib.so
:wq

#重启php-fpm服务，查看已挂载的模块列表
php -m

#模块列表中没有zlib，操作失败

#检查/usr/local/lib/php/extensions/no-debug-non-zts-20180731/下是否有zlib.so(有)
#检查php.ini文件是否修改成功(没有问题)

#也许php.ini文件根本就没有被加载？

php --ini

Configuration File (php.ini) Path: /usr/local/lib
Loaded Configuration File:         (none)
Scan for additional .ini files in: (none)
Additional .ini files parsed:      (none)
确实没有加载
```

#### 2.3 php不加载php.ini问题的解决：
```shell
#使用php --ini命令可以看到加载路径为/usr/local/lib
#此路径下并没有php.ini
#查找php.ini的位置：
find / -name php.ini

/usr/local/php/php.ini

#将php.ini复制到正确路径：
cp /usr/local/php/php.ini /usr/local/lib/

#重启php-fpm检查
service php-fpm restart
php --ini

Configuration File (php.ini) Path: /usr/local/lib
Loaded Configuration File:         /usr/local/lib/php.ini
Scan for additional .ini files in: (none)
Additional .ini files parsed:      (none)

php -m
zlib模块已经挂载
```
重新访问网站正常显示主页，**WordPress安装配置完成**，可以进入下一步操作了。

----

### 3 博客的个性化修改

#### 3.1 主题文件的修改

WordPress的主题资源很丰富，但完全符合个人喜好的主题很少，所以在此以个人比较喜欢的官方主题Twenty Sixteen为基础做一些个性化修改，对其他主题的操作同理。
```shell
    #主题文件位置:
    ./wp-content/themes/twentysixteen/

    #主题文件夹内文件(文件内有详细的注释)：
    style.css           全局样式表
    header.php          页眉
    footer.php          页脚
    sidebar.php         侧栏
    index.php           主页
    single.php          文章页
    search.php          搜索结果页
    ……                  ……
```
修改思路：
```shell
    1)定位元素位置(善用F12以及文档注释)
    2)找到对应文件
    3)进行相应修改(通过服务器或者在wordpress后台修改)
```
##### 3.1.1 配色调整

Twenty Sixteen提供了配色更改功能并给出了五套预设，可以按个人喜好调整色彩。若是主题没有提供配色更改的功能，请手动到样式表(style.css)中去更改。作为技术博客还是朴素一点为好，以简约为原则尽量削弱色彩的影响，让人专注于文字。
```shell
    #低纯度黑色系
    Background Color            #191919
    Page Background Color       #333333
    Link Color                  #8fd8fc
    Main Text Color             #e5e5e5
    Secondary Text Color        #c1c1c1

    #灰底白色系
    Background Color            #b2b2b2
    Page Background Color       #ffffff
    Link Color                  #358fcc
    Main Text Color             #1a1a1a
    Secondary Text Color        #686868
```
##### 3.1.2 页面布局调整

个人习惯将侧边栏放在页面左侧，即将整个页面左右两部分调换一下，另外将每篇文章的档案信息(footer)置于文章底部。
```css
#打开控制台，审查元素定位到侧边栏(sidebar)以及文本域(content-area)
#在style.css中找到刚刚定位的语句，将对应样式修改为如下：
.sidebar {
    float: left;
    /*margin-left: 75%;*/
    padding: 0;
    width: 25%;
}
.content-area {
    float: right;
    width: 65%;
}

#将booter的位置挤掉(将float: right;注释掉)，并给左侧留出1%的空隙：
body:not(.search-results) article:not(.type-page) .entry-content {
/*float: right;*/
margin-left: 1%;
width: 71.42857144%;
}

#调整footer的显示效果(使其并排显示)：
style.css第3600行一直到“14.5 - >= 1200px”之间的样式代码全部注释掉。

#让booter左边也留出1%的空隙(也就是标题比内容以及booter往左多处一格)
#style.css第3140几行处，将".entry-footer,"注释掉，并在下面添加：
.entry-footer {
    margin-right: 0;
    margin-left: 1%;
}
```
实现单独查看某篇文章时候不显示footer：
```css
#编辑
./wp-content/themes/twentysixteen/template-parts/content-single.php
#将最底部这段代码注释掉↓
<!-- 2019年3月11日将此段注释掉，使得单独查看某篇文章时候不显示footer 
    <footer class="entry-footer">
        <?php twentysixteen_entry_meta(); ?>
        <?php
            edit_post_link(
                sprintf(
                    /* translators: %s: Name of current post */
                    __( 'Edit<span class="screen-reader-text"> "%s"</span>', 'twentysixteen' ),
                    get_the_title()
                ),
                '<span class="edit-link">',
                '</span>'
            );
            ?>
    </footer><!-- .entry-footer -->
</article><!-- #post-## -->
```
##### 3.1.3 页脚信息修改

默认主题的页脚上有一行文字，"网站标题 / Proudly powered by wordpress" ，按个人喜好进行一定修改。
```css
编辑./wp-content/themes/twentysixteen/footer.php
找到下面的输出语句

<span class="site-title"><a href="<?php echo esc_url( home_url( '/' ) ); ?>" rel="home"><?php bloginfo( 'name' ); ?></a></span>
            <?php
            if ( function_exists( 'the_privacy_policy_link' ) ) {
                the_privacy_policy_link( '', '<span role="separator" aria-hidden="true"></span>' );
            }
            ?>
            <a href="<?php echo esc_url( __( 'https://wordpress.org/', 'twentysixteen' ) ); ?>" class="imprint">
                <?php printf( __( 'Proudly powered by %s', 'twentysixteen' ), 'WordPress' ); ?>
            </a>
```
##### 3.1.4 标题信息的修改

网站标题(Site Title)下面有一行网站描述(Tagline),个人喜欢在tagline的位置写上一句喜欢的话，但是Twenty Sixteen的网站标题会将网站描述加在一起，在浏览器的标签页上显示不全长长一行文字很不美观，虽然网站描述也是一门学问，作为个人网站不考虑那么多，简洁美观原则放在第一位。

如何让site title不集成tagline？思路很多，在Customizing界面将Tagline滞空，编辑header.php相应代码：
```css
$description = get_bloginfo( 'description', 'display' );
if ( $description || is_customize_preview() ) :
    ?>
    <p class="site-description"><?php echo $description; ?></p>
<?php endif; ?>
#这段代码控描述信息的输出，如果描述不为空则显示网站描述
#直接将$description改为true，在echo后面写上想输出的话即可
#改后如下
$description = get_bloginfo( 'description', 'display' );
if ( true || is_customize_preview() ) :
    ?>
    <p class="site-description"><?php echo "世界上只有一种真正的英雄主义,那就是在认清生活的真相后依然热爱生活。"; ?></p>
<?php endif; ?>

#目的达成 √
```
#### 3.2 上传限制的修改

有上传大文件的需求，但是wordpress上传文件有大小限制，而此限制又是由PHP的配置(以及Nginx的配置)决定的。遂有如下修改：
```shell
find / -name php.ini
vim /usr/local/lib/php.ini
#添加配置：
upload_max_filesize = 500M
post_max_size = 500M
max_execution_time = 300
#重启php
service php-fpm restart

find / -name nginx.conf
vim /usr/local/webserver/nginx.conf
#添加配置：
client_max_body_size 500m;
#重启nginx
service nginx restart
```
#### 3.3 解决无法裁剪图片的问题

设置wordpress首页图片的时候报错，无法裁剪图片，原因在于PHP缺少了gd库，拓展安装gd模块：
```shell
#安装依赖
yum install libpng
yum install libpng-devel
#找到gd源码文件夹，编译安装
cd /usr/local/php-7.3.3/ext/gd
phpize
./configure --with-php-config=/usr/local/bin/php-config
make && make install
#修改配置文件，重启
vim /usr/local/lib/php.ini
extension = gd.so
service php-fpm restart
#检查
php -m
```
裁剪图片后依然报错，经过检查发现是因为gd库默认是不支持jpeg拓展的，于是安装两个拓展库以使得gd支持更多的格式：
```shell
#安装jpeg支持
wget http://www.ijg.org/files/jpegsrc.v9c.tar.gz
tar -zxvf jpegsrc.v9c.tar.gz
rm jpegsrc.v9c.tar.gz
cd jpeg-9c
./configure --prefix=/usr/local/jpeg --enable-shared --enable-static 
make && make install

#安装freetype拓展
wget https://download.savannah.gnu.org/releases/freetype/freetype-2.9.tar.gz
tar -zxvf freetype-2.9.tar.gz
cd freetype-2.9
./configure --prefix=/usr/local/freetype --enable-shared --enable-static
make && make install 

#重新搭建gd.so
cd /usr/local/php-7.3.3/ext/gd
makeclean
phpize
./configure --with-php-config=/usr/local/bin/php-config --with-jpeg-dir=/usr/local/jpeg/ --with-freetype-dir=/usr/local/freetype/
make
make install
service php-fpm restart
#可以利用phpinfo()函数查看gd支持的格式，前文写过不再赘述(PHP安装部分)
```
#### 3.4 设置文章永久固定链接

充斥着杂乱参数的链接难以称得上美观，推荐使用`/%postname%`或者`/%postname%.html`这种格式，简介美观还在一定程度上有利于搜索引擎收录。

*%postname%的值为文章缩略名，若没设置缩略名则默认为文章标题。缩略名在文章编辑页面文章标题下面编辑*

在wordpress后台可以直接设置固定链接的格式，但只在wordpress后台设置完后还不可以，会发现访问以前的文章出现404notfound错误，因为修改完链接格式之后数据库并没有将以前的文章链接更新为新格式，这个问题可以通过Nginx的rewrite模块解决。

rewrite模块可以根据正则表达式匹配URL并改写URL，重定向到新地址。基本语法为：
```shell
rewrite regex replacement flag;
#url与regex匹配后将会被替换为replacement，flag为附加参数。
```
关于rewrite以及伪静态等相关内容不在此讨论，下面直接给出wordpress的rewrite方案：
```shell
#将以下代码加入到nginx配置文件中的server{}字段(或者其中的location/{}字段)中
if (-f $request_filename/index.html){
rewrite (.*) $1/index.html break;
}
if (-f $request_filename/index.php){
rewrite (.*) $1/index.php;
}
if (!-f $request_filename){
rewrite (.*) /index.php;
}
```
大概解释一下这段代码，if语句判断请求的url是否存在对应文章，存在则直接读取然后break，若请求不存在则带着参数转到index.php。index.php根据固定链接的格式解析参数并返回对应的文章。

#### 3.5 关闭自动保存功能

在WordPress的文章编辑过程中会产生自动保存的版本，并且每次修改都会产生一个修订版，在没有此需求的情况下，关闭此功能以保持数据库的干净。
```shell
#编辑wordpress配置文件wp-config.php(位于前文中设定的网站根目录下)
#禁用修订版本，自动保存时间为100000秒，
define('WP_POST_REVISIONS', false);
define(‘AUTOSAVE_INTERVAL’, 100000);
#如下语句是关闭自动保存，本人改了之后系统出问题，变成了无限自动保存(一直在保存)
define(‘AUTOSAVE_INTERVAL’, false);
#偷个懒没查什么原因，直接改成十万秒，相当于关闭此功能了
```

#### 3.6 网站备份方案

暂时没有发现较好的**免费备份方案**。有不少插件倒是提供免费远程备份到Google Drive或是FTP，一来Google Drive在国内环境下不好用，二来没有额外的服务器一直跑一个FTP。于是按照如下方案备份。
```shell
1)数据库文件通过UpdraftPlus插件定期备份到邮箱中(免费)。
2)wordpress整个目录定期打包备份到本地

#远程打包
tar -zcvf /home/wwwroot/default/wordpress_bak.tar.gz /home/wwwroot/default
#复制压缩包到本地
本文直接使用WinSCP软件拖拽下载

#tar命令的解释：
#命令格式：  
tar -参数 打包后文件名(包含路径) 待打包文件(目录)
#参数含义：
-z：使用gzip压缩
-c: 打包
-x  解包
-v  显示过程
-f: 相当于参数结束符,必须有且其后接文件名
```

关于WordPress博客的搭建与修改优化到此为止基本结束，篇幅过长修改优化部分不再添加过多内容。WordPress的相关教程、资源很多，可按需求拓展插件，对网站进行优化。

-------

###### 部分参考资料：
[nginx基本配置与参数说明](http://www.nginx.cn/76.html)<br>
[Nginx+Php-fpm运行原理详解](https://segmentfault.com/a/1190000007322358?utm_source=tag-newest)<br>
[PHP的性能演进(从PHP5.0到PHP7.1的性能全评测)](http://www.laruence.com/2016/12/18/3137.html)<br>
[Linux文件权限详解](https://www.cnblogs.com/webnote/p/5734714.html)

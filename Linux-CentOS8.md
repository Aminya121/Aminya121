
## 介绍Linux中`CentOS8`系统的基础操作与应用 
---

## 1.基础操作
- `touch` #创建文件
    - `touch exmple.txt` 
    - #创建一个名为exmple的文本文件

- `ls` #查看当前目录的文件
    - `ls` 
    - `a.txt b.conf` 
    - #该目录里的文件 

- `ll` #查看文件的属性
    - `ll`
    - `-rw-r--r--. 1 root root 12374 Jan  9 05:32 a.conf`
    - `-rw-r--r--. 1 root root 13430 May  9  2023 magic`
    - #显示的文件权限 创建时间 名称等

- `pwd` #查看当前的目录
    - `pwd`
    - `/root` 
    - #当前目录的路径

- `mv` #改名；移动文件
    - `mv file.txt /path/to/destination/` 
    - #将文件移动到/path/to/destination/
    - `mv a.txt b.txt` 
    - #将文件a.txt改名为b.txt

- `cd` #切换路径
    - `cd /root` 
    - #切换到root路径

- `rm` #删除文件
    - `rm a.txt` 
    - #移除a.txt文本文件并且进行询问
    - `rm -rf a.txt` 
    - #静默移除a.txt文本文件
    - `rm -rf *` 
    - #静默移除整个当前目录下的文件

- `echo` #输出内容
    - `echo 123 > a.txt` 
    - #向a.txt中输入123

- `cat` #查看文件
    - `cat a.txt` 
    - #查看a.txt里的内容 
    - `123` 
    - #a.txt包含的内容

- `cp` #拷贝文件
    - `cp -p a.txt b.txt` 
    - #将a.txt复制并且重命名为b.txt

- `history` #查看历史命令记录
    - `cat a.txt`
    - `cp -p a.txt b.txt` 
    - #显示历史命令记录
- `setenforce 0` #关闭ELinux
---
## 2.挂载yum源
- `cd /etc/yum.repos.d/`  
- #切换到yum源配置文件目录
- `rm -rf *`              
- #删除默认的配置文件
- `vi a.repo`             
- #新建一个配置文件
   ```bash
   [1]
   baseurl=file:///media/AppStream
   gpgcheck=0
   [2]
   baseurl=file:///media/BaseOS
   gpgcheck=0
  ```
- #配置文件举例

- `mount /dev/cdrom /media`
- `mount: /media: WARNING: source write-protected, mounted read-only.`
- #挂载成功并进入只读模式
---
## 3.通过yum源下载
- `yum install -y vim`
- #下载vim查看器
- `yum install -y bind*`
- #下载DNS解析服务
- `yum install -y httpd`
- #下载Apache服务
- `yum install -y httpd mod_ssl* openssl*`
- #下载Apache的扩展openssl插件
---
## 4.配置DNS解析服务
- ## 修改配置文件
    - `vim /etc/named.conf`
    - #进入DNS配置文件修改监听网址
        ```bash
        10 options {
        11         listen-on port 53 { any; };
        12         listen-on-v6 port 53 { ::1; };
        13         directory       "/var/named";
        14         dump-file       "/var/named/data/cache_dump.db";
        15         statistics-file "/var/named/data/named_stats.txt";
        16         memstatistics-file "/var/named/data/named_mem_stats.txt";
        17         secroots-file   "/var/named/data/named.secroots";
        18         recursing-file  "/var/named/data/named.recursing";
        19         allow-query     { any; };
                       
        ```
- ## 配置域名映射
    - `vim /etc/named.rfc1912.zones`
    - #配置正向解析目录和逆向解析目录
        ```bash
         1 zone "20.10.10.in-addr.arpa" IN {} #将IP地址10.10.20.x反向解析
         2         type master;
         3         file "named.10";
         4         allow-update { none; };
         5 };
         6 
         7 zone "skills.com" IN {             #将域名skills.com正向解析
         8         type master;
         9         file "named.skills";
        10         allow-update { none; };
        11 };
        ```
    - `cd /var/named`
    - #切换到解析定义域目录
    - `cp -p named.loopbcak named.10`
    - `cp -p named.localhost named.skills`
    - #复制模板文件
    - `vim named.10`#IP正向反向解析文件
        ```bash
        1 $TTL 1D
        2 @       IN SOA  @ rname.invalid. (
        3                                         0       ; serial
        4                                         1D      ; refresh
        5                                         1H      ; retry
        6                                         1W      ; expire
        7                                         3H )    ; minimum
        8         NS      @
        9         A       127.0.0.1
        10        AAAA    ::1
        11        PTR     localhost.
        12 101    PTR     abc.skills.com.

        ```
    - `vim named.skills`#域名正向解析文件
        ```bash
        1 $TTL 1D
        2 @       IN SOA  @ rname.invalid. (
        3                                         0       ; serial
        4                                         1D      ; refresh
        5                                         1H      ; retry
        6                                         1W      ; expire
        7                                         3H )    ; minimum
        8         NS      @
        9         A       127.0.0.1
        10        AAAA    ::1
        11 abc    A       10.10.20.101

        ```
- ## 应用配置文件并测试
    - `systemctl restart named`
    - #重启DNS服务
    - `dig @localhost abc.skills.com`
    - #查询DNS服务
        ```bash
        ; <<>> DiG 9.16.23-RH <<>> @localhost abc.skills.com
        ; (2 servers found)
        ;; global options: +cmd
        ;; Got answer:
        ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 2153
        ;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

        ;; OPT PSEUDOSECTION:
        ; EDNS: version: 0, flags:; udp: 1232
        ; COOKIE: 47bfcb290f9e2ead01000000677fb8e9879f6dd75c3a46c0 (good)
        ;; QUESTION SECTION:
        ;abc.skills.com.                        IN      A

        ;; ANSWER SECTION:
        abc.skills.com.         86400   IN      A       10.10.20.101

        ;; Query time: 0 msec
        ;; SERVER: ::1#53(::1)
        ;; WHEN: Thu Jan 09 06:54:17 EST 2025
        ;; MSG SIZE  rcvd: 87
        ```
    - #看到输出以上结果即配置成功

---

## 5.Apache配置openssl证书
- ## 颁发证书
    - `cd /etc/pki/CA/`     
    - #切换到CA颁发
    - `echo 00 > serial`   
    - #指定第一个颁发证书的序列号
    - `touch index.txt`   
    - #生成证书索引数据库文件
    - `openssl genrsa > private/cakey.pem`    
    - #生成CA私钥
    - `openssl req -new -x509 -key private/cakey.pem > cacert.pem -days 3650`   
    - #生成CA自签名证书，并指定CA私钥为cakey.pem，根证书有效期限3650天
    - #此处输入根证书信息...
    ---
    - `cd /etc/ssl/`
    - #切换到ssl配置
    - `openssl genrsa > skills.key`   
    - #生成Apache要使用的证书私钥
    - `openssl req -new -key skills.key > skills.csr`   
    - #基于私钥skills.key创建一个新的证书签名请求
    - #此处输入要颁发的证书信息...
    ---
    - `openssl ca -days 1825 -in skills.csr > skills.crt`   
    - #颁发证书，有效期限为1825天
    - #此处输入两次y确认
- ## 修改Apache配置文件
    - `vi /etc/httpd/conf/httpd.conf  +`  
    - #编辑原有大Apache配置
        ```bash
        128 #DocumentRoot /
        129 <Directory />
        130     Require all granted
        131 </Directory>
        ```
    - #在原有配置下添加新的Apache配置
        ```bash
         1 sslcertificatefile /etc/ssl/skills.crt
         2 sslcertificatekeyfile /etc/ssl/skills.key
         3 
         4 <VirtualHost *:80>
         5     ServerName abc.skills.com
         6     DocumentRoot /abc
         7         <Directory /abc>
         8             require all granted
         9         </Directory>
        10 </VirtualHost>
        11 
        12 <VirtualHost *:443>
        13     ServerName abc.skills.com
        14     DocumentRoot /abc
        15         <Directory /abc>
        16             Require all granted
        17         </Directory>
        18 </VirtualHost>
        ```
- ## 配置网址内容
    - `mkdir /abc`
    - #创建一个新的文件夹
    - `echo abc > /abc/index.html/`
    - #在该目录下创建一个网址文件，并输入abc
- ## 重启服务并应用
    - `systemctl stop firewalld`
    - #停止防火墙服务
    - `systemctl restart httpd`
    - #重启Apache服务
    - `curl -k https://abc.skills.com`
    - #测试网址是否可以访问
    - `abc`
    - #看到以上回复则配置成功
---
    
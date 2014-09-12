Speed up ghost
===================

由于Google公共库在国内访问不稳定，而Ghost后台和一些主题都引用了其API，导致Ghost博客加载阻塞。

对此有两个解决思路，一是禁止加载Google Fonts；二是使用镜像。国内某安全厂商推出相应CDN镜像服务，只需将引用源由googleapis.com改为useso.com，即可提速，但不支持https协议；而中国科技大学一团队也推出镜像服务，并支持https。

这是一个python脚本，用于自动修改Ghost博客系统对Google公共库和字体库的引用，达到在国内访问提速的目的，默认引用中科大源。脚本也可以用于wordpress等。

----------

依赖
-------------

1、Python 2.6+

----------

使用
-------------------

1、在ghost根目录下创建tools文件夹

2、将speedupghost.py文件放入tools

3、运行speedupghost.py

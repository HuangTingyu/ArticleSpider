## ArticleSpider
Scrapy框架用于爬取文章

<http://blog.jobbole.com/>

## government

Scrapy用于爬取部门网站

<http://www.gd.gov.cn/govpub/jg/>

## 搭建环境

## 搭建环境

### 1.下载python3.5.2，pip换源

在C:\Users\lenovo下面建立一个pip目录，建立一个pip.ini文件，写入内容如下

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

### 2.搭建虚拟环境（cmd命令行窗口）

```
pip install virtualenv
virtualenv scrapytest
```

### 3.进入虚拟环境

```
cd scrapytest
cd Scripts
dir
```

dir用于显示项目目录

```
activate.bat
python
```

进入python虚拟环境。

退出虚拟环境

```
deactivate.bat
```

### 4.在scrapytest\Scripts目录下，安装virtualenv管理工具

```
pip install virtualenvwrapper
pip install virtualenvwrapper-win
```

### 5.新建环境变量，用于重置虚拟环境的路径。

```
WORKON_HOME
D:\ArticleSpider\Evns
```

如图所示

![03 新建环境变量](E:\04 爬虫实战\笔记\图片\03 新建环境变量.png)

关掉CMD，重启输入

```
workon
```

![04 workon](E:\04 爬虫实战\笔记\图片\04 workon.png)

此时虚拟环境的存储目录已经转到了D:\ArticleSpider\Envs

记得要把C:User\Lenovo\Envs下的虚拟环境拷贝过来，然后进入刚刚建立的虚拟环境

```
workon py3scrapy
```

### 6.下载相关包

```
pip install requests
pip install scrapy
```

### scrapy安装失败解决办法

<https://zhuanlan.zhihu.com/p/24982105>

### 安装包失败解决办法

进入到下面的地址，重新安装

<https://www.lfd.uci.edu/~gohlke/pythonlibs/>

## 进入虚拟环境的方法

打开cmd，输入

```
D:
cd ArticleSpider\Envs
workon py3scrapy
```

## 创建scrapy项目

1.初始化项目环境

```
scrapy startproject Government
```

2.确认要爬取的网站(<http://www.gd.gov.cn/zwgk/szfjg/index.html>)

```
scrapy genspider government http://www.gd.gov.cn/zwgk/szfjg/index.html
```

3.在government文件下面建立main.py文件

```
import sys
import os
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "government"])
```

4.进入调试界面

```
scrapy shell http://blog.jobbole.com/114671/
```

5.pycharm导入已有的环境

```
C:\Users\lenovo\AppData\Local\Programs\Python\Python35
```

## 代码配置

setting文件



<!DOCTYPE html>
<head>
<meta charset="UTF-8">
<title>here is zhe title</title>
<h1 align="center">Study For HTML</h1>
</head>

***

<body><h5 align="center">
<a href="https://blog.csdn.net/qq_37084904/article/details/88089236?ops_request_misc=&request_id=&biz_id=102&utm_term=%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8html%E5%88%B6%E4%BD%9C%E5%9B%BE%E6%A0%87%E8%B6%85%E9%93%BE%E6%8E%A5&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0-88089236.142^v100^pc_search_result_base2&spm=1018.2226.3001.4187">HTML基础部分学习</a></h5>
</body>

-该网络资料来自CSDN官网

***

<body>
   <p><h3>1.首先来认识标题与段落</h3>
   </p>
</body>

<!--这是注释-->
<!--以下是段落-->
<p><h1 align="center">这是一级标题</h1>
   <h2 align="center">这是二级标题</h2>
   <h3 align="center">这是三级标题</h3>
   <h4 align="center">这是四级标题</h4>
   <h5 align="center">这是五级标题</h5>
   <h6 align="center" >这是六级标题</h6>
</p>
<!--以上是一个段落-->

<body>
<h5 align="center" style="color:#0083FC">HTML的标题分为1~6级</h5>
</body>

- 在html语言中用<h1~6>来表示
***   
- 表示方式如下
```HTML
<p><h1 align="center">这是一级标题</h1>
   <h2 align="center">这是二级标题</h2>
   <h3 align="center">这是三级标题</h3>
   <h4 align="center">这是四级标题</h4>
   <h5 align="center">这是五级标题</h5>
   <h6 align="center" >这是六级标题</h6>
</p>
```

***
<p><h5 align="center">流水落花春去也，天上人间。</h5></p>
<p><h5 align="center">自莫凭栏，无限江山，别时容易见时难</h5></p>
<p><h5 align="center">梦里不知身是客，一晌贪欢。</h5></p>
<p><h5 align="center">罗衾不耐五更寒。</h5></p>
<p><h5 align="center">帘外雨潺潺，春意阑珊。</h5></p>
<p><h5 align="center" style="color:#0083FC">----以上都是段落----</h5></p>

- 在html语言中用< p >< / p >表示
***

- 表示方式如下
```HTML
<p><h5 align="center">流水落花春去也，天上人间。</h5></p>
<p><h5 align="center">自莫凭栏，无限江山，别时容易见时难</h5></p>
<p><h5 align="center">梦里不知身是客，一晌贪欢。</h5></p>
<p><h5 align="center">罗衾不耐五更寒。</h5></p>
<p><h5 align="center">帘外雨潺潺，春意阑珊。</h5></p>
<p><h5 align="center" style="color:#0083FC">----以上都是段落----</h5></p>
```

***
<body>
   <p><h3>2.尝试使用超链接格式</h3>
   </p>
</body>

- 以下是一段html格式的超链接文本

<body>
   <p>
   <h5 align="center"><a herf="www.baidu.com">www.baidu.com</a></h5>
   </p>
</body>

***

- 它的表示方式如下

```HTML
<h5 align="center">
   <a herf="www.baidu.com">www.baidu.com</a></h5>
```

***    

- 接下来解释如何以图片按钮的方式超链接

<body>
<p>
<h5 align="center"><a herf="https://www.bilibili.com/"><img src="https://camo.githubusercontent.com/516b03a6af7b0d1eb9bddc71d1034b588c63ddc8e5072c6f9bd61d841c58dc02/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f42696c6962696c692d3139424244333f7374796c653d666c61742d737175617265266c6f676f3d62696c6962696c69266c6f676f436f6c6f723d666666"></a></h5></p>
</body>

***

- 它的表示方式如下,其实只要将文字部分替代为图片链接即可。
  
```html
<body>
<p>
<h5 align="center"><a herf="https://www.bilibili.com/"><img src="https://camo.githubusercontent.com/516b03a6af7b0d1eb9bddc71d1034b588c63ddc8e5072c6f9bd61d841c58dc02/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f42696c6962696c692d3139424244333f7374796c653d666c61742d737175617265266c6f676f3d62696c6962696c69266c6f676f436f6c6f723d666666"></h5></p>
</body>
```

***

<body>
<p><h3>3.接下来做一些新的尝试</h3>
</body>

- 以下是一段自定义颜色的文字
  
<body>
<p><h5 align="center" style="color:#FF5AB7" >测试颜色，嗷呜！</h5>
</p>

***
- 这是它的表达方式
```HTML
<body>
<p><h5 align="center" style="color:#FF5AB7" >测试颜色，嗷呜！</h5>
</p>
<!---这里的颜色可以为十六进制RGB颜色编码或者标准色--->

```

***
- 能不能做到渐变色呢

<p1><h5 align="center" class="gradient-color">这是一段渐变字体</h5></p1>

***

- 很显然这不是html自己可以做到的，这需要我们手
   动创建css配置文件

- 配置文件表示如下
  
- 将less文件支持的背景颜色编辑用在text文本上达到
渐变的效果
```less
.markdown-preview.markdown-preview {
}
.gradient-color {
  background-image: linear-gradient(to right, #222830, #007E83,#33AC8B);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
```
- 在html中应用配置文件的方法如下所示
```HTML
<p1><h5 align="center" class="gradient-color">这是一段渐变字体</h5></p1>
```
***







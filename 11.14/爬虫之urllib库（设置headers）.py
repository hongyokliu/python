﻿Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
>>> import urllib2
>>> url = 'http://cuiqingcai.com/954.html'
>>> user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
>>> values = {'username' : 'cqc',  'password' : 'XXXX' }
>>> headers = { 'User-Agent' : user_agent }
>>> data = urllib.urlencode(values)
>>> request = urllib2.Request(url, data, headers)
>>> response = urllib2.urlopen(request)
>>> page = response.read()
>>> print page
<!DOCTYPE HTML>
<html>
<head>
<meta charset="UTF-8">
<meta name="baidu-tc-verification" content="0fb041a64ee71333c957d8c784961cc8" />
<meta property="qc:admins" content="145637425211673116375" />
<meta http-equiv="X-UA-Compatible" content="IE=10,IE=9,IE=8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=0, minimum-scale=1.0, maximum-scale=1.0">
<title>Python爬虫入门四之Urllib库的高级用法 | 静觅</title>
<script>
window._deel = {name: '静觅',url: 'http://cuiqingcai.com/wp-content/themes/Yusi', ajaxpager: 'on', commenton: 1, roll: [0,0]}
</script>

<!-- All in One SEO Pack 2.3.12.2.1 by Michael Torbert of Semper Fi Web Design[392,434] -->
<meta name="description"  content="1.设置Headers 有些网站不会同意程序直接用上面的方式进行访问，如果识别有问题，那么站点根本不会响应，所以为了完全模拟浏览器的工作，我们需要设置一些Headers" />

<meta name="keywords"  content="python,爬虫" />

<!-- /all in one seo pack -->
<link rel='dns-prefetch' href='//libs.baidu.com' />
<link rel='dns-prefetch' href='//s.w.org' />
		<script type="text/javascript">
			window._wpemojiSettings = {"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/2.2.1\/72x72\/","ext":".png","svgUrl":"https:\/\/s.w.org\/images\/core\/emoji\/2.2.1\/svg\/","svgExt":".svg","source":{"concatemoji":"http:\/\/cuiqingcai.com\/wp-includes\/js\/wp-emoji-release.min.js?ver=4.7.3"}};
			!function(a,b,c){function d(a){var b,c,d,e,f=String.fromCharCode;if(!k||!k.fillText)return!1;switch(k.clearRect(0,0,j.width,j.height),k.textBaseline="top",k.font="600 32px Arial",a){case"flag":return k.fillText(f(55356,56826,55356,56819),0,0),!(j.toDataURL().length<3e3)&&(k.clearRect(0,0,j.width,j.height),k.fillText(f(55356,57331,65039,8205,55356,57096),0,0),b=j.toDataURL(),k.clearRect(0,0,j.width,j.height),k.fillText(f(55356,57331,55356,57096),0,0),c=j.toDataURL(),b!==c);case"emoji4":return k.fillText(f(55357,56425,55356,57341,8205,55357,56507),0,0),d=j.toDataURL(),k.clearRect(0,0,j.width,j.height),k.fillText(f(55357,56425,55356,57341,55357,56507),0,0),e=j.toDataURL(),d!==e}return!1}function e(a){var c=b.createElement("script");c.src=a,c.defer=c.type="text/javascript",b.getElementsByTagName("head")[0].appendChild(c)}var f,g,h,i,j=b.createElement("canvas"),k=j.getContext&&j.getContext("2d");for(i=Array("flag","emoji4"),c.supports={everything:!0,everythingExceptFlag:!0},h=0;h<i.length;h++)c.supports[i[h]]=d(i[h]),c.supports.everything=c.supports.everything&&c.supports[i[h]],"flag"!==i[h]&&(c.supports.everythingExceptFlag=c.supports.everythingExceptFlag&&c.supports[i[h]]);c.supports.everythingExceptFlag=c.supports.everythingExceptFlag&&!c.supports.flag,c.DOMReady=!1,c.readyCallback=function(){c.DOMReady=!0},c.supports.everything||(g=function(){c.readyCallback()},b.addEventListener?(b.addEventListener("DOMContentLoaded",g,!1),a.addEventListener("load",g,!1)):(a.attachEvent("onload",g),b.attachEvent("onreadystatechange",function(){"complete"===b.readyState&&c.readyCallback()})),f=c.source||{},f.concatemoji?e(f.concatemoji):f.wpemoji&&f.twemoji&&(e(f.twemoji),e(f.wpemoji)))}(window,document,window._wpemojiSettings);
		</script>
		<style type="text/css">
img.wp-smiley,
img.emoji {
	display: inline !important;
	border: none !important;
	box-shadow: none !important;
	height: 1em !important;
	width: 1em !important;
	margin: 0 .07em !important;
	vertical-align: -0.1em !important;
	background: none !important;
	padding: 0 !important;
}
</style>
<link rel='stylesheet' id='crayon-css'  href='http://cuiqingcai.com/wp-content/plugins/crayon-syntax-highlighter/css/min/crayon.min.css?ver=_2.7.2_beta' type='text/css' media='all' />
<link rel='stylesheet' id='crayon-theme-github-css'  href='http://cuiqingcai.com/wp-content/plugins/crayon-syntax-highlighter/themes/github/github.css?ver=_2.7.2_beta' type='text/css' media='all' />
<link rel='stylesheet' id='crayon-font-monaco-css'  href='http://cuiqingcai.com/wp-content/plugins/crayon-syntax-highlighter/fonts/monaco.css?ver=_2.7.2_beta' type='text/css' media='all' />
<link rel='stylesheet' id='page-list-style-css'  href='http://cuiqingcai.com/wp-content/plugins/sitemap/css/page-list.css?ver=4.3' type='text/css' media='all' />
<link rel='stylesheet' id='style-css'  href='http://cuiqingcai.com/wp-content/themes/Yusi/style.css?ver=33' type='text/css' media='all' />
<script type='text/javascript' src='//libs.baidu.com/jquery/1.8.3/jquery.min.js?ver=1.0'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var CrayonSyntaxSettings = {"version":"_2.7.2_beta","is_admin":"0","ajaxurl":"http:\/\/cuiqingcai.com\/wp-admin\/admin-ajax.php","prefix":"crayon-","setting":"crayon-setting","selected":"crayon-setting-selected","changed":"crayon-setting-changed","special":"crayon-setting-special","orig_value":"data-orig-value","debug":""};
var CrayonSyntaxStrings = {"copy":"\u4f7f\u7528 %s \u590d\u5236\uff0c\u4f7f\u7528 %s \u7c98\u8d34\u3002","minimize":"\u70b9\u51fb\u5c55\u5f00\u4ee3\u7801"};
/* ]]> */
</script>
<script type='text/javascript' src='http://cuiqingcai.com/wp-content/plugins/crayon-syntax-highlighter/js/min/crayon.min.js?ver=_2.7.2_beta'></script>
<script type='text/javascript' src='http://cuiqingcai.com/wp-content/themes/Yusi/js/jquery.fitvids.js?ver=2.0.110526'></script>
<link rel='https://api.w.org/' href='http://cuiqingcai.com/wp-json/' />
<link rel='prev' title='Python爬虫入门三之Urllib库的基本使用' href='http://cuiqingcai.com/947.html' />
<link rel='next' title='Python爬虫入门五之URLError异常处理' href='http://cuiqingcai.com/961.html' />
<link rel="canonical" href="http://cuiqingcai.com/954.html" />
<link rel='shortlink' href='http://cuiqingcai.com/?p=954' />
<link rel="alternate" type="application/json+oembed" href="http://cuiqingcai.com/wp-json/oembed/1.0/embed?url=http%3A%2F%2Fcuiqingcai.com%2F954.html" />
<link rel="alternate" type="text/xml+oembed" href="http://cuiqingcai.com/wp-json/oembed/1.0/embed?url=http%3A%2F%2Fcuiqingcai.com%2F954.html&#038;format=xml" />
<meta name="keywords" content="Python, 爬虫, Python">
<meta name="description" content="1.设置Headers 有些网站不会同意程序直接用上面的方式进行访问，如果识别有问题，那么站点根本不会响应，所以为了完全模拟浏览器的工作，我们需要设置一些Headers 的属性。  首先，打开我们的浏览器，调试浏览器F12，我用的是Chrome，打开网络监听，示意如下，比如知乎，点登录之后，我们会发现登陆之后界面都变化了，出现一个新的界面，实质上这个页面包含了许许多多的内容，这些内容也不是一次性就加载完成的，实质上是执行了好多次请求，一">
        <script type="text/javascript">
            jQuery(document).ready( function() {
                jQuery('.video').fitVids();
            });
        </script><!--[if lt IE 9]><script src="http://cuiqingcai.com/wp-content/themes/Yusi/js/html5.js"></script><![endif]-->

<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "//hm.baidu.com/hm.js?3ef185224776ec2561c9f7066ead4f24";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>
<meta name="360-site-verification" content="bdc579accc68a98f1258ebcce2266afa" />
<script type="text/javascript" name="baidu-tc-cerfication" data-appid="5411405" src="http://apps.bdimg.com/cloudaapi/lightapp.js"></script>
<link rel="shortcut icon" type="image/x-icon" href="http://cuiqingcai.com/fav.png" />
<script type="text/javascript" src="http://cuiqingcai.com/wp-content/themes/Yusi/js/main.js"></script>
<script type="text/javascript">

</script>
</head>
<body class="post-template-default single single-post postid-954 single-format-standard">

<header id="header" class="header">
<div class="container-inner">
 <div class="yusi-logo">
                    <a href="/">
                        <h1>
                                                        <span class="yusi-mono">静觅</span>
                                                        <span class="yusi-bloger">崔庆才的个人博客</span>
                                                    </h1>
                    </a>
    </div>
</div>

	<div id="nav-header" class="navbar">
		
		<ul class="nav">
			<li id="menu-item-44" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-home menu-item-44"><a href="http://cuiqingcai.com">首页</a></li>
<li id="menu-item-14" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children menu-item-14"><a href="http://cuiqingcai.com/category/life">生活笔记</a>
<ul class="sub-menu">
	<li id="menu-item-19" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-19"><a href="http://cuiqingcai.com/category/life/notes">个人随笔</a></li>
	<li id="menu-item-18" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-18"><a href="http://cuiqingcai.com/category/life/daily">个人日记</a></li>
	<li id="menu-item-15" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-15"><a href="http://cuiqingcai.com/category/life/presatation">个人展示</a></li>
</ul>
</li>
<li id="menu-item-7" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor menu-item-has-children menu-item-7"><a href="http://cuiqingcai.com/category/technique">技术杂谈</a>
<ul class="sub-menu">
	<li id="menu-item-9" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-9"><a href="http://cuiqingcai.com/category/technique/cc">C/C++</a></li>
	<li id="menu-item-11" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-11"><a href="http://cuiqingcai.com/category/technique/java">Java</a></li>
	<li id="menu-item-17" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-17"><a href="http://cuiqingcai.com/category/technique/php">PHP</a></li>
	<li id="menu-item-153" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-153"><a href="http://cuiqingcai.com/category/technique/html">HTML</a></li>
	<li id="menu-item-960" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent menu-item-960"><a href="http://cuiqingcai.com/category/technique/python">Python</a></li>
	<li id="menu-item-1277" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-1277"><a href="http://cuiqingcai.com/category/technique/javascript">JS</a></li>
	<li id="menu-item-16" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-16"><a href="http://cuiqingcai.com/category/technique/other">Other</a></li>
</ul>
</li>
<li id="menu-item-418" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-418"><a href="http://cuiqingcai.com/category/resources">福利专区</a></li>
<li id="menu-item-851" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-851"><a href="http://cuiqingcai.com/about">关于自己</a></li>
<li id="menu-item-251" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-251"><a href="http://cuiqingcai.com/message">给我留言</a></li>
<li id="menu-item-1131" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1131"><a href="http://cuiqingcai.com/donate">赞助作者</a></li>
<li id="menu-item-4571" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4571"><a href="http://cuiqingcai.com/exchange">技术交流</a></li>
<li style="float:right;">
                    <div class="toggle-search"><i class="fa fa-search"></i></div>
<div class="search-expand" style="display: none;"><div class="search-expand-inner"><form method="get" class="searchform themeform" onsubmit="location.href='http://cuiqingcai.com/?s=' + encodeURIComponent(this.s.value).replace(/%20/g, '+'); return false;" action="/"><div> <input type="ext" class="search" name="s" onblur="if(this.value=='')this.value='search...';" onfocus="if(this.value=='search...')this.value='';" value="search..."></div></form></div></div>
</li>
		</ul>
	</div>
	</div>
</header>
<section class="container"><div class="speedbar">
					<div class="pull-right">
				<i class="fa fa-user"></i> <a href="/wp-login.php?action=register">投稿</a>&nbsp;&nbsp;&nbsp;   <i class="fa fa-power-off"></i> <a href="http://cuiqingcai.com/wp-login.php">登录</a>			</div>
				<div class="toptip"><strong class="text-success"><i class="fa fa-volume-up"></i> </strong>   博主录制的Python3爬虫视频教程已发布！详情请戳<a href="http://cuiqingcai.com/4320.html">Python3爬虫视频教程</a>！希望大家支持！非常感谢！</div>
	</div>
	<div class="banner banner-site"></div><div class="content-wrap">
	<div class="content">
<div class="breadcrumbs"><a title="返回首页" href="http://cuiqingcai.com"><i class="fa fa-home"></i></a> <small>></small> <a href="http://cuiqingcai.com/category/technique">技术杂谈</a> <small>></small> <a href="http://cuiqingcai.com/category/technique/python">Python</a> <small>></small> <span class="muted">Python爬虫入门四之Urllib库的高级用法</span></div>
				<header class="article-header">
			<h1 class="article-title"><a href="http://cuiqingcai.com/954.html">Python爬虫入门四之Urllib库的高级用法</a></h1>
			<div class="meta">
				<span id="mute-category" class="muted"><i class="fa fa-list-alt"></i><a href="http://cuiqingcai.com/category/technique/python"> Python</a></span>				<span class="muted"><i class="fa fa-user"></i> <a href="http://cuiqingcai.com/author/cqcre">崔庆才</a></span>
				<time class="muted"><i class="fa fa-clock-o"></i> 3年前 (2015-02-12)</time>
				<span class="muted"><i class="fa fa-eye"></i> 219183浏览</span>
				<span class="muted"><i class="fa fa-comments-o"></i> <a href="http://cuiqingcai.com/954.html#comments">26评论</a></span>							</div>
		</header>
<div class="banner banner-post"><a href="https://edu.hellobi.com/course/157"><img src="http://qiniu.cuiqingcai.com/wp-content/uploads/2017/04/横图：崔庆才-自己动手，丰衣足食！Python3网络爬虫实战案例.png" /></a>
</div>		<article class="article-content">
			<h2>1.设置Headers</h2>
<p>有些网站不会同意程序直接用上面的方式进行访问，如果识别有问题，那么站点根本不会响应，所以为了完全模拟浏览器的工作，我们需要设置一些Headers 的属性。</p>
<p>首先，打开我们的浏览器，调试浏览器F12，我用的是Chrome，打开网络监听，示意如下，比如知乎，点登录之后，我们会发现登陆之后界面都变化了，出现一个新的界面，实质上这个页面包含了许许多多的内容，这些内容也不是一次性就加载完成的，实质上是执行了好多次请求，一般是首先请求HTML文件，然后加载JS，CSS 等等，经过多次请求之后，网页的骨架和肌肉全了，整个网页的效果也就出来了。</p>
<p><a href="http://qiniu.cuiqingcai.com/wp-content/uploads/2015/02/2015-02-13-013155-的屏幕截图-e1423762350360.png"><img class="alignnone size-large wp-image-950" src="http://qiniu.cuiqingcai.com/wp-content/uploads/2015/02/2015-02-13-013155-的屏幕截图-e1423762350360-1024x424.png" alt="2015-02-13 01:31:55 的屏幕截图" width="1024" height="424" srcset="http://qiniu.cuiqingcai.com/wp-content/uploads/2015/02/2015-02-13-013155-的屏幕截图-e1423762350360-1024x424.png 1024w, http://qiniu.cuiqingcai.com/wp-content/uploads/2015/02/2015-02-13-013155-的屏幕截图-e1423762350360-300x124.png 300w, http://qiniu.cuiqingcai.com/wp-content/uploads/2015/02/2015-02-13-013155-的屏幕截图-e1423762350360.png 1301w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></p>
<p>拆分这些请求，我们只看一第一个请求，你可以看到，有个Request URL，还有headers，下面便是response，图片显示得不全，小伙伴们可以亲身实验一下。那么这个头中包含了许许多多是信息，有文件编码啦，压缩方式啦，请求的agent啦等等。</p>
<p>其中，agent就是请求的身份，如果没有写入请求身份，那么服务器不一定会响应，所以可以在headers中设置agent,例如下面的例子，这个例子只是说明了怎样设置的headers，小伙伴们看一下设置格式就好。</p><!-- Crayon Syntax Highlighter v_2.7.2_beta -->

		<div id="crayon-5a0cfe6b15962883681262" class="crayon-syntax crayon-theme-github crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover wrap" style=" margin-top: 12px; margin-bottom: 12px; float: left; font-size: 12px !important; line-height: 15px !important;">
		
			<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
			<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="切换是否显示行编号"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="纯文本显示代码"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="切换自动换行"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="点击展开代码"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="复制代码"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="在新窗口中显示代码"><div class="crayon-button-icon"></div></div></div></div>
			<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
			<div class="crayon-plain-wrap"><textarea  class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
import urllib  
import urllib2  

url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
values = {'username' : 'cqc',  'password' : 'XXXX' }  
headers = { 'User-Agent' : user_agent }  
data = urllib.urlencode(values)  
request = urllib2.Request(url, data, headers)  
response = urllib2.urlopen(request)  
page = response.read() </textarea></div>
			<div class="crayon-main" style="">
				<table class="crayon-table">
					<tr class="crayon-row">
				<td class="crayon-nums " data-settings="show">
					<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5a0cfe6b15962883681262-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5a0cfe6b15962883681262-2">2</div><div class="crayon-num" data-line="crayon-5a0cfe6b15962883681262-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-5a0cfe6b15962883681262-4">4</div><div class="crayon-num" data-line="crayon-5a0cfe6b15962883681262-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-5a0cfe6b15962883681262-6">6</div><div class="crayon-num" data-line="crayon-5a0cfe6b15962883681262-7">7</div><div class="crayon-num crayon-striped-num" data-line="crayon-5a0cfe6b15962883681262-8">8</div><div class="crayon-num" data-line="crayon-5a0cfe6b15962883681262-9">9</div><div class="crayon-num crayon-striped-num" data-line="crayon-5a0cfe6b15962883681262-10">10</div><div class="crayon-num" data-line="crayon-5a0cfe6b15962883681262-11">11</div></div>
				</td>
						<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5a0cfe6b15962883681262-1"><span class="crayon-e">import </span><span class="crayon-e">urllib&nbsp;&nbsp;</span></div><div class="crayon-line crayon-striped-line" id="crayon-5a0cfe6b15962883681262-2"><span class="crayon-e">import </span><span class="crayon-e">urllib2&nbsp;&nbsp;</span></div><div class="crayon-line" id="crayon-5a0cfe6b15962883681262-3">&nbsp;</div><div class="crayon-line crayon-striped-line" id="crayon-5a0cfe6b15962883681262-4"><span class="crayon-v">url</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-s">'http://www.server.com/login'</span></div><div class="crayon-line" id="crayon-5a0cfe6b15962883681262-5"><span class="crayon-v">user_agent</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-s">'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'</span><span class="crayon-h">&nbsp;&nbsp;</span></div><div class="crayon-line crayon-striped-line" id="crayon-5a0cfe6b15962883681262-6"><span class="crayon-v">values</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-sy">{</span><span class="crayon-s">'username'</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-s">'cqc'</span><span class="crayon-sy">,</span><span class="crayon-h">&nbsp;&nbsp;</span><span class="crayon-s">'password'</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-s">'XXXX'</span><span class="crayon-h"> </span><span class="crayon-sy">}</span><span class="crayon-h">&nbsp;&nbsp;</span></div><div class="crayon-line" id="crayon-5a0cfe6b15962883681262-7"><span class="crayon-v">headers</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-sy">{</span><span class="crayon-h"> </span><span class="crayon-s">'User-Agent'</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-v">user</span><span class="crayon-sy">_</span>agent<span class="crayon-h"> </span><span class="crayon-sy">}</span><span class="crayon-h">&nbsp;&nbsp;</span></div><div class="crayon-line crayon-striped-line" id="crayon-5a0cfe6b15962883681262-8"><span class="crayon-v">data</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-v">urllib</span><span class="crayon-sy">.</span><span class="crayon-e">urlencode</span><span class="crayon-sy">(</span><span class="crayon-v">values</span><span class="crayon-sy">)</span><span class="crayon-h">&nbsp;&nbsp;</span></div><div class="crayon-line" id="crayon-5a0cfe6b15962883681262-9"><span class="crayon-v">request</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-v">urllib2</span><span class="crayon-sy">.</span><span class="crayon-e">Request</span><span class="crayon-sy">(</span><span class="crayon-v">url</span><span class="crayon-sy">,</span><span class="crayon-h"> </span><span class="crayon-v">data</span><span class="crayon-sy">,</span><span class="crayon-h"> </span><span class="crayon-v">headers</span><span class="crayon-sy">)</span><span class="crayon-h">&nbsp;&nbsp;</span></div><div class="crayon-line crayon-striped-line" id="crayon-5a0cfe6b15962883681262-10"><span class="crayon-v">response</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-v">urllib2</span><span class="crayon-sy">.</span><span class="crayon-e">urlopen</span><span class="crayon-sy">(</span><span class="crayon-v">request</span><span class="crayon-sy">)</span><span class="crayon-h">&nbsp;&nbsp;</span></div><div class="crayon-line" id="crayon-5a0cfe6b15962883681262-11"><span class="crayon-v">page</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-v">response</span><span class="crayon-sy">.</span><span class="crayon-e">read</span><span class="crayon-sy">(</span><span class="crayon-sy">)</span><span class="crayon-h"> </span></div></div></td>
					</tr>
				</table>
			</div>
		</div>
<!-- [Format Time: 0.0014 seconds] -->
<p>这样，我们设置了一个headers，在构建request时传入，在请求时，就加入了headers传送，服务器若识别了是浏览器发来的请求，就会得到响应。</p>
<p>另外，我们还有<strong>对付&#8221;反盗链&#8221;</strong>的方式，对付防盗链，服务器会识别headers中的referer是不是它自己，如果不是，有的服务器不会响应，所以我们还可以在headers中加入referer</p>
<p>例如我们可以构建下面的headers</p><!-- Crayon Syntax Highlighter v_2.7.2_beta -->

		<div id="crayon-5a0cfe6b1596c939405815" class="crayon-syntax crayon-theme-github crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover wrap" style=" margin-top: 12px; margin-bottom: 12px; float: left; font-size: 12px !important; line-height: 15px !important;">
		
			<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
			<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="切换是否显示行编号"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="纯文本显示代码"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="切换自动换行"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="点击展开代码"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="复制代码"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="在新窗口中显示代码"><div class="crayon-button-icon"></div></div></div></div>
			<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
			<div class="crayon-plain-wrap"><textarea  class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  ,
                        'Referer':'http://www.zhihu.com/articles' }  </textarea></div>
			<div class="crayon-main" style="">
				<table class="crayon-table">
					<tr class="crayon-row">
				<td class="crayon-nums " data-settings="show">
					<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5a0cfe6b1596c939405815-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5a0cfe6b1596c939405815-2">2</div></div>
				</td>
						<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5a0cfe6b1596c939405815-1"><span class="crayon-v">headers</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-sy">{</span><span class="crayon-h"> </span><span class="crayon-s">'User-Agent'</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-s">'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'</span><span class="crayon-h">&nbsp;&nbsp;</span><span class="crayon-sy">,</span></div><div class="crayon-line crayon-striped-line" id="crayon-5a0cfe6b1596c939405815-2"><span class="crayon-h">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="crayon-s">'Referer'</span><span class="crayon-o">:</span><span class="crayon-s">'http://www.zhihu.com/articles'</span><span class="crayon-h"> </span><span class="crayon-sy">}</span><span class="crayon-h">&nbsp;&nbsp;</span></div></div></td>
					</tr>
				</table>
			</div>
		</div>
<!-- [Format Time: 0.0003 seconds] -->
<p>同上面的方法，在传送请求时把headers传入Request参数里，这样就能应付防盗链了。</p>
<p>另外headers的一些属性，下面的需要特别注意一下：</p>
<blockquote><p>User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求<br />
Content-Type : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。<br />
application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用<br />
application/json ： 在 JSON RPC 调用时使用<br />
application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用<br />
在使用服务器提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务</p></blockquote>
<p>其他的有必要的可以审查浏览器的headers内容，在构建时写入同样的数据即可。</p>
<h2><strong>2. Proxy（代理）的设置</strong></h2>
<p>urllib2 默认会使用环境变量 http_proxy 来设置 HTTP Proxy。假如一个网站它会检测某一段时间某个IP 的访问次数，如果访问次数过多，它会禁止你的访问。所以你可以设置一些代理服务器来帮助你做工作，每隔一段时间换一个代理，网站君都不知道是谁在捣鬼了，这酸爽！</p>
<p>下面一段代码说明了代理的设置用法</p><!-- Crayon Syntax Highlighter v_2.7.2_beta -->

		<div id="crayon-5a0cfe6b15970049667744" class="crayon-syntax crayon-theme-github crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover wrap" style=" margin-top: 12px; margin-bottom: 12px; float: left; font-size: 12px !important; line-height: 15px !important;">
		
			<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
			<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="切换是否显示行编号"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="纯文本显示代码"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="切换自动换行"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="点击展开代码"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="复制代码"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="在新窗口中显示代码"><div class="crayon-button-icon"></div></div></div></div>
			<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
			<div class="crayon-plain-wrap"><textarea  class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
import urllib2
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)</textarea></div>
			<div class="crayon-main" style="">
				<table class="crayon-table">
					<tr class="crayon-row">
				<td class="crayon-nums " data-settings="show">
					<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5a0cfe6b15970049667744-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5a0cfe6b15970049667744-2">2</div><div class="crayon-num" data-line="crayon-5a0cfe6b15970049667744-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-5a0cfe6b15970049667744-4">4</div><div class="crayon-num" data-line="crayon-5a0cfe6b15970049667744-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-5a0cfe6b15970049667744-6">6</div><div class="crayon-num" data-line="crayon-5a0cfe6b15970049667744-7">7</div><div class="crayon-num crayon-striped-num" data-line="crayon-5a0cfe6b15970049667744-8">8</div><div class="crayon-num" data-line="crayon-5a0cfe6b15970049667744-9">9</div></div>
				</td>
						<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5a0cfe6b15970049667744-1"><span class="crayon-e">import </span><span class="crayon-e">urllib2</span></div><div class="crayon-line crayon-striped-line" id="crayon-5a0cfe6b15970049667744-2"><span class="crayon-v">enable_proxy</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-t">True</span></div><div class="crayon-line" id="crayon-5a0cfe6b15970049667744-3"><span class="crayon-v">proxy_handler</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-v">urllib2</span><span class="crayon-sy">.</span><span class="crayon-e">ProxyHandler</span><span class="crayon-sy">(</span><span class="crayon-sy">{</span><span class="crayon-s">"http"</span><span class="crayon-h"> </span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-s">'http://some-proxy.com:8080'</span><span class="crayon-sy">}</span><span class="crayon-sy">)</span></div><div class="crayon-line crayon-striped-line" id="crayon-5a0cfe6b15970049667744-4"><span class="crayon-v">null_proxy_handler</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-v">urllib2</span><span class="crayon-sy">.</span><span class="crayon-e">ProxyHandler</span><span class="crayon-sy">(</span><span class="crayon-sy">{</span><span class="crayon-sy">}</span><span class="crayon-sy">)</span></div><div class="crayon-line" id="crayon-5a0cfe6b15970049667744-5"><span class="crayon-st">if</span><span class="crayon-h"> </span><span class="crayon-v">enable_proxy</span><span class="crayon-o">:</span></div><div class="crayon-line crayon-striped-line" id="crayon-5a0cfe6b15970049667744-6"><span class="crayon-h">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="crayon-v">opener</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-v">urllib2</span><span class="crayon-sy">.</span><span class="crayon-e">build_opener</span><span class="crayon-sy">(</span><span class="crayon-v">proxy_handler</span><span class="crayon-sy">)</span></div><div class="crayon-line" id="crayon-5a0cfe6b15970049667744-7"><span class="crayon-st">else</span><span class="crayon-o">:</span></div><div class="crayon-line crayon-striped-line" id="crayon-5a0cfe6b15970049667744-8"><span class="crayon-h">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="crayon-v">opener</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-v">urllib2</span><span class="crayon-sy">.</span><span class="crayon-e">build_opener</span><span class="crayon-sy">(</span><span class="crayon-v">null_proxy_handler</span><span class="crayon-sy">)</span></div><div class="crayon-line" id="crayon-5a0cfe6b15970049667744-9"><span class="crayon-v">urllib2</span><span class="crayon-sy">.</span><span class="crayon-e">install_opener</span><span class="crayon-sy">(</span><span class="crayon-v">opener</span><span class="crayon-sy">)</span></div></div></td>
					</tr>
				</table>
			</div>
		</div>
<!-- [Format Time: 0.0009 seconds] -->
<p></p>
<h2>3.<strong>Timeout 设置</strong></h2>
<p>上一节已经说过urlopen方法了，第三个参数就是timeout的设置，可以设置等待多久超时，为了解决一些网站实在响应过慢而造成的影响。</p>
<p>例如下面的代码,如果第二个参数data为空那么要特别指定是timeout是多少，写明形参，如果data已经传入，则不必声明。</p><!-- Crayon Syntax Highlighter v_2.7.2_beta -->

		<div id="crayon-5a0cfe6b15974064863818" class="crayon-syntax crayon-theme-github crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover wrap" style=" margin-top: 12px; margin-bottom: 12px; float: left; font-size: 12px !important; line-height: 15px !important;">
		
			<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
			<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="切换是否显示行编号"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="纯文本显示代码"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="切换自动换行"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="点击展开代码"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="复制代码"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="在新窗口中显示代码"><div class="crayon-button-icon"></div></div></div></div>
			<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
			<div class="crayon-plain-wrap"><textarea  class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
import urllib2
response = urllib2.urlopen('http://www.baidu.com', timeout=10)</textarea></div>
			<div class="crayon-main" style="">
				<table class="crayon-table">
					<tr class="crayon-row">
				<td class="crayon-nums " data-settings="show">
					<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5a0cfe6b15974064863818-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5a0cfe6b15974064863818-2">2</div></div>
				</td>
						<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5a0cfe6b15974064863818-1"><span class="crayon-e">import </span><span class="crayon-e">urllib2</span></div><div class="crayon-line crayon-striped-line" id="crayon-5a0cfe6b15974064863818-2"><span class="crayon-v">response</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-v">urllib2</span><span class="crayon-sy">.</span><span class="crayon-e">urlopen</span><span class="crayon-sy">(</span><span class="crayon-s">'http://www.baidu.com'</span><span class="crayon-sy">,</span><span class="crayon-h"> </span><span class="crayon-v">timeout</span><span class="crayon-o">=</span><span class="crayon-cn">10</span><span class="crayon-sy">)</span></div></div></td>
					</tr>
				</table>
			</div>
		</div>
<!-- [Format Time: 0.0003 seconds] -->
<p></p><!-- Crayon Syntax Highlighter v_2.7.2_beta -->

		<div id="crayon-5a0cfe6b15977580491452" class="crayon-syntax crayon-theme-github crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover wrap" style=" margin-top: 12px; margin-bottom: 12px; float: left; font-size: 12px !important; line-height: 15px !important;">
		
			<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
			<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="切换是否显示行编号"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="纯文本显示代码"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="切换自动换行"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="点击展开代码"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="复制代码"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="在新窗口中显示代码"><div class="crayon-button-icon"></div></div></div></div>
			<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
			<div class="crayon-plain-wrap"><textarea  class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
import urllib2
response = urllib2.urlopen('http://www.baidu.com',data, 10)</textarea></div>
			<div class="crayon-main" style="">
				<table class="crayon-table">
					<tr class="crayon-row">
				<td class="crayon-nums " data-settings="show">
					<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5a0cfe6b15977580491452-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5a0cfe6b15977580491452-2">2</div></div>
				</td>
						<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5a0cfe6b15977580491452-1"><span class="crayon-e">import </span><span class="crayon-e">urllib2</span></div><div class="crayon-line crayon-striped-line" id="crayon-5a0cfe6b15977580491452-2"><span class="crayon-v">response</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-v">urllib2</span><span class="crayon-sy">.</span><span class="crayon-e">urlopen</span><span class="crayon-sy">(</span><span class="crayon-s">'http://www.baidu.com'</span><span class="crayon-sy">,</span><span class="crayon-v">data</span><span class="crayon-sy">,</span><span class="crayon-h"> </span><span class="crayon-cn">10</span><span class="crayon-sy">)</span></div></div></td>
					</tr>
				</table>
			</div>
		</div>
<!-- [Format Time: 0.0003 seconds] -->
<p></p>
<h2><strong>4.使用 HTTP 的 PUT 和 DELETE 方法</strong></h2>
<p>http协议有六种请求方法，get,head,put,delete,post,options，我们有时候需要用到PUT方式或者DELETE方式请求。</p>
<blockquote><p>PUT：这个方法比较少见。HTML表单也不支持这个。本质上来讲， PUT和POST极为相似，都是向服务器发送数据，但它们之间有一个重要区别，PUT通常指定了资源的存放位置，而POST则没有，POST的数据存放位置由服务器自己决定。<br />
DELETE：删除某一个资源。基本上这个也很少见，不过还是有一些地方比如amazon的S3云服务里面就用的这个方法来删除资源。</p></blockquote>
<p>如果要使用 HTTP PUT 和 DELETE ，只能使用比较低层的 httplib 库。虽然如此，我们还是能通过下面的方式，使 urllib2 能够发出 PUT 或DELETE 的请求，不过用的次数的确是少，在这里提一下。</p><!-- Crayon Syntax Highlighter v_2.7.2_beta -->

		<div id="crayon-5a0cfe6b1597b556412037" class="crayon-syntax crayon-theme-github crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover wrap" style=" margin-top: 12px; margin-bottom: 12px; float: left; font-size: 12px !important; line-height: 15px !important;">
		
			<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
			<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="切换是否显示行编号"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="纯文本显示代码"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="切换自动换行"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="点击展开代码"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="复制代码"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="在新窗口中显示代码"><div class="crayon-button-icon"></div></div></div></div>
			<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
			<div class="crayon-plain-wrap"><textarea  class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
import urllib2
request = urllib2.Request(uri, data=data)
request.get_method = lambda: 'PUT' # or 'DELETE'
response = urllib2.urlopen(request)</textarea></div>
			<div class="crayon-main" style="">
				<table class="crayon-table">
					<tr class="crayon-row">
				<td class="crayon-nums " data-settings="show">
					<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5a0cfe6b1597b556412037-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5a0cfe6b1597b556412037-2">2</div><div class="crayon-num" data-line="crayon-5a0cfe6b1597b556412037-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-5a0cfe6b1597b556412037-4">4</div></div>
				</td>
						<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5a0cfe6b1597b556412037-1"><span class="crayon-e">import </span><span class="crayon-e">urllib2</span></div><div class="crayon-line crayon-striped-line" id="crayon-5a0cfe6b1597b556412037-2"><span class="crayon-v">request</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-v">urllib2</span><span class="crayon-sy">.</span><span class="crayon-e">Request</span><span class="crayon-sy">(</span><span class="crayon-v">uri</span><span class="crayon-sy">,</span><span class="crayon-h"> </span><span class="crayon-v">data</span><span class="crayon-o">=</span><span class="crayon-v">data</span><span class="crayon-sy">)</span></div><div class="crayon-line" id="crayon-5a0cfe6b1597b556412037-3"><span class="crayon-v">request</span><span class="crayon-sy">.</span><span class="crayon-v">get_method</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-v">lambda</span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-s">'PUT'</span><span class="crayon-h"> </span><span class="crayon-p"># or 'DELETE'</span></div><div class="crayon-line crayon-striped-line" id="crayon-5a0cfe6b1597b556412037-4"><span class="crayon-v">response</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-v">urllib2</span><span class="crayon-sy">.</span><span class="crayon-e">urlopen</span><span class="crayon-sy">(</span><span class="crayon-v">request</span><span class="crayon-sy">)</span></div></div></td>
					</tr>
				</table>
			</div>
		</div>
<!-- [Format Time: 0.0006 seconds] -->
<p></p>
<h2> 5.使用DebugLog</h2>
<p>可以通过下面的方法把 Debug Log 打开，这样收发包的内容就会在屏幕上打印出来，方便调试，这个也不太常用，仅提一下</p><!-- Crayon Syntax Highlighter v_2.7.2_beta -->

		<div id="crayon-5a0cfe6b1597e073075660" class="crayon-syntax crayon-theme-github crayon-font-monaco crayon-os-pc print-yes notranslate" data-settings=" minimize scroll-mouseover wrap" style=" margin-top: 12px; margin-bottom: 12px; float: left; font-size: 12px !important; line-height: 15px !important;">
		
			<div class="crayon-toolbar" data-settings=" mouseover overlay hide delay" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><span class="crayon-title"></span>
			<div class="crayon-tools" style="font-size: 12px !important;height: 18px !important; line-height: 18px !important;"><div class="crayon-button crayon-nums-button" title="切换是否显示行编号"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-plain-button" title="纯文本显示代码"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-wrap-button" title="切换自动换行"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-expand-button" title="点击展开代码"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-copy-button" title="复制代码"><div class="crayon-button-icon"></div></div><div class="crayon-button crayon-popup-button" title="在新窗口中显示代码"><div class="crayon-button-icon"></div></div></div></div>
			<div class="crayon-info" style="min-height: 16.8px !important; line-height: 16.8px !important;"></div>
			<div class="crayon-plain-wrap"><textarea  class="crayon-plain print-no" data-settings="dblclick" readonly style="-moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4; font-size: 12px !important; line-height: 15px !important;">
import urllib2
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')</textarea></div>
			<div class="crayon-main" style="">
				<table class="crayon-table">
					<tr class="crayon-row">
				<td class="crayon-nums " data-settings="show">
					<div class="crayon-nums-content" style="font-size: 12px !important; line-height: 15px !important;"><div class="crayon-num" data-line="crayon-5a0cfe6b1597e073075660-1">1</div><div class="crayon-num crayon-striped-num" data-line="crayon-5a0cfe6b1597e073075660-2">2</div><div class="crayon-num" data-line="crayon-5a0cfe6b1597e073075660-3">3</div><div class="crayon-num crayon-striped-num" data-line="crayon-5a0cfe6b1597e073075660-4">4</div><div class="crayon-num" data-line="crayon-5a0cfe6b1597e073075660-5">5</div><div class="crayon-num crayon-striped-num" data-line="crayon-5a0cfe6b1597e073075660-6">6</div></div>
				</td>
						<td class="crayon-code"><div class="crayon-pre" style="font-size: 12px !important; line-height: 15px !important; -moz-tab-size:4; -o-tab-size:4; -webkit-tab-size:4; tab-size:4;"><div class="crayon-line" id="crayon-5a0cfe6b1597e073075660-1"><span class="crayon-e">import </span><span class="crayon-e">urllib2</span></div><div class="crayon-line crayon-striped-line" id="crayon-5a0cfe6b1597e073075660-2"><span class="crayon-v">httpHandler</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-v">urllib2</span><span class="crayon-sy">.</span><span class="crayon-e">HTTPHandler</span><span class="crayon-sy">(</span><span class="crayon-v">debuglevel</span><span class="crayon-o">=</span><span class="crayon-cn">1</span><span class="crayon-sy">)</span></div><div class="crayon-line" id="crayon-5a0cfe6b1597e073075660-3"><span class="crayon-v">httpsHandler</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-v">urllib2</span><span class="crayon-sy">.</span><span class="crayon-e">HTTPSHandler</span><span class="crayon-sy">(</span><span class="crayon-v">debuglevel</span><span class="crayon-o">=</span><span class="crayon-cn">1</span><span class="crayon-sy">)</span></div><div class="crayon-line crayon-striped-line" id="crayon-5a0cfe6b1597e073075660-4"><span class="crayon-v">opener</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-v">urllib2</span><span class="crayon-sy">.</span><span class="crayon-e">build_opener</span><span class="crayon-sy">(</span><span class="crayon-v">httpHandler</span><span class="crayon-sy">,</span><span class="crayon-h"> </span><span class="crayon-v">httpsHandler</span><span class="crayon-sy">)</span></div><div class="crayon-line" id="crayon-5a0cfe6b1597e073075660-5"><span class="crayon-v">urllib2</span><span class="crayon-sy">.</span><span class="crayon-e">install_opener</span><span class="crayon-sy">(</span><span class="crayon-v">opener</span><span class="crayon-sy">)</span></div><div class="crayon-line crayon-striped-line" id="crayon-5a0cfe6b1597e073075660-6"><span class="crayon-v">response</span><span class="crayon-h"> </span><span class="crayon-o">=</span><span class="crayon-h"> </span><span class="crayon-v">urllib2</span><span class="crayon-sy">.</span><span class="crayon-e">urlopen</span><span class="crayon-sy">(</span><span class="crayon-s">'http://www.baidu.com'</span><span class="crayon-sy">)</span></div></div></td>
					</tr>
				</table>
			</div>
		</div>
<!-- [Format Time: 0.0008 seconds] -->
<p>以上便是一部分高级特性，前三个是重要内容，在后面，还有cookies的设置还有异常的处理，小伙伴们加油！</p>
<p>转载请注明：<a href="http://cuiqingcai.com">静觅</a> &raquo; <a href="http://cuiqingcai.com/954.html">Python爬虫入门四之Urllib库的高级用法</a></p>

      
<div class="article-social">
			<a href="javascript:;" data-action="ding" data-id="954" id="Addlike" class="action"><i class="fa fa-heart-o"></i>喜欢 (<span class="count">768</span>)</a><span class="or">or</span><span class="action action-share bdsharebuttonbox"><i class="fa fa-share-alt"></i>分享 (<span class="bds_count" data-cmd="count" title="累计分享0次">0</span>)<div class="action-popover"><div class="popover top in"><div class="arrow"></div><div class="popover-content"><a href="#" class="sinaweibo fa fa-weibo" data-cmd="tsina" title="分享到新浪微博"></a><a href="#" class="bds_qzone fa fa-star" data-cmd="qzone" title="分享到QQ空间"></a><a href="#" class="tencentweibo fa fa-tencent-weibo" data-cmd="tqq" title="分享到腾讯微博"></a><a href="#" class="qq fa fa-qq" data-cmd="sqq" title="分享到QQ好友"></a><a href="#" class="bds_renren fa fa-renren" data-cmd="renren" title="分享到人人网"></a><a href="#" class="bds_weixin fa fa-weixin" data-cmd="weixin" title="分享到微信"></a><a href="#" class="bds_more fa fa-ellipsis-h" data-cmd="more"></a></div></div></div></span>	
</div>
	</article>	
				<div style="background:#fff;padding-bottom:20px;font-size:14px;">
			<p style="text-align: center;margin-bottom:20px;padding:0px 20px">您的支持是博主写作最大的动力，如果您喜欢我的文章，感觉我的文章对您有帮助，请狠狠点击下面的</p>
			<p style="text-align: center;"><a href="http://cuiqingcai.com/donate"> <input style="width: 310px; margin: 10px auto 0px; background-color: #f58a87; color: #ffffff; height: 40px; border: none; font-family: 'Microsoft Yahei'; font-size: 16px; letter-spacing: 2px;" type="button" value="我要小额赞助" /></a>
		</div>
		<div class="">
    <div id="qrcodes">
        <div class="row">
            <div class="col-xs-12 col-md-4">
                <div class="p-sm" style="overflow: hidden; padding-bottom: 15px;">
                    <p class="text-center">想结交更多的朋友吗?</p>
                    <p class="text-center">来进击的Coder瞧瞧吧</p>
                    <div class="text-center">
                        <img class="code-img"
                             src="http://qiniu.cuiqingcai.com/wp-content/uploads/2017/05/QRCode1.png"/>
                    </div>
                    <div class="text-center">
                        <p style="color: #e9415a; font-size: 15px;">进击的Coder</p>
                        <p>
                            <span>QQ群号 </span><span style="color: #e9415a; font-size: 15px; margin-bottom: 45px;"> 99350970  </span><a class="btn btn-xs btn-danger"
                                                                                                                                       href="http://shang.qq.com/wpa/qunwpa?idkey=31ed8a7d15339353ad090379bb9243118f90220324a7a0f4b453bce52dcd02b6"
                                                                                                                                       target="_blank">立即加入</a>
                        </p>
                    </div>
                </div>
            </div>

            <div class="col-xs-12 col-md-4">
                <div class="p-sm" style="overflow: hidden; padding-bottom: 15px;">
                    <p class="text-center">进击的Coder灌水太多?</p>
                    <p class="text-center">这里是纯粹的技术领地</p>
                    <div class="text-center">
                        <img class="code-img"
                             src="http://qiniu.cuiqingcai.com/wp-content/uploads/2017/05/QRCode2.png"/>
                    </div>
                    <div class="text-center">
                        <p style="color: #18A57D; font-size: 15px;">激进的Coder</p>
                        <p>
                            <span>QQ群号 </span><span style="color: #18A57D; font-size: 15px; margin-bottom: 45px;"> 627725766  </span><a target="_blank" class="btn btn-xs" style="background-color: #18A57D"
                                                                                                                                        href="//shang.qq.com/wpa/qunwpa?idkey=6096ee3de52a5a948a9fe45178ed9e9ba9084b909815c5f7775b85f4734fdda1">立即加入</a>
                        </p>
                    </div>
                </div>
            </div>
            <div class="col-xs-12 col-md-4">
                <div class="p-sm" style="overflow: hidden; padding-bottom: 15px;">
                    <p class="text-center">想找人聊天解闷？想要学习干货？</p>
                    <p class="text-center">微信公众号进击的Coder为你打造</p>
                    <div class="text-center">
                        <img class="code-img"
                             src="http://qiniu.cuiqingcai.com/wp-content/uploads/2017/05/qrcode_for_gh_5b0546ddd2d0_430.jpg"/>
                    </div>
                    <div class="text-center">
                        <p style="color: #e9415a; font-size: 15px;">进击的Coder</p>
                        <p>
                            <span>微信公众号 </span><span style="color: #e9415a; font-size: 15px; margin-bottom: 45px;"> 扫一扫关注</span>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <style>
    #qrcodes {
        min-height: 350px;
    background: white;
    }
    #qrcodes .btn {
        background-color: #eb586f;
        height: 22px;
        line-height: 22px !important;
        font-size: 12px;
        color: white;padding: initial;font-size: 12px;width: 65px;
    }
    .article-content #qrcodes{
        text-indent: 0px !important;
    }
    .article-content #qrcodes a {
        color: white;
    }
    #qrcodes .btn:hover {
        color: white;
    }
    #qrcodes .code-img {
        width: 180px;
    }
    </style>
    <style>
        #qrcodes * {
            -webkit-box-sizing: border-box;
            -moz-box-sizing: border-box;
            box-sizing: border-box;
        }
        *:before,
        *:after {
            -webkit-box-sizing: border-box;
            -moz-box-sizing: border-box;
            box-sizing: border-box;
        }
        .row {
            margin-right: -15px;
            margin-left: -15px;
        }
        .col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
            position: relative;
            min-height: 1px;
            padding-right: 15px;
            padding-left: 15px;
        }
        .col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
            float: left;
        }
        .col-xs-12 {
            width: 100%;
        }
        .col-xs-11 {
            width: 91.66666667%;
        }
        .col-xs-10 {
            width: 83.33333333%;
        }
        .col-xs-9 {
            width: 75%;
        }
        .col-xs-8 {
            width: 66.66666667%;
        }
        .col-xs-7 {
            width: 58.33333333%;
        }
        .col-xs-6 {
            width: 50%;
        }
        .col-xs-5 {
            width: 41.66666667%;
        }
        .col-xs-4 {
            width: 33.33333333%;
        }
        .col-xs-3 {
            width: 25%;
        }
        .col-xs-2 {
            width: 16.66666667%;
        }
        .col-xs-1 {
            width: 8.33333333%;
        }
        .col-xs-pull-12 {
            right: 100%;
        }
        .col-xs-pull-11 {
            right: 91.66666667%;
        }
        .col-xs-pull-10 {
            right: 83.33333333%;
        }
        .col-xs-pull-9 {
            right: 75%;
        }
        .col-xs-pull-8 {
            right: 66.66666667%;
        }
        .col-xs-pull-7 {
            right: 58.33333333%;
        }
        .col-xs-pull-6 {
            right: 50%;
        }
        .col-xs-pull-5 {
            right: 41.66666667%;
        }
        .col-xs-pull-4 {
            right: 33.33333333%;
        }
        .col-xs-pull-3 {
            right: 25%;
        }
        .col-xs-pull-2 {
            right: 16.66666667%;
        }
        .col-xs-pull-1 {
            right: 8.33333333%;
        }
        .col-xs-pull-0 {
            right: auto;
        }
        .col-xs-push-12 {
            left: 100%;
        }
        .col-xs-push-11 {
            left: 91.66666667%;
        }
        .col-xs-push-10 {
            left: 83.33333333%;
        }
        .col-xs-push-9 {
            left: 75%;
        }
        .col-xs-push-8 {
            left: 66.66666667%;
        }
        .col-xs-push-7 {
            left: 58.33333333%;
        }
        .col-xs-push-6 {
            left: 50%;
        }
        .col-xs-push-5 {
            left: 41.66666667%;
        }
        .col-xs-push-4 {
            left: 33.33333333%;
        }
        .col-xs-push-3 {
            left: 25%;
        }
        .col-xs-push-2 {
            left: 16.66666667%;
        }
        .col-xs-push-1 {
            left: 8.33333333%;
        }
        .col-xs-push-0 {
            left: auto;
        }
        .col-xs-offset-12 {
            margin-left: 100%;
        }
        .col-xs-offset-11 {
            margin-left: 91.66666667%;
        }
        .col-xs-offset-10 {
            margin-left: 83.33333333%;
        }
        .col-xs-offset-9 {
            margin-left: 75%;
        }
        .col-xs-offset-8 {
            margin-left: 66.66666667%;
        }
        .col-xs-offset-7 {
            margin-left: 58.33333333%;
        }
        .col-xs-offset-6 {
            margin-left: 50%;
        }
        .col-xs-offset-5 {
            margin-left: 41.66666667%;
        }
        .col-xs-offset-4 {
            margin-left: 33.33333333%;
        }
        .col-xs-offset-3 {
            margin-left: 25%;
        }
        .col-xs-offset-2 {
            margin-left: 16.66666667%;
        }
        .col-xs-offset-1 {
            margin-left: 8.33333333%;
        }
        .col-xs-offset-0 {
            margin-left: 0;
        }
        @media (min-width: 768px) {
            .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
                float: left;
            }
            .col-sm-12 {
                width: 100%;
            }
            .col-sm-11 {
                width: 91.66666667%;
            }
            .col-sm-10 {
                width: 83.33333333%;
            }
            .col-sm-9 {
                width: 75%;
            }
            .col-sm-8 {
                width: 66.66666667%;
            }
            .col-sm-7 {
                width: 58.33333333%;
            }
            .col-sm-6 {
                width: 50%;
            }
            .col-sm-5 {
                width: 41.66666667%;
            }
            .col-sm-4 {
                width: 33.33333333%;
            }
            .col-sm-3 {
                width: 25%;
            }
            .col-sm-2 {
                width: 16.66666667%;
            }
            .col-sm-1 {
                width: 8.33333333%;
            }
            .col-sm-pull-12 {
                right: 100%;
            }
            .col-sm-pull-11 {
                right: 91.66666667%;
            }
            .col-sm-pull-10 {
                right: 83.33333333%;
            }
            .col-sm-pull-9 {
                right: 75%;
            }
            .col-sm-pull-8 {
                right: 66.66666667%;
            }
            .col-sm-pull-7 {
                right: 58.33333333%;
            }
            .col-sm-pull-6 {
                right: 50%;
            }
            .col-sm-pull-5 {
                right: 41.66666667%;
            }
            .col-sm-pull-4 {
                right: 33.33333333%;
            }
            .col-sm-pull-3 {
                right: 25%;
            }
            .col-sm-pull-2 {
                right: 16.66666667%;
            }
            .col-sm-pull-1 {
                right: 8.33333333%;
            }
            .col-sm-pull-0 {
                right: auto;
            }
            .col-sm-push-12 {
                left: 100%;
            }
            .col-sm-push-11 {
                left: 91.66666667%;
            }
            .col-sm-push-10 {
                left: 83.33333333%;
            }
            .col-sm-push-9 {
                left: 75%;
            }
            .col-sm-push-8 {
                left: 66.66666667%;
            }
            .col-sm-push-7 {
                left: 58.33333333%;
            }
            .col-sm-push-6 {
                left: 50%;
            }
            .col-sm-push-5 {
                left: 41.66666667%;
            }
            .col-sm-push-4 {
                left: 33.33333333%;
            }
            .col-sm-push-3 {
                left: 25%;
            }
            .col-sm-push-2 {
                left: 16.66666667%;
            }
            .col-sm-push-1 {
                left: 8.33333333%;
            }
            .col-sm-push-0 {
                left: auto;
            }
            .col-sm-offset-12 {
                margin-left: 100%;
            }
            .col-sm-offset-11 {
                margin-left: 91.66666667%;
            }
            .col-sm-offset-10 {
                margin-left: 83.33333333%;
            }
            .col-sm-offset-9 {
                margin-left: 75%;
            }
            .col-sm-offset-8 {
                margin-left: 66.66666667%;
            }
            .col-sm-offset-7 {
                margin-left: 58.33333333%;
            }
            .col-sm-offset-6 {
                margin-left: 50%;
            }
            .col-sm-offset-5 {
                margin-left: 41.66666667%;
            }
            .col-sm-offset-4 {
                margin-left: 33.33333333%;
            }
            .col-sm-offset-3 {
                margin-left: 25%;
            }
            .col-sm-offset-2 {
                margin-left: 16.66666667%;
            }
            .col-sm-offset-1 {
                margin-left: 8.33333333%;
            }
            .col-sm-offset-0 {
                margin-left: 0;
            }
        }
        @media (min-width: 992px) {
            .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
                float: left;
            }
            .col-md-12 {
                width: 100%;
            }
            .col-md-11 {
                width: 91.66666667%;
            }
            .col-md-10 {
                width: 83.33333333%;
            }
            .col-md-9 {
                width: 75%;
            }
            .col-md-8 {
                width: 66.66666667%;
            }
            .col-md-7 {
                width: 58.33333333%;
            }
            .col-md-6 {
                width: 50%;
            }
            .col-md-5 {
                width: 41.66666667%;
            }
            .col-md-4 {
                width: 33.33333333%;
            }
            .col-md-3 {
                width: 25%;
            }
            .col-md-2 {
                width: 16.66666667%;
            }
            .col-md-1 {
                width: 8.33333333%;
            }
            .col-md-pull-12 {
                right: 100%;
            }
            .col-md-pull-11 {
                right: 91.66666667%;
            }
            .col-md-pull-10 {
                right: 83.33333333%;
            }
            .col-md-pull-9 {
                right: 75%;
            }
            .col-md-pull-8 {
                right: 66.66666667%;
            }
            .col-md-pull-7 {
                right: 58.33333333%;
            }
            .col-md-pull-6 {
                right: 50%;
            }
            .col-md-pull-5 {
                right: 41.66666667%;
            }
            .col-md-pull-4 {
                right: 33.33333333%;
            }
            .col-md-pull-3 {
                right: 25%;
            }
            .col-md-pull-2 {
                right: 16.66666667%;
            }
            .col-md-pull-1 {
                right: 8.33333333%;
            }
            .col-md-pull-0 {
                right: auto;
            }
            .col-md-push-12 {
                left: 100%;
            }
            .col-md-push-11 {
                left: 91.66666667%;
            }
            .col-md-push-10 {
                left: 83.33333333%;
            }
            .col-md-push-9 {
                left: 75%;
            }
            .col-md-push-8 {
                left: 66.66666667%;
            }
            .col-md-push-7 {
                left: 58.33333333%;
            }
            .col-md-push-6 {
                left: 50%;
            }
            .col-md-push-5 {
                left: 41.66666667%;
            }
            .col-md-push-4 {
                left: 33.33333333%;
            }
            .col-md-push-3 {
                left: 25%;
            }
            .col-md-push-2 {
                left: 16.66666667%;
            }
            .col-md-push-1 {
                left: 8.33333333%;
            }
            .col-md-push-0 {
                left: auto;
            }
            .col-md-offset-12 {
                margin-left: 100%;
            }
            .col-md-offset-11 {
                margin-left: 91.66666667%;
            }
            .col-md-offset-10 {
                margin-left: 83.33333333%;
            }
            .col-md-offset-9 {
                margin-left: 75%;
            }
            .col-md-offset-8 {
                margin-left: 66.66666667%;
            }
            .col-md-offset-7 {
                margin-left: 58.33333333%;
            }
            .col-md-offset-6 {
                margin-left: 50%;
            }
            .col-md-offset-5 {
                margin-left: 41.66666667%;
            }
            .col-md-offset-4 {
                margin-left: 33.33333333%;
            }
            .col-md-offset-3 {
                margin-left: 25%;
            }
            .col-md-offset-2 {
                margin-left: 16.66666667%;
            }
            .col-md-offset-1 {
                margin-left: 8.33333333%;
            }
            .col-md-offset-0 {
                margin-left: 0;
            }
        }
        @media (min-width: 1200px) {
            .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
                float: left;
            }
            .col-lg-12 {
                width: 100%;
            }
            .col-lg-11 {
                width: 91.66666667%;
            }
            .col-lg-10 {
                width: 83.33333333%;
            }
            .col-lg-9 {
                width: 75%;
            }
            .col-lg-8 {
                width: 66.66666667%;
            }
            .col-lg-7 {
                width: 58.33333333%;
            }
            .col-lg-6 {
                width: 50%;
            }
            .col-lg-5 {
                width: 41.66666667%;
            }
            .col-lg-4 {
                width: 33.33333333%;
            }
            .col-lg-3 {
                width: 25%;
            }
            .col-lg-2 {
                width: 16.66666667%;
            }
            .col-lg-1 {
                width: 8.33333333%;
            }
            .col-lg-pull-12 {
                right: 100%;
            }
            .col-lg-pull-11 {
                right: 91.66666667%;
            }
            .col-lg-pull-10 {
                right: 83.33333333%;
            }
            .col-lg-pull-9 {
                right: 75%;
            }
            .col-lg-pull-8 {
                right: 66.66666667%;
            }
            .col-lg-pull-7 {
                right: 58.33333333%;
            }
            .col-lg-pull-6 {
                right: 50%;
            }
            .col-lg-pull-5 {
                right: 41.66666667%;
            }
            .col-lg-pull-4 {
                right: 33.33333333%;
            }
            .col-lg-pull-3 {
                right: 25%;
            }
            .col-lg-pull-2 {
                right: 16.66666667%;
            }
            .col-lg-pull-1 {
                right: 8.33333333%;
            }
            .col-lg-pull-0 {
                right: auto;
            }
            .col-lg-push-12 {
                left: 100%;
            }
            .col-lg-push-11 {
                left: 91.66666667%;
            }
            .col-lg-push-10 {
                left: 83.33333333%;
            }
            .col-lg-push-9 {
                left: 75%;
            }
            .col-lg-push-8 {
                left: 66.66666667%;
            }
            .col-lg-push-7 {
                left: 58.33333333%;
            }
            .col-lg-push-6 {
                left: 50%;
            }
            .col-lg-push-5 {
                left: 41.66666667%;
            }
            .col-lg-push-4 {
                left: 33.33333333%;
            }
            .col-lg-push-3 {
                left: 25%;
            }
            .col-lg-push-2 {
                left: 16.66666667%;
            }
            .col-lg-push-1 {
                left: 8.33333333%;
            }
            .col-lg-push-0 {
                left: auto;
            }
            .col-lg-offset-12 {
                margin-left: 100%;
            }
            .col-lg-offset-11 {
                margin-left: 91.66666667%;
            }
            .col-lg-offset-10 {
                margin-left: 83.33333333%;
            }
            .col-lg-offset-9 {
                margin-left: 75%;
            }
            .col-lg-offset-8 {
                margin-left: 66.66666667%;
            }
            .col-lg-offset-7 {
                margin-left: 58.33333333%;
            }
            .col-lg-offset-6 {
                margin-left: 50%;
            }
            .col-lg-offset-5 {
                margin-left: 41.66666667%;
            }
            .col-lg-offset-4 {
                margin-left: 33.33333333%;
            }
            .col-lg-offset-3 {
                margin-left: 25%;
            }
            .col-lg-offset-2 {
                margin-left: 16.66666667%;
            }
            .col-lg-offset-1 {
                margin-left: 8.33333333%;
            }
            .col-lg-offset-0 {
                margin-left: 0;
            }
        }
    </style>
</div>
		<footer class="article-footer">
			<div class="article-tags"><i class="fa fa-tags"></i><a href="http://cuiqingcai.com/tag/python" rel="tag">Python</a><a href="http://cuiqingcai.com/tag/%e7%88%ac%e8%99%ab" rel="tag">爬虫</a></div>		</footer>
	<nav class="article-nav">
			<span class="article-nav-prev"><i class="fa fa-angle-double-left"></i> <a href="http://cuiqingcai.com/947.html" rel="prev">Python爬虫入门三之Urllib库的基本使用</a></span>
			<span class="article-nav-next"><a href="http://cuiqingcai.com/961.html" rel="next">Python爬虫入门五之URLError异常处理</a>  <i class="fa fa-angle-double-right"></i></span>
		</nav>

		<div class="related_top">
			<div class="related_posts"><ul class="related_img">

		<li class="related_box"  >
		<a href="http://cuiqingcai.com/4816.html" title="自建免费PYTHON爬虫代理IP池" target="_blank">
<img src="http://cuiqingcai.com/wp-content/themes/Yusi/timthumb.php?src=http://qiniu.cuiqingcai.com/wp-content/uploads/2016/10/9555112.jpg&h=110&w=185&q=90&zc=1&ct=1" alt="自建免费PYTHON爬虫代理IP池" />	<br><span class="r_title">自建免费PYTHON爬虫代理IP池</span></a>
		</li>
	
		<li class="related_box"  >
		<a href="http://cuiqingcai.com/4791.html" title="轻型爬虫框架" target="_blank">
<img src="http://cuiqingcai.com/wp-content/themes/Yusi/timthumb.php?src=http://qiniu.cuiqingcai.com/wp-content/uploads/2017/02/QQ图片20170205084843.jpg&h=110&w=185&q=90&zc=1&ct=1" alt="轻型爬虫框架" />	<br><span class="r_title">轻型爬虫框架</span></a>
		</li>
	
		<li class="related_box"  >
		<a href="http://cuiqingcai.com/4778.html" title="Neo4j简介及Py2Neo的用法" target="_blank">
<img src="http://cuiqingcai.com/wp-content/themes/Yusi/timthumb.php?src=http://qiniu.cuiqingcai.com/wp-content/uploads/2017/09/25.jpg&h=110&w=185&q=90&zc=1&ct=1" alt="Neo4j简介及Py2Neo的用法" />	<br><span class="r_title">Neo4j简介及Py2Neo的用法</span></a>
		</li>
	
		<li class="related_box"  >
		<a href="http://cuiqingcai.com/4607.html" title="获取知乎问题答案并转换为MarkDown文件" target="_blank">
<img src="http://cuiqingcai.com/wp-content/themes/Yusi/timthumb.php?src=http://qiniu.cuiqingcai.com/wp-content/uploads/2017/06/f8acc0c27d15fcfd8b2c9682aabe6633_r.png&h=110&w=185&q=90&zc=1&ct=1" alt="获取知乎问题答案并转换为MarkDown文件" />	<br><span class="r_title">获取知乎问题答案并转换为MarkDown文件</span></a>
		</li>
	</ul>

<div class="relates">
<ul>
<li><i class="fa fa-minus"></i><a href="http://cuiqingcai.com/4816.html">自建免费PYTHON爬虫代理IP池</a></li><li><i class="fa fa-minus"></i><a href="http://cuiqingcai.com/4791.html">轻型爬虫框架</a></li><li><i class="fa fa-minus"></i><a href="http://cuiqingcai.com/4778.html">Neo4j简介及Py2Neo的用法</a></li><li><i class="fa fa-minus"></i><a href="http://cuiqingcai.com/4607.html">获取知乎问题答案并转换为MarkDown文件</a></li><li><i class="fa fa-minus"></i><a href="http://cuiqingcai.com/4465.html">密码保护：免登录新浪微博爬虫系列之第一篇  单博主微博及评论数据</a></li><li><i class="fa fa-minus"></i><a href="http://cuiqingcai.com/4380.html">利用Scrapy爬取知乎用户详细信息并存至MongoDB</a></li><li><i class="fa fa-minus"></i><a href="http://cuiqingcai.com/4352.html">小白学爬虫系列教程</a></li><li><i class="fa fa-minus"></i><a href="http://cuiqingcai.com/4320.html">Python3爬虫视频学习教程</a></li>
</ul></div></div>		</div>
						<a name="comments"></a>
<div id="SOHUCS" sid="954"></div> 
<script type="text/javascript"> 
(function(){ 
    var appid = 'cyse2vKeA'; 
    var conf = 'prod_e440e40ef998fc11db594040d810aefb'; 
    var width = window.innerWidth || document.documentElement.clientWidth; 
    if (width < 960) { 
        window.document.write('<script id="changyan_mobile_js" charset="utf-8" type="text/javascript" src="http://changyan.sohu.com/upload/mobile/wap-js/changyan_mobile.js?client_id=' + appid + '&conf=' + conf + '"><\/script>'); 
    } else { 
        var loadJs=function(d,a){var c=document.getElementsByTagName("head")[0]||document.head||document.documentElement;var b=document.createElement("script");b.setAttribute("type","text/javascript");b.setAttribute("charset","UTF-8");b.setAttribute("src",d);if(typeof a==="function"){if(window.attachEvent){b.onreadystatechange=function(){var e=b.readyState;if(e==="loaded"||e==="complete"){b.onreadystatechange=null;a()}}}else{b.onload=a}}c.appendChild(b)};loadJs("http://changyan.sohu.com/upload/changyan.js",function(){window.changyan.api.config({appid:appid,conf:conf})}); 
    }})(); 
</script>            
<div id="ds-ssr" style="display:none">
				<nav id="comment-nav-above">
			<h1 class="assistive-text">Comment navigation</h1>
			<div class="nav-previous"><a href="http://cuiqingcai.com/954.html/comment-page-1#comments" >&larr; Older Comments</a></div>
			<div class="nav-next"></div>
		</nav>
		            <ol id="commentlist">
                		<li class="comment even thread-even depth-1" id="li-comment-4067">
			<article id="comment-4067" class="comment">
				<footer class="comment-meta">
					<cite class="comment-author vcard">
						<span class="fn">百炮污师干到服</span> on <a rel="nofollow" href="http://cuiqingcai.com/954.html/comment-page-2#comment-4067"><time pubdate datetime="2017-05-12T15:18:51+00:00">2017年5月12日 at 下午3:18</time></a> <span class="says">said:</span>					</cite>
				</footer>
	
				<div class="comment-content"><p>正则表达式获取网站中的url还是会出现很多问题！~</p>
</div>
				
			</article>
		</li><!-- #comment-## -->
		<li class="comment odd alt thread-odd thread-alt depth-1" id="li-comment-3838">
			<article id="comment-3838" class="comment">
				<footer class="comment-meta">
					<cite class="comment-author vcard">
						<span class="fn"><a href='http://t.qq.com/zhaoyu863943' rel='external nofollow' class='url'>赵娱</a></span> on <a rel="nofollow" href="http://cuiqingcai.com/954.html/comment-page-2#comment-3838"><time pubdate datetime="2017-04-05T09:21:48+00:00">2017年4月5日 at 上午9:21</time></a> <span class="says">said:</span>					</cite>
				</footer>
	
				<div class="comment-content"><p>请问楼主：page与print是相等的吗，与print是同一个意思吗，那这爬虫程序为什么不用print，而用page呢</p>
</div>
				
			</article>
		</li><!-- #comment-## -->
            </ol>

				<nav id="comment-nav-below">
			<h1 class="assistive-text">Comment navigation</h1>
			<div class="nav-previous"><a href="http://cuiqingcai.com/954.html/comment-page-1#comments" >&larr; Older Comments</a></div>
			<div class="nav-next"></div>
		</nav>
		    </div>
			
	</div>
</div>
<aside class="sidebar">	
<div class="widget widget_text"><div class="textwidget"><div class="social">

<a href="http://weibo.com/u/2830678474" rel="external nofollow" title="新浪微博" target="_blank"><i class="sinaweibo fa fa-weibo"></i></a><a  href="http://t.qq.com/CQCcqc123456?preview" rel="external nofollow" title="腾讯微博" target="_blank"><i class="tencentweibo fa fa-tencent-weibo"></i></a><a class="weixin"><i class="weixins fa fa-weixin"></i><div class="weixin-popover"><div class="popover bottom in"><div class="arrow"></div><div class="popover-title"></div><div class="popover-content"><img src="http://cuiqingcai.com/wp-content/themes/Yusi/img/weixin.gif" ></div></div></div></a>
<a href="http://mail.qq.com/cgi-bin/qm_share?t=qm_mailme&email=cqc@cuiqingcai.com" rel="external nofollow" title="Email" target="_blank"><i class="email fa fa-envelope-o"></i></a><a href="?feed=rss2" rel="external nofollow" target="_blank"  title="订阅本站"><i class="rss fa fa-rss"></i></a>
</div></div></div>

<div class="widget widget_metaslider_widget"><div class="title"><h2>热门专题</h2></div><!-- meta slider -->
<div style="width: 100%;" class="metaslider metaslider-nivo metaslider-2698 ml-slider meta-slider">
    
    <div id="metaslider_container_2698">
        <div class='slider-wrapper theme-bar'>
            <div class='ribbon'></div>
            <div id='metaslider_2698' class='nivoSlider'>
                <a href="http://cuiqingcai.com/1052.html" target="_blank"><img src="http://qiniu.cuiqingcai.com/wp-content/uploads/2015/04/wallpaper_5263464.jpg" height="300" width="320" data-title="Python爬虫学习系列教程" title="Python爬虫学习系列教程" alt="Python爬虫学习系列教程" class="slider-2698 slide-1720" /></a>
                <a href="http://cuiqingcai.com/4320.html" target="_blank"><img src="http://qiniu.cuiqingcai.com/wp-content/uploads/2015/02/wallpaper_5226849-1.jpg" height="300" width="320" data-title="Python3爬虫学习视频教程" title="OpenGL绘图系列教程" alt="OpenGL绘图系列教程" class="slider-2698 slide-951" /></a>
                <a href="http://cuiqingcai.com/4352.html" target="_blank"><img src="http://qiniu.cuiqingcai.com/wp-content/uploads/2016/03/20-234x220.jpg" height="300" width="320" data-title="小白学爬虫系列教程" alt="" class="slider-2698 slide-4372" /></a>
            </div>
        </div>
        
    </div>
    <script type="text/javascript">
        var metaslider_2698 = function($) {
            $('#metaslider_2698').nivoSlider({ 
                boxCols:7,
                boxRows:5,
                pauseTime:3000,
                effect:"random",
                controlNav:false,
                directionNav:true,
                pauseOnHover:true,
                animSpeed:600,
                prevText:"&lt;",
                nextText:"&gt;",
                slices:15,
                manualAdvance:false
            });
        };
        var timer_metaslider_2698 = function() {
            var slider = !window.jQuery ? window.setTimeout(timer_metaslider_2698, 100) : !jQuery.isReady ? window.setTimeout(timer_metaslider_2698, 1) : metaslider_2698(window.jQuery);
        };
        timer_metaslider_2698();
    </script>
</div>
<!--// meta slider--></div><div class="widget widget_text"><div class="title"><h2>职位推荐</h2></div>			<div class="textwidget"><div class="p-sm" style="padding-bottom:15px">
<ul>
<li>
<div style="overflow:hidden">
<div style="float:left;width: 35%;text-align: center;">
<img src="http://qiniu.cuiqingcai.com/wp-content/uploads/2016/11/baiguan_logo.png" style="width:80px"/>
</div>
<div style="float:left;width:60%;line-height:30px">
<a href="http://cuiqingcai.com/3323.html">百观科技 – 爬虫数据工程师</a>
</div>
</div>
</li>
<li style="margin-top:20px">
<div style="overflow:hidden">
<div style="float:left;width: 35%;text-align: center;">
<img src="http://qiniu.cuiqingcai.com/wp-content/uploads/2017/01/logo.png" style="width:80px"/>
</div>
<div style="float:left;width:60%;line-height:30px">
<a href="http://cuiqingcai.com/3912.html">灵析 – PHP/前端工程师</a>
</div>
</div>
</li>
</ul>
</div></div>
		</div><div class="widget widget_archive"><div class="title"><h2>文章归档</h2></div>		<ul>
			<li><a href='http://cuiqingcai.com/date/2017/10'>2017年十月</a></li>
	<li><a href='http://cuiqingcai.com/date/2017/09'>2017年九月</a></li>
	<li><a href='http://cuiqingcai.com/date/2017/08'>2017年八月</a></li>
	<li><a href='http://cuiqingcai.com/date/2017/07'>2017年七月</a></li>
	<li><a href='http://cuiqingcai.com/date/2017/06'>2017年六月</a></li>
	<li><a href='http://cuiqingcai.com/date/2017/05'>2017年五月</a></li>
	<li><a href='http://cuiqingcai.com/date/2017/04'>2017年四月</a></li>
	<li><a href='http://cuiqingcai.com/date/2017/03'>2017年三月</a></li>
	<li><a href='http://cuiqingcai.com/date/2017/02'>2017年二月</a></li>
	<li><a href='http://cuiqingcai.com/date/2017/01'>2017年一月</a></li>
	<li><a href='http://cuiqingcai.com/date/2016/12'>2016年十二月</a></li>
	<li><a href='http://cuiqingcai.com/date/2016/11'>2016年十一月</a></li>
	<li><a href='http://cuiqingcai.com/date/2016/10'>2016年十月</a></li>
	<li><a href='http://cuiqingcai.com/date/2016/09'>2016年九月</a></li>
	<li><a href='http://cuiqingcai.com/date/2016/08'>2016年八月</a></li>
	<li><a href='http://cuiqingcai.com/date/2016/07'>2016年七月</a></li>
	<li><a href='http://cuiqingcai.com/date/2016/06'>2016年六月</a></li>
	<li><a href='http://cuiqingcai.com/date/2016/03'>2016年三月</a></li>
	<li><a href='http://cuiqingcai.com/date/2016/02'>2016年二月</a></li>
	<li><a href='http://cuiqingcai.com/date/2016/01'>2016年一月</a></li>
	<li><a href='http://cuiqingcai.com/date/2015/12'>2015年十二月</a></li>
	<li><a href='http://cuiqingcai.com/date/2015/11'>2015年十一月</a></li>
	<li><a href='http://cuiqingcai.com/date/2015/10'>2015年十月</a></li>
	<li><a href='http://cuiqingcai.com/date/2015/09'>2015年九月</a></li>
	<li><a href='http://cuiqingcai.com/date/2015/08'>2015年八月</a></li>
	<li><a href='http://cuiqingcai.com/date/2015/07'>2015年七月</a></li>
	<li><a href='http://cuiqingcai.com/date/2015/06'>2015年六月</a></li>
	<li><a href='http://cuiqingcai.com/date/2015/05'>2015年五月</a></li>
	<li><a href='http://cuiqingcai.com/date/2015/04'>2015年四月</a></li>
	<li><a href='http://cuiqingcai.com/date/2015/03'>2015年三月</a></li>
	<li><a href='http://cuiqingcai.com/date/2015/02'>2015年二月</a></li>
	<li><a href='http://cuiqingcai.com/date/2015/01'>2015年一月</a></li>
	<li><a href='http://cuiqingcai.com/date/2014/12'>2014年十二月</a></li>
	<li><a href='http://cuiqingcai.com/date/2014/11'>2014年十一月</a></li>
	<li><a href='http://cuiqingcai.com/date/2014/10'>2014年十月</a></li>
	<li><a href='http://cuiqingcai.com/date/2014/09'>2014年九月</a></li>
		</ul>
		</div><div class="widget widget_text"><div class="title"><h2>交流分享</h2></div>			<div class="textwidget"><div class="p-sm" style="overflow:hidden;padding-bottom:15px">
<p class="text-center">
想一起交流学习经验吗？来进击的Coder瞧瞧吧
</p>
<div class="text-center" style="float:left">
<img src="http://qiniu.cuiqingcai.com/wp-content/uploads/2016/12/QQqun.png" style="width:250px"/>
</div>
<div class="text-left" style="float:left;padding-top: 10px;width:90px">
<p>学习？交流？分享？吐槽？</p>
<p>尽在</p>
<p style="
    color: #E9415A;
    font-size: 15px;">进击的Coder</p>
<p>QQ群号</p>
<p style="
    color: #E9415A;
    font-size: 15px;margin-bottom:45px">99350970</p>
<a style="background-color: #EB586F;
    height: 16px;
    display: block;
    line-height: 16px;
    font-size: 13px;" class="btn btn-xs btn-danger" target="_blank" href="http://shang.qq.com/wpa/qunwpa?idkey=31ed8a7d15339353ad090379bb9243118f90220324a7a0f4b453bce52dcd02b6">立即加入</a>
</div>
</div></div>
		</div><div class="widget widget_text"><div class="title"><h2>微信公众号</h2></div>			<div class="textwidget"><div class="p-sm" style="overflow:hidden;padding-bottom:12px">
<p class="text-center">
学习累了吧，扫个码玩玩吧~
</p>
<div class="text-center" style="float:left">
<img src="http://qiniu.cuiqingcai.com/wp-content/uploads/2017/05/qrcode_for_gh_5b0546ddd2d0_430.jpg" style="width:250px"/>
</div>
<div class="text-left" style="float:left;padding-top: 10px;width:90px">
<p>想找人聊天解闷？<br />想要学习干货？<br />想要更多福利？</p>
<p>尽在</p>
<p style="
    color: #E9415A;
    font-size: 15px;">进击的Coder</p>
<p>公众号搜索</p>
<a style="background-color: #EB586F;
    height: 16px;
    display: block;
    line-height: 14px; width: 70px;
    font-size: 12px;" class="btn btn-xs btn-danger" target="_blank">进击的Coder</a>
</div>
</div></div>
		</div><div class="widget d_postlist"><div class="title"><h2>猜你喜欢</h2></div><ul><li><a href="http://cuiqingcai.com/990.html" title="Python爬虫实战一之爬取糗事百科段子" ><span class="thumbnail"><img src="http://cuiqingcai.com/wp-content/themes/Yusi/timthumb.php?src=http://qiniu.cuiqingcai.com/wp-content/uploads/2015/02/wallpaper_5228661.jpg&h=64&w=100&q=90&zc=1&ct=1" alt="Python爬虫实战一之爬取糗事百科段子" /></span><span class="text">Python爬虫实战一之爬取糗事百科段子</span><span class="muted">2015-02-17</span><span class="muted">576评论</span></a></li>
<li><a href="http://cuiqingcai.com/993.html" title="Python爬虫实战二之爬取百度贴吧帖子" ><span class="thumbnail"><img src="http://cuiqingcai.com/wp-content/themes/Yusi/timthumb.php?src=http://qiniu.cuiqingcai.com/wp-content/uploads/2015/02/wallpaper_5265936.jpg&h=64&w=100&q=90&zc=1&ct=1" alt="Python爬虫实战二之爬取百度贴吧帖子" /></span><span class="text">Python爬虫实战二之爬取百度贴吧帖子</span><span class="muted">2015-02-17</span><span class="muted">193评论</span></a></li>
<li><a href="http://cuiqingcai.com/1001.html" title="Python爬虫实战四之抓取淘宝MM照片" ><span class="thumbnail"><img src="http://cuiqingcai.com/wp-content/themes/Yusi/timthumb.php?src=http://qiniu.cuiqingcai.com/wp-content/uploads/2015/02/wallpaper_5270641.jpg&h=64&w=100&q=90&zc=1&ct=1" alt="Python爬虫实战四之抓取淘宝MM照片" /></span><span class="text">Python爬虫实战四之抓取淘宝MM照片</span><span class="muted">2015-02-20</span><span class="muted">153评论</span></a></li>
<li><a href="http://cuiqingcai.com/3179.html" title="小白爬虫第一弹之抓取妹子图" ><span class="thumbnail"><img src="http://cuiqingcai.com/wp-content/themes/Yusi/timthumb.php?src=http://qiniu.cuiqingcai.com/wp-content/uploads/2016/10/1-1506261ZI7.jpg&h=64&w=100&q=90&zc=1&ct=1" alt="小白爬虫第一弹之抓取妹子图" /></span><span class="text">小白爬虫第一弹之抓取妹子图</span><span class="muted">2016-10-28</span><span class="muted">149评论</span></a></li>
<li><a href="http://cuiqingcai.com/1076.html" title="Python爬虫实战五之模拟登录淘宝并获取所有订单" ><span class="thumbnail"><img src="http://cuiqingcai.com/wp-content/themes/Yusi/timthumb.php?src=http://qiniu.cuiqingcai.com/wp-content/uploads/2015/02/wallpaper_5226152.jpg&h=64&w=100&q=90&zc=1&ct=1" alt="Python爬虫实战五之模拟登录淘宝并获取所有订单" /></span><span class="text">Python爬虫实战五之模拟登录淘宝并获取所有订单</span><span class="muted">2015-02-24</span><span class="muted">131评论</span></a></li>
<li><a href="http://cuiqingcai.com/2652.html" title="Python爬虫进阶四之PySpider的用法" ><span class="thumbnail"><img src="http://cuiqingcai.com/wp-content/themes/Yusi/timthumb.php?src=http://qiniu.cuiqingcai.com/wp-content/uploads/2016/03/兔小妖39.jpg&h=64&w=100&q=90&zc=1&ct=1" alt="Python爬虫进阶四之PySpider的用法" /></span><span class="text">Python爬虫进阶四之PySpider的用法</span><span class="muted">2016-03-26</span><span class="muted">130评论</span></a></li>
<li><a href="http://cuiqingcai.com/3472.html" title="小白进阶之Scrapy第一篇" ><span class="thumbnail"><img src="http://cuiqingcai.com/wp-content/themes/Yusi/timthumb.php?src=http://qiniu.cuiqingcai.com/wp-content/uploads/2016/07/DSC00123.jpg&h=64&w=100&q=90&zc=1&ct=1" alt="小白进阶之Scrapy第一篇" /></span><span class="text">小白进阶之Scrapy第一篇</span><span class="muted">2016-12-07</span><span class="muted">116评论</span></a></li>
<li><a href="http://cuiqingcai.com/968.html" title="Python爬虫入门六之Cookie的使用" ><span class="thumbnail"><img src="http://cuiqingcai.com/wp-content/themes/Yusi/timthumb.php?src=http://qiniu.cuiqingcai.com/wp-content/uploads/2015/02/wallpaper_5258536-1.jpg&h=64&w=100&q=90&zc=1&ct=1" alt="Python爬虫入门六之Cookie的使用" /></span><span class="text">Python爬虫入门六之Cookie的使用</span><span class="muted">2015-02-15</span><span class="muted">109评论</span></a></li>
<li><a href="http://cuiqingcai.com/1052.html" title="Python爬虫学习系列教程" ><span class="thumbnail"><img src="http://cuiqingcai.com/wp-content/themes/Yusi/timthumb.php?src=http://qiniu.cuiqingcai.com/wp-content/uploads/2015/02/wallpaper_5254665-e1424499272248.jpg&h=64&w=100&q=90&zc=1&ct=1" alt="Python爬虫学习系列教程" /></span><span class="text">Python爬虫学习系列教程</span><span class="muted">2015-02-21</span><span class="muted">108评论</span></a></li>
<li><a href="http://cuiqingcai.com/2416.html" title="弃用多说，改用畅言" ><span class="thumbnail"><img src="http://cuiqingcai.com/wp-content/themes/Yusi/timthumb.php?src=http://qiniu.cuiqingcai.com/wp-content/uploads/2016/02/bg1-e1454442892955.jpg&h=64&w=100&q=90&zc=1&ct=1" alt="弃用多说，改用畅言" /></span><span class="text">弃用多说，改用畅言</span><span class="muted">2016-02-03</span><span class="muted">84评论</span></a></li>
</ul></div><div class="widget d_tag"><div class="title"><h2>标签云</h2></div><div class="d_tags"><a title="43个话题" href="http://cuiqingcai.com/tag/python">Python (43)</a><a title="38个话题" href="http://cuiqingcai.com/tag/%e7%88%ac%e8%99%ab">爬虫 (38)</a><a title="31个话题" href="http://cuiqingcai.com/tag/php">PHP (31)</a><a title="21个话题" href="http://cuiqingcai.com/tag/js">JS (21)</a><a title="12个话题" href="http://cuiqingcai.com/tag/html">HTML (12)</a><a title="11个话题" href="http://cuiqingcai.com/tag/opengl">OpenGL (11)</a><a title="9个话题" href="http://cuiqingcai.com/tag/jquery">jQuery (9)</a><a title="7个话题" href="http://cuiqingcai.com/tag/linux">Linux (7)</a><a title="7个话题" href="http://cuiqingcai.com/tag/wordpress">WordPress (7)</a><a title="7个话题" href="http://cuiqingcai.com/tag/winpcap">Winpcap (7)</a><a title="6个话题" href="http://cuiqingcai.com/tag/css">CSS (6)</a><a title="6个话题" href="http://cuiqingcai.com/tag/security">Security (6)</a><a title="4个话题" href="http://cuiqingcai.com/tag/git">Git (4)</a><a title="4个话题" href="http://cuiqingcai.com/tag/bootstrap">Bootstrap (4)</a><a title="4个话题" href="http://cuiqingcai.com/tag/net">Net (4)</a><a title="3个话题" href="http://cuiqingcai.com/tag/java">Java (3)</a><a title="3个话题" href="http://cuiqingcai.com/tag/mysql">Mysql (3)</a><a title="2个话题" href="http://cuiqingcai.com/tag/cocos2d-x">Cocos2d-x (2)</a><a title="2个话题" href="http://cuiqingcai.com/tag/jsp">JSP (2)</a><a title="2个话题" href="http://cuiqingcai.com/tag/matlab">Matlab (2)</a><a title="2个话题" href="http://cuiqingcai.com/tag/photoshop">Photoshop (2)</a><a title="2个话题" href="http://cuiqingcai.com/tag/less">LESS (2)</a><a title="2个话题" href="http://cuiqingcai.com/tag/sass">SASS (2)</a><a title="1个话题" href="http://cuiqingcai.com/tag/json">Json (1)</a><a title="1个话题" href="http://cuiqingcai.com/tag/redis">Redis (1)</a><a title="1个话题" href="http://cuiqingcai.com/tag/nginx">Nginx (1)</a><a title="1个话题" href="http://cuiqingcai.com/tag/appium">Appium (1)</a><a title="1个话题" href="http://cuiqingcai.com/tag/gulp">Gulp (1)</a><a title="1个话题" href="http://cuiqingcai.com/tag/laravel">Laravel (1)</a><a title="1个话题" href="http://cuiqingcai.com/tag/%e6%b5%8b%e8%af%95">测试 (1)</a><a title="1个话题" href="http://cuiqingcai.com/tag/app">APP (1)</a><a title="1个话题" href="http://cuiqingcai.com/tag/ssh">SSH (1)</a><a title="1个话题" href="http://cuiqingcai.com/tag/scrapy%e5%88%86%e5%b8%83%e5%bc%8f">Scrapy分布式 (1)</a><a title="1个话题" href="http://cuiqingcai.com/tag/%e8%a7%86%e9%a2%91">视频 (1)</a><a title="1个话题" href="http://cuiqingcai.com/tag/python3">Python3 (1)</a><a title="1个话题" href="http://cuiqingcai.com/tag/scrapy">Scrapy (1)</a><a title="1个话题" href="http://cuiqingcai.com/tag/%e7%9f%a5%e4%b9%8e">知乎 (1)</a><a title="1个话题" href="http://cuiqingcai.com/tag/neo4j">Neo4j (1)</a><a title="1个话题" href="http://cuiqingcai.com/tag/http">HTTP (1)</a></div></div><div class="widget widget_links"><div class="title"><h2>友情链接</h2></div>
	<ul class='xoxo blogroll'>
<li><a href="http://www.99banzou.com" target="_blank">99伴奏网</a></li>
<li><a href="http://www.anotherhome.net" target="_blank">Anotherhome</a></li>
<li><a href="http://zhouchenwen.com" rel="acquaintance" target="_blank">ColdCoder</a></li>
<li><a href="https://www.3maio.com" target="_blank">Cpphp</a></li>
<li><a href="http://www.spotty.com.cn/" target="_blank">DevNews</a></li>
<li><a href="http://www.findspace.name" target="_blank">Findspace</a></li>
<li><a href="http://blog.hickwu.com/" target="_blank">Hick</a></li>
<li><a href="http://www.jankl.com/">jank</a></li>
<li><a href="http://www.keen8.com/">keen8博客</a></li>
<li><a href="http://lise.io/" target="_blank">Keep It Simple</a></li>
<li><a href="http://www.k2zone.cn/" target="_blank">kTWO</a></li>
<li><a href="http://monkeyblog.cn/">Monkey前端博客</a></li>
<li><a href="http://www.newbieblog.cc/" target="_blank">newbie&#039;blog</a></li>
<li><a href="http://www.urselect.com/?aid=dnk9st" target="_blank">nopcommerce</a></li>
<li><a href="http://www.imop.us/" target="_blank">phper.yang</a></li>
<li><a href="http://www.shangzekai.xyz">Shang</a></li>
<li><a href="http://wonderlee.me">Wonder’s Land</a></li>
<li><a href="http://wxinjie.cn/">XJIE</a></li>
<li><a href="http://www.atrail.cn/" target="_blank">从前以后</a></li>
<li><a href="http://lanbing510.info" target="_blank">冰蓝</a></li>
<li><a href="http://www.61mon.com/" target="_blank">刘毅</a></li>
<li><a href="http://www.superqq.com/">刚刚在线</a></li>
<li><a href="http://qianxunclub.com/" target="_blank">千寻啊千寻</a></li>
<li><a href="http://kodcloud.com/">可道云</a></li>
<li><a href="http://www.lvtao.net" target="_blank">吕滔博客</a></li>
<li><a href="https://wujunze.com" target="_blank">吴钧泽博客</a></li>
<li><a href="http://www.hellobi.com/" target="_blank">天善智能</a></li>
<li><a href="http://www.fddcn.cn" target="_blank">奋斗的承诺</a></li>
<li><a href="http://www.jrady.cn/" target="_blank">宏愿</a></li>
<li><a href="http://www.cenchong.com/" target="_blank">岑冲个人博客</a></li>
<li><a href="https://upliu.net/" target="_blank">开飞机的小蜗牛</a></li>
<li><a href="http://www.chrafz.com/">张弦先生</a></li>
<li><a href="http://www.503error.com/">张志明的个人博客</a></li>
<li><a href="https://www.sastdoglcy.cn/" target="_blank">成长的柚子</a></li>
<li><a href="http://www.jishux.com/" target="_blank">技术栈</a></li>
<li><a href="https://seofangfa.com" target="_blank">方法SEO顾问</a></li>
<li><a href="http://www.lishengcn.cn/" target="_blank">李胜的脚步</a></li>
<li><a href="http://liaoyuming.cn" rel="acquaintance" target="_blank">永远站</a></li>
<li><a href="http://www.hubwiz.com" target="_blank">汇智网</a></li>
<li><a href="http://frankchen.xyz/" target="_blank">江南消夏</a></li>
<li><a href="http://bysocket.com" target="_blank">泥瓦匠BYSocket</a></li>
<li><a href="http://www.xiaoxiangyucuo.com/">潇湘雨错</a></li>
<li><a href="http://www.xiongge.club/">熊哥club</a></li>
<li><a href="https://geekspider.org/" target="_blank">爬虫实验室</a></li>
<li><a href="http://www.aihongxin.com/">爱红心 爱分享</a></li>
<li><a href="http://blog.wangjingxin.top/">王镜鑫的博客</a></li>
<li><a href="http://zerlong.com/" target="_blank">知语</a></li>
<li><a href="https://www.binblogs.cn" target="_blank">码农De边缘世界</a></li>
<li><a href="http://ibloger.net" target="_blank">程序喵</a></li>
<li><a href="http://www.numberer.net/" target="_blank">第二导航</a></li>
<li><a href="http://blog.csdn.net/lu_wei_wei">米四度的思考</a></li>
<li><a href="http://www.zoeys.cn/" target="_blank">糊糊</a></li>
<li><a href="https://www.carlstedt.cn/">紫杉倒影</a></li>
<li><a href="http://www.laodong.me" target="_blank">老董博客</a></li>
<li><a href="http://zangyiwei.com">臧义伟博客</a></li>
<li><a href="http://www.lanqibing.com/" target="_blank">蓝骑兵</a></li>
<li><a href="http://www.zhan0929.cc">詹加兵个人博客</a></li>
<li><a href="http://zhaoshuai.me/%20" target="_blank">赵帅的个人博客</a></li>
<li><a href="http://blog.zfuyun.top/">赵浮云博客</a></li>
<li><a href="http://www.leyle.com/" target="_blank">遗落岛</a></li>

	</ul>
</div>
<div class="widget widget_text"><div class="title"><h2>精品推荐</h2></div>			<div class="textwidget"><div class="side-ad">
<script type="text/javascript">
var cpro_id="u2578794";
(window["cproStyleApi"] = window["cproStyleApi"] || {})[cpro_id]={at:"3",rsi0:"300",rsi1:"250",pat:"17",tn:"baiduCustNativeAD",rss1:"#FFFFFF",conBW:"1",adp:"1",ptt:"0",titFF:"%E5%BE%AE%E8%BD%AF%E9%9B%85%E9%BB%91",titFS:"14",rss2:"#00a67c",titSU:"0"}
</script>
<script src="http://cpro.baidustatic.com/cpro/ui/c.js" type="text/javascript"></script>
</div>
<style>
#BAIDU_SSP__wrapper_u2578794_1 {
display:none;
}
#BAIDU_SSP__wrapper_u2578794_0 #iframeu2578794_0  .bd-logo2 {
display:none !important;
}
</style></div>
		</div><div class="widget widget_text"><div class="title"><h2>新浪微博</h2></div>			<div class="textwidget"><iframe width="100%" height="550" class="share_self"  frameborder="0" scrolling="no" src="http://widget.weibo.com/weiboshow/index.php?language=&width=0&height=550&fansRow=2&ptype=1&speed=0&skin=1&isTitle=0&noborder=0&isWeibo=1&isFans=1&uid=2830678474&verifier=7468dc7b&dpc=1"></iframe></div>
		</div><div class="widget widget_text"><div class="title"><h2>热门评论</h2></div>			<div class="textwidget"><div style="background:#fff;margin-top:5px;padding:0 20px 10px 10px;display:none">
			<div id="cyReping" role="cylabs" data-use="reping"></div>	
			<script type="text/javascript" charset="utf-8" src="http://changyan.itc.cn/js/lib/jquery.js"></script>
			<script type="text/javascript" charset="utf-8" src="https://changyan.sohu.com/js/changyan.labs.https.js?appid=cyse2vKeA"></script>
            	</div></div>
		</div><div class="widget widget_text"><div class="title"><h2>交流问答</h2></div>			<div class="textwidget"><div class="p-sm">
<p style="
    margin-left: 20px;
    color: #00a67c;
">遇到问题没有解决方案？来论坛提问吧</p><p style="
    margin-left: 10px;
">
<a href="http://bbs.cuiqingcai.com/">
<input type="button" value="点我提问" style="width: 310px; margin: 10px auto 0px; background-color: rgb(245, 138, 135); color: rgb(255, 255, 255); height: 40px; border: none; font-family: 'Microsoft Yahei'; font-size: 16px; letter-spacing: 2px;" onmouseover="this.style.backgroundColor='rgb(252, 125, 121)'" onmouseout="this.style.backgroundColor='#F58A87'"/></a>
</p></div></div>
		</div><div class="widget widget_text">			<div class="textwidget"><p><a href="https://edu.hellobi.com/course/157"><br />
<img src="http://qiniu.cuiqingcai.com/wp-content/uploads/2017/04/WechatIMG258.jpeg"/><br />
</a></p>
</div>
		</div></aside></section>
<footer class="footer">
    <div class="footer-inner">
        <div class="copyright pull-left">
         <a href="http://cuiqingcai.com " title="静觅">静觅</a> 版权所有丨采用<a href="http://yusi123.com/"> 欲思 </a>主题丨基于<a href="http://cn.wordpress.org/" title="WordPress"> WordPress </a>构建   © 2015丨托管于 <a rel="nofollow" target="_blank" href="http://www.aliyun.com/">阿里云主机</a> & <a rel="nofollow" target="_blank" href="http://www.qiniu.com/">七牛云存储 </a>丨鲁ICP备14030596号
		 <div>
			<script type="text/javascript">var cnzz_protocol = (("https:" == document.location.protocol) ? " https://" : " http://");document.write(unescape("%3Cspan id='cnzz_stat_icon_1253486800'%3E%3C/span%3E%3Cscript src='" + cnzz_protocol + "s4.cnzz.com/z_stat.php%3Fid%3D1253486800%26online%3D1%26show%3Dline' type='text/javascript'%3E%3C/script%3E"));</script>
		 </div>
		</div>
        
    </div>
</footer>

<link rel='stylesheet' id='metaslider-nivo-slider-css'  href='http://cuiqingcai.com/wp-content/plugins/ml-slider/assets/sliders/nivoslider/nivo-slider.css?ver=3.5' type='text/css' media='all' property='stylesheet' />
<link rel='stylesheet' id='metaslider-public-css'  href='http://cuiqingcai.com/wp-content/plugins/ml-slider/assets/metaslider/public.css?ver=3.5' type='text/css' media='all' property='stylesheet' />
<link rel='stylesheet' id='metaslider-nivo-slider-bar-css'  href='http://cuiqingcai.com/wp-content/plugins/ml-slider/assets/sliders/nivoslider/themes/bar/bar.css?ver=3.5' type='text/css' media='all' property='stylesheet' />
<script type='text/javascript'>
/* <![CDATA[ */
var viewsCacheL10n = {"admin_ajax_url":"http:\/\/cuiqingcai.com\/wp-admin\/admin-ajax.php","post_id":"954"};
/* ]]> */
</script>
<script type='text/javascript' src='http://cuiqingcai.com/wp-content/plugins/wp-postviews/postviews-cache.js?ver=1.68'></script>
<script type='text/javascript' src='http://cuiqingcai.com/wp-content/themes/Yusi/js/jquery.js?ver=1.0'></script>
<script type='text/javascript' src='http://cuiqingcai.com/wp-includes/js/wp-embed.min.js?ver=4.7.3'></script>
<script type='text/javascript' src='http://cuiqingcai.com/wp-content/plugins/ml-slider/assets/sliders/nivoslider/jquery.nivo.slider.pack.js?ver=3.5'></script>
<script>with(document)0[(getElementsByTagName("head")[0]||body).appendChild(createElement("script")).src="http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion="+~(-new Date()/36e5)];</script><!-- xuanfu -->
 <script type="text/javascript">
    /*300*25 创建于 2015-02-23*/
    var cpro_id = "u1959047";
</script>
<script src="http://cpro.baidustatic.com/cpro/ui/s.js" type="text/javascript"></script>
<script type="text/javascript">
var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");
document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3F3ef185224776ec2561c9f7066ead4f24' type='text/javascript'%3E%3C/script%3E"));
</script>
<script>
setTimeout(function(){
	
$('#cpv6_left_lower,#cpv6_right_lower').css({
'width': 0
});
}, 500);
</script>
<script type="text/javascript">
$(document).ready(function(){
	var imgs = new Array();
	imgs[0] = 'http://qiniu.cuiqingcai.com/wp-content/uploads/2015/05/20150525111154.jpg';
	imgs[1] = 'http://qiniu.cuiqingcai.com/wp-content/uploads/2015/05/20150525111447.jpg';
	imgs[2] = 'http://qiniu.cuiqingcai.com/wp-content/uploads/2015/05/20150525112058.jpg';
	imgs[3] = 'http://qiniu.cuiqingcai.com/wp-content/uploads/2015/05/20150525112112.jpg';
	imgs[4] = 'http://qiniu.cuiqingcai.com/wp-content/uploads/2015/05/20150525112129.jpg';
	imgs[5] = 'http://qiniu.cuiqingcai.com/wp-content/uploads/2015/05/20150525112155.jpg';
	$('.ds-avatar img[src*="cdncache"], .ds-avatar img[src*="avatar-50"]').each(function(){
		var rand = Math.floor(Math.random()*imgs.length);
		$(this).attr("src",imgs[rand]);
	})
});
</script>
</body>
</html>
>>> 

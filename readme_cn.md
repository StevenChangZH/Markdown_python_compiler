Markdown Compiler
========================

本项目是一个Markdown语法分析器，实现了从Markdown语法到HTML文件的转换。
项目使用Python作为开发语言，使用了ply和MathJax库，并且使用了来自R Studio的js文件。

开发环境 Mac OS 10.10.1, python version 2.7, safari 8.0.2

在 Mac OS 10.10.1、Linus 14.04 LTS测试通过，Windows平台下可能会出现编码相关的错误。

本项目部分功能需要网络连接支持，请保证在联网环境下使用。

最新版本是7.0。

##项目基本功能
以下是我们支持的Markdown语法：

+ 标题：使用1-10个 `#` 来指明各阶标题 e.g.`# TITLE` `## SUBTITLE`
+ 斜体：使用一个 `*` 或者一个 `_` 来包围一段字符来设置斜体 e.g.`*latics*` `_latics_`
+ 强调：使用 `**` 或者 `__` 来包围一段字符来设置加粗强调 e.g.`**bold**` `__bold__`
+ 分割线：在空行里使用三个以上的 `*`, `=` 或者 `-` 来添加一条分割线 e.g.`---` `===` `***`
  	>其中可以插入空格，而 `===` 仅被Github支持
+ 列表：使用 `1. `, `+ `, `- ` 或者 `* ` 来建立列表
+ 图片：使用 `![imglabel](url)` 来插入图片
+ 区块引用：使用 `> blabla` 来引用文字 
+ 代码块：使用两行 ``` 来包围你的代码块
	>仅在 GitHub 中被支持


## 扩展功能 

+ 数学表达式：使用 `$ formula $` 来编写你的 LaTex 数学表达式 
	>不支持在表达式中插入新行； 表达式的输入规范由 MathJax 规定. 请访问 http://www.mathjax.org 了解更多 LaTex 数学表达式的输入规范
+ 视频：使用 `!![videolabel](url)` 来插入 Youtube 视频
	>仅能插入YouTube的链接形如 "https://www.youtube.com/watch?v=XXXXXXXXXXX..." 、 "http://youtu.be/XXXXXXXXXXX" 的视频，并请保证你的网络条件能正常播放这些视频*)

+ 图片能被转换为二进制流集成在HTML文件里
	>测试功能，有时可能会不能正常工作（但并不影响正常使用）。如果没有网络连接，则不会集二进制流，而是插入图片的URL（与正规语法一样）

**NOTICE**: 暂**不支持**语法嵌套。类似于 `*_``hello``_*` 的语法将不能被正确解析


##运行环境
运行本项目之前，请保证安装了 Python 的运行环境 (only for windows users) 和 ply 库。

所有源代码文件存放在 `../src` 目录下。直接运行plyRun.py即可。

##运行方法

请将目录切换到 `src` 文件夹

```
cd .../src/
```

请输入以下命令来运行我们的分析器：
```
python plyRun.py
python plyRun.py [imported Markdown filename]
python plyRun.py [imported Markdown filename] [Exported HTML filename]
```

请使用 `data.md` 来测试所有支持的语法。

由于支持的语法略有差别，请不要使用本文档来测试我们的分析器。

##文件组织
+ `ply` 使用的 ply 库文件夹
+ `plyLex.py` lexer
+ `plyExport.py` 导出HTML文件需要用到的前后缀字段
+ `plyYacc.py` 语义分析器
+ `plyScripts_2_7.py` 导出HTML文件需要用到的一些方法，给 Python 版本 3.3 以下的使用
+ `plyScripts_3_3.py` 导出HTML文件需要用到的一些方法，给 Python 版本 3.3 以上的使用
+ `plyRun.py` 运行的主文件
+ `test0x.md` 课程Repository下的三个测试文件
+ `data.md` 我们自己编写的测试项目（使用了所有支持的语法）


#组队信息
组员：

肖志康

* 学号：1252916

* 手机：18817876277

* 邮箱：xiaozhikang0916@gmail.com

* 分工：插入分割线、列表、图片、区块引用等，撰写说明文档

* 贡献率：30%

常智辉

* 学号：1252920

* 手机：13127736127

* 邮箱：stevenchang12@hotmail.com@

* 分工：插入代码块、数学表达式、视频、图片二进制流嵌入等扩展功能，编写测试文档

* 贡献率：40%

许好运

* 学号：1252919

* 手机：18817870521

* 邮箱：1039147110@qq.com

* 分工：插入标题、斜体、强调等，撰写说明文档

* 贡献率：30%

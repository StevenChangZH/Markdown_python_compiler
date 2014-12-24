Markdown_python_compiler
========================

This is a Markdown compiler, converting Markdown to HTML with python. We've used ply and MathJax.

Some .js scripts used from Markdown interpreter of R studio.

Our development environment is Mac OS 10.10.1, python version 2.7, safari 8.0.2

This project can be run in Mac OS 10.10.1 and Ubuntu 14.04 LTS

Current version is 7.0

##Functions
Supported Markdown grammars:
+ Using `#` to create title and subtitles, e.g. `# TITLE` `## SUBTITLE`
+ Using one `*` or one `_` to set to latics, e.g. `*latics*` `_latics_`
+ Using `**` or `__` to set to bold, e.g.`**bold**` `__bold__`
+ Using more than three `*`, `=` or `-` to add a separation line, e.g.`---` `===` `***`
  ( *you can be insert a space, and please notice that `===` is only supported by GitHub.*)
+ Using `1. `, `+ `, `- ` or `* ` for listing.
+ Using `![imglabel](url)` to show image
+ Using `> contents` to support quote.
+ Using ``` to support code fields.( *please notice this is only supported by GitHub.*)
+ Using `$ formula $` to support LaTex mathematical formulas. ( *Do not support newline; restrictions of formula types depended by MathJax. Refer http://www.mathjax.org for more information.*)
+ Using `!![videolabel](url)` to show Youtube videos ( *Certainly this is a function provided by me, which is not supported by standard Markdown grammar. Also, it will only support url like "https://www.youtube.com/watch?v=XXXXXXXXXXX..." or "http://youtu.be/XXXXXXXXXXX"*)

+ Image embedded into html automatically( *This is only a test function. Sometimes it will not transform( but no problems). And image url need internet access. If cannot, it will output url directly.*)


##Environment
If you want to test it, first you need to set up python environment (only for windows users) and ply (lexer and yacc for python).
All the source code files are placed in folder `code`. Just simply run the  code on your terminal:

##Folder orgnization
+ `ply` imported code folder
+ `plyLex.py` lexer
+ `plyExport.py` two string for html output
+ `plyYacc.py`semantic analyzer
+ `plyScripts_2_7.py` some methods for htmlouput, only applied for python version under 3.3
+ `plyScripts_3_3.py` some methods for htmlouput, only applied for python version above 3.3
+ `plyRun.py` script interface
+ `test0x.md` requirements files from course Github website
+ `data.md` ourselfs' md file for test

##How to use

To run this analyzer, You have three optional commands:
```
python plyRun.py
python plyRun.py [imported Markdown filename]
python plyRun.py [imported Markdown filename] [Exported HTML filename]
```

Please use `data.md` to test all the grammers supported.


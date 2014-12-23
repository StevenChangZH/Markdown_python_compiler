Markdown_python_compiler
========================

This is a Markdown compiler, converting Markdown to HTML with python. We've used ply and MathJax.

Some .js scripts used from Markdown interpreter of R studio.

My development environment is Mac OS 10.10.1, python version 2.7

Current version is 5.1

Now I have realized some functions, check it below.

##Functions
Supported Markdown grammars:
+ Using `#` to create title and subtitles, e.g. `# TITLE` `## SUBTITLE`
+ Using one `*` or one `_` to set to latics, e.g. `*latics*` `_latics_`
+ Using `**` or `__` to set to bold, e.g.`**bold**` `__bold__`
+ Using more than three `*`, `=` or `-` to add a separation line, e.g.`---` `===` `***`
  (you can be insert a space, and please notice that `===` is only supported by GitHub.)
+ Using `1. `, `+ `, `- ` or `* ` for listing.
+ Using `![img](url)` to show image
+ Using `> contents` to support quote.
+ Using ``` to support code fields.
  (please notice this is only supported by GitHub.)

+ Image embedded into html automatically( image url need internet access. If cannot, it will output url directly.)


##Environment
If you want to test it, first you need to set up python environment (only for windows users) and ply (lexer and yacc for python).
At the root of this repository exists a file named `ply-3.4.zip`. Unzip it and run this code on your terminal:

```
python setup.py install
```
then you can test it.

##How to use

+ `plyLex.py` lexer
+ `plyExport.py` two string for html output
+ `plyYacc.py`semantic analyzer
+ `plyRun.py` script interface

+ `plyScripts_2_7.py` some methods for htmlouput, only applied for python version under 3.3
+ `plyScripts_3_3.py` some methods for htmlouput, only applied for python version above 3.3

To run this analyzer, You have three optional commands:
```
+ python plyRun.py
+ python plyRun.py *imported Markdown filename*
+ python plyRun.py *imported Markdown filename* *Exported HTML filename*
```

You can use `data.md` as a test.


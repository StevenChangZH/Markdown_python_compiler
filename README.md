Markdown_python_compiler
========================

This is a Markdown compiler, converting Markdown to HTML with python. We've used ply and MathJax.

Every Iteration will add some functions. So please add an iteration directly and debug in that folder only.

Now we have Iteration1, and you can check it in the Iteration1 folder.

##Functions
+ Using `#` to create title and subtitles, e.g. `# TITLE` `## SUBTITLE`
+ Using one `*` or one `_` to set to latics, e.g. `*latics*` `_latics_`
+ Using `**` or `__` to set to bold, e.g.`**bold**` `__bold__
+ Using more than three `*`, `=` or `-` to add a separation line, e.g.`---` `===` `***`
  (you can be insert a space, and please notice that `===` is only supported by GitHub.)



##Environment
If you want to test it, first you need to set up python environment (only for windows users) and ply (lexer and yacc for python).
At the root of this repository exists a file named `ply-3.4.tar.gz`. Unzip it and run this code:
```
python setup.py install
```
then you can test it.

##How to use
Only three `.py` files are codes. They are:

+ `plyLex.py` lexer
+ `plyExport.py` two string for html output
+ `plyYacc.py`semantic analyzer and script interface

To run this analyzer, You have three optional commands:

+ python plyYacc.py
+ python plyYacc.py *imported Markdown filename*
+ python plyYacc.py *imported Markdown filename* *Exported HTML filename*

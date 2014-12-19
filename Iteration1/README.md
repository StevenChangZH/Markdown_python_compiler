# README

This iteration realize those things:

+ Using `#` to create title and subtitles, e.g. `# TITLE` `## SUBTITLE`
+ Using one `*` or one `_` to set to latics, e.g. `*latics*` `_latics_`
+ Using `**` or `__` to set to bold, e.g.`**bold**` `__bold__
+ Using more than three `*`, `=` or `-` to add a separation line, e.g.`---` `===` `***`
  (you can be insert a space, and please notice that `===` is only supported by GitHub.)
  
## How to use
Only three `.py` files are codes. They are:

+ `plyLex.py` lexer
+ `plyExport.py` two string for html output
+ `plyYacc.py`semantic analyzer and script interface

To run this analyzer, You have three optional commands:

+ python plyYacc.py
+ python plyYacc.py <imported Markdown filename>
+ python plyYacc.py <imported Markdown filename> <Exported HTML filename>

But first you need to set up python environment (only for windows users) and ply (lexer and yacc for python).
At the root of this repository exists a file named `ply-3.4.tar.gz`. Unzip it and run this code:
```
python setup.py install
```
then you can test it.

# ------------------------------------------------------------
# plyYacc.py
#
# Semantic analyzer for Markdown elements
# version 1.0 for test-1
# ------------------------------------------------------------
import ply.yacc as yacc
import sys
from plyExport import html_head
from plyExport import html_tails

# Terminal command:
# python plyYacc.py
# python plyYacc.py <imported Markdown filename>
# python plyYacc.py <imported Markdown filename> <Exported HTML filename>
commandlength = len(sys.argv)
if commandlength==1:
    Markdown_filename = "data.md"
    HTML_filename = "html_md.html"
elif commandlength==2:
    Markdown_filename = sys.argv[1]
    HTML_filename = "html_md.html"
else:
    Markdown_filename = sys.argv[1]
    HTML_filename = sys.argv[2]

# Get the token map from the lexer.  This is required.
from plyLex import tokens

# Expressions
# This non-terminal 'all' has no meaning but only to reduce
def p_all_empty(p):
    'all : empty'
    p[0] = p[1]

def p_all_title(p):
    'all : all title'
    p[0] = p[1] + p[2] + "\n"

def p_all_separator(p):
    'all : all separator'
    p[0] = p[1] + p[2] + "\n"

def p_all_paragraph(p):
    'all : all paragraph'
    p[0] = p[1] + "<p>" + p[2] + "</p>\n"

def p_all_newline(p):
    'all : all newline'
    p[0] = p[1] + p[2]



def p_sep_separator(p):
    'separator : SEPARATOR'
    p[0] = "<hr />"

def p_sep_newline(p):
    'newline : NEWLINE'
    p[0] = ""
#    if p[1] > 4:
#        p[0] = "<br/>\n"
#    else:
#        p[0] = ""

def p_title_poundsign(p):
    'title : POUNDSIGN CONTENTS'
    p[0] = "<div id=\"" + p[2] + "\" class=\"section level" + p[1] +"1\">\n"
    p[0] = p[0] + "<h"+ p[1] + ">" + p[2] + "</h" + p[1] + "></div>"



def p_paragraph_empty(p):
    'paragraph : texts'
    p[0] = p[1]

def p_paragraph_texts(p):
    'paragraph : paragraph texts'
    p[0] = p[1] + p[2]

def p_texts_latics(p):
    'texts : LATICS texts LATICS'
    p[0] = "<em>" + p[2] + "</em>"

def p_texts_bold(p):
    'texts : BOLD texts BOLD'
    p[0] = "<strong>" + p[2] + "</strong>"

def p_texts_contents(p):
    'texts : CONTENTS'
    p[0] = p[1]

def p_empty(p):
    'empty : '
    p[0] = ""


# Error rule for syntax errors
def p_error(p):
    print "Syntax error in input!"

# Build the parser
parser = yacc.yacc()


# Test Yacc
# Open markdown file
markdown_input = open('./' + Markdown_filename)
try:
    data = markdown_input.read()
finally:
    markdown_input.close()
# Parse
parsing_result = parser.parse(data)
print "Parsing success"
# Add html heads and tails from plyExport.py
html_result = html_head + parsing_result +html_tails;

# Write to a html file
html_output = open('./'+HTML_filename, 'w')
try:
    html_output.write(html_result)
finally:
    html_output.close
    print "Exporting success"


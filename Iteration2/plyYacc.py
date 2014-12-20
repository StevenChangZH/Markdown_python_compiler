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

def p_all_tab(p):
    'all : all tab'
    p[0] = p[1] + p[2] + "\n"

#def p_all_list(p):
#    'all : all list'
#    p[0] = p[1] + p[2] + "\n"




def p_title_poundsign(p):
    'title : POUNDSIGN CONTENTS'
    p[0] = "<div id=\"" + p[2] + "\" class=\"section level" + p[1] +"1\">\n"
    p[0] = p[0] + "<h"+ p[1] + ">" + p[2] + "</h" + p[1] + ">\n</div>"

#def p_list_empty(p):
#    'list : empty'
#    p[0] = p[1]
#
#def p_list_listsingle(p):
#    'list : LISTSINGLE texts'
#    p[0] = "<ul>\n<li>" + p[2] + "</li>\n</ul>"
#
#
#def p_list_bold(p):
#    'list : list LISTDOUBLE texts'
#    if p[1].endwith("\n</ul>"):
#        p[1] = (p[1])[:end-5];





def p_separator_separator(p):
    'separator : SEPARATOR'
    p[0] = "<hr />"

def p_newline_newline(p):
    'newline : NEWLINE'
    p[0] = ""
#    if p[1] > 4:
#        p[0] = "<br/>\n"
#    else:
#        p[0] = ""

def p_tab_tab(p):
    'tab : TAB'
    p[0] = ""




def p_paragraph_empty(p):
    'paragraph : sentences'
    p[0] = p[1]

def p_paragraph_sentences(p):
    'paragraph : paragraph sentences'
    p[0] = p[1] + p[2]

def p_paragraph_add_notation(p):
    '''paragraph : paragraph LBRACKET
                | paragraph RBRACKET
                | paragraph LPAREN
                | paragraph RPAREN
                | paragraph LANGLE
                | paragraph RANGLE
                | paragraph LATICS
                | paragraph BOLD
                | paragraph CODE'''
    p[0] = p[1] + p[2]




def p_sentences_latics(p):
    'sentences : LATICS sentences LATICS'
    p[0] = "<em>" + p[2] + "</em>"

def p_sentences_bold(p):
    'sentences : BOLD sentences BOLD'
    p[0] = "<strong>" + p[2] + "</strong>"

def p_sentences_code(p):
    'sentences : CODE sentences CODE'
    p[0] = "<code>" + p[2] + "</code>"

def p_sentences_url_redirect(p):
    'sentences : LBRACKET sentences RBRACKET LPAREN sentences RPAREN'
    p[0] = "<a href=\"" + p[5] + "\">" + p[2] + "</a>"

def p_sentences_url(p):
    'sentences : LANGLE sentences RANGLE'
    p[0] = "<p><a href=\"" + p[2] + "\">" + p[2] + "</a></p>"

def p_sentences_contents(p):
    'sentences : CONTENTS'
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


# ------------------------------------------------------------
# plyYacc.py
#
# Semantic analyzer for Markdown elements
# version 7.0 for Markdown_python_compiler
# ------------------------------------------------------------
import ply.yacc as yacc
import sys
if sys.version_info<(3,3): import plyScripts_2_7 as plyScripts
else: import plyScripts_3_3 as plyScripts
#from plyExport import html_head
#from plyExport import html_tails

# Get the token map from the lexer.  This is required.
from plyLex import tokens

# Methods to operate list strings
def getListLevel(string):
    listlevel = 0
    index=0
    for char in string:
        if char==" ":listlevel += 1
        elif char=="\t":listlevel +=4
        else:return (listlevel)/4

def getFormerListEnd(string, listlevel):
    str = string[::-1]
    formerlevel = -1
    index = 0
    if len(str)<5:return 0
    while 1:
        if listlevel==formerlevel:return index
        elif str[index:index+5]==">lu/<":formerlevel+=1;index+=5
        elif str[index:index+5]==">lo/<":formerlevel+=1;index+=5
        elif str[index:index+1]=="\n":index+=1
        elif str[index:index+5]==">il/<":return -index
        else:return 0

def adjustMathFormula(string):
    str = ""
    strlen = len(string)
    index = 0
    while index<strlen:
        i=2
        if string[index:index+4]=="<em>":str+="_";index+=4;
        elif string[index:index+5]=="</em>":str+="_";index+=5;
        else:str+=string[index:index+1];index+=1;
    return str



# Priority
precedence = (
              ('left', 'PRIORITY0'),
              ('left', 'PRIORITY1'),
              ('left', 'PRIORITY2'),
              )
# Expressions
# This non-terminal 'all' has no meaning but only to reduce
# ORDER IS PRIORITY - suck.
def p_all_empty(p):
    'all : empty'
    p[0] = p[1]

def p_all_title(p):
    'all : all title'
    p[0] = p[1] + p[2] + "\n"

def p_all_image(p):
    'all : all image'
    p[0] = p[1] + p[2] + "\n"

def p_all_video(p):
    'all : all video'
    p[0] = p[1] + p[2] + "\n"

def p_all_quote(p):
    'all : all quote'
    if (p[1])[-18:]=="</p></blockquote>\n":p[0] = (p[1])[:-18] + p[2] + (p[1])[-18:]
    else: p[0] = p[1] + "<blockquote><p>" + p[2] + "\n"

def p_all_codefield(p):
    'all : all codefield newline CODEFIELD %prec PRIORITY0'
    p[0] = p[1] + p[2] + "\n</code></pre>"

def p_all_separator(p):
    'all : all separator'
    p[0] = p[1] + p[2] + "\n"

def p_all_newline(p):
    'all : all newline'
    p[0] = p[1] + p[2]

def p_all_tab(p):
    'all : all tab'
    p[0] = p[1] + p[2] + "\n"

def p_all_paragraph(p):
    'all : all newline paragraph %prec PRIORITY0'
    p[0] = p[1] + "<p>" + p[3] + "</p>\n"

# List expressions
def p_all_listnumber(p):
    'all : all LISTNUMBER paragraph %prec PRIORITY0'
    p[0] = p[1] + "\n<ol start=\"" + p[2] + "\" style=\"list-style-type: decimal\"><li>" + p[3] + "</li></ol>"

def p_all_listsingle(p):
    'all : all LISTSINGLE paragraph %prec PRIORITY0'
    listlevel = getListLevel(p[2])
    string = p[1]
    index = getFormerListEnd(string,listlevel)
    if index>0:
        p[0] = string[:-index] + "\n<li>" + p[3] + "</li>\n" + string[-index:]
    if index<0:
        p[0] = string[:index] + "<ul>\n<li>" + p[3] + "</li>\n</ul>" + string[index:]
    if index==0:
        if string[-5:]=="</ul>" or string[-5:]=="</ol>":
            p[0] = string[:-5] + "<li>" + p[3] + "</li>\n" + string[-5:]
        else:
            p[0] = p[1] + "<ul>\n<li>" + p[3] + "</li></ul>"

def p_all_listdouble(p):
    'all : all LISTDOUBLE paragraph %prec PRIORITY0'
    string = p[1]
    listdoubleindex = getListLevel(p[2])
    index = getFormerListEnd(string,1)
    if index>0:
        p[0] = string[:-index] + "\n<li>" + p[3] + "</li>" + string[-index:]
    if index<0:
        p[0] = string[:index] + "\n<ul>\n<li>" + p[3] + "</li>\n</ul>" + string[index:]
    if index==0:
        p[0] = p[1] + "\n" + (p[2])[listdoubleindex:] + (p[2])[listdoubleindex:] + " " + p[3] + "\n&amp;"




# code field
def p_codefield0_create(p):
    'codefield0 : newline CODEFIELD'
    p[0] = "<pre><code>"

def p_codefield0_newline(p):
    'codefield : codefield0 newline newline'
    p[0] = p[1]

def p_codefield0_paragraph(p):
    'codefield0 : codefield0 paragraph'
    p[0] = p[1] + p[2] + "\n"

def p_codefield_paragraph(p):
    'codefield0 : codefield paragraph'
    p[0] = p[1] + p[2] + "\n"
    
def p_codefield_newline(p):
    'codefield : codefield newline newline'
    p[0] = p[1] + "\n"





def p_title_poundsign(p):
    'title : POUNDSIGN CONTENTS'
    p[0] = "<div id=\"" + p[2] + "\" class=\"section level" + p[1] +"\">\n"
    p[0] = p[0] + "<h"+ p[1] + ">" + p[2] + "</h" + p[1] + ">\n</div>"

def p_image_exclamation(p):
    'image : newline EXCLAMATION LBRACKET CONTENTS RBRACKET LPAREN CONTENTS RPAREN %prec PRIORITY2'
    imagedata = plyScripts.getImageContents(p[7])
    p[0] = "<img src=\"" + imagedata + "\" alt=\"" + p[4] + "\" />"

def p_video_exclamation(p):
    'video : newline EXCLAMATION EXCLAMATION LBRACKET CONTENTS RBRACKET LPAREN CONTENTS RPAREN %prec PRIORITY2'
    videourl = plyScripts.getYoutubeVideoContents(p[8])
    p[0] = "<br/>\n<iframe id=\"player\" type=\"text/html\" width=\"640\" height=\"390\" src=\"" + videourl + "\" alt=\"" + p[5] + "\" frameborder=\"0\"></iframe>\n<br/>"

def p_quote_rangle(p):
    'quote : newline RANGLE paragraph %prec PRIORITY2'
    p[0] = p[3] + "</p></blockquote>"

def p_separator_separator(p):
    'separator : SEPARATOR'
    p[0] = "<hr />"

def p_newline_newline(p):
    'newline : NEWLINE'
    p[0] = ""

def p_tab_tab(p):
    'tab : TAB'
    p[0] = ""





def p_paragraph_empty(p):
    'paragraph : sentences'
    p[0] = p[1]

def p_paragraph_sentences(p):
    'paragraph : paragraph sentences %prec PRIORITY1'
    p[0] = p[1] + p[2]

def p_paragraph_mathformula(p):
    'paragraph : paragraph DOLLAR paragraph DOLLAR sentences'
    formula = adjustMathFormula(p[3])
    p[0] = p[1] + "<span class=\"math\">\\(" + formula + "\\)</span>" + p[5]

def p_sentences_url_redirect(p):
    'paragraph : paragraph LBRACKET sentences RBRACKET LPAREN sentences RPAREN %prec PRIORITY2'
    p[0] = p[1] + "<a href=\"" + p[6] + "\">" + p[3] + "</a>"

def p_sentences_code(p):
    'paragraph : paragraph CODE sentences CODE %prec PRIORITY2'
    p[0] = p[1] + "<code>" + p[3] + "</code>"

def p_sentences_latics(p):
    'paragraph : paragraph LATICS sentences LATICS %prec PRIORITY2'
    p[0] = p[1] + "<em>" + p[3] + "</em>"

def p_sentences_bold(p):
    'paragraph : paragraph BOLD sentences BOLD %prec PRIORITY2'
    p[0] = p[1] + "<strong>" + p[3] + "</strong>"

def p_sentences_url(p):
    'paragraph : LANGLE sentences RANGLE %prec PRIORITY2'
    p[0] = "<a href=\"" + p[2] + "\">" + p[2] + "</a>"

def p_paragraph_add_exclamation(p):
    'paragraph : paragraph EXCLAMATION newline %prec PRIORITY1'
    p[0] = p[1] + p[2]

def p_paragraph_add_notation(p):
    '''paragraph : paragraph EXCLAMATION sentences %prec PRIORITY1
                | paragraph LBRACKET sentences %prec PRIORITY1
                | paragraph RBRACKET sentences %prec PRIORITY1
                | paragraph LPAREN sentences %prec PRIORITY1
                | paragraph RPAREN sentences %prec PRIORITY1
                | paragraph LANGLE sentences %prec PRIORITY1
                | paragraph RANGLE sentences %prec PRIORITY1
                | paragraph LATICS sentences %prec PRIORITY1
                | paragraph BOLD sentences %prec PRIORITY1
                | paragraph CODE sentences %prec PRIORITY1'''
    p[0] = p[1] + p[2] + p[3]

def p_sentences_contents(p):
    'sentences : CONTENTS'
    p[0] = p[1]

def p_empty(p):
    'empty : '
    p[0] = ""


# Error rule for syntax errors
def p_error(p):
    print ("Syntax error in input!")
    print (p)
    print ("Syntax error in input!")

# Build the parser
parser = yacc.yacc()


# Parse method for plyRun
def yaccparse(data):
    parsing_result = parser.parse(data)
    return parsing_result

## Test Yacc
## Open markdown file
#markdown_input = open('./data.md')
#try:
#    data = markdown_input.read()
#finally:
#    markdown_input.close()
## Parse
#parsing_result = parser.parse(data)
#print ("Parsing success")
## Add html heads and tails from plyExport.py
#html_result = html_head + parsing_result +html_tails;
#
## Write to a html file
#html_output = open('./html_md.html', 'w')
#try:
#    html_output.write(html_result)
#finally:
#    html_output.close
#    print ("Exporting success")


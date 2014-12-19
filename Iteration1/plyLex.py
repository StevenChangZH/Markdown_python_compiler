# coding=utf-8
# ------------------------------------------------------------
# plyLex.py
#
# tokenizer for Markdown elements
# version 1.0 for test-1
# ------------------------------------------------------------
import ply.lex as lex

# List of token names
tokens = (
    'POUNDSIGN',
    'SEPERATOR',
    'LATICS',
    'BOLD',
    'NEWLINE',
    'CONTENTS'
    );

# Regular expression rules for simple tokens
# Chinese coding if possible: \u4e00-\u9fa5 ( '_' has an error)
# NOTICE the priority of each token
def t_SEPERATOR(t):
    r'[*\-=]([ ]{0,1}[*\-=]){2,}'
    return t

def t_NEWLINE(t):
    r'[\r\n]+'
    t.value = len(t.value)
    return t

def t_POUNDSIGN(t):
    r'[#]{1,6}'
    t.value = str(len(t.value))
    return t

def t_BOLD(t):
    r'[*_]{2}'
    return t

def t_LATICS(t):
    r'[*_]{1}'
    return t

def t_CONTENTS(t):
    r'([0-9a-zA-Z]|[., :\'\(\)\?])+'
    return t

## Ignored only \n not \n\n
#def t_COMMENTS(t):
#    r'[\n\r]'
#    pass

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
#t_ignore  = '\n\t\r'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


# Test lex
file_object = open('./data.md')
try:
    data = file_object.read()
finally:
    file_object.close()
# Give the lexer some input
lexer.input(data)


# Tokenize
while True:
    tok = lexer.token()
    if not tok: break      # No more input
    print tok

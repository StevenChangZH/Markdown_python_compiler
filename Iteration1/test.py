# python test
print "hello world"
import plyLex.py

# test lex
# Test it out
data =
# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: break      # No more input
    print tok